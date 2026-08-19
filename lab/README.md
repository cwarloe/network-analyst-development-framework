# The capture lab

Every capture this project ships is generated here and validated before it is used.

## Why not just download a public dataset

[R004](../docs/research/R004-pcap-and-telemetry-sourcing.md) worked out which public corpora can lawfully be republished under this repository's licence. The answer is: some of them, with citations. That research stands and those sources are still the right choice for lesson 07, where realistic attack traffic matters more than control.

For lessons 02, 03 and 04 — normal behaviour, expected shapes, baselines — generating the traffic is simply better:

- **Ground truth is known.** The lesson can state what happened because the lab made it happen. An incidental public capture does not come with a correct answer.
- **The files are tiny.** Twenty packets instead of a gigabyte.
- **No licence surface at all.** Nothing to cite, nothing to re-verify, nothing that changes terms next year.
- **A learner can regenerate them** and watch the same behaviour occur live, which no downloaded file allows.

The traffic is real. Real sockets, real DNS resolvers on the public internet, a real TLS stack negotiating real ciphers. Nothing is synthesised packet by packet. What the lab controls is the *situation*, not the protocol behaviour.

## The standard a capture has to meet

**A capture is usable if the tools a learner will point at it can read it. Both of them.**

1. **Wireshark must dissect it cleanly** — the protocol is recognised, no malformed packets, checksums verify.
2. **Zeek must parse it into logs** — a DNS capture produces a `dns.log`, a TLS capture produces `ssl.log` and `x509.log`, and the fields an analyst would pivot on are populated.

The second check is the one that decides. The target environment for this material is Security Onion with the Elastic stack, where analysts work in Hunt and Kibana against Zeek logs and only pivot to the packets when the logs raise a question. A capture that Wireshark renders beautifully but Zeek will not parse is **invisible** in that workflow. It teaches nothing, because nobody would ever find it.

This applies regardless of where a capture came from. A file pulled off a production tap that Zeek chokes on is a bad file for training purposes. Real is not the standard; **ingestible and correctly interpreted** is the standard. Begin with the end in mind: the end is a searchable log in Kibana.

Anonymisation has to respect this too. Rewriting addresses is fine; rewriting them into something Zeek then misreads is not. That is why the rewriter recomputes checksums rather than leaving them stale, and why validation runs after anonymisation rather than before.

## Running it

```bash
# generate (needs root for tcpdump, and outbound DNS for lesson 03)
sudo python3 lab/generate-captures.py assets/pcaps

# validate -- must pass before anything is committed
python3 lab/validate-captures.py assets/pcaps
```

Requirements: `tcpdump`, `openssl`, `python3`, `tshark`, and — for the check that counts — `zeek`.

The validator looks for `zeek` on `PATH` and then at `/opt/zeek-install/bin/zeek`. If Zeek is missing it says so and fails, rather than passing quietly on the Wireshark half alone. A green Wireshark check with no Zeek check is not a pass.

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

Addresses, ports and MACs change. Timing, sequence numbers, payloads, TLS records and protocol behaviour do not. IP and TCP checksums are recomputed so the result verifies clean.

The DNS capture is not rewritten. It was taken on a real interface whose address is already in `192.0.2.0/24`, and the resolvers in it are public infrastructure.

## Adding a capture

1. Add a generator function to `generate-captures.py`.
2. Add an entry to `EXPECTED` in `validate-captures.py` naming the Zeek logs it must produce and the fields that must be populated.
3. Run both. If validation fails, the capture is wrong — fix the capture, not the expectation.
