# Milestone 1 Performance Assessment — Foundational Triage & Baselines
## Integrating Lessons 01, 02, and 03

> **Operational Role:** Junior SOC Network Analyst at Harrowmere Equipment Group.  
> **Prerequisites:** Completion of [Lesson 01](../01-what-the-analyst-is-for.md), [Lesson 02](../02-reading-a-conversation.md), and [Lesson 03](../03-names-and-expectations.md).  
> **Time Budget:** 30–45 minutes.  
> **Supporting Files:** [Evidence Packet](evidence-packet.md) · [Review & Scoring Guide](review-guide.md).  
> **Tools Required:** Text editor or markdown notebook. Raw telemetry is provided; no specialized tool installation is required.

---

## 1. Operational Context & Ticket Handed to You

At 10:14 local time, the SIEM console triggers an escalated ticket assigned to your triage queue:

> **Ticket #10842:** `CRITICAL: Possible Data Staging & DNS Exfiltration Leak — Workstation WS-108`

A tier-1 colleague has appended a note:
> *"Workstation WS-108 is showing rapid DNS lookups to multiple external IPs in under a minute, followed by an immediate connection attempt to an internal file server admin portal that failed with an error, and then a 4.8 MB outbound connection to an untracked external server. Looks like an active lateral probe and data staging. Recommend isolating WS-108 immediately."*

Before anyone triggers a disruptive workstation isolation, your job is to perform an authentic, evidence-based triage assessment.

---

## 2. Available Evidence Packet

### Telemetry Item 1: DNS Activity (`dns.log`)
Client `192.0.2.108` made two DNS requests to the internal resolver `192.0.2.2`:

| Time | Query Name | Type | Response Code | Answers / Resolved IPs | TTLs |
|---|---|---|---|---|---|
| `10:11:02.104` | `cdn.harrowmere-cloud.example` | `A` | `NOERROR` | `203.0.113.15, 203.0.113.16` | `60, 60` |
| `10:11:45.320` | `cdn.harrowmere-cloud.example` | `A` | `NOERROR` | `203.0.113.88, 203.0.113.89` | `60, 60` |
| `10:11:50.012` | `telemetry.harrowsync-update.example` | `A` | `NOERROR` | *(Empty / 0 Answer RRs; SOA present)* | `1800` |

### Telemetry Item 2: Transport & HTTP Sessions (`conn.log` & `http.log`)

| Timestamp | Source Socket | Destination Socket | Duration | Protocol | State | Method | URI | User-Agent | Status Code | Bytes (Out/In) |
|---|---|---|---|---|---|---|---|---|---|---|
| `10:11:15.012` | `192.0.2.108:49210` | `198.51.100.20:80` | `0.000192s` | `http` | `SF` | `GET` | `/api/v2/admin/status` | `harrow-sync/3.21` | `403 Forbidden` | `148 / 44` |
| `10:11:22.400` | `192.0.2.108:49218` | `203.0.113.15:443` | `12.4102s` | `tls` | `SF` | — | — | — | — | `4,812,040 / 1,200` |

### Telemetry Item 3: Fleet Peer Context & Change Log
* **Change Log Entry #991:** At 09:30, Enterprise Applications updated `harrow-sync` to version 3.21 across 15 workstations in the Finance sub-group.
* **Asset Database:** `198.51.100.20` is the internal reporting repository managed by Leah Moreno. `203.0.113.0/24` is an approved AWS cloud subnet utilized by Harrowmere's contracted document backup vendor.

---

## 3. Your Work Product (The 1-Page Triage Deliverable)

Produce a structured, 1-page assessment that another analyst or supervisor can immediately act on. It must contain the following four sections:

### Section 1: The Smuggled Word Strike & Reframed Question (Lesson 01)
* Explicitly identify and strike out all smuggled adjectives from the ticket title and colleague's note.
* Formulate the single, objective **Analytical Question (IR-1)** that evidence can answer without presupposing an attack.

### Section 2: The 3-Column Discrimination Record (Lesson 01)
Construct a clean table dividing the findings into:
1. **Observations:** Checkable facts with limitations (ports, bytes, durations, status codes).
2. **Interpretations:** Competing hypotheses (Why did the DNS IPs change in 43 seconds? Why did `/api/v2/admin/status` return 403? What is the 4.8 MB transfer?).
3. **Bounded Judgment & Action:** Sized strictly to the evidence.

### Section 3: The Dual-Layer Split (Lesson 02)
Address the connection to `198.51.100.20:80`:
* State what happened at the **Transport Layer** vs. what happened at the **Application Layer**.
* Explain why the colleague's claim that *"the connection failed"* is technically incorrect, and state what the 0.000192s duration proves about who initiated it.

### Section 4: Normal DNS Baseline Evaluation (Lesson 03)
Address the two DNS anomalies flagged by your colleague:
* Explain why `cdn.harrowmere-cloud.example` returning completely different IP addresses 43 seconds later is **not** evidence of fast-flux DNS poisoning.
* Explain what `NOERROR` with 0 answer records means for `telemetry.harrowsync-update.example` (NODATA vs. NXDOMAIN), and why this is not a "DNS leak".
* Prove whether `telemetry.harrowsync-update.example` was ever contacted by the workstation.

---

## 4. Self-Review & Scoring Guide (Formative Check)

Before submitting or reviewing with your mentor, verify your work product against this checklist:

- [ ] **Smuggled Words Stripped:** Did you strike "Data Staging", "DNS Exfiltration", "Lateral Probe", and "Failed"?
- [ ] **Dual-Layer Independence:** Did you explicitly state that `connection.state: SF` proves transport delivery was 100% successful, while `403 Forbidden` was a deliberate application-layer denial?
- [ ] **DNS Reality:** Did you correctly identify that `TTL 60` predicts and explains the address change across the CDN pool?
- [ ] **Lookup != Connection:** Did you note that despite the lookup for `telemetry.harrowsync-update.example`, `conn.log` shows zero connections to that service?
- [ ] **Proportionate Recommendation:** Did you reject immediate isolation of WS-108, and instead recommend validating the backup sync manifest with Leah Moreno?

---

## 5. The 4DX Scorecard Entry

Complete the daily tracking block for your desk card:

```
[ MILESTONE 1 4DX AUDIT ]:
- 3-Column Split Formatted?          [ YES / NO ]
- Transport vs App Layer Separated?  [ YES / NO ]
- DNS Baseline Verified in conn.log? [ YES / NO ]
- Resulting Action Calibrated?       [ YES / NO ]
```

