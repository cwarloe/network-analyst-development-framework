# Hunt 05 — The Whole-Fleet Hunt Crucible (Capstone)

## At a glance

- **Part of:** [Book 2 — The Hunter's Eye](#/BOOK-2) · Proactive Network Threat Hunting Track
- **Follows:** [Chapter 14 (Story) — The Hunter's Crucible](#/narrative/14-the-hunters-crucible)
- **Version:** 0.1 — draft
- **Date:** 2026-08-27
- **Capability targets:** TH-1 through TH-8 (Complete Proactive Threat Hunting Loop), OE-4 (Evidence Boundary Declaration), IR-4 (Multi-Site Adversary Campaign Reconstruction)
- **Time:** about 4.0 hours
- **Workbench:** Security Onion Hunt, Kibana, Elasticsearch (KQL / Lucene / ES|QL), Sigma Rule Engine
- **Dataset:** 14-day multi-campus enterprise telemetry package (10M+ connection, DNS, NetFlow, and TLS sessions across Portland, Chicago, and Corporate HQ)

---

## The Situation: Zero Alerts, Ten Million Records

In the Book 2 Capstone, the safety nets are removed:
- **No alert fired.**
- **No ticket is assigned.**
- **No vendor threat intelligence feed points to an IP address.**

You are provided with 14 days of raw multi-campus enterprise telemetry across Harrowmere Equipment Group. Operating within the data lake, an advanced cyber espionage adversary has compromised infrastructure, moved laterally across inter-site IPsec tunnels, and staged intellectual property exfiltration.

Your mission is to independently execute the 6-phase **Proactive Hunt Loop**:
1. Formulate falsifiable hypotheses for each phase of the attack lifecycle.
2. Execute disciplined, memory-bounded Elasticsearch queries.
3. Isolate the statistical anomalies (long-tail stacking, delta-time jitter, Shannon entropy).
4. Uncover the adversary's complete multi-stage operational chain.
5. Author an **Adversary Campaign Dossier**.
6. Deliver production-ready **Detection Engineering Rules** (Sigma & Elastic format) to defend the enterprise permanently.

---

## 1. The 3-Stage Adversary Campaign Architecture

```
[ Chicago Manufacturing ]
  Workstation 10.120.32.14
          │
          ├──────────────────────────► C2 Egress: 198.51.100.84:443
          │                            (5-min interval ± 15% jitter, CV = 0.08, JA4 Go runtime)
          │
          ▼ (Lateral Movement across WAN IPsec Tunnel)
[ Portland Warehouse ]
  Repository Server 10.110.16.5
  (Living off the Land: SMB IPC$/ADMIN$ pipes, staged CAD archives)
          │
          ▼ (Strict Egress Deny-All Firewall Policy Bypassed)
[ Corporate Recursive DNS Resolvers ]
  10.100.1.10 / 10.100.1.11
          │
          └──────────────────────────► Covert Exfiltration: data-sync-telemetry[.]net
                                       (142,890 TXT queries, 62-char subdomains, Shannon Entropy 4.86 bits)
```

---

## 2. Capstone Performance Deliverable 1: Adversary Campaign Dossier

Complete the formal 4-part **Adversary Campaign Dossier**:

| Phase | Observed Footprint | Mathematical Proof | Environmental Impact | Operational Disposition |
|---|---|---|---|---|
| **Phase 1: Command & Control** | `10.120.32.14` $\rightarrow$ `198.51.100.84:443` | Mean $\mu = 300.2\text{s}$, $\sigma = 24.1\text{s}$, $CV = 0.08$; JA4: `t13d1516h2_...` | Compromised engineering terminal in Chicago manufacturing. | **Immediate Endpoint Isolation & Memory Preservation** |
| **Phase 2: Lateral Movement** | `10.120.32.14` $\rightarrow$ `10.110.16.5` (SMB 445 / RPC 135) | 22 East-West wide-area sessions over IPsec; native Windows network pipes (`ADMIN$`) | Compromised documentation repository in Portland warehouse; staged CAD archives. | **Service Account Credential Revocation** |
| **Phase 3: Data Exfiltration** | `10.110.16.5` $\rightarrow$ `data-sync-telemetry[.]net` via recursive DNS | 142,890 queries; label length = 62 chars; Shannon entropy $H = 4.86\text{ bits/symbol}$ | Bypassed strict egress firewall rules by tunneling ciphertext through corporate resolvers. | **RPZ DNS Sinkholing & Upstream Null-Route** |

---

## 3. Capstone Performance Deliverable 2: Detection Engineering Rules

To close the loop, write three production-ready Sigma and Elastic Detection rules:

### Rule 1: Automated Jittered Beacon Detection (Elastic ES|QL)
```sql
FROM so-zeek-conn-*
| WHERE destination.port == 443 AND network.direction == "egress"
| STATS 
    event_count = COUNT(*),
    avg_duration = AVG(duration),
    min_time = MIN(@timestamp),
    max_time = MAX(@timestamp)
  BY source.ip, destination.ip, tls.client.ja4
| EVAL duration_span_sec = TO_DOUBLE(DATE_DIFF("seconds", min_time, max_time))
| EVAL interval_sec = duration_span_sec / event_count
| WHERE event_count > 50 AND interval_sec BETWEEN 40 AND 600
| LIMIT 20
```

### Rule 2: High-Entropy DNS Tunneling Detection (Sigma Rule Format)
```yaml
title: High-Entropy DNS Subdomain Tunneling
id: 8c34f19b-7e12-4a52-b331-50e3b97f0a12
status: production
description: Detects outbound DNS TXT queries with label lengths exceeding 50 characters and high character entropy.
logsource:
    category: dns
    product: zeek
detection:
    selection:
        qtype_name: 'TXT'
    filter_length:
        query|re: '^[a-zA-Z0-9]{50,}\..*'
    condition: selection and filter_length
fields:
    - id.orig_h
    - query
    - qtype_name
falsepositives:
    - Anti-spam reputation lookups (DKIM/SPF)
    - Cloud security vendor telemetry agents
level: high
```

---

<div class="bridge-card">
  <div class="bridge-label">Curriculum Completion</div>
  <div class="bridge-title">Congratulations — Book 2 Complete!</div>
  <p class="bridge-desc">You have successfully mastered the proactive threat hunting track: hypothesis testing, outlier stacking, beacon jitter analysis, domain clustering, and detection engineering. Return to the curriculum overview or review the master glossary.</p>
  <a href="#/BOOK-2" class="bridge-btn">Return to Book 2 Architecture →</a>
</div>
