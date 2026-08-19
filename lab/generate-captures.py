#!/usr/bin/env python3
"""Generate the packet captures used by lessons 02, 03 and 04.

Every capture is produced live: real DNS queries against public resolvers,
a real TCP conversation, real TLS 1.2 and TLS 1.3 handshakes. Nothing is
synthesised packet-by-packet, so protocol behaviour in the files is whatever
the stack and the network actually did.

Loopback captures are then rewritten into RFC 5737 documentation address
ranges so they read as a realistic exchange between two hosts. Addresses,
ports and MACs change; protocol behaviour, timing and payloads do not.

Requires: tcpdump, python3. Run as root.
    sudo python3 lab/generate-captures.py assets/pcaps
"""
import ipaddress, os, random, socket, ssl, struct, subprocess, sys, tempfile, threading, time

OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "assets/pcaps")
TMP = tempfile.mkdtemp()
CLIENT, SERVER_A, SERVER_B = "192.0.2.10", "198.51.100.20", "198.51.100.30"
CMAC, SMAC = bytes.fromhex("001c421a2b3c"), bytes.fromhex("0050569f4d1e")
RESOLVER = "1.1.1.1"


# ---------------------------------------------------------------- capture ---
def capture(iface, bpf, path):
    p = subprocess.Popen(["tcpdump", "-i", iface, "-w", path, "-s", "0", bpf],
                         stderr=subprocess.DEVNULL)
    time.sleep(2)
    return p


def stop(p):
    time.sleep(2)
    p.terminate()
    p.wait()


def client_socket(dest_port, src_port):
    """Connect from a fixed source port so regenerated captures are stable.

    Ephemeral ports would otherwise change every run, and the lessons quote
    port numbers.
    """
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", src_port))
    s.settimeout(5)
    s.connect(("127.0.0.1", dest_port))
    return s


# -------------------------------------------------------------------- DNS ---
def dns_query(name, qtype=1, server=RESOLVER):
    labels = b"".join(bytes([len(l)]) + l.encode() for l in name.split(".")) + b"\x00"
    pkt = struct.pack(">HHHHHH", random.randint(0, 0xFFFF), 0x0100, 1, 0, 0, 0) \
        + labels + struct.pack(">HH", qtype, 1)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(6)
    try:
        s.sendto(pkt, (server, 53))
        return s.recvfrom(4096)[0]
    finally:
        s.close()


def gen_dns():
    """Real lookups. CNAME chains, TTL asymmetry, AAAA, and an NXDOMAIN."""
    path = os.path.join(OUT, "03-dns.pcap")
    cap = capture("eth0", "udp port 53", path)
    plan = [
        ("www.github.com", 1),            # CNAME chain, short A TTL
        ("en.wikipedia.org", 1),          # CNAME chain, long CNAME TTL
        ("www.example.com", 1),
        ("www.example.com", 28),          # AAAA for the same name
        ("outlook.office365.com", 1),     # multi-step chain
        ("nonexistent-host-fbc19.example.com", 1),   # NXDOMAIN
    ]
    for name, qtype in plan:
        try:
            dns_query(name, qtype)
        except Exception as e:
            print(f"  ! {name}: {e}")
        time.sleep(0.4)
    time.sleep(3)
    for name in ("www.github.com", "en.wikipedia.org"):   # repeat: TTL has moved
        try:
            dns_query(name, 1)
        except Exception:
            pass
        time.sleep(0.3)
    stop(cap)
    print("dns  ->", path)


# ------------------------------------------------------------------- HTTP ---
BODY = (b'{"report":"finance-export","rows":1284,'
        b'"generated":"2026-08-19T09:14:22Z","format":"json"}')


def http_server():
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 8080))
    srv.listen(5)
    while True:
        try:
            c, _ = srv.accept()
            path = c.recv(4096).split(b" ")[1]
            if path.startswith(b"/api/v2/export"):
                c.sendall(b"HTTP/1.1 200 OK\r\nServer: nginx/1.24.0\r\n"
                          b"Content-Type: application/json\r\nContent-Length: "
                          + str(len(BODY)).encode() + b"\r\nX-Request-Id: 7f3a91c2\r\n\r\n" + BODY)
            elif path.startswith(b"/api/v2/admin"):
                denied = b'{"error":"insufficient_scope","code":"E403"}'
                c.sendall(b"HTTP/1.1 403 Forbidden\r\nServer: nginx/1.24.0\r\n"
                          b"Content-Type: application/json\r\nContent-Length: "
                          + str(len(denied)).encode() + b"\r\n\r\n" + denied)
            else:
                c.sendall(b"HTTP/1.1 404 Not Found\r\nServer: nginx/1.24.0\r\nContent-Length: 0\r\n\r\n")
            c.close()
        except Exception:
            pass


def gen_http():
    threading.Thread(target=http_server, daemon=True).start()
    time.sleep(1)
    raw = os.path.join(TMP, "http.pcap")
    cap = capture("lo", "tcp port 8080", raw)
    for src_port, path in ((42876, b"/api/v2/export?page=1"), (42886, b"/api/v2/admin/users")):
        s = client_socket(8080, src_port)
        s.sendall(b"GET " + path + b" HTTP/1.1\r\nHost: files.contoso-internal.example\r\n"
                  b"User-Agent: contoso-sync/3.2\r\nAccept: application/json\r\n"
                  b"Connection: close\r\n\r\n")
        while s.recv(65535):
            pass
        s.close()
        time.sleep(0.4)
    stop(cap)
    out = os.path.join(OUT, "02-conversation.pcap")
    anonymize(raw, out, {8080: 80}, {8080: SERVER_A})
    print("http ->", out)


