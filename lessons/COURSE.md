# The Course — Foundations of Network Analysis

> **Book 1 direction:** These nine written lessons are now the technical source material for a proposed 14-episode first book, **[Learning to See](/BOOK-1.md)**. They remain the current runnable course until replacement episodes have technically validated exercises. The [existing-material map](/BOOK-1.md?id=existing-material-map) records what is reused, split, extended, or newly built.

Nine lessons. **All are written** — [01](/lessons/01-what-the-analyst-is-for.md), [02](/lessons/02-reading-a-conversation.md), [03](/lessons/03-names-and-expectations.md), [04](/lessons/04-what-encryption-hides.md), [05](/lessons/05-vantage-point-and-evidence.md), [06](/lessons/06-when-it-breaks.md), [07](/lessons/07-when-its-suspicious.md), [08](/lessons/08-judgment-and-handoff.md), and the [09 capstone](/lessons/09-capstone-encrypted-outbound-traffic/README.md).

The course develops an analyst who can look at network activity, explain what is happening and why it matters, and produce a defensible assessment that another person can act on.

---

## Technical Curriculum Sequence

| # | Lesson | Technical spine | Analytical development | Work product |
|---|---|---|---|---|
| **00** | [Day 0: Baseline Triage Alert](/lessons/00-baseline-alert.md) | Pre-course diagnostic triage | 20-minute unassisted baseline note | SEC-3904 Triage Note |
| **01** | [What the analyst is for](/lessons/01-what-the-analyst-is-for.md) | The decision an analyst serves | Separating observation, interpretation, and judgment | 1-paragraph assessment |
| **02** | [Reading a conversation](/lessons/02-reading-a-conversation.md) | Hosts, services, ports, sessions; layer decoupling | Framing questions about unfamiliar exchanges | Narrated walkthrough of capture |
| **E03** | [Episode 03: Before You Look](/lessons/e03-before-you-look/README.md) | Prediction before inspection; model revision | Committing to hypotheses before looking | Prediction log & revision |
| **03** | [Names and expectations](/lessons/03-names-and-expectations.md) | DNS resolution, caching, TTLs, resolver paths | Establishing expected behavior before deviation | 1-page environment baseline |
| **04** | [What encryption hides](/lessons/04-what-encryption-hides.md) | HTTP and TLS; metadata, SNI, certificates | Reasoning from partial evidence; declaring limits | 3-column bounded claims |
| **05** | [Vantage point and evidence](/lessons/05-vantage-point-and-evidence.md) | Capture vs flow vs logs vs EDR; perishability | Choosing sources and knowing what each cannot answer | Prioritized evidence plan |
| **06** | [When it breaks](/lessons/06-when-it-breaks.md) | Latency, loss, path MTU, fragmentation | Causal models, competing explanations, discriminating tests | Root-cause diagnosis |
| **07** | [When it's suspicious](/lessons/07-when-its-suspicious.md) | Beaconing, tunneling, staging, convergence | Resisting indicator-first labeling; dual hypotheses | SOC Triage Tri-Check |
| **08** | [Judgment and handoff](/lessons/08-judgment-and-handoff.md) | Escalation paths, adjacent roles, reversibility | Calibrated confidence, confidence breakers | Peer handoff & leadership brief |
| **09** | [Capstone: Encrypted Outbound](/lessons/09-capstone-encrypted-outbound-traffic/README.md) | Whole-chain synthesis, staged evidence release | Integrating 01–08; model revision under pressure | Full Triage Brief & Revision |

---

<div class="bridge-card">
  <div class="bridge-label">Start Learning</div>
  <div class="bridge-title">Begin with Day 0: Baseline Triage Alert</div>
  <p class="bridge-desc">Establish your Day 0 baseline performance before starting Lesson 01. You will return to this exact alert after the Capstone to measure your longitudinal skill transformation.</p>
  <a href="#/lessons/00-baseline-alert" class="bridge-btn">Open Day 0 Baseline Alert →</a>
</div>
