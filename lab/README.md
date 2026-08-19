# The capture lab

Every capture this project ships is generated here and validated before it is used.

## Why not just download a public dataset

[R004](../docs/research/R004-pcap-and-telemetry-sourcing.md) worked out which public corpora can lawfully be republished under this repository's license. The answer is: some of them, with citations. That research stands and those sources are still the right choice for lesson 07, where realistic attack traffic matters more than control.

For lessons 02, 03 and 04 — normal behavior, expected shapes, baselines — generating the traffic is simply better:

- **Ground truth is known.** The lesson can state what happened because the lab made it happen. An incidental public capture does not come with a correct answer.
- **The files are tiny.** Twenty packets instead of a gigabyte.
- **No license surface at all.** Nothing to cite, nothing to re-verify, nothing that changes terms next year.
- **A learner can regenerate them** and watch the same behavior occur live, which no downloaded file allows.

The traffic is real. Real sockets, real DNS resolvers on the public internet, a real TLS stack negotiating real ciphers. Nothing is synthesised packet by packet. What the lab controls is the *situation*, not the protocol behavior.

## The standard a capture has to meet

**A capture is usable if the tools a learner will point at it can read it. All of them.**

1. **Checksums must verify**, computed by the validator itself rather than asked of a tool. See below for why that distinction is not pedantry.
2. **Wireshark must dissect it cleanly** — the protocol is recognized, no malformed packets.
3. **Zeek must parse it into logs** — a DNS capture produces a `dns.log`, a TLS capture produces `ssl.log` and `x509.log`, and the fields an analyst would pivot on are populated.

The second check is the one that decides. The target environment for this material is Security Onion with the Elastic stack, where analysts work in Hunt and Kibana against Zeek logs and only pivot to the packets when the logs raise a question. A capture that Wireshark renders beautifully but Zeek will not parse is **invisible** in that workflow. It teaches nothing, because nobody would ever find it.

This applies regardless of where a capture came from. A file pulled off a production tap that Zeek chokes on is a bad file for training purposes. Real is not the standard; **ingestible and correctly interpreted** is the standard. Begin with the end in mind: the end is a searchable log in Kibana.

Anonymization has to respect this too. Rewriting addresses is fine; rewriting them into something Zeek then misreads is not. That is why the rewriter recomputes checksums rather than leaving them stale, and why validation runs after anonymization rather than before.

## The captures

| File | Lesson | What it contains | Stable across runs? |
|---|---|---|---|
| `02-conversation.pcap` | [02](../lessons/02-reading-a-conversation.md) | Two TCP+HTTP conversations, one `200` and one `403`, full handshake to teardown | Yes |
| `03-dns.pcap` | [03](../lessons/03-names-and-expectations.md) | Eight live lookups against `1.1.1.1` — CNAME chains, TTL asymmetry, AAAA, and a NOERROR/no-answer response | **No** |
| `04-tls.pcap` | [04](../lessons/04-what-encryption-hides.md) | One TLS 1.2 and one TLS 1.3 handshake from a client that offered both identically | Shape yes, certificate dates no |
| `06-failures.pcap` | [06](../lessons/06-when-it-breaks.md) | Four faults: refused, dropped, reset mid-transfer, slow-but-correct | Yes |
| `07-suspicious.pcap` | [07](../lessons/07-when-its-suspicious.md) | Two shape-identical beacons, a tunnelling-shaped DNS stream, one bulk upload | Mostly — connection counts can vary by one |

Total: about 124 KB.

`03-dns.pcap` is the one that genuinely drifts, because it queries the real internet. Regenerate it and you will get different addresses, different TTLs, and possibly a different cache node answering — which is exactly what [lesson 03](../lessons/03-names-and-expectations.md) is about, but it does mean the specific values quoted in that lesson will no longer match the file. If you regenerate, reread the lesson against the new capture and update the numbers.

`04-tls.pcap` regenerates its certificate each run, so the validity window moves. The handshake structure — which messages are visible in 1.2 and which vanish in 1.3 — does not.

Client source ports are pinned for exactly this reason: the lessons quote port numbers, and ephemeral ports would otherwise change on every run.

## Running it

```bash
# generate (needs root for tcpdump, and outbound DNS for lesson 03)
sudo python3 lab/generate-captures.py assets/pcaps

# validate -- must pass before anything is committed
python3 lab/validate-captures.py assets/pcaps

# check every relative link in the repository still resolves
python3 lab/check-links.py
```

