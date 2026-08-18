# C001 — Foundations of Network Analysis

## Status & Overview

- **Artifact:** Course outline
- **Version:** 0.1 — outline only
- **Date:** 2026-08-18
- **Status:** Draft for review. No module content, exercise, or dataset is authored yet.
- **Implements:** [NADF Active Training Architecture Baseline](../../NADF-Architecture-Baseline.md), [Capability Model v0.1](../../docs/design-studio/2026-07-12-nadf-network-analyst-capability-model-v0.1-proposed.md), [Assessment Evidence Model v0.1](../../docs/design-studio/2026-07-13-nadf-assessment-evidence-model-v0.1-proposed.md)

C001 is NADF's entry course. It develops an analyst who can look at network activity, explain what is happening and why it matters, and produce a defensible assessment that another person can act on.

## Design commitments

These follow from the baseline and constrain the outline. They are the reason the module order looks the way it does.

- **Reasoning is threaded, not bolted on.** Baseline principle 3 rules out a standalone "analytical method" module. Each module develops analytical capability *through* its technical subject matter.
- **Expected behavior precedes anomaly.** Baseline principle 4. Normal DNS, normal TLS, and normal failure come before beaconing, tunneling, and exfiltration. An analyst who cannot describe healthy traffic cannot justify calling anything unhealthy.
- **Troubleshooting precedes threat.** A misread firewall change and a covert channel look alike to someone who has only been taught to look for covert channels. M6 exists to make M7 honest.
- **Guidance fades.** Baseline principle 5. M1–M4 are worked examples and guided practice; M5–M7 move to guided-independent; M8–M9 are independent.
- **Every module ends in a work product,** not a quiz. Capability is integrated performance, so the module's output is the evidence.

## Entry assumptions

Drafted for a learner who can use a computer confidently and has seen a network diagram, but who has no analysis experience and no assumed tooling background. **This is an assumption, not a decision** — see Open Questions.

## Module outline

Capability IDs reference Capability Model v0.1. Evidence families (EF) reference Assessment Evidence Model v0.1.

| # | Module | Technical spine | Analytical development | Capability IDs | Work product | EF |
|---|---|---|---|---|---|---|
| M1 | What the analyst is for | The decision an analyst serves; where analysis sits in a cyber defense team | Separating observation, interpretation, and judgment as a working habit, applied to one small case | OE-2, IR-1 | One-paragraph assessment of a supplied miniature case | EF-1, EF-2 |
| M2 | Reading a conversation | Hosts, services, ports, sessions; layers as a reasoning tool rather than a memorization ladder | Framing a question about an unfamiliar exchange; describing before concluding | OC-1, OC-2, OE-1 | Narrated walkthrough of one capture: who talked to whom, and why | EF-1, EF-2 |
| M3 | Names and expectations | DNS resolution, caching, TTLs, resolver paths; what healthy name resolution looks like | Establishing expected behavior and legitimate variation before deviation has meaning | OC-3, OE-1 | Written baseline description of normal resolution for a given environment | EF-2, EF-3 |
| M4 | What encryption hides | HTTP and TLS; handshake metadata, SNI, certificates; the boundary of what is observable | Reasoning from partial evidence; naming the limits of a source | OC-2, OE-4 | Assessment of an encrypted exchange stating explicitly what cannot be determined | EF-2, EF-5 |
| M5 | Vantage point and evidence | Capture vs. flow vs. logs vs. endpoint telemetry; sensor placement, retention, gaps | Evidence planning: choosing sources for a question and knowing what each cannot answer | OE-3, OE-4, OE-5 | Evidence plan for a supplied question, with prioritization and rationale | EF-4, EF-5 |
| M6 | When it breaks | Latency, loss, path behavior, MTU and fragmentation, policy effects | Causal models, competing explanations, discriminating tests, revising when a prediction fails | OC-4, IR-2, IR-3, IR-5, IR-6 | Diagnosis of a failure with alternatives considered and the discriminating evidence named | EF-3, EF-4, EF-8 |
| M7 | When it's suspicious | Beaconing, tunneling, staging and exfiltration shapes; peer comparison and history | Resisting indicator-first labeling; holding benign and malicious explanations open together | IR-2, IR-4, IR-5, OC-3 | Assessment of ambiguous activity that argues both explanations before choosing | EF-3, EF-4, EF-6 |
| M8 | Judgment and handoff | Escalation paths, adjacent roles, proportionate action | Calibrated confidence; recommending action sized to evidence and risk; role boundaries | JU-1, JU-2, JU-3, JU-4, CT-1, CT-2, CT-3, CT-4 | Two products from one analysis: a peer handoff and a leadership summary | EF-6, EF-7 |
| M9 | Capstone and transfer | Integrated scenario, then an unrelated situation | Performing the whole chain unaided, then carrying the reasoning to changed technology | All domains, esp. LR-1 – LR-4 | Full assessment, revision under new evidence, and a transfer response | EF-1 – EF-8 |

## The capstone already exists

M9 does not need to be authored from scratch. [PILOT-001 — Encrypted outbound traffic](../pilots/encrypted-outbound-traffic/README.md) is already built as a full-chain performance experience with a staged evidence release, a revision task, a transfer case, and a review guide. It is the natural C001 capstone.

This has a useful consequence for sequencing: running the pilot now, before M1–M8 exist, tests the course's endpoint first. Whatever the pilot's [run records](../pilots/encrypted-outbound-traffic/run-records.md) expose about the capability and evidence models will be cheaper to fix now than after eight modules are written against them.

The pilot's DNS fragmentation transfer case also belongs to M6's subject matter and can seed that module's worked example.

## Dataset and lab dependencies

Authoring is gated on capture data for M2, M3, M4, M6, and M7, and on a lab environment for M5.

This is the roadmap's open PCAP and telemetry sourcing question, and it is now on the critical path: authentic capture data and redistributable capture data are frequently not the same data, and the answer changes what these modules can be built from. M1 and M8 have no dataset dependency and can be authored first.

## What this outline does not establish

Per the baseline's Standing Qualifications: no proficiency levels, mastery thresholds, scoring, completion criteria, or assessment validity are defined here. Module work products are evidence for review and feedback, not scored artifacts. The course sequence is a design proposal, not a validated learning progression.

## Open questions

These change the design materially and are worth answering before module authoring begins.

1. **Who is the learner?** The outline assumes no analysis experience and no tooling background. An audience of working IT staff would compress M2–M4 substantially and change the entry point.
2. **How is it delivered?** Self-guided like PILOT-001, or instructor-led with live review? This determines whether feedback is a review guide or a person, which in turn determines whether EF-8 is reachable in modules before M9.
3. **What is the time budget?** The outline is roughly 20–30 hours as drafted. A shorter budget means cutting modules rather than thinning all of them.
