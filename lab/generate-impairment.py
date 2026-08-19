#!/usr/bin/env python3
"""Generate the impairment captures lesson 06 is missing: latency and loss.

WHY THIS IS A SEPARATE SCRIPT
    Everything in generate-captures.py runs without special privileges. This
    does not. It needs root, NET_ADMIN, and the netem kernel module, none of
    which were available where the rest of the lab was built. Keeping it
    separate means the main generator never fails on a machine without netem.

WHAT IT TOUCHES
    Nothing of yours. All traffic runs between a veth pair, with one end
    inside a dedicated network namespace called `nadf-lab`. Your real
    interfaces, routes and firewall rules are never modified. The namespace
    and veth are removed on exit, including on error or Ctrl-C.

    The one thing to know: if a namespace called `nadf-lab` already exists,
    this refuses to run rather than clobbering it.

USAGE
    sudo python3 lab/generate-impairment.py [output-dir]

    Default output directory is assets/pcaps/ relative to the repo root.

REQUIRES
    root, iproute2 (`ip`), tcpdump, python3, and a kernel with sch_netem.
    On Debian/Ubuntu: apt-get install iproute2 tcpdump
"""
import atexit
import importlib.util
import os
import signal
import socket
import subprocess
import sys
import threading
import time

NS = "nadf-lab"
VETH_HOST, VETH_NS = "nadf-a", "nadf-b"
CLIENT_IP, SERVER_IP = "192.0.2.10", "198.51.100.60"   # match the other captures
PORT = 8080

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(REPO, "assets", "pcaps")


# ------------------------------------------------------------------ helpers --
def run(cmd, check=True, ns=False):
    """Run a command, optionally inside the lab namespace."""
    if ns:
        cmd = ["ip", "netns", "exec", NS] + cmd
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)}\n{r.stderr.strip()}")
    return r


