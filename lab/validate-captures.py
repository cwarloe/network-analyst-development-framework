#!/usr/bin/env python3
"""Acceptance gate for every capture this project ships.

A capture is only usable as training material if the tools a learner will
actually point at it can read it. Two checks, both mandatory:

  1. Wireshark must dissect it -- no malformed packets, no bad checksums,
     and the protocol we claim is in there must actually be recognised.

  2. Zeek must parse it into logs. This is the stricter test and the one
     that decides. Security Onion ingests Zeek logs into Elastic; if Zeek
     does not produce a dns.log from a DNS capture, that traffic is
     invisible in Hunt and Kibana no matter how good it looks in Wireshark.

A capture that fails either check is a bad capture, whether it was
synthesised in a lab or taken off a production tap.

    python3 lab/validate-captures.py assets/pcaps
"""
import json, os, shutil, struct, subprocess, sys, tempfile

# What each capture must yield. Zeek log -> minimum row count, plus fields
# that must be populated on at least one row.
EXPECTED = {
    "02-conversation.pcap": {
        "tshark_protocols": ["tcp", "http"],
        "zeek": {
            "conn.log": (2, ["id.orig_h", "id.resp_p", "conn_state", "service"]),
            "http.log": (2, ["method", "uri", "status_code", "host"]),
        },
    },
    "03-dns.pcap": {
        "tshark_protocols": ["udp", "dns"],
        "zeek": {
            "conn.log": (1, ["id.resp_p", "proto"]),
            "dns.log":  (8, ["query", "qtype_name", "rcode_name", "answers"]),
        },
    },
    "07-suspicious.pcap": {
        "tshark_protocols": ["tcp", "udp", "http", "dns"],
        "zeek": {
            "conn.log": (50, ["id.resp_h", "service", "orig_bytes"]),
            "http.log": (20, ["method", "host", "uri", "request_body_len"]),
            "dns.log":  (40, ["query", "qtype_name", "answers"]),
        },
    },
    # Provisional -- these two do not exist yet. They are produced by
    # generate-impairment.py, which needs NET_ADMIN and netem. Expectations are
    # deliberately loose for 06-loss: under heavy loss the transfer may not
    # complete, which is a legitimate capture but leaves no finished http entry.
    "06-latency.pcap": {
        "tshark_protocols": ["tcp", "http"],
        "zeek": {
            "conn.log": (1, ["conn_state", "duration", "id.resp_p"]),
            "http.log": (1, ["method", "status_code"]),
        },
    },
    "06-loss.pcap": {
        "tshark_protocols": ["tcp"],
        "zeek": {
            "conn.log": (1, ["conn_state", "id.resp_p"]),
        },
    },
    "06-fragmentation.pcap": {
        "tshark_protocols": ["udp", "dns"],
        "zeek": {
            "conn.log": (1, ["id.resp_p", "proto"]),
            "dns.log":  (1, ["query", "qtype_name"]),
        },
    },
    "06-failures.pcap": {
        "tshark_protocols": ["tcp"],
        "zeek": {
            "conn.log": (4, ["conn_state", "history", "id.resp_p"]),
            "http.log": (2, ["method", "status_code"]),
        },
    },
    "04-tls.pcap": {
        "tshark_protocols": ["tcp", "tls"],
        "zeek": {
            "conn.log":  (2, ["id.resp_p", "service"]),
            "ssl.log":   (2, ["version", "cipher", "server_name"]),
            "x509.log":  (1, ["certificate.subject", "certificate.issuer"]),
        },
    },
}

GREEN, RED, YELLOW, RESET = "\033[32m", "\033[31m", "\033[33m", "\033[0m"


def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def _cksum(data):
    if len(data) % 2:
        data += b"\x00"
    s = sum(struct.unpack(f">{len(data)//2}H", data))
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    return (~s) & 0xFFFF


def check_checksums(path):
    """Verify IP and TCP/UDP checksums without asking a tool.

    This exists because tshark 4.2.2 and tshark 4.0.17 disagreed about the
    same file: one reported every UDP checksum good, the other reported every
    one bad, and independent arithmetic showed the second was right. A gate
    that trusts a single tool's verdict is only as strong as that tool's
    version. Arithmetic does not have versions.
    """
    data = open(path, "rb").read()
    off, n, bad = 24, 0, 0
    while off + 16 <= len(data):
        _, _, cl, _ = struct.unpack("<IIII", data[off:off + 16])
        pkt = data[off + 16:off + 16 + cl]
        off += 16 + cl
        if len(pkt) < 34 or struct.unpack(">H", pkt[12:14])[0] != 0x0800:
            continue
        o = 14
        ihl = (pkt[o] & 0x0F) * 4
        t = o + ihl
        proto = pkt[o + 9]
        n += 1
        hdr = bytearray(pkt[o:o + ihl])
        stored_ip = struct.unpack(">H", bytes(hdr[10:12]))[0]
        hdr[10:12] = b"\x00\x00"
        if stored_ip != _cksum(bytes(hdr)):
            bad += 1
            continue
        if proto not in (6, 17):
            continue
        ff = struct.unpack(">H", pkt[o + 6:o + 8])[0]
        if (ff & 0x2000) or (ff & 0x1FFF):
            continue        # fragment: the transport checksum covers the
                            # reassembled datagram, not this piece of it
        seglen = struct.unpack(">H", pkt[o + 2:o + 4])[0] - ihl
        if t + seglen > len(pkt):          # truncated capture, cannot verify
            continue
        coff = t + (16 if proto == 6 else 6)
        stored = struct.unpack(">H", pkt[coff:coff + 2])[0]
        if proto == 17 and stored == 0:    # UDP checksum is optional over IPv4
            continue
        seg = bytearray(pkt[t:t + seglen])
        seg[coff - t:coff - t + 2] = b"\x00\x00"
        pseudo = pkt[o + 12:o + 20] + bytes([0, proto]) + struct.pack(">H", seglen)
        if stored != (_cksum(pseudo + bytes(seg)) or 0xFFFF):
            bad += 1
    return [f"{bad} of {n} packets have checksums that do not verify"] if bad else []