Both checks run automatically on every pull request via [`.github/workflows/checks.yml`](../.github/workflows/checks.yml), which pins the `zeek/zeek:7.0.4` container — the same version the captures were validated against, so a red build means a real regression rather than a version difference.

`validate-captures.py` finds Zeek on `PATH`, at `$ZEEK`, or in the usual install prefixes, and prints the Zeek and tshark versions it used before running. If a check ever disagrees between two machines, those two lines are the first thing to compare.

Requirements: `tcpdump`, `openssl`, `python3`, `tshark`, and — for the check that counts — `zeek`.

The validator looks for `zeek` on `PATH` and then at `/opt/zeek-install/bin/zeek`. If Zeek is missing it says so and fails, rather than passing quietly on the Wireshark half alone. A green Wireshark check with no Zeek check is not a pass.

Zeek is not in the Ubuntu repositories. Install it from the [official packages](https://zeek.org/get-zeek/), or build from source if your network policy blocks the package repository:

```bash
git clone --recursive --depth 1 --branch v7.0.4 https://github.com/zeek/zeek.git
cd zeek && ./configure --prefix=/opt/zeek-install --build-type=Release \
    --disable-zeekctl --disable-auxtools
make -j"$(nproc)" && make install
```

Build dependencies on Ubuntu: `cmake make g++ bison flex libpcap-dev libssl-dev zlib1g-dev python3-dev swig`. It takes a while.

The generator produces DNS by querying `1.1.1.1` live, so lesson 03's capture differs slightly every run: different addresses, different TTLs, different cache nodes answering. That is a feature. The lesson is about what varies legitimately, and a regenerated capture demonstrates the point rather than describing it. If you regenerate it, the specific values quoted in [lesson 03](../lessons/03-names-and-expectations.md) will no longer match, and the lesson text needs updating to whatever the internet said that day.

The HTTP and TLS captures are deterministic in shape and safe to regenerate.

## What gets rewritten

Loopback captures are rewritten into RFC 5737 documentation ranges so they read as a conversation between two hosts:

| | |
|---|---|
| Client | `192.0.2.10`, MAC `00:1c:42:1a:2b:3c` |
| Server A | `198.51.100.20` |
| Server B | `198.51.100.30` |
| Ports | `8080` → `80`, `8443`/`8444` → `443` |

Addresses, ports and MACs change. Timing, sequence numbers, payloads, TLS records and protocol behavior do not. IP and TCP checksums are recomputed so the result verifies clean.

The DNS capture is not rewritten. It was taken on a real interface whose address is already in `192.0.2.0/24`, and the resolvers in it are public infrastructure.

## Adding a capture

1. Add a generator function to `generate-captures.py`.
2. Add an entry to `EXPECTED` in `validate-captures.py` naming the Zeek logs it must produce and the fields that must be populated.
3. Run both. If validation fails, the capture is wrong — fix the capture, not the expectation.

### Why the checksum check does its own arithmetic

The first time CI ran, it failed on `03-dns.pcap`: sixteen packets with bad UDP checksums. The same file had passed locally minutes earlier.

Neither machine was lying. **tshark 4.2.2 reported every UDP checksum in that file as good; tshark 4.0.17 reported every one as bad.** Computing them by hand settled it — the 4.0.17 verdict was correct and the file was genuinely defective. The DNS capture is the only one taken on a live interface rather than loopback, and it was the only one that never went through the rewriter, so nothing had ever recomputed its checksums.

Two things came out of that, and both are now in the code:

- `fix_checksums()` runs over the DNS capture, so live-interface artifacts do not ship.
- The validator computes checksums itself instead of asking tshark. A gate that trusts one tool's verdict is only as strong as that tool's version, and arithmetic does not have versions.

It is worth noticing what nearly happened. A defective file passed a green local check for several hours because the tool consulted happened to be wrong about it. That is the same failure the lessons keep pointing at — a confident, correct-looking answer to a question the instrument could not actually settle.

The gate has already earned itself three times. It caught a `403` response advertising `Content-Length: 43` for a 44-byte body, and it caught plaintext HTTP mapped to port 443, which made Zeek run the SSL analyzer and log a protocol violation that was an artefact of the anonymization rather than anything in the traffic. Both would have shipped as "looks fine in Wireshark."
