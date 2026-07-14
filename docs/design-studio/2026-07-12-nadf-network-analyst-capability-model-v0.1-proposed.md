# NADF Network Analyst Capability Model v0.1 — Proposed

## Status and purpose

| Field | Value |
|---|---|
| Status | Proposed working model |
| Date | 2026-07-12 |
| Owner | Integrated NADF Project Director / Design Studio |
| Primary decision | [ADR-0001](../decisions/0001-adopt-expertise-development-network-analyst-architecture.md) |
| Architecture posture | [ADR-0002](../decisions/0002-adopt-deliberate-multi-view-architecture-posture.md) |
| View interpretation | [ADR-0003](../decisions/0003-use-lightweight-portfolio-concern-flow-view-interpretation.md) |
| Evidence basis | [R001–R003 reconciliation and provenance recovery](../research/2026-07-11-r001-r003-reconciliation-provenance-recovery.md) |
| Governing proposal | [Architecture Baseline v0.2](2026-07-11-nadf-architecture-baseline-v0.2-proposed.md) |

This model turns NADF's accepted identity and existing evidence into a usable first description of network-analyst capability. It is designed to support practical architecture work, expose gaps, and give later assessment and learning design a concrete target.

It is intentionally not a comprehensive or validated competency taxonomy. It does not define proficiency levels, mastery thresholds, scoring, curriculum sequence, job grades, certifications, staffing requirements, or tool-specific tasks.

## Design constraints

The model follows these constraints:

- Capability means integrated performance, not content coverage or tool operation alone.
- Statements should describe something an analyst can demonstrate through work.
- Technical understanding remains connected to systems, communications, behavior, and operational context.
- Observation, interpretation, evidence, judgment, and recommendation remain distinguishable.
- Uncertainty, evidence gaps, and alternative explanations remain visible.
- Communication and team interfaces are part of analyst performance.
- Tools and procedures support capability but do not define NADF's identity.
- R002-dependent lifecycle or doctrinal claims remain qualified.
- The model remains compact enough to use and revise.

## Evidence and judgment labels

- **RS:** Research-supported direction. Existing evidence materially supports the broad capability direction, but not necessarily this exact wording or decomposition.
- **AJ:** Architectural judgment. The statement organizes existing direction into a proposed NADF capability model.
- **RS/AJ:** Research supports the direction and Design Studio judgment defines its NADF-specific expression.

These labels prevent proposed structure from being misrepresented as a research finding.

## Capability model

### Domain 1 — Operational context and system understanding

The analyst connects technical observations to the systems, communications, purposes, dependencies, and conditions that make them meaningful.

| ID | Observable capability statement | Example evidence | Basis |
|---|---|---|---|
| OC-1 | Explain the relevant purpose, actors, systems, and communications in an operational situation. | A concise system or communication explanation that identifies what is happening and why it matters. | RS/AJ |
| OC-2 | Explain how relevant protocols, services, and components contribute to observed behavior. | A technically accurate explanation connecting mechanisms to behavior rather than listing facts. | RS/AJ |
| OC-3 | Describe expected behavior and legitimate variation in the specific context. | Contextual expectations that identify assumptions and avoid treating all deviation as malicious. | RS/AJ |
| OC-4 | Identify material relationships, dependencies, and plausible causal paths. | A diagram, narrative, or model that connects conditions and effects and can be checked against observations. | RS/AJ |

### Domain 2 — Observation and evidence

The analyst turns available data into traceable, appropriately qualified evidence without collapsing observation into conclusion.

| ID | Observable capability statement | Example evidence | Basis |
|---|---|---|---|
| OE-1 | Identify and describe relevant observations accurately. | A record of observed values, events, timing, or patterns that avoids unsupported interpretation. | RS/AJ |
| OE-2 | Distinguish data and observation from interpretation, finding, judgment, and recommendation. | Work products that make the transition from what was seen to what it may mean explicit. | RS/AJ |
| OE-3 | Select evidence relevant to the question and explain its relevance. | Evidence selections tied to a hypothesis, decision, or uncertainty rather than collected without purpose. | RS/AJ |
| OE-4 | Evaluate evidence quality, limitations, provenance, and possible distortion. | Identification of telemetry gaps, collection limits, ambiguity, missing context, or unreliable sources. | RS/AJ |
| OE-5 | Identify what additional evidence would materially change confidence or direction. | A prioritized next-evidence request connected to a live uncertainty or competing explanation. | RS/AJ |

### Domain 3 — Investigation and analytical reasoning

The analyst frames questions, develops and tests explanations, and adapts an investigation as evidence changes.

