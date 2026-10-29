# Book 2 — The Hunter's Eye: Hypothesis-Driven Network Threat Hunting at Scale

> **Status:** Active Curriculum & Architectural Baseline for Book 2  
> **Prerequisites:** Completion of [Book 1 — Learning to See](BOOK-1.md) (Lessons 01–09 & Capstone).  
> **Operational Paradigm:** Proactive, Self-Directed Threat Hunting & Detection Engineering across enterprise-scale telemetry in Security Onion, Elasticsearch, and Kibana.

---

## 1. The Core Paradigm Shift

In Book 1 (*Learning to See*), the analyst was **reactive**: an alert fired, a ticket was assigned (`SEC-4021`), and the data was bounded to a single connection or capture file. The analyst's job was to prevent hindsight bias, separate observation from interpretation, and make a safe operational call.

In Book 2 (*The Hunter's Eye*), the analyst is **proactive**:

> **The SIEM is completely silent. No ticket has been opened. No alert has fired.**  
> You are staring at 45 million connection records, 18 million DNS queries, and 9 million TLS handshakes across Harrowmere's multi-site enterprise over a 14-day window. Somewhere in that haystack, an adversary has established persistence.

Your job is not to wait for an alert. Your job is to formulate a testable hypothesis, query the data lake, isolate the statistical anomalies that signatures missed, pivot across telemetry sources, uncover the adversary campaign, and author the permanent detection rule that stops it from ever being silent again.

---

## 2. The Recurring Move: The Proactive Hunt Loop

Across Book 2, the hunter repeatedly executes the 6-phase **Proactive Hunt Loop**:

```
Threat Model & Intelligence
           ↓
[ 1. Falsifiable Hypothesis ] ──► "If an adversary is doing X, we will observe Y in telemetry Z."
           ↓
[ 2. Telemetry Scoping ] ──────► Construct precise Elastic (ES|QL / KQL / Lucene) & Zeek queries.
           ↓
[ 3. Outlier Stacking ] ───────► Long-tail / least-frequency analysis & statistical aggregation.
           ↓
[ 4. Behavioral Pivoting ] ────► Converge DNS + TLS (JA4) + Flow + Rolling PCAP slice.
           ↓
[ 5. Adversary Discrimination ] ─► Separate administrative weirdness from malicious intent.
           ↓
[ 6. Detection Engineering ] ──► Author Sigma / Elastic / Zeek rules to eliminate the blind spot.
```

---

## 3. Persistent Setting & Expanding Cast

The setting remains **Harrowmere Equipment Group**, now months into Ethan's tenure. Having proven his analytical discipline during the Book 1 capstone, Ethan transitions from the Tier-1/2 triage queue into Harrowmere's **Proactive Threat Hunting & Detection Engineering Pod**.

* **Ethan Mercer:** Now confident in reading individual packets and conversations, Ethan faces a new kind of vertigo: *scale*. Looking at 50 million rows of data, his old habit of opening a capture in Wireshark is impossible. He must learn to think statistically and query relationally.
* **Cal Rowan (Security Engineer):** Takes on a primary mentorship role alongside Dana. Cal owns Harrowmere's Elasticsearch clusters, Zeek sensors, logstash pipelines, and Security Onion Hunt interfaces. Cal teaches Ethan how search engines actually index telemetry, why queries choke under scale, and how to write efficient aggregations.
* **Owen Kline (Senior Analyst):** The institutional memory. When Ethan finds an anomaly with 1 event in 10 million and thinks he's found APT29, Owen is the reality check: *"That's just the heating control daemon in the Portland warehouse that hasn't been rebooted since 2018."*
* **Dana Shah (Principal Analyst):** Steps back from day-to-day oversight, reviewing Ethan's hunt packages and holding the line on epistemic rigor: *"A hunting hypothesis that cannot be disproven by your query is just a fishing expedition."*
* **Nia Alvarez (SOC Manager):** Allocates hunt sprint cycles. Demands that every hunt produce two deliverables: an **Adversary Assessment** and a **Permanent Detection Rule**.

---

## 4. The Five Advanced Hunting Modules

| Module | Title | Core Analytical Discipline | Security Onion / Elastic Workbench | Target Telemetry |
|---|---|---|---|---|
| **H-01** | **The Falsifiable Hypothesis** | Moving from alert consumption to threat modeling; structuring hunts that cannot be satisfied by confirmation bias. | Translating MITRE ATT&CK techniques into structured Elastic queries; mapping visibility boundaries. | `conn.log`, `dns.log`, `ssl.log` |
| **H-02** | **The Long Tail & Stacking Analysis** | Least-Frequency Analysis (LFA): isolating the 1-in-a-million outlier across multi-host enterprise fleets. | Terms aggregations, cardinality counts, rare destination stacking, single-host egress isolation. | Fleet-wide NetFlow, Zeek `conn`, `http.log` |
| **H-03** | **Beaconing & Statistical Jitter** | Detecting automated C2 check-ins without signatures; computing delta-time variance ($\Delta t$) and packet size clustering. | Elasticsearch Date Histogram aggregations, standard deviation profiling, duration vs. byte scatter. | `conn.log` (`duration`, `orig_bytes`, `resp_bytes`) |
| **H-04** | **Domain & TLS Clustering** | Uncovering high-volume tunneling, DGA domains, and unauthenticated SNI divergence in enterprise noise. | JA4/JA3 fingerprint stacking, Shannon entropy calculations on DNS query labels, CNAME depth analysis. | `dns.log`, `ssl.log`, `x509.log` |
| **H-05** | **The Whole-Fleet Hunt Crucible (Capstone)** | **Unsupervised Enterprise Dataset:** 14 days of raw enterprise logs (10M+ events) containing three stealthy adversary campaigns. | Autonomous end-to-end hunt: formulate hypotheses, execute queries, pivot to PCAP, isolate campaigns, and author detection rules. | Full Enterprise Multi-Source Telemetry Packet |

---

## 5. Module Syllabi & Specifications

### Module H-01: The Falsifiable Hypothesis
* **The Situation:** Nia allocates Ethan his first 3-day hunt sprint. Ethan opens Kibana and starts typing random IP queries and browsing dashboards. Cal stops him: *"Browsing is not hunting. If you don't know what evidence would prove you wrong before you hit enter, you will find whatever you want to believe."*
* **Core Competencies:**
  - Formulating hypotheses with explicit **Falsification Criteria**.
  - Query construction in Elastic (KQL, ES|QL, and Lucene).
  - Understanding pipeline ingestion drops and field normalization across Zeek and Elastic Common Schema (ECS).
* **Work Product:** A formal 1-page **Hunt Package Specification** defining the threat model, required telemetry, search syntax, and expected baseline false-positives.

---

### Module H-02: The Long Tail & Stacking Analysis
* **The Situation:** An unknown actor has compromised a single laptop in Harrowmere's engineering wing and established egress. No signature alerts fired because the malware communicates over standard HTTPS to a low-profile cloud instance.
* **Core Competencies:**
  - The mathematics of the Long Tail: why the most common 1% of network destinations account for 95% of traffic volume.
  - Stacking external destinations by `cardinality: source.ip == 1`.
  - User-Agent stacking: finding the single endpoint in 2,000 workstations running an unauthorized Python or PowerShell web client.
* **Work Product:** An **Outlier Stacking Ledger** identifying 3 suspicious long-tail anomalies from a 500,000-connection sample, with the specific justification that ruled out normal enterprise noise.

---

### Module H-03: Beaconing & Statistical Jitter
* **The Situation:** An implant uses jittered beaconing: it checks in approximately every 60 seconds, but adds $\pm 20\%$ random variation (48s to 72s) to bypass rigid interval detection rules.
* **Core Competencies:**
  - Inter-packet delta timing calculation ($\Delta t$).
  - Using Elasticsearch aggregations to calculate mean, median, and variance across connection intervals.
  - Decoupling beacon frequency from data payload size (distinguishing heartbeat pings from bulk exfiltration transfers).
* **Work Product:** A **Temporal Beacon Analysis Brief** graphing connection intervals across time, calculating jitter percentages, and proving machine automation over human web browsing.

---

### Module H-04: Domain & TLS Clustering
* **The Situation:** Ethan investigates DNS and TLS egress. An adversary is using DNS TXT records to stage commands and domain fronting to disguise C2 endpoints under trusted CDN infrastructure.
* **Core Competencies:**
  - Measuring Shannon entropy on DNS query labels to differentiate human-typed hostnames from algorithmically generated domains (DGA) and encoded data tunnels.
  - Stacking client TLS handshakes via **JA4 fingerprints** to identify anomalous non-browser TLS stacks originating from standard workstations.
  - Spotting SNI vs. Certificate Subject discrepancies across enterprise edge sensors.
* **Work Product:** A **Covert Channel Discrimination Report** proving DNS tunneling through entropy and resolver cache-busting telemetry.

---

### Module H-05: The Whole-Fleet Hunt Crucible (Capstone)
* **The Situation:** A multi-site enterprise telemetry dump covering 14 days of operations across Portland, the Chicago manufacturing site, and corporate HQ in Chicago (over 10 million records). Three separate adversary campaigns are embedded:
  1. A low-and-slow jittered C2 beacon.
  2. A high-entropy DNS tunneling channel exfiltrating intellectual property.
  3. An internal living-off-the-land lateral movement campaign using non-standard SMB/RPC pipes.
* **The Challenge:** No tickets, no hints, no alerts. The student must apply the full Proactive Hunt Loop independently.
* **Work Product:** 
  1. Complete **Adversary Campaign Dossier** identifying all affected hosts, C2 infrastructure, and exfiltration timelines.
  2. Three production-grade **Detection Engineering Rules** (Sigma and Elastic Detection format) to permanently defend the enterprise against each technique.