# -------------------------------------------------------------------- TLS ---
def tls_server(port, maxver, crt, key):
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.maximum_version = maxver
    ctx.load_cert_chain(crt, key)
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(5)
    while True:
        try:
            c, _ = srv.accept()
            t = ctx.wrap_socket(c, server_side=True)
            t.recv(4096)
            t.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n"
                      b"Content-Length: 38\r\n\r\n"
                      b'{"status":"ok","records":1284,"pg":1}')
            t.close()
        except Exception:
            pass


def gen_tls():
    crt, key = os.path.join(TMP, "s.crt"), os.path.join(TMP, "s.key")
    subprocess.run(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
                    "-keyout", key, "-out", crt, "-days", "365",
                    "-subj", "/C=US/ST=Oregon/L=Portland/O=Contoso Ltd"
                             "/CN=files.contoso-internal.example",
                    "-addext", "subjectAltName=DNS:files.contoso-internal.example"],
                   check=True, capture_output=True)
    threading.Thread(target=tls_server, args=(8443, ssl.TLSVersion.TLSv1_2, crt, key), daemon=True).start()
    threading.Thread(target=tls_server, args=(8444, ssl.TLSVersion.TLSv1_3, crt, key), daemon=True).start()
    time.sleep(1)
    raw = os.path.join(TMP, "tls.pcap")
    cap = capture("lo", "tcp port 8443 or tcp port 8444", raw)
    for port, src_port in ((8443, 44120), (8444, 44130)):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        s = client_socket(port, src_port)
        w = ctx.wrap_socket(s, server_hostname="files.contoso-internal.example")
        print(f"  {port}: {w.version()} / {w.cipher()[0]}")
        w.sendall(b"GET /api/v2/export?page=1 HTTP/1.1\r\n"
                  b"Host: files.contoso-internal.example\r\n"
                  b"User-Agent: contoso-sync/3.2\r\n\r\n")
        w.recv(4096)
        w.close()
        time.sleep(0.5)
    stop(cap)
    out = os.path.join(OUT, "04-tls.pcap")
    anonymize(raw, out, {8443: 443, 8444: 443}, {8443: SERVER_A, 8444: SERVER_B})
    print("tls  ->", out)


# -------------------------------------------------------------- anonymize ---
def cksum(data):
    if len(data) % 2:
        data += b"\x00"
    s = sum(struct.unpack(f">{len(data)//2}H", data))
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    return (~s) & 0xFFFF


def anonymize(src, dst, portmap, servermap):
    """Rewrite a loopback capture into a two-host conversation.

    Direction is inferred from the destination port: a packet addressed to a
    server port is client-to-server. Checksums are recomputed, so the output
    verifies clean in Wireshark.
    """
    data = open(src, "rb").read()
    off, out = 24, [data[:24]]
    while off + 16 <= len(data):
        ts, tus, cl, _ = struct.unpack("<IIII", data[off:off + 16])
        pkt = bytearray(data[off + 16:off + 16 + cl])
        off += 16 + cl
        o = 14
        ihl = (pkt[o] & 0x0F) * 4
        t = o + ihl
        sp, dp = struct.unpack(">HH", pkt[t:t + 4])
        if dp in servermap:
            s_ip, d_ip, s_mac, d_mac = CLIENT, servermap[dp], CMAC, SMAC
        else:
            s_ip, d_ip, s_mac, d_mac = servermap[sp], CLIENT, SMAC, CMAC
        pkt[0:6], pkt[6:12] = d_mac, s_mac
        pkt[o + 12:o + 16] = ipaddress.IPv4Address(s_ip).packed
        pkt[o + 16:o + 20] = ipaddress.IPv4Address(d_ip).packed
        pkt[t:t + 2] = struct.pack(">H", portmap.get(sp, sp))
        pkt[t + 2:t + 4] = struct.pack(">H", portmap.get(dp, dp))
        pkt[o + 10:o + 12] = b"\x00\x00"
        pkt[o + 10:o + 12] = struct.pack(">H", cksum(bytes(pkt[o:o + ihl])))
        seglen = struct.unpack(">H", pkt[o + 2:o + 4])[0] - ihl
        coff = t + 16
        pkt[coff:coff + 2] = b"\x00\x00"
        pseudo = bytes(pkt[o + 12:o + 20]) + bytes([0, 6]) + struct.pack(">H", seglen)
        c = cksum(pseudo + bytes(pkt[t:t + seglen]))
        pkt[coff:coff + 2] = struct.pack(">H", c or 0xFFFF)
        out.append(struct.pack("<IIII", ts, tus, len(pkt), len(pkt)) + bytes(pkt))
    open(dst, "wb").write(b"".join(out))


if __name__ == "__main__":
    if os.geteuid() != 0:
        sys.exit("needs root for tcpdump")
    os.makedirs(OUT, exist_ok=True)
    gen_dns()
    gen_http()
    gen_tls()
    print("\ndone ->", OUT)
