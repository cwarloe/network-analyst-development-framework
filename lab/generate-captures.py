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
    p = subprocess.Popen(["tcpdump", "-i", iface, "-U", "-w", path, "-s", "0", bpf],
                         stderr=subprocess.DEVNULL)
    time.sleep(2)
    return p


def stop(p):
    time.sleep(2)
    p.send_signal(2)      # SIGINT, so tcpdump flushes what it is holding
    p.wait()


def client_socket(dest_port, src_port, timeout=5):
    """Connect from a fixed source port so regenerated captures are stable.

    Ephemeral ports would otherwise change every run, and the lessons quote
    port numbers.
    """
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if src_port:
        s.bind(("127.0.0.1", src_port))
    s.settimeout(timeout)
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
    fix_checksums(path)
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


# --------------------------------------------------------------- failures ---
def failure_servers():
    """Three servers, each broken in a different, deliberate way."""
    # 8100: accepts nothing. Its backlog is filled below so the kernel
    #       silently drops further SYNs -- what a firewall DROP looks like.
    drop = socket.socket()
    drop.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    drop.bind(("127.0.0.1", 8100))
    drop.listen(1)

    # 8102: answers, then resets the connection mid-response.
    def resetter():
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", 8102))
        s.listen(5)
        while True:
            try:
                c, _ = s.accept()
                c.recv(1024)
                c.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 5000\r\n\r\n" + b"A" * 400)
                c.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                             struct.pack("ii", 1, 0))     # linger 0 -> RST on close
                c.close()
            except Exception:
                pass

    # 8103: correct, just slow. Nothing is wrong with the network.
    def slow():
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", 8103))
        s.listen(5)
        while True:
            try:
                c, _ = s.accept()
                c.recv(1024)
                time.sleep(4)
                body = b'{"report":"finance-export","rows":1284}'
                c.sendall(b"HTTP/1.1 200 OK\r\nServer: nginx/1.24.0\r\n"
                          b"Content-Type: application/json\r\nContent-Length: "
                          + str(len(body)).encode() + b"\r\n\r\n" + body)
                c.close()
            except Exception:
                pass

    threading.Thread(target=resetter, daemon=True).start()
    threading.Thread(target=slow, daemon=True).start()
    return drop


def gen_failures():
    """Four ways the same user complaint -- 'it doesn't work' -- can arise."""
    drop_srv = failure_servers()
    time.sleep(1)

    # fill 8100's accept queue so its SYNs go unanswered
    backlog = []
    for _ in range(12):
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect(("127.0.0.1", 8100))
            backlog.append(s)
        except Exception:
            break

    raw = os.path.join(TMP, "fail.pcap")
    # only the four deliberate client ports -- the sockets used to fill 8100's
    # backlog keep retransmitting and would otherwise contaminate the capture
    cap = capture("lo", "tcp portrange 41000-41003", raw)

    # 1. refused -- nothing is listening on 8101
    s = socket.socket(); s.settimeout(5)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 41001))
    try:
        s.connect(("127.0.0.1", 8101))
    except Exception as e:
        print(f"  refused : {type(e).__name__}")
    s.close()
    time.sleep(1)

    # 2. reset mid-transfer
    try:
        s = client_socket(8102, 41002)
        s.sendall(b"GET /report/full HTTP/1.1\r\nHost: files.contoso-internal.example\r\n\r\n")
        while s.recv(4096):
            pass
    except Exception as e:
        print(f"  reset   : {type(e).__name__}")
    time.sleep(1)

    # 3. slow but correct
    t0 = time.time()
    s = client_socket(8103, 41003, timeout=20)
    s.sendall(b"GET /api/v2/export?page=1 HTTP/1.1\r\nHost: files.contoso-internal.example\r\n"
              b"Connection: close\r\n\r\n")
    while s.recv(4096):
        pass
    s.close()
    print(f"  slow    : completed in {time.time() - t0:.1f}s")

    # 4. dropped -- SYNs into a full accept queue, retransmitted, never answered
    s = socket.socket(); s.settimeout(14)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 41000))
    t0 = time.time()
    try:
        s.connect(("127.0.0.1", 8100))
    except Exception as e:
        print(f"  dropped : {type(e).__name__} after {time.time() - t0:.1f}s")
    s.close()

    stop(cap)
    for b in backlog:
        b.close()
    drop_srv.close()
    out = os.path.join(OUT, "06-failures.pcap")
    # plain HTTP, so port 80 -- mapping these to 443 makes Zeek try the SSL
    # analyzer and log a protocol violation that is an artefact, not a finding
    anonymize(raw, out, {8100: 80, 8101: 80, 8102: 80, 8103: 80},
              {8100: SERVER_A, 8101: SERVER_B, 8102: "198.51.100.40", 8103: "198.51.100.50"})
    print("fail ->", out)