def check_tshark(path, protocols):
    """Wireshark's dissector must recognise the traffic and find no damage."""
    problems = []
    if not shutil.which("tshark"):
        return ["tshark not installed - cannot run this check"]

    phs = sh(["tshark", "-r", path, "-q", "-z", "io,phs"]).stdout
    for proto in protocols:
        if f"\n  {proto}" not in phs and f"    {proto}" not in phs and proto not in phs:
            problems.append(f"tshark did not dissect any {proto}")

    malformed = sh(["tshark", "-r", path, "-Y", "_ws.malformed"]).stdout.strip()
    if malformed:
        problems.append(f"malformed packets: {len(malformed.splitlines())}")

    bad = sh(["tshark", "-r", path,
              "-o", "tcp.check_checksum:TRUE", "-o", "ip.check_checksum:TRUE",
              "-o", "udp.check_checksum:TRUE",
              "-Y", "tcp.checksum.status==0 || ip.checksum.status==0 "
                    "|| udp.checksum.status==0"]).stdout.strip()
    if bad:
        problems.append(f"bad checksums: {len(bad.splitlines())} packets")
    return problems


ZEEK_PATHS = ["/opt/zeek-install/bin/zeek", "/usr/local/zeek/bin/zeek",
              "/opt/zeek/bin/zeek", "/usr/bin/zeek"]


def find_zeek():
    """Zeek is rarely on PATH -- it installs to its own prefix."""
    cand = os.environ.get("ZEEK") or shutil.which("zeek")
    if cand and os.path.exists(cand):
        return cand
    for p in ZEEK_PATHS:
        if os.path.exists(p):
            return p
    return None


def check_zeek(path, expected):
    """Zeek must produce the logs Security Onion would index."""
    zeek = find_zeek()
    if not zeek:
        return ["zeek not found - THIS IS THE CHECK THAT MATTERS. Set $ZEEK or see lab/README.md"]

    problems = []
    with tempfile.TemporaryDirectory() as d:
        r = sh([zeek, "-C", "-r", os.path.abspath(path),
                "LogAscii::use_json=T"], cwd=d)
        if r.returncode != 0:
            return [f"zeek exited {r.returncode}: {r.stderr.strip()[:200]}"]
        produced = sorted(f for f in os.listdir(d) if f.endswith(".log"))

        for logname, (minrows, fields) in expected.items():
            if logname not in produced:
                problems.append(f"no {logname} (zeek wrote: {', '.join(produced) or 'nothing'})")
                continue
            rows = []
            with open(os.path.join(d, logname)) as fh:
                for line in fh:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        try:
                            rows.append(json.loads(line))
                        except json.JSONDecodeError:
                            pass
            if len(rows) < minrows:
                problems.append(f"{logname}: {len(rows)} rows, expected >= {minrows}")
            for field in fields:
                if not any(r.get(field) not in (None, "", [], "-") for r in rows):
                    problems.append(f"{logname}: field '{field}' never populated")
    return problems


def main(directory):
    caps = sorted(f for f in os.listdir(directory) if f.endswith(".pcap"))
    if not caps:
        sys.exit(f"no captures in {directory}")

    zeek = find_zeek()
    ver = sh([zeek, "--version"]).stdout.strip().splitlines()[0] if zeek else "not found"
    tsv = sh(["tshark", "--version"]).stdout.split("\n")[0] if shutil.which("tshark") else "not found"
    print(f"zeek:   {ver}\ntshark: {tsv}")

    failed = False
    for cap in caps:
        path = os.path.join(directory, cap)
        spec = EXPECTED.get(cap)
        print(f"\n{cap}")
        if not spec:
            print(f"  {YELLOW}?{RESET} no expectations defined - add it to EXPECTED")
            continue

        problems = check_checksums(path)
        print(f"  {RED + 'FAIL' + RESET if problems else GREEN + 'ok  ' + RESET}  checksums (computed here, not asked)")
        for p in problems:
            print(f"         - {p}")
        failed |= bool(problems)

        problems = check_tshark(path, spec["tshark_protocols"])
        print(f"  {RED + 'FAIL' + RESET if problems else GREEN + 'ok  ' + RESET}  wireshark dissection")
        for p in problems:
            print(f"         - {p}")
        failed |= bool(problems)

        problems = check_zeek(path, spec["zeek"])
        print(f"  {RED + 'FAIL' + RESET if problems else GREEN + 'ok  ' + RESET}  zeek log generation")
        for p in problems:
            print(f"         - {p}")
        failed |= bool(problems)

    print("\n" + ("FAILED - do not ship these captures" if failed else "all captures pass"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "assets/pcaps"))
