# Hunt 01 — The Falsifiable Hypothesis

## At a glance

- **Part of:** [Book 2 — The Hunter's Eye](#/BOOK-2) · Proactive Network Threat Hunting Track
- **Follows:** [Chapter 10 (Story) — The Silence of the Data Lake](#/narrative/10-the-silence-of-the-data-lake)
- **Version:** 0.1 — draft
- **Date:** 2026-08-23
- **Capability targets:** TH-1 (Hypothesis Formulation), TH-2 (Telemetry Scoping), OE-4 (Boundary Declaration), IR-1 (Observation vs Interpretation)
- **Time:** about 2.5 hours
- **Workbench:** Security Onion Hunt, Kibana, Elasticsearch (KQL / Lucene / ES|QL)
- **Assumes:** [Book 1 Capstone](#/lessons/09-capstone-encrypted-outbound-traffic/README). You can separate observation from interpretation, understand TCP/HTTP/TLS protocol mechanics, and declare evidence boundaries.

---

## The Situation: Why You Cannot Just "Browse"

Ethan Mercer sat in front of Harrowmere's primary Security Onion console. Across three 32-inch displays, the cluster held over **42 million connection documents**, **16 million DNS records**, and **8 million TLS handshakes** collected across the Portland, Chicago, and corporate network edges over the preceding seven days.

There were no red alert banners. No high-priority tickets sat in his queue. The SIEM dashboard was green.

Ethan opened the Kibana Discover tab, clicked into the search bar, typed `destination.port: 443`, and hit Enter.

A waterfall of 28 million records filled the table. He clicked a random IP address in the `destination.ip` column, scrolled through a dozen rows of encrypted payloads, opened another tab to search for `conn_state: S0`, and began clicking through destination hostnames.

A chair rolled up beside him. It was Cal Rowan, Harrowmere's Senior Security Engineer. Cal had built the ingest pipelines that normalized Zeek's raw output into the Elastic Common Schema (ECS).

Cal watched Ethan click through a list of Amazon AWS IP addresses for thirty seconds in silence.

“What are you looking for, Ethan?” Cal asked.

“Adversary activity,” Ethan replied, not looking up. “Checking if anything looks weird in the outbound 443 traffic.”

Cal reached over and tapped the monitor.

“Browsing is not hunting,” Cal said, his voice quiet but firm. “In 42 million records, there are ten thousand things that look weird. Developers running unauthorized test scripts, HVAC controllers running obsolete SSL v3 handshakes, marketing telemetry beacons, and misconfigured NTP daemons. If you go into a data lake looking for 'weird,' your brain will find whatever pattern satisfies your boredom, and you will spend four days chasing a benign cloud load balancer.”

Ethan stopped clicking. “Then where do we start?”

“With a **falsifiable hypothesis**,” Cal said. “Before you write a single search query, you define the adversary behavior you are hunting, the exact telemetry where it must leave a footprint, and—most importantly—**the specific evidence that would prove the hypothesis false.** If you don't know what disproves you before you hit Enter, you aren't hunting. You're just sightseeing.”

---

## 1. The Anatomy of a Threat Hunting Hypothesis

A hunting hypothesis is not an alert and it is not a guess. It is a formal, testable proposition derived from threat intelligence, adversary tradecraft (e.g., MITRE ATT&CK), or architectural vulnerabilities.

Every valid hunting hypothesis contains four distinct components:

| Component | Scope & Description | Concrete Example |
| :--- | :--- | :--- |
| **1. Threat Actor Tradecraft** | MITRE ATT&CK technique or observable adversary tradecraft. | `T1071.001: Web Protocols`, `T1071.004: DNS Tunneling` |
| **2. Environmental Scope** | Specific subnet, device role, or business workflow under hunt. | Engineering CAD workstations (`10.42.0.0/16`), branch VPN egress |
| **3. Observable Wire Footprint** | Exact data fields and metrics that MUST appear if attack is occurring. | Low cardinality (`source.ip == 1`), persistent `conn_state`, script User-Agents |
| **4. Falsification Condition** | Specific empirical finding that proves traffic is legitimate enterprise activity. | Destination resolves to approved CDN tenant list, managed browser hash match |

### The Falsification Test
An unfalsifiable hypothesis is dangerous because any query result can be interpreted as "suspicious."

* **Bad (Unfalsifiable / Fishing):** *"An adversary might be beaconing out of our network using HTTPS."*  
  *(Problem: Every machine in the company connects via HTTPS constantly. No search result can ever disprove this statement.)*
* **Good (Falsifiable):** *"An adversary is using a non-standard HTTP client library to establish persistent, low-frequency egress to an untracked external IP from internal developer workstations."*  
  *(Falsification criteria: If all matching User-Agent strings match corporate-managed browser hashes, or if the destination IPs resolve to Harrowmere's approved CDN tenant list, the hypothesis is falsified and the hunt concludes.)*

---

## 2. Interactive Micro-Drills

### Drill H1.1: Falsifiable vs. Fishing Expedition (15-Second Spotting Rep)

Evaluate the three statements below. Which **one** represents a rigorous, falsifiable hunting hypothesis?

1. **Statement A:** *"There could be advanced persistent threat (APT) activity hiding in our DNS logs because DNS is often abused for covert communications."*
2. **Statement B:** *"An external adversary is exploiting unmanaged internal servers by scanning for open database ports (3306, 5432) across the corporate LAN."*
3. **Statement C:** *"Adversaries are exfiltrating intellectual property via outbound DNS queries that exceed 50 characters in query length, exhibit high Shannon entropy, and resolve to apex domains unqueried by any other peer workstation."*

<details class="reveal-gate">
  <summary>🔍 Check Evaluation Key</summary>
  <div class="reveal-content">
    <p><strong>Answer: Statement C.</strong></p>
    <ul>
      <li><strong>Statement A</strong> is a passive generalization. It provides no observable metric, no scope, and cannot be falsified.</li>
      <li><strong>Statement B</strong> is a broad port-scan fear. While somewhat specific on ports, it lacks telemetry boundaries and falsification criteria.</li>
      <li><strong>Statement C</strong> is an authentic, highly falsifiable hunting hypothesis: it names the protocol (DNS), the specific metric (query length &gt; 50), the mathematical property (high Shannon entropy), and the peer baseline discriminator (apex unqueried by peers). If queries are short or shared across the fleet, the hypothesis is immediately disproven.</li>
    </ul>
  </div>
</details>

---

## 3. Query Construction: Translating Hypotheses into Elastic Syntax

In Security Onion Hunt and Kibana, threat hunters translate hypotheses into search queries using **Kibana Query Language (KQL)** and **Lucene**.

### The Rule of Ingestion Scoping
When querying 50 million records, broad queries will timeout or crash browser memory. A hunter always scopes queries in this strict order:

1. **Dataset Scope:** Filter by `event.dataset` first (`conn`, `dns`, `ssl`, `http`).
2. **Direction & Boundary:** Filter for external traffic (`network.direction: "outbound"` or private $\rightarrow$ public CIDR).
3. **Aggregations:** Group by terms rather than pulling raw documents.

```kql
# Example KQL Hunt Query: Rare External Connections from Engineering Subnet
event.dataset: "conn" 
  and source.ip: 192.0.2.0/24 
  and not (destination.ip: (10.0.0.0/8 or 172.16.0.0/12 or 192.168.0.0/16)) 
  and network.bytes > 1000000
```

---

## 4. Practice Application: The Engineering Subnet Hunt Case

Review the simulated 24-hour telemetry aggregate from Harrowmere's Engineering CAD subnet (`192.0.2.100` to `192.0.2.150`).

The team is investigating the hypothesis:
> *"An adversary has established an unauthorized persistence channel from an engineering workstation to an external VPS using non-standard high ports, evading corporate proxy inspection."*

### Query Aggregate: Top 5 Outbound Flows by Duration & Destination Port

```
destination.ip    destination.port   flow_count   total_duration_sec   total_bytes   peer_count
198.51.100.12     443                14,210       84,200               4.2 GB        48 hosts
203.0.113.88      8443               1            86,100               14.8 MB       1 host (192.0.2.114)
198.51.100.25     443                8,900        42,100               890 MB        42 hosts
198.51.100.99     123 (NTP)          2,880        120                  180 KB        50 hosts
203.0.113.4       443                12           340                  1.2 MB        2 hosts
```

### Your Analytical Questions
1. **The Peer Baseline Check:** How does `peer_count` immediately separate `203.0.113.88:8443` from the other web destinations?
2. **The Duration Anomaly:** What does a single connection (`flow_count: 1`) lasting 86,100 seconds (23.9 hours) with only 14.8 MB of total transfer indicate about the nature of the socket?
3. **The Falsification Test:** What single inquiry to Leah Moreno or the IT helpdesk could immediately falsify the hypothesis that `203.0.113.88` is an adversary implant?

<details class="reveal-gate">
  <summary>🔍 Check Expert Hunt Debrief</summary>
  <div class="reveal-content">
    <ol>
      <li><strong>Peer Isolation:</strong> <code>203.0.113.88</code> was contacted by exactly <em>one host</em> (<code>192.0.2.114</code>), whereas the legitimate cloud services show broad adoption across 42–48 engineering workstations.</li>
      <li><strong>Persistent Interactive Shell / Tunnel:</strong> A single continuous connection spanning nearly 24 hours with low byte volume (14.8 MB) is the classic signature of an idle reverse shell or persistent SSH/VPN tunnel, maintaining an open TCP socket without bulk data transfer.</li>
      <li><strong>Falsification Check:</strong> Check whether host <code>192.0.2.114</code> is assigned to a contractor or developer who has an approved change request or corporate exception to access an external client repository or dev server on port 8443. If an approved change ticket exists, the adversary hypothesis is disproven.</li>
    </ol>
  </div>
</details>

---

## 5. Your Work Product: 1-Page Hunt Package Specification

Draft a formal **Hunt Package Specification** for your team. Use this structure:

1. **Hunt Identifier & Title:** (e.g., `HUNT-2026-01: Non-Standard Outbound Port Persistence`).
2. **Target Threat Model:** MITRE ATT&CK technique code, actor motivation, and attack phase.
3. **Falsifiable Hypothesis Statement:** One clear sentence defining the expected observation and the boundary.
4. **Telemetry Scope:** Datasets, sensor locations, and date ranges required.
5. **Elastic / KQL Search Queries:** The exact query syntax to isolate candidates from the enterprise baseline.
6. **Falsification Criteria:** What specific evidence proves the finding is benign operations and closes the hunt without escalation.
7. **Handoff Target:** What detection logic (Sigma or Elastic alert) should be authored if the hunt identifies unmonitored adversary behavior.

---

## 6. The Threat Hunter's Daily 4DX Scorecard

```
WEEKLY 4DX THREAT HUNTING SCORECARD — HUNTER: [ ____________ ]  WEEK: [ _________ ]

[ WIG / LAG TARGET ]: Zero unmonitored persistent channels; 100% hunt-to-detection conversion.

[ LEAD MEASURE ]: % of executed hunts that have a written Falsification Criterion documented
                 BEFORE running queries in Kibana/Hunt. (Target: 100%)

  HUNT ID       HYPOTHESIS WRITTEN?   FALSIFICATION NAMED?   DETECTION RULE CODIFIED?
  HUNT-01              [   ]                  [   ]                    [   ]
  HUNT-02              [   ]                  [   ]                    [   ]
  HUNT-03              [   ]                  [   ]                    [   ]

  WEEKLY HUNT RIGOR RATE: [ _____ / _____ ] = [ _____ % ]
```

---

<div class="bridge-card">
  <div class="bridge-label">Next Step in Curriculum</div>
  <div class="bridge-title">Hunt 02 — The Long Tail & Stacking Analysis</div>
  <p class="bridge-desc">Learn the mathematics of the Long Tail: how to use Elasticsearch Terms Aggregations to stack millions of network events and bubble the single 1-in-a-million outlier to the surface.</p>
  <a href="#/lessons/hunt-02-the-long-tail" class="bridge-btn">Continue to Hunt 02 →</a>
</div>
