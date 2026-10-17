# Milestone 2 Review & Scoring Guide — Path Failure, Evidence Vantage, and Encryption

## Purpose of This Milestone Evaluation
Milestone 2 evaluates the learner's ability to integrate:
- **Lesson 04:** Declaring the boundary of encrypted traffic (TLS 1.2 vs 1.3) without succumbing to suspicion bias.
- **Lesson 05:** Prioritizing evidence collection by perishability clocks, identifying collection traps, and accounting for vantage point limits.
- **Lesson 06:** Discriminating transport states (`REJ`, `S0`, `SF`, `RSTR`) and network vs application latency using packet delta times.

---

## 1. Exemplary Model Deliverable

### Section 1: TLS 1.3 Visibility Boundary & Deconstruction
- **Observable from Wire (Item E-02):**
  - Frame 201 shows cleartext Server Name Indication (`SNI: vault-saas.harrowmere-cloud.example`).
  - Frame 202 shows server selected TLS 1.3 (`supported_versions: 0x0304`) and cipher `TLS_AES_256_GCM_SHA384`.
  - Byte volume (1,420 bytes out, 4,850 bytes back) and duration (1.12s) are observable.
- **Unobservable under TLS 1.3:**
  - The server certificate Subject, Issuer, and SHA-256 fingerprint are encapsulated in encrypted Application Data records (Frame 203) and cannot be inspected on the wire.
  - The HTTP request URI, headers, response status code (e.g., 200 vs 500), and payload are fully encrypted.
- **Required Source to Verify:**
  - SaaS Vendor Admin Console (Item E-04) or Workstation EDR/Browser logs.
- **Cognitive Bias Debrief:**
  - The colleague confuses *reduced sensor visibility* with *malicious activity*. TLS 1.3 is the standard modern security protocol; its encryption of server certificates is expected behavior, not an indicator of compromise or MITM.

---

### Section 2: Vantage Point & Evidence Collection Plan
- **The Firewall Log Trap:**
  - The perimeter firewall is configured to log **denied connections only**. Searching this log for `198.51.100.20` and finding zero hits proves only that the firewall did not drop the packets; it does *not* prove packets were permitted or delivered. If a permit rule matched, or if packets were dropped elsewhere, zero logs are produced.
- **Prioritized Evidence Collection Order (Shortest Clock First):**
  1. **HQ Edge Full PCAP (36-hour buffer):** Highest perishability. Must extract and archive capture streams immediately before the ring buffer overwrites.
  2. **SaaS Admin Console (7-day retention):** Check cloud-side server processing latencies.
  3. **Portland Branch Switch NetFlow (14-day retention):** Verify local branch egress volumes.
  4. **Workstation EDR & Edge Zeek (30-day retention):** Stable; can be queried after capturing perishable packet traces.
  5. **Perimeter Firewall (90-day retention):** Lowest priority due to long retention and "denies only" blind spot.
- **Vantage Point Blind Spot:**
  - The HQ edge sensor sees Portland traffic after it transits the IPSec tunnel and passes NAT. It cannot see internal Portland branch east-west traffic or distinguish local switch port congestion without branch-level telemetry.

---

### Section 3: Multi-Fault Causal Classification Matrix

| Target IP | State | Observations & Frame Proof | True Causal Domain / Responsible Team |
|---|---|---|---|
| `198.51.100.30` | `REJ` | Instant RST-ACK returned in 12 µs. Proves path is 100% healthy in both directions. Port 80 is closed. | **Systems / Host Admin** (Web service daemon is down). |
| `198.51.100.20` | `S0` | Repeated SYNs sent with exponential backoff (4s, 2s); zero return packets. | **Network Engineering** (Routing black hole or intermediate drop). |
| `198.51.100.50` | `SF` | Handshake completes in 0.3 ms. Frame 105 shows server TCP ACK in 0.2 ms. 5.0001s delay occurs before Frame 106 HTTP 200. | **Database / Application Team** (Backend slow query processing time, NOT network WAN latency). |
| `203.0.113.50` | `SF` | Normal TLS 1.3 handshake and transaction completion in 1.12s. | **Healthy Production Traffic** (SaaS Vault sync). |

---

### Section 4: The Silent Fragmentation Diagnosis
- **The Root Cause:**
  - The DNS resolver returned a 1,740-byte response over UDP.
  - The IPSec VPN tunnel has an MTU of 1,400 bytes, forcing the IP stack to fragment the datagram into Frame 501 (1,400 bytes, `MF=1, offset=0`) and Frame 502 (380 bytes, `MF=0, offset=170`).
- **The Protocol Trap:**
  - Frame 501 contains the IP header and UDP header, but Wireshark defers UDP dissection until full reassembly, displaying `udp.dstport` only on the terminal fragment (Frame 502).
  - Intermediate security firewalls configured to "Drop non-initial fragments" discard Frame 502 because it lacks a Layer 4 port header.
  - Without Frame 502, reassembly fails entirely. The client stack receives an incomplete datagram, discards it, and times out silently with no ICMP or RST generated.
- **Remediation:**
  - Permit IP fragments on the internal tunnel interface, configure DNS to use EDNS buffer size clamping, or allow TCP fallback for DNS queries exceeding tunnel MTU.

---

## 2. Evaluation Rubric & Capability Scoring

| Capability Target | Proficient Behavior (Pass) | Developing / Novice Trap (Needs Coaching) |
|---|---|---|
| **OC-2 (Encryption Boundary)** | Accurately identifies observable TLS 1.3 fields (SNI, ciphers) and unobservable fields (certs, HTTP data). | Claims TLS 1.3 is "suspicious" or attempts to find certificate hashes in PCAP. |
| **OE-3 / OE-4 (Evidence Planning)** | Prioritizes the 36-hour PCAP buffer; identifies that "denies only" firewall logs cannot prove connectivity. | Queries 90-day firewall log first; relies on absence of deny logs as proof of delivery. |
| **OC-4 / IR-2 (Transport vs App)** | Uses Frame 105 to prove the 5-second delay is server-side application think time. | Blames the network team for "WAN latency" on `198.51.100.50`. |
| **IR-3 (State Discrimination)** | Assigns `REJ` to Systems/Host and `S0` to Network Engineering. | Assigns both `REJ` and `S0` to Network Engineering as "connection failed." |
| **IR-5 / EF-8 (Fragmentation)** | Explains that dropped non-initial fragments cause silent UDP timeouts. | Diagnoses DNS timeout as a dead DNS server or rogue firewall block without checking fragmentation. |
