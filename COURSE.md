# The Course — Foundations of Network Analysis

Nine lessons. **All are written** — [01](lessons/01-what-the-analyst-is-for.md), [02](lessons/02-reading-a-conversation.md), [03](lessons/03-names-and-expectations.md), [04](lessons/04-what-encryption-hides.md), [05](lessons/05-vantage-point-and-evidence.md), [06](lessons/06-when-it-breaks.md), [07](lessons/07-when-its-suspicious.md), [08](lessons/08-judgment-and-handoff.md), and the [09 capstone](lessons/09-capstone-encrypted-outbound-traffic/README.md).

The course develops an analyst who can look at network activity, explain what is happening and why it matters, and produce a defensible assessment that another person can act on.

Design references: [architecture](docs/architecture.md), [capability model](docs/capability-model.md), [evidence model](docs/evidence-model.md).

## Entry assumptions

Drafted for a learner who can use a computer confidently and has seen a network diagram, but who has no analysis experience and no assumed tooling background. **This is an assumption, not a decision** — see Open Questions.

## Design commitments

These follow from the baseline and constrain the outline. They are the reason the lesson order looks the way it does.

- **Reasoning is threaded, not bolted on.** Baseline principle 3 rules out a standalone "analytical method" lesson. Each lesson develops analytical capability *through* its technical subject matter.
- **Expected behavior precedes anomaly.** Baseline principle 4. Normal DNS, normal TLS, and normal failure come before beaconing, tunneling, and exfiltration. An analyst who cannot describe healthy traffic cannot justify calling anything unhealthy.
- **Troubleshooting precedes threat.** A misread firewall change and a covert channel look alike to someone who has only been taught to look for covert channels. Lesson 06 exists to make lesson 07 honest.
- **Guidance fades.** Baseline principle 5. 01–04 are worked examples and guided practice; 05–07 move to guided-independent; 08–09 are independent.
- **Every lesson ends in a work product,** not a quiz. Capability is integrated performance, so the lesson's output is the evidence.

## The nine lessons

Capability IDs reference the [capability model](docs/capability-model.md). Evidence families (EF) reference the [evidence model](docs/evidence-model.md).

