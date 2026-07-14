# NADF Assessment Evidence Model v0.1 — Proposed

## Status and purpose

| Field | Value |
|---|---|
| Status | Proposed working model |
| Date | 2026-07-13 |
| Owner | Integrated NADF Project Director / Design Studio |
| Capability target | [Network Analyst Capability Model v0.1](2026-07-12-nadf-network-analyst-capability-model-v0.1-proposed.md) |
| Validation inputs | [Encrypted outbound traffic](2026-07-13-encrypted-outbound-traffic-capability-validation-slice.md); [DNS failure and model revision](2026-07-13-dns-failure-model-revision-capability-validation-slice.md) |
| Governing identity | [ADR-0001](../decisions/0001-adopt-expertise-development-network-analyst-architecture.md) |

This model defines the observable evidence that can make network-analyst capability inspectable. It completes a minimal architecture chain:

> **Capability → realistic task → observable evidence → feedback**

It does not define scores, proficiency levels, mastery thresholds, passing standards, item banks, curriculum sequences, certifications, or a required assessment product. It is a practical design aid, not a validated assessment system.

## Why this model exists

Capability statements are not useful if later work cannot identify evidence that distinguishes meaningful performance from recall, tool familiarity, unsupported confidence, or stylistic conformity.

The first two capability-validation slices produced recurring evidence patterns without requiring a formal rubric. This model preserves those patterns so future tasks can be designed and reviewed consistently enough to learn from, while avoiding premature scoring machinery.

## Evidence principles

- Evidence must come from performance on a meaningful task or from a work product generated through that performance.
- Evidence should be traceable to the capability claim it supports.
- One artifact may provide evidence for several capabilities; one capability may require several evidence sources.
- Internal reasoning should not be inferred from verbosity or agreement with one preferred procedure.
- Tool speed, command recall, and interface familiarity are not substitutes for conceptual understanding, evidence use, or judgment.
- Conclusions should be judged against the evidence available in the task, including its limitations—not against hidden information the analyst could not access.
- Uncertainty and appropriate restraint can be positive evidence.
- Feedback and model revision require an observable change across time, not a claim that learning occurred.
- Assessment formality should increase only when a real consumer needs stronger consistency, comparability, or defensibility.

## Evidence families

### EF-1 — Situation framing

Evidence that the analyst understands the operational purpose, relevant systems, actors, communications, constraints, and decision question.

Observable forms may include:

- a bounded analytical question;
- a concise context statement;
- a system, communication, or dependency explanation; or
- identification of what is inside and outside the immediate scope.

### EF-2 — Observation record

Evidence that relevant observations are accurate, sourced, and separated from interpretation.

Observable forms may include:

- a timeline;
- an observation table;
- selected telemetry excerpts;
- a description of patterns or differences; or
- explicit collection and provenance limitations.

### EF-3 — Explanatory model

Evidence that the analyst can connect observations to structural, relational, or causal understanding.

Observable forms may include:

- a causal narrative;
- a system or communication diagram;
- an expected-behavior model;
- an explanation of a relevant mechanism; or
- predictions derived from the model.

The representation matters only insofar as it makes the explanation inspectable.

### EF-4 — Alternative and investigation analysis

Evidence that the analyst considers plausible explanations and seeks information that can distinguish among them.

Observable forms may include:

- competing explanations;
- expected observations under each explanation;
- prioritized evidence requests;
- a reasoned investigation path; or
- documented revision or rejection of a hypothesis.

No universal analytical sequence is required.

### EF-5 — Evidence evaluation

Evidence that the analyst judges relevance, quality, limitations, contradictions, and evidentiary weight.

Observable forms may include:

- claim-to-evidence links;
- source and telemetry limitations;
- comparison across sources, peers, time, or segments;
- unresolved contradictions; or
- identification of evidence that would change the judgment.

### EF-6 — Judgment and uncertainty

Evidence that the analyst reaches a bounded conclusion proportionate to available evidence.

Observable forms may include:

- an assessment or finding;
- material assumptions;
- alternative explanations that remain plausible;
- confidence or uncertainty with a stated basis;
- a stopping point; or
- a proportionate next action.

### EF-7 — Communication and interface product

Evidence that the analyst makes the work usable to the intended audience and adjacent roles.

Observable forms may include:

- a technical assessment;
- an operational summary;
- a briefing;
- a handoff package;
- an escalation statement; or
- audience-specific versions that preserve the same underlying evidence.

### EF-8 — Feedback, revision, and transfer trace

Evidence that the analyst learns from outcomes, feedback, or changed conditions.

Observable forms may include:

- comparison of expected and actual outcomes;
- a before-and-after model;
- a revised assessment with the cause of revision;
- a checked prediction in a related context;
- correction of a procedure or representation; or
- a targeted learning need tied to observed performance.

## Capability-to-evidence relationships

This matrix identifies likely evidence families, not mandatory one-to-one mappings.

| Capability domain | Primary evidence families | Common supporting evidence |
|---|---|---|
| Operational context and system understanding | EF-1, EF-3 | EF-2, EF-5 |
| Observation and evidence | EF-2, EF-5 | EF-1, EF-4 |
| Investigation and analytical reasoning | EF-3, EF-4, EF-5 | EF-2, EF-6 |
| Judgment and uncertainty | EF-6 | EF-4, EF-5, EF-7 |
| Communication and team interfaces | EF-7 | EF-1, EF-5, EF-6 |
| Learning and model revision | EF-8 | Any earlier evidence family used before and after feedback or outcome |

## Minimum task conditions

A task intended to expose integrated capability should provide enough structure to make performance possible without dictating the answer.

Use only the conditions the task actually needs:

- a meaningful operational question or decision;
- sufficient context to avoid pure guessing;
- observable data with realistic limitations;
- at least one plausible alternative when reasoning or judgment is being examined;
- an opportunity to select, interpret, or request evidence;
- a consumer or action when communication is being examined; and
- feedback, new evidence, or an outcome when learning and revision are being examined.

Do not add ambiguity, noise, tool complexity, or time pressure unless the capability under examination requires it.

## Minimal evidence bundle

A lightweight evidence bundle may contain:

1. **Task context:** what the analyst was asked to understand or decide and what evidence was available.
2. **Analyst work product:** the resulting explanation, investigation, assessment, communication, or revised model.
3. **Evidence trace:** enough linkage to inspect how material claims relate to observations and limitations.
4. **Outcome or feedback trace when relevant:** what changed and how the analyst responded.

Not every task needs four separate documents. These elements may appear in one concise artifact, system trace, discussion record, or annotated work product.

## Review questions

Use questions before rubrics. For a given task, ask only what is relevant:

- Did the analyst frame the real question and context?
- Are observations accurate and distinguishable from interpretation?
- Is the explanation technically and causally coherent enough for the task?
- Were plausible alternatives considered where ambiguity existed?
- Was evidence selected and weighted for a reason?
- Are limitations, assumptions, and uncertainty visible?
- Is the judgment proportionate to the evidence?
- Is the recommended action proportionate to risk and scope?
- Can the intended consumer use the communication or handoff?
- Did feedback or outcome produce a justified model revision?
- Can claims about capability be supported without relying on verbosity, style, or tool fluency?

These questions support design review and feedback. They are not a scoring scale.

## Validation against existing slices

### Encrypted outbound traffic

The first slice produced EF-1 through EF-7 through a bounded question, observation table, alternative analysis, prioritized evidence needs, qualified assessment, action, and handoff. It did not produce EF-8 because no later outcome or feedback existed.

This absence was informative: a single initial assessment should not be used to claim learning or model revision.

### DNS failure and model revision

The second slice produced all eight evidence families. Its initial overclaim, peer feedback, path evidence, policy rollback, revised model, transfer check, and audience-specific products made learning and adaptation observable without a maturity level or formal rubric.

Together, the slices show that the evidence families can describe different task structures without requiring one analytical procedure or tool.

## Misuse boundaries

Do not use this model to:

- assign scores or proficiency levels without separate design and validation;
- claim mastery from one work product;
- reward length, jargon, stylistic conformity, or agreement with a preferred narrative;
- require analysts to expose private internal thought processes when observable work is sufficient;
- treat every evidence family as mandatory in every task;
- turn a tool interface into the assessment construct;
- infer curriculum sequence; or
- claim assessment validity that has not been established.

## Open issues

- Evidence sufficiency for high-consequence claims remains undefined.
- Reliability and consistency across reviewers have not been tested.
- No proficiency, independence, complexity, or transfer thresholds are defined.
- The model has not been tested against real practitioner work products.
- Accessibility and alternative response forms require later consideration if formal assessments are developed.
- Strong claims that NADF develops or validates expertise remain unsupported until implementation and validation exist.

These issues limit claims but do not prevent practical use as a design aid.

## Intended use now

Use Assessment Evidence Model v0.1 to:

- design or review representative tasks;
- check whether a work product can expose the intended capability;
- structure useful feedback;
- avoid mistaking recall or tool operation for integrated performance;
- identify when an assessment claim would exceed available evidence; and
- decide later whether a rubric, proficiency model, or stronger validation effort has a real consumer.

Do not formalize further until practical use demonstrates a need.
