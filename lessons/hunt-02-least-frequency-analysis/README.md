# Hunt 02 — Least-Frequency Analysis & Outlier Stacking

## At a glance

- **Part of:** [Book 2 — The Hunter's Eye](/BOOK-2.md) · Proactive Network Threat Hunting Track
- **Follows:** [Chapter 11 (Story) — The Long Tail](/narrative/11-the-long-tail.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-24
- **Capability targets:** TH-3 (Least-Frequency Analysis), TH-4 (Cardinality & Stacking), OE-4 (Administrative Noise Discrimination), IR-2 (Hypothesis Testing)
- **Time:** about 2.5 hours
- **Workbench:** Security Onion Hunt, Kibana, Elasticsearch (KQL / Lucene / ES|QL)
- **Dataset:** 500,000 Zeek connection & HTTP records across Harrowmere Engineering & CAD subnets (`conn.log`, `http.log`)

> **New to the Hunt screen?** Watch the [two-minute primer](../security-onion-groupby-primer.md) first. It shows this lesson's stack on the Hunt screen with `| groupby`. The data comes from the [Hunt data guide](../../lab/HUNT-DATA-GUIDE.md). It uses ECS-style field names such as `user_agent.original`, while Zeek logs imported from a pcap use Security Onion's names such as `http.useragent` (see [field-names.md](../field-names.md)). Check your data's field list before you copy a query.

---

## The Situation: The Trap of the High-Volume Outlier

Ethan Mercer sat in the threat hunting pod with a fresh 48-hour export of 500,000 connection records. His initial instinct—sorting by `source.bytes` to spot large data exfiltration streams—wasted forty-five minutes identifying Dave Henderson streaming 4K lathe maintenance videos and Priya Raman's automated Azure database backup worker.

When Ethan flipped his query to search for the rarest destination IP addresses, the cluster returned **14,218 destinations that received exactly one connection**. Attempting to inspect each record manually resulted in immediate fatigue and false leads: legitimate developers compiling Rust libraries, temperature sensors pinging dead portals, and misconfigured NTP daemons.

As Cal Rowan and Owen Kline demonstrated:
1. **Adversaries do not shout:** Modern stealthy command-and-control software avoids high-volume spikes.
2. **The Long Tail is noisy:** Enterprise environments are saturated with "administrative weirdness."
3. **Mathematical stacking provides leverage:** By using multi-bucket Elasticsearch `terms` aggregations and nesting `cardinality` metrics on `source.ip`, analysts can mathematically isolate single-host outliers running unmanaged software stacks.

---

## 1. The Mathematics of the Long Tail

In enterprise network traffic, connection volume follows a steep power-law distribution (the Pareto principle or "long tail"):

```text
Volume (Events)
▲
│ ████████
│ ████████  ◄── Head (95% of traffic):
│ ████████      Microsoft, Google, Internal DBs
│ █             (High volume, > 1,500 hosts)
│ █ ▂ ▂ ▂   ◄── Torso: IT tools, dev mirrors
│               (Moderate volume, multi-host)
│
│ ░░░░░░░░  ◄── Long Tail (5% of traffic)
└─────────► Unique Destinations
  (Rare destinations; implants hide with source.ip == 1)
```

### Why Raw Destination Stacking Fails
If you group by `destination.ip` alone:
- Thousands of dynamic CDN IP addresses appear with `count: 1`.
- A developer fetching an obscure open-source package appears with `count: 1`.
- You cannot differentiate between an ephemeral web request and a scripted implant.

### The Winning Move: Dual-Key Stacking
To eliminate administrative noise, you stack by **Software Client Fingerprint** (`user_agent.original` in HTTP, or `tls.ja4` in HTTPS) and calculate the **Unique Source Host Cardinality**:

$$\text{Cardinality}(S) = |\{ \text{source.ip} \in \text{Bucket} \}|$$

* If an unmanaged software client has $\text{Cardinality} == 1$ and contacts an unclassified destination over an unusual port, the statistical anomaly is acute and immediately actionable.

---

## 2. Elasticsearch Stacking Syntax

In the Security Onion Hunt or Kibana Dev Tools console, execute the following multi-bucket aggregation against `http.log`:

```json
POST /so-zeek-http-*/_search
{
  "size": 0,
  "query": {
    "range": {
      "@timestamp": {
        "gte": "now-48h"
      }
    }
  },
  "aggs": {
    "stacked_user_agents": {
      "terms": {
        "field": "user_agent.original",
        "size": 50,
        "order": { "_count": "asc" }
      },
      "aggs": {
        "unique_hosts": {
          "cardinality": {
            "field": "source.ip"
          }
        },
        "destinations": {
          "terms": {
            "field": "destination.ip",
            "size": 5
          }
        }
      }
    }
  }
}
```

### Reading the Query Results:
- `order: { "_count": "asc" }`: Brings the rarest User-Agent strings to the top.
- `unique_hosts`: Immediately tells you whether the client is deployed across 500 computers or only 1.
- `destinations`: Reveals the external infrastructure receiving the communication.

---

## 3. Interactive Micro-Drills

### Drill H2.1: Evaluating the Long-Tail Output (30-Second Triage)

You run the aggregation query above across Harrowmere's engineering subnet. The top three rarest buckets return:

```
Bucket 1:
- User-Agent: "git/2.39.1 (libcurl/7.87.0 OpenSSL/3.0.7 zlib/1.2.13)"
- Document Count: 14
- Host Cardinality: 12 machines (Subnet 10.100.42.0/24)
- Destination: 140.82.112.4 (github.com)

Bucket 2:
- User-Agent: "HP-LaserJet-M404-SNMP-Agent/1.0"
- Document Count: 3
- Host Cardinality: 1 machine (10.100.12.15)
- Destination: 10.100.1.5 (Internal Print Server)

Bucket 3:
- User-Agent: "python-requests/2.28.1"
- Document Count: 48
- Host Cardinality: 1 machine (10.100.14.88)
- Destination: 198.51.100.84:8080 (Unclassified VPS, no DNS record)
```

Which bucket warrants immediate priority escalation, and why?

<details class="reveal-gate">
  <summary>🔍 Check Evaluation Key</summary>
  <div class="reveal-content">
    <p><strong>Answer: Bucket 3.</strong></p>
    <ul>
      <li><strong>Bucket 1</strong> is legitimate developer tooling: 12 different machines are running standard Git operations against GitHub's verified IP space.</li>
      <li><strong>Bucket 2</strong> is administrative weirdness: an internal printer communicating with the internal print server. Host cardinality is 1, but destination is RFC1918 internal.</li>
      <li><strong>Bucket 3</strong> satisfies all criteria for stealthy adversary egress: single host cardinality (10.100.14.88 in the CAD drafting subnet), non-browser client library (<code>python-requests</code>), external destination on a non-standard port (8080), and no preceding DNS resolution.</li>
    </ul>
  </div>
</details>

---

## 4. The Outlier Stacking Ledger (Performance Deliverable)

When executing an enterprise hunt using Least-Frequency Analysis, you must document your findings in a structured **Outlier Stacking Ledger**:

| Candidate Anomaly | Telemetry Observation | Host Cardinality | Verified Environmental Context | Operational Disposition |
|---|---|---|---|---|
| **Anomaly A** | `user_agent: "Mozilla/5.0 ..."` contacting `52.84.120.45` (48 GB) | 1 (`10.100.12.44`) | Dave Henderson streaming authorized lathe training video archive via AWS CloudFront CDN. | **Benign Volume Outlier (Closed)** |
| **Anomaly B** | `conn.log` 312 bytes to European IP, no DNS query | 1 (`10.100.42.18`) | Marcus Whitlock downloading Rust crate dependencies from an unmanaged mirror. | **Administrative Weirdness (Referred to IT)** |
| **Anomaly C** | `user_agent: "python-requests/2.28.1"` to `198.51.100.84:8080` | 1 (`10.100.14.88`) | Workstation is a CAD terminal with no authorized scripting tools; regular check-in interval. | **High-Confidence Intrusion Indicator (Escalated to IR)** |

---

<div class="bridge-card">
  <div class="bridge-label">Next Module in Book 2</div>
  <div class="bridge-title">Chapter 12 — The Heartbeat with a Stutter</div>
  <p class="bridge-desc">When adversaries introduce random timing variations into their command-and-control beacons, simple interval queries break down. Learn how to calculate statistical jitter and analyze delta-time distributions.</p>
  <a href="#/narrative/12-the-heartbeat-with-a-stutter" class="bridge-btn">Continue to Chapter 12 Story →</a>
</div>