def preflight():
    problems = []
    if os.geteuid() != 0:
        problems.append("not root -- rerun with sudo")
    for tool in ("ip", "tcpdump"):
        if subprocess.run(["which", tool], capture_output=True).returncode != 0:
            problems.append(f"{tool} not found (apt-get install iproute2 tcpdump)")
    if subprocess.run(["ip", "netns", "list"], capture_output=True,
                      text=True).stdout.find(NS) >= 0:
        problems.append(f"a network namespace called {NS!r} already exists -- "
                        f"remove it with `ip netns del {NS}` if it is stale")
    if problems:
        print("Cannot run:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)


def netem_available():
    """Check the kernel actually has netem before building anything."""
    run(["ip", "link", "add", "nadf-probe", "type", "dummy"], check=False)
    ok = run(["tc", "qdisc", "add", "dev", "nadf-probe", "root", "netem",
              "delay", "1ms"], check=False).returncode == 0
    run(["ip", "link", "del", "nadf-probe"], check=False)
    return ok


# ------------------------------------------------------------- environment --
def teardown():
    run(["ip", "netns", "del", NS], check=False)
    run(["ip", "link", "del", VETH_HOST], check=False)


def setup():
    """Client on the host side, server inside the namespace, one veth between."""
    run(["ip", "netns", "add", NS])
    run(["ip", "link", "add", VETH_HOST, "type", "veth", "peer", "name", VETH_NS])
    run(["ip", "link", "set", VETH_NS, "netns", NS])

    run(["ip", "addr", "add", f"{CLIENT_IP}/32", "dev", VETH_HOST])
    run(["ip", "link", "set", VETH_HOST, "up"])
    run(["ip", "route", "add", f"{SERVER_IP}/32", "dev", VETH_HOST])

    run(["ip", "addr", "add", f"{SERVER_IP}/32", "dev", VETH_NS], ns=True)
    run(["ip", "link", "set", VETH_NS, "up"], ns=True)
    run(["ip", "link", "set", "lo", "up"], ns=True)
    run(["ip", "route", "add", f"{CLIENT_IP}/32", "dev", VETH_NS], ns=True)

    # checksum offload on veth leaves outgoing checksums unset in the capture;
    # turning it off means the packets we record verify like real ones
    for dev, in_ns in ((VETH_HOST, False), (VETH_NS, True)):
        for feature in ("tx", "rx", "tso", "gso", "gro"):
            run(["ethtool", "-K", dev, feature, "off"], check=False, ns=in_ns)


def impair(*args):
    """Replace the qdisc on the namespace side of the link."""
    run(["tc", "qdisc", "del", "dev", VETH_NS, "root"], check=False, ns=True)
    if args:
        run(["tc", "qdisc", "add", "dev", VETH_NS, "root", "netem"] + list(args), ns=True)


# ----------------------------------------------------------------- server ---
BODY = (b'{"report":"finance-export","rows":1284,'
        b'"generated":"2026-08-19T09:14:22Z","format":"json"}')
PAYLOAD = b"A" * 40000        # large enough to need many segments, so loss shows


def server():
    """Runs inside the namespace. Small response, or a large one on /bulk."""
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((SERVER_IP, PORT))
    srv.listen(8)
    while True:
        try:
            c, _ = srv.accept()
            path = c.recv(4096).split(b" ")[1]
            body = PAYLOAD if path.startswith(b"/bulk") else BODY
            c.sendall(b"HTTP/1.1 200 OK\r\nServer: nginx/1.24.0\r\n"
                      b"Content-Type: application/json\r\nContent-Length: "
                      + str(len(body)).encode() + b"\r\n\r\n" + body)
            c.close()
        except Exception:
            pass


def start_server():
    """Fork into the namespace so the listener lives on the far side."""
    pid = os.fork()
    if pid == 0:
        os.execvp("ip", ["ip", "netns", "exec", NS, sys.executable, __file__, "--server"])
    return pid


def fetch(path, src_port, timeout=30):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((CLIENT_IP, src_port))
    s.settimeout(timeout)
    t0 = time.time()
    s.connect((SERVER_IP, PORT))
    s.sendall(b"GET " + path + b" HTTP/1.1\r\nHost: files.contoso-internal.example\r\n"
              b"User-Agent: contoso-sync/3.2\r\nConnection: close\r\n\r\n")
    n = 0
    while True:
        d = s.recv(65535)
        if not d:
            break
        n += len(d)
    s.close()
    return n, time.time() - t0


# ------------------------------------------------------------------ capture --
def capture(path, bpf):
    p = subprocess.Popen(["tcpdump", "-i", VETH_HOST, "-U", "-w", path, "-s", "0", bpf],
                         stderr=subprocess.DEVNULL)
    time.sleep(2)
    return p


def stop(p):
    time.sleep(2)
    p.send_signal(signal.SIGINT)
    p.wait()


def fix_checksums(path):
    """Reuse the main generator's repair, which is fragment-aware."""
    spec = importlib.util.spec_from_file_location(
        "gen", os.path.join(REPO, "lab", "generate-captures.py"))
    m = importlib.util.module_from_spec(spec)
    m.__name__ = "gen"
    spec.loader.exec_module(m)
    m.fix_checksums(path)


# ------------------------------------------------------------------- cases --
def case_latency():
    """200 ms each way. The delay is in the handshake, not the response."""
    out = os.path.join(OUT, "06-latency.pcap")
    impair("delay", "200ms", "20ms", "distribution", "normal")
    cap = capture(out, f"host {SERVER_IP}")
    n, secs = fetch(b"/api/v2/export?page=1", 41100)
    stop(cap)
    fix_checksums(out)
    print(f"  latency : {n} bytes in {secs:.2f}s -> {out}")


def case_loss():
    """12% loss on a transfer big enough to need many segments."""
    out = os.path.join(OUT, "06-loss.pcap")
    impair("loss", "12%")
    cap = capture(out, f"host {SERVER_IP}")
    try:
        n, secs = fetch(b"/bulk", 41101, timeout=60)
        print(f"  loss    : {n} bytes in {secs:.2f}s -> {out}")
    except Exception as e:
        print(f"  loss    : transfer did not complete ({type(e).__name__}) -- "
              f"still a usable capture")
    stop(cap)
    fix_checksums(out)


# -------------------------------------------------------------------- main --
def main():
    if "--server" in sys.argv:          # re-entry inside the namespace
        server()
        return

    preflight()
    if not netem_available():
        print("Cannot run: the kernel has no sch_netem module.\n"
              "  Debian/Ubuntu: apt-get install linux-modules-extra-$(uname -r)\n"
              "  then: modprobe sch_netem")
        sys.exit(1)

    os.makedirs(OUT, exist_ok=True)
    atexit.register(teardown)
    print(f"building {NS} namespace ...")
    setup()

    pid = start_server()
    time.sleep(1.5)
    try:
        case_latency()
        case_loss()
    finally:
        os.kill(pid, signal.SIGTERM)
        os.waitpid(pid, 0)

    print(f"\ndone -> {OUT}")
    print("\nNext:")
    print("  python3 lab/validate-captures.py assets/pcaps")
    print("  git checkout -b lab/impairment-captures")
    print("  git add assets/pcaps/06-latency.pcap assets/pcaps/06-loss.pcap")
    print("  git commit -m 'lab: add latency and loss captures' && git push -u origin HEAD")


if __name__ == "__main__":
    main()
