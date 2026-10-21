# The Technical Lessons

The technical lessons form the rigorous analytical spine of the **Network Analyst Development Framework**. They develop an analyst who can inspect raw traffic, isolate transport-vs-application behavior, establish environment baselines, declare visibility boundaries under encryption, and produce defensible incident handoffs.

* **Full Curriculum Plan:** [The Course Plan (COURSE.md)](/COURSE.md)
* **Narrative Companion:** [The Narrative Track (Story)](/narrative/README.md)
* **Longitudinal Capability Record:** [Run Records & Same-Task-Twice Protocol](/lessons/run-records.md)

---

## Technical Curriculum Sequence

| Module | Technical Lesson | Core Analytical Target | Evidence / Capture |
|---|---|---|---|
| **Day 0** | [Day 0: Baseline Triage Alert (SEC-3904)](/lessons/00-baseline-alert.md) | Pre-course diagnostic triage (Same-Task-Twice Protocol) | Connection log & ticket prompt |
| **01** | [Lesson 01: What the Analyst Is For](/lessons/01-what-the-analyst-is-for.md) | Separating observation, interpretation, and judgment | Miniature case triage |
| **02** | [Lesson 02: Reading a Conversation](/lessons/02-reading-a-conversation.md) | Layer decoupling (TCP vs HTTP) & bare ACK hunting | `02-conversation.pcap` |
| **E03** | [Episode 03: Prediction Before Inspection](/lessons/e03-before-you-look/README.md) | Committing to hypotheses before looking; model revision | `e03-prediction.pcap` |
| **03** | [Lesson 03: Names and Expectations](/lessons/03-names-and-expectations.md) | DNS resolution, client caching, TTLs, and CDN baselines | `03-dns.pcap` |
| **M1** | [Milestone 1: Foundational Triage](/lessons/milestone-01-foundational-triage/README.md) | Multi-service triage: stripping smuggled words, dual-layer reading, CDN baselines | Synthetic triage packet |
| **04** | [Lesson 04: What Encryption Hides](/lessons/04-what-encryption-hides.md) | TLS 1.3 visibility boundaries & 3-column bounded claims | `04-tls.pcap` |
| **05** | [Lesson 05: Vantage Point and Evidence](/lessons/05-vantage-point-and-evidence.md) | Multi-vantage reasoning & evidence perishability clocks | Architecture case study |
| **06** | [Lesson 06: When It Breaks](/lessons/06-when-it-breaks.md) | Active refusal (REJ) vs silent drop (S0) vs server stalls | `06-failures.pcap` & `06-fragmentation.pcap` |
| **M2** | [Milestone 2: Path Failure & Encryption](/lessons/milestone-02-path-failure-and-encryption/README.md) | Diagnosing path impairment vs server delays vs encrypted blindspots | Synthetic triage packet |
| **07** | [Lesson 07: When It's Suspicious](/lessons/07-when-its-suspicious.md) | Beacon regularity, DNS entropy, and SOC Tri-Check | `07-suspicious.pcap` |
| **08** | [Lesson 08: Judgment and Handoff](/lessons/08-judgment-and-handoff.md) | Two-audience handoffs, confidence breakers, reversibility | 94/6 incident case study |
| **09** | [Lesson 09: Capstone — Encrypted Outbound](/lessons/09-capstone-encrypted-outbound-traffic/README.md) | Whole-chain synthesis, staged contradictory telemetry | Capstone evidence packet |

---

<div class="bridge-card">
  <div class="bridge-label">Start the Technical Spine</div>
  <div class="bridge-title">Begin with Day 0: Baseline Triage Alert</div>
  <p class="bridge-desc">Record your 20-minute baseline triage on Alert SEC-3904 before starting Lesson 01. You will revisit this exact alert after the Capstone to measure your capability delta.</p>
  <a href="#/lessons/00-baseline-alert" class="bridge-btn">Open Day 0 Baseline Alert →</a>
</div>