# ------------------------------------------------------------- suspicious ---
def dns_responder(port=8053):
    """A local authoritative-ish responder, so tunneling-shaped queries stay
    inside the lab instead of being sprayed at a public resolver."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", port))
    while True:
        try:
            data, addr = s.recvfrom(4096)
            tid = data[:2]
            # walk the question section to find where it ends
            i = 12
            while data[i] != 0:
                i += 1 + data[i]
            qend = i + 5
            qtype = struct.unpack(">H", data[qend - 4:qend - 2])[0]
            if qtype == 16:      # TXT -- a short payload, as a tunnel would carry
                rdata = bytes([31]) + b"v=1;seq=%04d;ok" % (int(time.time()) % 10000)
                rdata = bytes([len(rdata) - 1]) + rdata[1:]
                rr = b"\xc0\x0c" + struct.pack(">HHIH", 16, 1, 1, len(rdata) + 1) \
                     + bytes([len(rdata)]) + rdata
            else:
                rr = b"\xc0\x0c" + struct.pack(">HHIH", 1, 1, 60, 4) \
                     + ipaddress.IPv4Address("198.51.100.80").packed
            s.sendto(tid + b"\x81\x80" + struct.pack(">HHHH", 1, 1, 0, 0)
                     + data[12:qend] + rr, addr)
        except Exception:
            pass


def beacon_server(port, path_prefix):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(8)
    while True:
        try:
            c, _ = srv.accept()
            c.recv(2048)
            body = b'{"t":%d,"q":[]}' % int(time.time())
            c.sendall(b"HTTP/1.1 200 OK\r\nServer: nginx/1.24.0\r\n"
                      b"Content-Type: application/json\r\nContent-Length: "
                      + str(len(body)).encode() + b"\r\n\r\n" + body)
            c.close()
        except Exception:
            pass


def bulk_server(port=8203):
    """Accepts a large HTTP POST. Plaintext HTTP so Zeek records it in
    http.log with a real request_body_len -- random bytes on port 443 get
    misread as TLS, which would be an artefact rather than a finding."""
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", port))
    srv.listen(4)
    while True:
        try:
            c, _ = srv.accept()
            while c.recv(65535):
                pass
            c.close()
        except Exception:
            pass


def gen_suspicious():
    """Two beacons with the same shape and different causes, a tunneling-shaped
    DNS stream, and one bulk outbound transfer."""
    threading.Thread(target=dns_responder, daemon=True).start()
    threading.Thread(target=beacon_server, args=(8201, "/api"), daemon=True).start()
    threading.Thread(target=beacon_server, args=(8202, "/hb"), daemon=True).start()
    threading.Thread(target=bulk_server, daemon=True).start()
    time.sleep(1)

    raw = os.path.join(TMP, "susp.pcap")
    cap = capture("lo", "tcp portrange 8201-8203 or udp port 8053", raw)

    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    rnd = random.Random(20260819)          # fixed seed -- reproducible captures

    def beacon(port, path, tag):
        s = client_socket(port, 0)
        s.sendall(b"GET " + path + b" HTTP/1.1\r\nHost: " + tag + b"\r\n"
                  b"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n"
                  b"Connection: close\r\n\r\n")
        while s.recv(4096):
            pass
        s.close()

    def tunnel_query(i):
        label = "".join(rnd.choice(alphabet) for _ in range(48))
        name = f"{label}.d{i:03d}.sync.cdn-metrics.example"
        q = b"".join(bytes([len(l)]) + l.encode() for l in name.split(".")) + b"\x00"
        pkt = struct.pack(">HHHHHH", rnd.randint(0, 0xFFFF), 0x0100, 1, 0, 0, 0) \
            + q + struct.pack(">HH", 16, 1)
        u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        u.settimeout(3)
        try:
            u.sendto(pkt, ("127.0.0.1", 8053))
            u.recvfrom(4096)
        except Exception:
            pass
        u.close()

    # Two beacons on independent timers, each regular, each slightly jittered.
    # A tunnelling-shaped DNS stream runs underneath at a much higher rate.
    def beacon_loop(port, path, tag, interval, jitter, rounds, seed):
        r = random.Random(seed)
        for _ in range(rounds):
            try:
                beacon(port, path, tag)
            except Exception:
                pass
            time.sleep(interval + r.uniform(-jitter, jitter))

    threads = [
        threading.Thread(target=beacon_loop, args=(
            8201, b"/api/v1/tasks?id=8842", b"cdn-metrics.example",
            4.0, 0.12, 11, 11), daemon=True),
        threading.Thread(target=beacon_loop, args=(
            8202, b"/hb", b"updates.contoso-internal.example",
            5.0, 0.30, 9, 22), daemon=True),
    ]
    for th in threads:
        th.start()
    for i in range(40):
        tunnel_query(i)
        time.sleep(1.1)
    for th in threads:
        th.join(timeout=10)

    # one bulk outbound transfer, as an HTTP POST
    body_len = 15 * 4096
    s = client_socket(8203, 0)
    s.sendall(b"POST /upload/session HTTP/1.1\r\nHost: cdn-metrics.example\r\n"
              b"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n"
              b"Content-Type: application/octet-stream\r\nContent-Length: "
              + str(body_len).encode() + b"\r\n\r\n")
    chunk = bytes(rnd.getrandbits(8) for _ in range(4096))
    for _ in range(15):
        s.sendall(chunk)
    s.close()

    stop(cap)
    out = os.path.join(OUT, "07-suspicious.pcap")
    anonymize(raw, out, {8201: 80, 8202: 80, 8203: 80, 8053: 53},
              {8201: "198.51.100.60", 8202: "198.51.100.70",
               8203: "198.51.100.90", 8053: "198.51.100.80"}, udp_ports={8053})
    print("susp ->", out)


def fix_checksums(path):
    """Recompute IP and UDP/TCP checksums in place.

    Captures taken on a live interface carry whatever the capture point saw,
    which is not always a valid checksum -- offload and intermediate rewriting
    both leave the field wrong on the wire we record. Wireshark then marks
    every packet red and a learner spends the lesson on an artefact.

    The loopback captures get this for free from anonymize(). The DNS capture
    is not rewritten, so it needs the repair on its own.
    """
    data = open(path, "rb").read()
    off, out = 24, [data[:24]]
    while off + 16 <= len(data):
        ts, tus, cl, ol = struct.unpack("<IIII", data[off:off + 16])
        pkt = bytearray(data[off + 16:off + 16 + cl])
        off += 16 + cl
        if len(pkt) > 14 and struct.unpack(">H", pkt[12:14])[0] == 0x0800:
            o = 14
            ihl = (pkt[o] & 0x0F) * 4
            t = o + ihl
            proto = pkt[o + 9]
            pkt[o + 10:o + 12] = b"\x00\x00"
            pkt[o + 10:o + 12] = struct.pack(">H", cksum(bytes(pkt[o:o + ihl])))
            # A transport checksum covers the whole datagram, so it is only
            # meaningful on a packet that is not a fragment. Touching the bytes
            # at the transport offset of a fragment corrupts payload.
            ff = struct.unpack(">H", pkt[o + 6:o + 8])[0]
            fragmented = (ff & 0x2000) or (ff & 0x1FFF)
            if proto in (6, 17) and not fragmented:
                seglen = struct.unpack(">H", pkt[o + 2:o + 4])[0] - ihl
                coff = t + (16 if proto == 6 else 6)
                pkt[coff:coff + 2] = b"\x00\x00"
                pseudo = bytes(pkt[o + 12:o + 20]) + bytes([0, proto]) \
                    + struct.pack(">H", seglen)
                c = cksum(pseudo + bytes(pkt[t:t + seglen]))
                pkt[coff:coff + 2] = struct.pack(">H", c or 0xFFFF)
        out.append(struct.pack("<IIII", ts, tus, len(pkt), ol) + bytes(pkt))
    open(path, "wb").write(b"".join(out))


def gen_fragmentation():
    """A DNS query too large for the path MTU, fragmented by the real stack.

    EDNS0 padding (option 12) inflates a legitimate query past the interface
    MTU, so the kernel fragments it on the way out. Nothing is crafted -- the
    stack does the splitting, and the capture records what left the interface.
    """
    out = os.path.join(OUT, "06-fragmentation.pcap")
    # filter on host, NOT port: a port filter cannot match non-initial
    # fragments, because they carry no UDP header. That is the lesson.
    cap = capture("eth0", "host 1.1.1.1", out)

    name = "www.example.com"
    labels = b"".join(bytes([len(l)]) + l.encode() for l in name.split(".")) + b"\x00"
    pad = 2400
    rdata = struct.pack(">HH", 12, pad) + b"\x00" * pad          # EDNS0 Padding
    opt = b"\x00" + struct.pack(">HHIH", 41, 4096, 0, len(rdata)) + rdata
    pkt = struct.pack(">HHHHHH", random.randint(0, 0xFFFF), 0x0100, 1, 0, 0, 1) \
        + labels + struct.pack(">HH", 1, 1) + opt

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(4)
    s.sendto(pkt, ("1.1.1.1", 53))
    try:
        s.recvfrom(65535)
    except Exception:
        print(f"  query {len(pkt)}B fragmented; no reply (expected)")
    s.close()

    stop(cap)
    fix_checksums(out)
    print("frag ->", out)


# -------------------------------------------------------------- anonymize ---
def cksum(data):
    if len(data) % 2:
        data += b"\x00"
    s = sum(struct.unpack(f">{len(data)//2}H", data))
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    return (~s) & 0xFFFF


def anonymize(src, dst, portmap, servermap, udp_ports=frozenset()):
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
        proto = pkt[o + 9]
        seglen = struct.unpack(">H", pkt[o + 2:o + 4])[0] - ihl
        coff = t + (16 if proto == 6 else 6)
        pkt[coff:coff + 2] = b"\x00\x00"
        pseudo = bytes(pkt[o + 12:o + 20]) + bytes([0, proto]) + struct.pack(">H", seglen)
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
    gen_failures()
    gen_suspicious()
    gen_fragmentation()
    print("\ndone ->", OUT)