| ID | Observable capability statement | Example evidence | Basis |
|---|---|---|---|
| IR-1 | Frame an actionable analytical question from an ambiguous condition or operational need. | A bounded question that identifies the decision, behavior, or uncertainty under investigation. | RS/AJ |
| IR-2 | Generate plausible explanations without prematurely committing to one. | Multiple explanations that are technically and contextually credible. | RS/AJ |
| IR-3 | Derive observable expectations that help distinguish among explanations. | Predictions or discriminating indicators linked to competing explanations. | RS/AJ |
| IR-4 | Plan and perform an investigation that prioritizes informative evidence. | A reasoned sequence of checks that adapts to findings rather than follows a rigid universal procedure. | RS/AJ |
| IR-5 | Integrate evidence across sources, time, layers, or systems when the question requires it. | A coherent account that reconciles or calls out conflicts among observations. | RS/AJ |
| IR-6 | Revise or reject explanations when evidence does not support them. | A visible change in the working model, hypothesis, or investigative direction with reasons. | RS/AJ |

### Domain 4 — Judgment and uncertainty

The analyst reaches bounded, defensible conclusions while making assumptions, uncertainty, and decision limits visible.

| ID | Observable capability statement | Example evidence | Basis |
|---|---|---|---|
| JU-1 | Reach a judgment that is proportionate to the available evidence. | A conclusion whose strength does not exceed the evidence and whose reasoning can be examined. | RS/AJ |
| JU-2 | State material assumptions, alternative explanations, and evidence gaps. | Explicit qualifications that identify what remains unknown or could change the judgment. | RS/AJ |
| JU-3 | Express confidence or uncertainty in terms appropriate to the decision and evidence. | Calibrated language with a clear basis rather than unsupported certainty or vague hedging. | RS/AJ |
| JU-4 | Identify a proportionate next action, escalation, or stopping point. | A recommendation tied to the question, risk, evidence, and cost of further investigation. | AJ |

### Domain 5 — Communication and team interfaces

The analyst makes technical reasoning useful to others and participates in team work without silently expanding NADF into every adjacent role.

| ID | Observable capability statement | Example evidence | Basis |
|---|---|---|---|
| CT-1 | Communicate observations, reasoning, evidence, uncertainty, and judgment clearly. | A concise oral, written, or visual product whose claims can be traced to supporting evidence. | RS/AJ |
| CT-2 | Adapt communication to the audience, decision, and operational context without changing the underlying evidence. | Different levels of detail or framing for technical peers, leaders, or adjacent roles. | AJ |
| CT-3 | Provide and receive usable handoffs with relevant context, boundaries, and open questions. | A handoff that lets another role act without reconstructing the analysis or mistaking uncertainty for fact. | AJ |
| CT-4 | Identify when work crosses into an adjacent role and clarify the interface. | Explicit boundaries and coordination needs involving response, hunting, detection engineering, intelligence, or system ownership. | AJ |

### Domain 6 — Learning and model revision

The analyst improves performance by using feedback, outcomes, and new evidence to revise understanding and approach.

| ID | Observable capability statement | Example evidence | Basis |
|---|---|---|---|
| LR-1 | Compare expected and observed outcomes and identify meaningful differences. | A post-task review that connects surprises or errors to the model or method used. | RS/AJ |
| LR-2 | Revise mental models, explanations, or procedures when feedback or evidence warrants it. | A corrected representation or approach with the reason for the change. | RS/AJ |
| LR-3 | Transfer relevant concepts and reasoning to a changed tool, system, or situation. | Effective performance in a novel but related context without relying solely on memorized interface steps. | RS/AJ |
| LR-4 | Identify current limits and seek targeted guidance, practice, or information. | A specific learning need connected to observed performance rather than a generic topic list. | RS/AJ |

## Cross-domain expectations

The domains are not independent silos. Meaningful network-analysis work normally combines several of them.

The model therefore expects later architecture and assessment work to preserve these cross-domain relationships:

- Operational context gives observations meaning.
- Knowledge and mental models support explanation and prediction.
- Investigation turns questions into targeted evidence gathering.
- Evidence constrains judgment.
- Uncertainty shapes communication and action.
- Feedback and outcomes revise future understanding and performance.

No fixed universal sequence is implied. Analysts may enter, revisit, or combine these functions according to the situation.

## Practical scenario checks

These checks test whether the model is useful enough to describe real work. They are not curriculum labs or validated assessments.

### Scenario A — Unexpected encrypted outbound traffic

A workstation begins making sustained encrypted outbound connections after a software update.

The model supports the analyst in:

- establishing the workstation's purpose, software change, destinations, timing, and expected communication patterns (OC-1 through OC-4);
- recording connection behavior separately from assumptions about compromise (OE-1 and OE-2);
- comparing benign update behavior, misconfiguration, unwanted software, and adversary activity (IR-2 and IR-3);
- identifying telemetry limits created by encryption and deciding what endpoint, DNS, certificate, proxy, or timing evidence would discriminate among explanations (OE-4, OE-5, and IR-4);
- communicating a bounded assessment and proportionate next action (JU-1 through JU-4 and CT-1).

**Result:** The model covers the integrated work without requiring a specific tool or declaring one investigation sequence canonical.

### Scenario B — Intermittent DNS failures with a possible tunneling concern

Users report intermittent name-resolution failures while monitoring also shows unusual query lengths and frequency.

The model supports the analyst in:

- connecting resolver design, client behavior, caching, application activity, and network conditions to expected behavior (OC-2 through OC-4);
- separating service-impact observations from a tunneling interpretation (OE-1 and OE-2);
- considering configuration faults, load, application behavior, malformed clients, and adversary use as alternatives (IR-2);
- selecting discriminating evidence across clients, resolvers, timing, domains, response codes, and payload characteristics (OE-3, IR-3, and IR-5);
- keeping confidence qualified when payload or endpoint context is missing (JU-2 and JU-3);
- handing off clearly if endpoint response or detection engineering work becomes necessary (CT-3 and CT-4).

**Result:** The model exposes the importance of expected behavior, alternative explanations, evidence quality, and adjacent-role boundaries.

### Scenario C — Application latency after a network change

A business application becomes slow after a routing and security-policy change. There is no initial indication of adversary activity.

The model supports the analyst in:

- understanding application purpose, communication paths, dependencies, and recent changes (OC-1 through OC-4);
- framing the question around where and under what conditions latency appears (IR-1);
- comparing network path, policy enforcement, name resolution, transport behavior, server performance, and client effects (IR-2 and IR-3);
- integrating evidence across telemetry sources without treating any single tool as authoritative (OE-3, OE-4, and IR-5);
- identifying when system owners, application teams, or network engineering must act (CT-3 and CT-4);
- using the outcome to revise expectations about the environment (LR-1 and LR-2).

**Result:** The model applies to operational analysis, not only security alerts, and keeps team interfaces visible.

## Findings from the scenario checks

The checks suggest that the six-domain model is usable as a first architecture target. They also expose unresolved issues that should remain open:

- The exact boundary between network analysis, troubleshooting, threat hunting, incident response, and detection engineering needs practical clarification.
- Technical coverage is represented through integrated performance rather than a protocol or topic inventory; a separate knowledge-content view may still be useful later.
- Capability statements do not yet define proficiency, independence, complexity, consistency, or transfer thresholds.
- Example evidence is illustrative and does not establish assessment validity or scoring.
- The model has not been validated for completeness against external role standards or a representative practitioner population.

None of these gaps prevents using v0.1 as a working model.

## Intended use

Use Capability Model v0.1 to:

- test whether proposed NADF work contributes to network-analyst capability;
- organize early assessment-evidence thinking;
- identify missing or overlapping capability statements;
- check whether scenarios exercise integrated performance;
- clarify where adjacent-role interfaces matter; and
- guide a later decision about whether a more formal competency architecture is justified.

Do not use v0.1 as:

- a hiring or performance-management standard;
- a certification blueprint;
- a validated assessment framework;
- a curriculum sequence;
- a proficiency-level model;
- proof that NADF develops expertise; or
- a complete inventory of network-analysis knowledge and tasks.

## Next useful test

Before adding formal levels, schemas, or a larger taxonomy, apply v0.1 to a small set of representative work products or scenario outlines. Revise statements that fail to distinguish meaningful performance, duplicate one another, or leave important analyst work undescribed.

Formalization should occur only when practical use demonstrates a need.

## Validation history

| Date | Validation slice | Result |
|---|---|---|
| 2026-07-13 | [Encrypted outbound traffic](2026-07-13-encrypted-outbound-traffic-capability-validation-slice.md) | The model described the work without structural revision. Learning/model revision and audience adaptation were not observable in the single initial-assessment sample; these are sampling limits rather than model defects. |
| 2026-07-13 | [DNS failure and model revision](2026-07-13-dns-failure-model-revision-capability-validation-slice.md) | Feedback, new evidence, an observed outcome, a transfer check, and two audience-specific products made LR-1 through LR-4 and CT-2 observable. No structural revision was required. |
