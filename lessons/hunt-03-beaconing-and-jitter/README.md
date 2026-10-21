# Hunt 03 — Beaconing & Statistical Jitter

## At a glance

- **Part of:** [Book 2 — The Hunter's Eye](/BOOK-2.md) · Proactive Network Threat Hunting Track
- **Follows:** [Chapter 12 (Story) — The Heartbeat with a Stutter](/narrative/12-the-heartbeat-with-a-stutter.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-25
- **Capability targets:** TH-5 (Beacon Timing Analysis), TH-6 (Statistical Jitter Profiling), IR-3 (Machine vs Human Behavioral Discrimination)
- **Time:** about 2.5 hours
- **Workbench:** Security Onion Hunt, Kibana, Elasticsearch (KQL / Lucene / ES|QL), Python / Jupyter
- **Dataset:** 7 days of Zeek connection records (`conn.log`) tracking outbound TLS flows from Engineering Workstation `10.42.18.91`

---

## The Situation: Beyond the Metronome

In elementary security courses, command-and-control (C2) beaconing is frequently modeled as a metronome: an infected machine executing a rigid `sleep(60)` loop, generating an outbound packet every 60.00 seconds.

In an enterprise environment, however:
1. **Simple interval queries find nothing malicious:** Modern attack frameworks (Cobalt Strike, Sliver, Brute Ratel, Mythic) inject configurable **timing jitter** ($\pm 10\text{--}50\%$) into their sleep routines to foil static cron signatures.
2. **Fixed timers find benign administrative noise:** Exact interval queries invariably hit legitimate NTP synchronization, VMware heartbeats, or cloud storage telemetry daemons.
3. **Statistical variance exposes the machine:** While jitter changes individual inter-arrival times, the delta-time distribution ($\Delta t$) remains tightly bounded by the configured parameters, creating a distinctive mathematical signature fundamentally different from human web browsing.

---

## 1. Mathematical Foundation: Human vs. Machine Egress

### The Inter-Arrival Delta ($\Delta t$) :id=the-inter-arrival-delta-delta-t
For an ordered series of connections occurring at timestamps $t_1, t_2, \dots, t_n$, the inter-arrival delta time is defined as:

$$\Delta t_i = t_i - t_{i-1}$$

### Coefficient of Variation ($CV$) :id=coefficient-of-variation-cv
The coefficient of variation standardizes dispersion relative to the mean:

$$CV = \frac{\sigma}{\mu}$$

Where:
- $\mu = \frac{1}{N}\sum_{i=1}^N \Delta t_i$ (Mean Interval)
- $\sigma = \sqrt{\frac{1}{N}\sum_{i=1}^N (\Delta t_i - \mu)^2}$ (Standard Deviation)

```text
Distribution Density
▲
│        ┌─┐  ◄── Jittered Beacon (60s ± 20%)
│       ┌┘ └┐     μ ≈ 60s, σ ≈ 6.9s, CV ≈ 0.11
│      ┌┘   └┐    Bounded: 48s to 72s
│ ────┴───────┴───────────────────────────────
│ 
│ █  ◄── Human Browsing (Power-law / Pareto)
│ █      Sub-second bursts (CV > 1.5)
│ █      punctuated by long idle think times.
│ █▂▂▂▂▂                                  ▂▂▂▂
└─────────────────────────────────────────────►
  0s   10s   20s   30s   40s   50s   60s   70s  (Δt)
```

* **Human Web Browsing:** Highly bursty, heavy-tailed ($CV > 1.0$). Long idle periods punctuated by rapid multi-tab clicks.
* **Jittered Beacon:** Bounded random variable ($CV < 0.30$). Never bursts into sub-second clusters; never pauses beyond $(1 + \text{jitter}) \times \text{interval}$.

---

## 2. Elasticsearch Date Histogram & Interval Profiling

In Kibana or Security Onion Hunt, calculate connection frequency across time using a `date_histogram` aggregation:

```json
POST /so-zeek-conn-*/_search
{
  "size": 0,
  "query": {
    "bool": {
      "filter": [
        { "term": { "source.ip": "10.42.18.91" } },
        { "term": { "destination.ip": "198.51.100.84" } },
        { "range": { "@timestamp": { "gte": "now-7d" } } }
      ]
    }
  },
  "aggs": {
    "minute_buckets": {
      "date_histogram": {
        "field": "@timestamp",
        "fixed_interval": "1m"
      }
    }
  }
}
```

If every 1-minute bucket consistently contains exactly 1 or 0 connections across 24 hours, including overnight periods and weekends, machine automation is confirmed.

---

## 3. Interactive Micro-Drills

### Drill H3.1: Identifying Beacon Jitter (45-Second Triage)

Examine the four candidate network streams below. Each stream represents 500 consecutive connections originating from a single internal endpoint.

| Candidate | Mean $\mu$ | Std Dev $\sigma$ | Min $\Delta t$ | Max $\Delta t$ | $CV = \sigma / \mu$ |
|---|---|---|---|---|---|
| **Stream A** | 1.4s | 8.2s | 0.05s | 184.2s | **5.85** |
| **Stream B** | 300.0s | 0.0s | 300.0s | 300.0s | **0.00** |
| **Stream C** | 59.8s | 6.9s | 48.1s | 71.9s | **0.11** |
| **Stream D** | 3,600.0s | 0.1s | 3,599.9s | 3,600.1s | **0.00** |

Which candidate represents a **stealthy jittered adversary beacon**, and why?

<details class="reveal-gate">
  <summary>🔍 Check Evaluation Key</summary>
  <div class="reveal-content">
    <p><strong>Answer: Stream C.</strong></p>
    <ul>
      <li><strong>Stream A</strong> ($CV = 5.85$) is characteristic of authentic human interaction: sub-second burst requests mixed with minutes of idle think time.</li>
      <li><strong>Streams B and D</strong> ($CV = 0.00$) represent rigid, non-jittered system cron jobs (e.g., 5-minute health telemetry and 1-hour certificate synchronization). While automated, adversaries rarely use zero-jitter timers due to signature detection.</li>
      <li><strong>Stream C</strong> ($CV = 0.11$) is the textbook signature of a modern C2 implant configured with a 60-second base sleep and 20% jitter. All connections fall strictly between 48.1s and 71.9s, with low dispersion and no sub-second bursting.</li>
    </ul>
  </div>
</details>

---

## 4. The Temporal Beacon Analysis Brief (Performance Deliverable)

When escalating a suspected beaconing host to Incident Response, document your findings using the **Temporal Beacon Analysis Brief**:

```markdown
### TEMPORAL BEACON ANALYSIS BRIEF
1. Target Host: 10.42.18.91 (Engineering CAD Workstation)
2. Remote Infrastructure: 198.51.100.84:443 (Unclassified VPS, Ashburn VA)
3. Observation Window: 2026-08-18 00:00:00 to 2026-08-25 00:00:00 (7 Days)
4. Event Sample: 642 Outbound TLS Sessions

STATISTICAL METRICS:
- Base Sleep Interval (μ): 59.85 seconds (~60s)
- Standard Deviation (σ): 6.91 seconds
- Observed Bounds: [48.12s, 71.94s] (Calculated Jitter: ±19.8%)
- Coefficient of Variation (CV): 0.115

BEHAVIORAL DISCRIMINATION:
- Off-hours persistence: Continuous check-in activity throughout non-business hours (01:00–05:00 UTC).
- Payload invariance: orig_bytes consistently 248–312 bytes; resp_bytes consistently 140–180 bytes.
- Falsification check: Host does not run authorized remote administration software or VPN heartbeats to this provider netblock.

CONCLUSION & RECOMMENDATION:
- High confidence of automated C2 implant persistence.
- Isolate host 10.42.18.91 from LAN; preserve RAM for volatile memory extraction.
```

---

<div class="bridge-card">
  <div class="bridge-label">Next Module in Book 2</div>
  <div class="bridge-title">Chapter 13 — The Forest and the Trees</div>
  <p class="bridge-desc">When adversaries hide behind trusted content delivery networks and tunnel through DNS records, IP addresses lose meaning. Learn how to calculate Shannon entropy and analyze JA4 TLS fingerprints.</p>
  <a href="#/narrative/13-the-forest-and-the-trees" class="bridge-btn">Continue to Chapter 13 Story →</a>
</div>
