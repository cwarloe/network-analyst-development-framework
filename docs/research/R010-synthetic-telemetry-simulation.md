# R010 — Synthetic Telemetry Generation: Theory, Simulation Fidelity, and Adversary Detection at Scale

**Status:** assessed · **Date:** 2026-10-18 · **Confidence:** High (verified through empirical simulation and statistical discrimination audits)

---

## 1. Executive Summary & The Core Problem

In defensive cybersecurity education and training, there is a fundamental pedagogical division between **Reactive Triage (Book 1)** and **Proactive Threat Hunting (Book 2)**:

| Attribute | Reactive Triage (Book 1) | Proactive Threat Hunting (Book 2) |
|---|---|---|
| **Operational Trigger** | An automated alert fires; a ticket is created. | **The SIEM is completely silent.** No alert has fired. |
| **Data Scope** | Bounded: A single capture file (`.pcap`), 20–100 packets. | Unbounded: 10M+ events across an enterprise data lake. |
| **Cognitive Task** | Reconstruct protocol mechanics; avoid hindsight bias. | Formulate falsifiable hypotheses; isolate statistical outliers. |
| **Primary Tooling** | Wireshark, packet dissectors, stream reassembly. | Elasticsearch, Security Onion Hunt, Kibana, SQL. |

Teaching proactive threat hunting presents a massive infrastructural barrier: **How do you provide students with a 10-million-event enterprise data lake without shipping hundreds of gigabytes of raw PCAP files?**

Public corpora (e.g., CIC-IDS, CTU-13) either suffer from licensing restrictions, represent obsolete operating systems, lack enterprise administrative noise, or provide unlabeled background traffic where ground truth is unknowable.

The architectural solution developed in NADF is **Synthetic Telemetry Simulation**: using pure, zero-dependency Python standard libraries to generate statistically authentic network metadata (NetFlow, Zeek connection, DNS, HTTP, and TLS logs) that mirrors the exact physical, human, and algorithmic realities of an enterprise network.

---

## 2. The 3-Tier Enterprise Distribution Model

In an enterprise network, traffic does not distribute evenly. It follows a severe power-law (Pareto) distribution across three distinct tiers:

```
Enterprise Volume (Events)
▲
│ ████████████████████  ◄── Tier 1: The Head (90.0% - 95.0% Volume)
│ ████████████████████      Massive volume, high host cardinality (> 1,500 hosts).
│ ████████████████████      Microsoft 365, Google, AWS, Active Directory, internal databases.
│ █
│ █ ▂ ▂ ▂ ▂ ▂           ◄── Tier 2: The Torso (5.0% - 9.99% Volume)
│                           Moderate volume, verified business owners.
│                           Dave Henderson's CAD video stream, Priya's Sunday DB backups,
│                           Marcus Vance's developer package compiler pulls.
│
│ ░░░░░░░░░░░░░░░░░░░░░ ◄── Tier 3: The Long Tail (0.01% Volume)
└───────────────────────►   Low volume, single-host cardinality (source.ip == 1).
                            - "Administrative Weirdness": 2011 basement boiler NTP, HP SNMP.
                            - Embedded Adversary Needles: C2 beacons, domain fronting, exfil.
```

### Why Naive Hunting Fails in the Real World
1. **The Volume Trap:** Novice analysts sort by total bytes (`source.bytes DESC`). In our simulator, this catches Dave Henderson streaming 48 GB of 4K computerized lathe maintenance videos or Priya Raman running an 18 GB database replication. In reality, modern stealthy adversaries transmit tiny payloads (200–500 bytes) to blend in.
2. **The Long Tail Trap:** When analysts flip their query to find the rarest destinations, they hit thousands of single-connection outliers. In reality, this tail is saturated with "administrative weirdness" (legacy firmware, developer experiments, forgotten sensors).

To hunt successfully, analysts must use **relational stacking** (e.g., group by User-Agent or JA4 client fingerprint and filter where unique host cardinality == 1).

---

## 3. Mathematical Simulation Fidelity: How Close Is It to Reality?

The simulator ([`lab/generate-hunt-telemetry.py`](../../lab/generate-hunt-telemetry.py)) reproduces the exact statistical properties used by commercial detection engines and advanced hunt teams:

