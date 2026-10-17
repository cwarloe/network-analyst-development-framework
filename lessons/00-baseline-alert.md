# Day 0 — Baseline Triage Alert (The Longitudinal Delta)

## At a glance

- **Part of:** [The Technical Lessons](README.md) · Pre-Course Diagnostic Baseline
- **When to take this:** **Day 0, BEFORE reading the Prologue or starting Lesson 01.**
- **Time:** exactly 20 minutes (timed).
- **Prerequisites:** None. Do not consult RFCs, search engines, or AI assistants. Use only your current analytical instincts.
- **Why this exists:** To measure your genuine capability delta without artificial multiple-choice tests or bureaucratic grading rubrics.

> *"Detecting real capability change does not require a rubric, levels, or a passing standard. It requires the same task twice."*  
> — Research Review R005

---

## The Scenario

You are sitting in the SOC on shift. A high-priority alert fires into the SIEM queue and auto-populates a ticket:

<div class="ticket-chrome">
  <div class="ticket-bar">
    <span class="ticket-id">SEC-3904</span>
    <span class="sev high">High Priority</span>
    <span class="ticket-status">Queue: Triage / Unassigned</span>
  </div>
  <div class="ticket-subject">Anomalous encrypted outbound beaconing detected from payroll workstation (192.0.2.45)</div>
  <dl class="ticket-meta">
    <dt>Source Host</dt>
    <dd>FIN-WRK-042 (192.0.2.45)</dd>
    <dt>Destination Host</dt>
    <dd>198.51.100.88:443 (External)</dd>
    <dt>Sensor Rule</dt>
    <dd>ET MALWARE Suspicious TLS SNI with Low-Entropy Dynamic Domain</dd>
    <dt>Detection Engine</dt>
    <dd>Security Onion / Suricata + Zeek</dd>
  </dl>
</div>

---

## The Available Telemetry

Your SIEM dashboard surfaces the following 3 log excerpts for this connection window:

### 1. Zeek `conn.log` (Summary of Layer 3/4 Sessions)

```
ts             uid               id.orig_h    id.orig_p  id.resp_h      id.resp_p  proto  service  duration  orig_bytes  resp_bytes  conn_state
1723459100.12  C81xKa3N19Klz8    192.0.2.45   51204      198.51.100.88  443        tcp    ssl      0.0410    382         1420        SF
1723459160.15  C99aMb4L22Pqw1    192.0.2.45   51210      198.51.100.88  443        tcp    ssl      0.0395    382         1420        SF
1723459220.18  C11zQe9W34Mno4    192.0.2.45   51218      198.51.100.88  443        tcp    ssl      0.0421    382         1420        SF
1723459280.22  C44xRt7Y55Kza9    192.0.2.45   51224      198.51.100.88  443        tcp    ssl      0.0408    382         1420        SF
```

### 2. Zeek `ssl.log` (TLS Handshake Metadata)

```
uid               server_name              version   cipher                        ja3                               resumed  established
C81xKa3N19Klz8    api-edge.sync-telemetry  TLSv13    TLS_AES_128_GCM_SHA256        a0e9f5d64349fb13191bc781f81f42e1  F        T
C99aMb4L22Pqw1    api-edge.sync-telemetry  TLSv13    TLS_AES_128_GCM_SHA256        a0e9f5d64349fb13191bc781f81f42e1  F        T
C11zQe9W34Mno4    api-edge.sync-telemetry  TLSv13    TLS_AES_128_GCM_SHA256        a0e9f5d64349fb13191bc781f81f42e1  F        T
C44xRt7Y55Kza9    api-edge.sync-telemetry  TLSv13    TLS_AES_128_GCM_SHA256        a0e9f5d64349fb13191bc781f81f42e1  F        T
```

### 3. Zeek `dns.log` (Resolver Lookups)

```
ts             uid               query                    qtype_name  rcode_name  answers           TTLs
1723459099.98  C01dEf2G34Hjk5    api-edge.sync-telemetry  A           NOERROR     198.51.100.88     60.0
```

---

## Your Task: Write Work Product A (20 Minutes)

Open a blank document or text file. Set a timer for **20 minutes**. 

Write your initial triage note for Ticket `SEC-3904` answering:

1. **What happened?** (Summarize what the data shows).
2. **What is your assessment?** (Is this malicious? Benign? What are you assuming?).
3. **What immediate operational action should be taken?** (e.g. Host isolation? Block IP at firewall? Close ticket? Escalate?).

---

## Critical Filing Protocol

1. **Save this file** as `work-product-a-baseline.md` on your machine.
2. **Do NOT grade or analyze it right now.**
3. **Do NOT look for an answer key.** (There is no answer key in this file).
4. **Do NOT edit it later.**

You will seal this document away. After you complete the entire curriculum and work through the Capstone in Lesson 09, you will be handed this **exact same alert** and asked to write a fresh triage note without reviewing your Day 0 baseline. 

Comparing Work Product A (Day 0) and Work Product B (Post-Capstone) side-by-side will provide indisputable, empirical proof of how your analytical judgment, epistemic discipline, and technical precision have transformed.

---

<div class="bridge-card">
  <div class="bridge-label">Baseline Recorded</div>
  <div class="bridge-title">Begin the Curriculum: Prologue — The Word in the Ticket</div>
  <p class="bridge-desc">Your Day 0 baseline is now recorded. Step into the shoes of apprentice analyst Ethan Vance on his first morning in the SOC as he encounters Ticket SEC-4021.</p>
  <a href="#/narrative/00-prologue" class="bridge-btn">Start Prologue (Story) →</a>
</div>
