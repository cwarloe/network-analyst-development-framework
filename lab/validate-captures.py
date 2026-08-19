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
import json, os, shutil, subprocess, sys, tempfile

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


def check_zeek(path, expected):
    """Zeek must produce the logs Security Onion would index."""
    zeek = shutil.which("zeek") or "/opt/zeek-install/bin/zeek"
    if not os.path.exists(zeek):
        return ["zeek not installed - THIS IS THE CHECK THAT MATTERS, install it"]

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

    failed = False
    for cap in caps:
        path = os.path.join(directory, cap)
        spec = EXPECTED.get(cap)
        print(f"\n{cap}")
        if not spec:
            print(f"  {YELLOW}?{RESET} no expectations defined - add it to EXPECTED")
            continue

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