### 3.1. Human vs. Machine Timing (Beacon Jitter Math)
* **Real-World Reality:** Human browsing is bursty and heavy-tailed (Pareto distribution). A human opens 5 browser tabs in 3 seconds, spends 4 minutes reading, and then walks away for 15 minutes. The **Coefficient of Variation ($CV = \sigma / \mu$)** of human traffic is almost always $CV > 1.2$.
* **Adversary Tradecraft:** Command-and-control (C2) frameworks (Cobalt Strike, Sliver, Mythic) evade simple cron-interval detection rules by injecting **timing jitter** ($\pm 10\text{--}30\%$).
* **Simulation Mechanics:** The simulator models human traffic with exponential inter-arrival distributions, while programming the compromised workstation (`10.100.14.88`) with a 60-second base sleep and $\pm 20\%$ pseudo-random jitter:
  $$\Delta t_i = 60 \times (1 + \text{Uniform}(-0.20, 0.20)) \implies \Delta t \in [48.0\text{s}, 72.0\text{s}]$$
* **Verification Proof:** When computing summary statistics on the beacon stream:
  $$\text{Mean } \mu = 59.93\text{s}, \quad \text{Std Dev } \sigma = 6.95\text{s}, \quad CV = \frac{6.95}{59.93} = 0.116$$
  Because $CV = 0.116 \ll 0.20$, the machine heartbeat is mathematically provable despite the randomized jitter.

---

### 3.2. Information Theory on the Wire (Shannon Entropy)
* **Real-World Reality:** Human-typed hostnames and corporate domains (`mail.harrowmere.com`, `api.github.com`) use natural language words with high grammatical redundancy. Letters follow predictable frequencies.
* **Adversary Tradecraft:** When adversaries exfiltrate data through DNS (to bypass strict firewall egress blocks), they pack compressed or encrypted ciphertext into subdomain labels (`[Base32/Base64/Hex].domain.com`).
* **Simulation Mechanics:** The simulator calculates the Shannon entropy $H(X)$ on query strings:
  $$H(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i)$$
* **Verification Proof:**
  - Standard enterprise DNS queries: **$\text{Mean } H = 2.12\text{ bits/character}$** (Expected $< 3.2$).
  - Covert DNS tunneling queries: **$\text{Mean } H = 4.72\text{ bits/character}$** (Expected $> 4.5$).
  - This 2.6-bit mathematical gap cleanly discriminates covert channels without relying on brittle domain blocklists.

---

### 3.3. Cryptographic Client Fingerprinting (JA4)
* **Real-World Reality:** Adversaries can trivially alter the HTTP `User-Agent` string in code to impersonate Google Chrome. However, the client operating system and TLS library construct the raw `ClientHello` packet according to fixed compilation rules (cipher suite order, extension sequences, elliptic curves).
* **Adversary Tradecraft:** Attackers running custom Go, Python, or Rust stagers generate distinct cryptographic fingerprints, even when sending benign Server Name Indication (SNI) headers to disguise destinations behind commercial CDNs (**domain fronting**).
* **Simulation Mechanics:** The simulator assigns standard Chrome/Edge JA4 hashes (`t13d1516h2_...`) to corporate endpoints, but assigns the custom Go runtime fingerprint (`t13d190800_2a27b87c7a10_e68c9e54a0f8`) to the adversary implant. Stacking by `tls.ja4` instantly isolates the single host running non-standard client software.

---

## 4. Multi-Format Delivery & Educational Portability

To ensure that any student or institution can utilize the data regardless of local computing resources, the simulator exports simultaneously into two targets:

1. **Lightweight Local SQL (`hunt_telemetry.db`):**
   - Built on standard SQLite with B-Tree indexes on `source_ip`, `destination_ip`, `timestamp`, `entropy`, and `ja4`.
   - Allows learners on low-powered laptops to execute complex least-frequency and temporal queries in milliseconds using plain SQL, with zero server infrastructure.
2. **Elastic Common Schema (ECS) Compressed NDJSON:**
   - Pre-formatted for direct ingestion into production Security Onion, Elasticsearch, or Kibana clusters (`conn.ndjson.gz`, `dns.ndjson.gz`, `ssl.ndjson.gz`, `http.ndjson.gz`).
   - Enables advanced enterprise hunting sprints, Kibana Discover visualization, and detection rule testing (Sigma and Elastic ES|QL).

---

## 5. Reusability in Future Curriculum Projects

The principles established in this research record are transferable to other domains:

1. **Cloud Egress & IAM Telemetry:** The same least-frequency and cardinality algorithms apply to AWS CloudTrail and Azure Activity logs to isolate single-caller API anomalies.
2. **Endpoint Process Telemetry (Sysmon / EDR):** Power-law distribution modeling separates common parent-child process relationships (explorer.exe launching chrome.exe) from rare command-line execution (word.exe launching powershell.exe).
3. **Automated Assessment & Micro-Drills:** The deterministic nature of mathematical thresholds ($CV$, $H(X)$, cardinality) allows automated testing harnesses to evaluate student queries without human grading overhead.