| # | Lesson | Technical spine | Analytical development | Capability IDs | Work product | EF |
|---|---|---|---|---|---|---|
| 01 | [What the analyst is for](lessons/01-what-the-analyst-is-for.md) | The decision an analyst serves; where analysis sits in a cyber defense team | Separating observation, interpretation, and judgment as a working habit, applied to one small case | OE-2, IR-1 | One-paragraph assessment of a supplied miniature case | EF-1, EF-2 |
| 02 | [Reading a conversation](lessons/02-reading-a-conversation.md) | Hosts, services, ports, sessions; layers as a reasoning tool rather than a memorization ladder | Framing a question about an unfamiliar exchange; describing before concluding | OC-1, OC-2, OE-1 | Narrated walkthrough of one capture: who talked to whom, and why | EF-1, EF-2 |
| 03 | [Names and expectations](lessons/03-names-and-expectations.md) | DNS resolution, caching, TTLs, resolver paths; what healthy name resolution looks like | Establishing expected behavior and legitimate variation before deviation has meaning | OC-3, OE-1 | Written baseline description of normal resolution for a given environment | EF-2, EF-3 |
| 04 | [What encryption hides](lessons/04-what-encryption-hides.md) | HTTP and TLS; handshake metadata, SNI, certificates; the boundary of what is observable | Reasoning from partial evidence; naming the limits of a source | OC-2, OE-4 | Assessment of an encrypted exchange stating explicitly what cannot be determined | EF-2, EF-5 |
| 05 | [Vantage point and evidence](lessons/05-vantage-point-and-evidence.md) | Capture vs. flow vs. logs vs. endpoint telemetry; sensor placement, retention, gaps | Evidence planning: choosing sources for a question and knowing what each cannot answer | OE-3, OE-4, OE-5 | Evidence plan for a supplied question, with prioritization and rationale | EF-4, EF-5 |
| 06 | [When it breaks](lessons/06-when-it-breaks.md) | Latency, loss, path behavior, MTU and fragmentation, policy effects | Causal models, competing explanations, discriminating tests, revising when a prediction fails | OC-4, IR-2, IR-3, IR-5, IR-6 | Diagnosis of a failure with alternatives considered and the discriminating evidence named | EF-3, EF-4, EF-8 |
| 07 | [When it's suspicious](lessons/07-when-its-suspicious.md) | Beaconing, tunneling, staging and exfiltration shapes; peer comparison and history | Resisting indicator-first labeling; holding benign and malicious explanations open together | IR-2, IR-4, IR-5, OC-3 | Assessment of ambiguous activity that argues both explanations before choosing | EF-3, EF-4, EF-6 |
| 08 | [Judgment and handoff](lessons/08-judgment-and-handoff.md) | Escalation paths, adjacent roles, proportionate action | Calibrated confidence; recommending action sized to evidence and risk; role boundaries | JU-1, JU-2, JU-3, JU-4, CT-1, CT-2, CT-3, CT-4 | Two products from one analysis: a peer handoff and a leadership summary | EF-6, EF-7 |
| 09 | Capstone and transfer | Integrated scenario, then an unrelated situation | Performing the whole chain unaided, then carrying the reasoning to changed technology | All domains, esp. LR-1 – LR-4 | Full assessment, revision under new evidence, and a transfer response | EF-1 – EF-8 |

## The capstone already exists

Lesson 09 does not need to be authored from scratch. [PILOT-001 — Encrypted outbound traffic](lessons/09-capstone-encrypted-outbound-traffic/README.md) is already built as a full-chain performance experience with a staged evidence release, a revision task, a transfer case, and a review guide. It is the natural capstone.

Whatever a run exposes about the capability and evidence models is cheaper to fix than to leave standing under nine lessons. See [run records](lessons/run-records.md).

The pilot's DNS fragmentation transfer case also belongs to lesson 06's subject matter and can seed that lesson's worked example.

## What is written, and why these first

01, 05, and 08 are authored — the three modules that can be built without capture data.

lessons 01 and 08 bracket the course: lesson 01 establishes the habit the whole sequence rests on, lesson 08 the product it builds toward. Writing the ends first tests the outline from both directions before the middle is committed to.

Lesson 05 was originally scoped here as lab-gated. That was wrong, and the correction is worth recording: lesson 05's work product is an *evidence plan*, which is reasoning about what sources can and cannot answer. Producing one requires a described environment, not an accessed one. The lab exercise — configuring a sensor, running a capture, discovering what a tap actually sees — remains worth building, but it is an addition to lesson 05 rather than a precondition for it. The lesson states this limit explicitly.

## Why the capstone has no capture

Lessons 02, 03, 04, 06 and 07 all work from packet captures. Lesson 09 does not, and that is deliberate rather than an oversight.

The capstone supplies nine evidence items across change records, DNS logs, flow data, TLS metadata, endpoint process records, peer comparison, proxy categorisation, a user report, and software inventory. Its difficulty is **integrating sources that disagree in scope and reliability** — which is [lesson 05](lessons/05-vantage-point-and-evidence.md)'s capability, and the one that actually decides real cases. Handing the learner a capture instead would narrow the exercise to the skill they just spent five lessons practising.

Put another way: the middle of the course teaches you to read evidence. The capstone tests whether you can decide when the evidence is partial, mixed, and pointing in different directions. Those are different things, and only the second one is what the job is.

If a future version adds a capture, it should be *in addition to* the nine items, replacing the prose in E-03 and E-04 so the learner derives those observations instead of being given them — not as a substitute for the rest. Worth deciding after someone has actually run it, not before.

## Capability coverage

Checked rather than assumed. Of the [capability model](docs/capability-model.md)'s 27 statements:

- **23 are named as targets by lessons 01–08** — every statement in the OC, OE, IR, JU and CT domains.
- **The four LR statements — learning and model revision — are reached only by the capstone.** Its revision task exercises LR-1 and LR-2, its transfer case LR-3, and its review guide's insistence that a learning need be specific rather than "study all of DNS" is LR-4.

That concentration is worth being explicit about, because it has a consequence: **a learner who stops before the capstone is never asked to revise a model under new evidence.** Lessons 02 through 07 each end in a work product that is written once. Only lesson 09 stages evidence so that a first answer has to be reconsidered.

Whether that is a flaw or the correct design is a real question, and running the course is what answers it. The argument for leaving it: model revision needs something substantial enough to be wrong about, which the smaller lessons do not provide. The argument against: it is the capability most likely to distinguish a good analyst, and it gets one exposure at the very end.

## Known gaps

Every lesson is authored. Two carry gaps they declare in their own text rather than hiding.

**Lesson 06** teaches five failure signatures — refused, dropped, reset mid-transfer, slow-but-correct, and fragment loss. The fifth is the one worth having: it is the only fault in the course that leaves *no trace shaped like a fault*, and it is the mechanic behind the capstone's transfer case. Packet loss and induced latency are still missing, because generating those needs traffic impairment (`netem`) the [capture lab](lab/README.md) cannot produce without privileges.

**Lesson 07** uses lab-generated shapes, not real adversary traffic. The reasoning transfers; the specifics do not. [R004](docs/research/R004-pcap-and-telemetry-sourcing.md) cleared CIC and Stratosphere/CTU-13 for exactly this, and reworking the lesson against captured intrusion traffic is the intended next step. Anything downloaded still has to clear the [validation gate](lab/validate-captures.py).

The larger gap is neither of those. **No lesson has been used by a learner.** Until that happens, the sequence is a design proposal that reads well.

## What this plan does not establish

Per the baseline's Standing Qualifications: no proficiency levels, mastery thresholds, scoring, completion criteria, or assessment validity are defined here. Lesson work products are evidence for review and feedback, not scored artifacts. The course sequence is a design proposal, not a validated learning progression.

## Open questions

These were open while the course was being written. Two are still open.

1. **Who is the learner?** The outline assumes no analysis experience and no tooling background. An audience of working IT staff would compress 02–04 substantially and change the entry point.
2. **How is it delivered?** Self-guided like PILOT-001, or instructor-led with live review? This determines whether feedback is a review guide or a person, which in turn determines whether EF-8 is reachable in lessons before lesson 09.
3. ~~**What is the time budget?**~~ **Answered by construction: about 18 hours.** Lessons 01–08 state 17 hours between them and the capstone adds 60–90 minutes. If a delivery needs less, the honest move is cutting whole lessons rather than thinning all of them — though note that 02 through 07 each depend on the one before.
