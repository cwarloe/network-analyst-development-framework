# Milestone 2 Performance Assessment — Path Failure, Evidence Vantage, and Encryption
## Integrating Lessons 04, 05, and 06

> **Operational Role:** Network Operations & Security Analyst at Harrowmere Equipment Group.  
> **Prerequisites:** Completion of [Lesson 04](../04-what-encryption-hides.md), [Lesson 05](../05-vantage-point-and-evidence.md), and [Lesson 06](../06-when-it-breaks.md).  
> **Time Budget:** 45 minutes.  
> **Supporting Files:** [Evidence Packet](evidence-packet.md) · [Review & Scoring Guide](review-guide.md).  
> **Tools Required:** Text editor or markdown notebook. Raw telemetry is provided; no specialized tool installation is required.

---

## 1. Operational Context & Ticket Handed to You

At 14:15 local time, an urgent escalation is assigned to you during an active operational disruption:

> **Ticket #12094:** `SEV-1 OUTAGE / SUSPECTED COVERED ATTACK: Core ERP degraded, external Vault TLS sessions dropping, and network latency reported across branches.`

A junior colleague has appended an alarming note:
> *"The external SaaS vault is dropping connections or failing with TLS errors. The edge PCAP shows TLS 1.3 connections where we can't see the certificates or HTTP statuses, so this might be encrypted data exfiltration or a man-in-the-middle attack. Also, connection to the internal reporting server (`198.51.100.20`) is completely down—we ran a firewall search for denies and found nothing, so the core router must be dropping packets. And the database query interface is taking 5 seconds, so the network team needs to fix their WAN latency immediately."*

Before the incident commander declares a security breach or pages out the WAN network engineering team, your job is to produce an authoritative, evidence-based triage report.

---

## 2. Review the Evidence Packet

Open and inspect the [Evidence Packet](evidence-packet.md):
- **Item E-01:** Zeek connection summary (`conn.log`) for the four target destinations.
- **Item E-02:** Frame-level TCP timestamps and HTTP/TLS dissection.
- **Item E-03:** DNS resolution telemetry and packet fragmentation traces.
- **Item E-04:** Organizational telemetry inventory, vantage points, and retention clocks.
- **Item E-05:** Colleague's escalation note.

---

## 3. Your Work Product (The 1-Page Triage Deliverable)

Produce a structured, 1-page triage and root-cause deliverable that can be handed directly to the Incident Commander. It must contain the following four sections:

### Section 1: TLS 1.3 Visibility Boundary & Deconstruction (Lesson 04)
Address your colleague's claim that the connection to `vault-saas.harrowmere-cloud.example` is "a suspected covert attack because certificates and HTTP status are hidden":
* State what can be directly observed from the capture (naming the specific frames and fields).
* State what cannot be determined from network packets under TLS 1.3.
* Name the specific non-network telemetry source required to audit the application transaction.
* Explain why the colleague's fear that *"TLS 1.3 means an attack"* represents a cognitive failure mode.

### Section 2: Vantage Point & Evidence Collection Plan (Lesson 05)
Construct a prioritized evidence collection plan for this incident:
* Address the colleague's search of the firewall log: explain why finding zero deny events does **not** prove the network path is clean.
* Rank the available sources (PCAP, Zeek, Firewall, Branch NetFlow, EDR, SaaS Console) strictly by **perishability clock** (shortest clock first).
* Declare what the HQ edge sensor **cannot** see regarding Portland branch workstations (the VPN hairpin and NAT boundary).

### Section 3: Multi-Fault Causal Classification Matrix (Lesson 06)
Evaluate the four backend connections from Item E-01 (`198.51.100.30`, `198.51.100.20`, `198.51.100.50`, and `203.0.113.50`):
* Construct a table detailing:
  1. Zeek Connection State (`conn_state`).
  2. Observed behavior (what the wire shows).
  3. Decisive frame proof and delta timestamps.
  4. True causal domain / responsible team (Systems, Network Engineering, Database/App Dev).
* Specifically address the 5.0001-second delay on `198.51.100.50`: cite Frame 105 to prove whether this is WAN network latency or server processing time.

### Section 4: The Silent Fragmentation Diagnosis (Lesson 06)
Diagnose why Portland workstations experience timeouts when resolving `cluster-sync.harrowmere.internal`:
* Using Item E-03, explain what happens to the 1,740-byte DNS response across the 1400-byte VPN tunnel.
* Explain why Frame 502 carries `udp.dstport=53` while Frame 501 has an empty port, and why intermediate security firewalls drop non-initial fragments.
* State the specific policy or MTU fix required to restore service.

---

## 4. Self-Review & Scoring Guide (Formative Check)

Before submitting your deliverable, verify your analysis against the [Review & Scoring Guide](review-guide.md):

- [ ] **TLS Reality:** Did you explain that TLS 1.3 encrypts certificates by design, and that cleartext SNI confirms the connection was to `vault-saas.harrowmere-cloud.example`?
- [ ] **Firewall Denial Trap:** Did you point out that a firewall logging *only denies* is structurally blind to permitted traffic, making zero results non-discriminating?
- [ ] **Clock Priority:** Did you prioritize archiving the 36-hour PCAP buffer before querying 30-day Zeek or 90-day firewall logs?
- [ ] **Frame 105 Proof:** Did you cite Frame 105's immediate 0.2ms ACK to prove the network delivered the request instantly, and that the 5-second delay was server think time?
- [ ] **`REJ` vs `S0`:** Did you assign `REJ` (`198.51.100.30`) to the Systems team and `S0` (`198.51.100.20`) to Network Engineering?
- [ ] **Fragment Loss:** Did you identify that the second fragment was dropped by firewall policy, causing a silent UDP timeout?

---

## 5. The 4DX Scorecard Entry

Record this assessment in your daily 4DX tracking log:

```
[ MILESTONE 2 4DX AUDIT ]:
- TLS 1.3 Boundary Declared?                 [ YES / NO ]
- Perishability Clock Prioritized First?     [ YES / NO ]
- Transport State (REJ/S0/SF) Classified?    [ YES / NO ]
- Delta Time / Frame ACK Verified?           [ YES / NO ]
- Fragment Loss Mechanism Identified?        [ YES / NO ]
```

