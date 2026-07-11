# NADF Architecture Baseline v0.2 — Proposed

## Document Status

| Field | Value |
|---|---|
| Artifact | NADF Architecture Baseline v0.2 |
| Owning studio | NADF Design Studio |
| Status | **PROPOSED — FOR ORCHESTRATOR ARCHITECTURAL REVIEW** |
| Architecture approval status | **Not accepted architecture unless and until approved through governance** |
| ADR status | **No ADR created or drafted** |
| Research status | No new research conducted |
| Curriculum status | No curriculum implementation authorized |
| Engineering status | No Engineering changes authorized |
| Primary predecessor | `docs/design-studio/2026-07-10-nadf-architecture-baseline.md` |
| Research input | Accepted NADF Research Reconciliation Package covering R001, R002, and R003 |
| Gate input | Gate G2 — **PASS WITH CONDITIONS** |
| Design Studio synthesis date | 2026-07-11 |
| Timezone | America/Boise |

> **Governance status:** This document is a Design Studio proposal. It synthesizes the preserved Architecture Baseline with the accepted R001–R003 Research Reconciliation Package and the Gate G2 disposition of **PASS WITH CONDITIONS**. It does not, by itself, approve architecture, create an ADR, authorize Engineering work, modify `docs/framework/`, or authorize curriculum implementation.

---

# 1. Purpose

NADF Architecture Baseline v0.2 reconciles the prior Architecture Baseline with the completed research reconciliation of R001, R002, and R003.

Its purpose is to make the current architectural state easier to understand by separating:

1. **research-supported architectural direction**;
2. **research-informed architectural judgment**;
3. **unresolved architectural questions**;
4. **deferred evidence or feasibility dependencies**; and
5. **consequential decision candidates**.

This proposal also identifies where prior architectural directions should be:

- strengthened;
- retained but qualified or narrowed;
- left unresolved;
- deferred;
- or no longer carried forward in their prior form.

This document does not attempt to make research perform the role of architecture. Research constrains and informs architectural judgment; it does not automatically select the NADF architecture.

---

# 2. Governing Inputs and Gate G2 Conditions

## 2.1 Architecture Baseline input

The predecessor Architecture Baseline preserves a historical set of NADF design directions, including:

- NADF as an expertise-development architecture;
- reality-first and mission-before-mechanics orientation;
- normal before abnormal;
- mental models before memorization;
- a shared knowledge-model concept;
- enterprise activity;
- communication stories;
- analyst competency;
- analytical reasoning;
- systems thinking;
- learning architecture;
- assessment architecture;
- generated learning and practice artifacts;
- TOM and COM;
- tool and vendor neutrality;
- architecture before implementation.

It also preserves three historical architectural formulations without claiming that they are one settled hierarchy:

### Historical model-category view

- analyst competency models;
- knowledge models;
- enterprise activity models;
- communication stories;
- learning architecture;
- assessment architecture;
- generation specifications.

### Historical conceptual-layer view

- philosophy;
- competencies;
- knowledge domains;
- communication stories;
- observables;
- analyst decisions;
- detection;
- threat emulation.

### Historical reality-to-detection view

- reality;
- problems;
- protocols;
- conversations;
- systems;
- behaviors;
- evidence;
- detection.

The predecessor baseline intentionally left the relationship among those formulations unresolved.

## 2.2 Research Reconciliation input

The accepted Research Reconciliation Package concluded that R001, R002, and R003 provide substantial directional support for an NADF concerned with:

- expertise rather than recall;
- structured, causal, and revisable mental models;
- analytical reasoning;
- evidence use;
- uncertainty;
- guided and scaffolded development;
- authentic practice;
- feedback;
- model revision;
- integrated analyst performance.

The evidence was judged strongest for:

- cognitive direction;
- developmental direction;
- instructional direction.

The evidence was judged weaker for:

- specific NADF structural choices.

The evidence was judged largely absent for:

- project-specific ontology;
- universal artifact coupling;
- generation architecture;
- project-specific governance structure.

The reconciliation found no direct material contradiction requiring rejection of a currently preserved baseline proposal, but it also made clear that absence of contradiction does not establish an architectural proposal as correct.

## 2.3 Gate G2 conditions preserved in v0.2

This proposal preserves the Gate G2 **PASS WITH CONDITIONS** disposition.

The following conditions remain active:

1. **R002-dependent conclusions remain qualified.**  
   R002 is useful as a conceptual and design input, but its citation alignment, source quality, and claim-to-source traceability require future remediation before selected high-consequence claims are treated as settled doctrine.

2. **Research support does not automatically determine architecture.**  
   A research-supported direction may still permit multiple reasonable architectural solutions.

3. **Absence of contradiction is not proof.**  
   A proposal is not validated merely because R001–R003 did not contradict it.

4. **Project-specific structural choices remain architectural matters unless explicitly synthesized and later governed.**  
   This includes:
   - the shared knowledge model;
   - the architecture root;
   - enterprise activity;
   - communication stories;
   - TOM;
   - COM;
   - model-once/generate-many;
   - the relationship among historical architecture views.

5. **No new research is implied or authorized.**  
   Evidence remediation, validation work, provenance recovery, or engineering feasibility work requires Orchestrator assignment where applicable.

---

# 3. Status Language Used in v0.2

## 3.1 Research-Supported Architectural Direction

A direction for which the research reconciliation found direct or substantial directional support.

This status does **not** mean that a specific implementation, taxonomy, schema, sequence, rubric, or governance mechanism is research-proven.

## 3.2 Research-Informed Architectural Judgment

A Design Studio synthesis that is consistent with the research record but not determined by it.

These judgments are proposed architecture and remain subject to Orchestrator review.

## 3.3 Unresolved Architectural Question

A consequential architectural issue for which the current baseline does not select a durable answer.

## 3.4 Deferred Dependency

An issue intentionally withheld from architectural commitment because of:

- evidence limitations;
- provenance limitations;
- validation needs;
- engineering feasibility needs;
- or dependency on a prior architectural definition.

## 3.5 Consequential Decision Candidate

A choice that may eventually warrant an explicit governed architectural decision because it is:

- durable;
- cross-cutting;
- difficult to reverse;
- constraining to multiple studios or artifact types;
- or likely to create significant downstream coupling.

A consequential decision candidate is **not** an ADR and does not imply that an ADR must be created.

---

# 4. Proposed Architectural Identity

## 4.1 Research-supported direction

NADF should develop network analysts who can do more than recall protocol facts or operate tools.

The integrated performance target includes the ability to:

- observe network activity accurately;
- explain system and communication behavior;
- connect observations to structural and causal models;
- investigate ambiguous conditions;
- evaluate evidence;
- distinguish observation from interpretation and judgment;
- manage uncertainty and alternative explanations;
- communicate defensible assessments;
- learn from outcomes and revise mental models.

R001–R003 materially strengthen this direction.

## 4.2 Design Studio judgment

**v0.2 proposes that NADF be treated as an expertise-development architecture for the network analyst role.**

This is an architectural judgment, not a research conclusion.

The research supports expertise development as a legitimate and important target. The Design Studio judgment is that this target should define NADF's architectural identity.

NADF is therefore proposed as:

> A developmental architecture for building the technical understanding, structured mental models, analytical reasoning, evidence use, judgment, communication, and adaptive learning required to perform network analysis in uncertain operational environments.

This statement is intentionally broader than a course sequence, protocol syllabus, skills checklist, or tool-training program.

## 4.3 Scope judgment

**v0.2 proposes that the primary scope remain the network analyst role.**

The architecture should recognize that network analysts:

- operate within teams;
- consume and produce information used by adjacent roles;
- depend on shared telemetry and operational context;
- may support detection, investigation, response, engineering, threat hunting, and validation activities.

However, NADF should not silently expand into a general architecture for all cybersecurity roles.

Team interfaces remain relevant, but the network analyst remains the primary development target unless future governance changes the scope.

---

# 5. Proposed v0.2 Architectural Concerns

v0.2 does **not** select a single universal root object.

Instead, it proposes a set of architectural concerns that must remain coherent and traceable to one another.

These concerns are not a rigid hierarchy and should not be interpreted as a required implementation schema.

## 5.1 Concern A — Operational and Domain Reality

NADF must preserve connection to real systems, communications, behaviors, constraints, and operational purposes.

Relevant questions include:

- What systems and actors exist?
- What are they trying to accomplish?
- Why do they communicate?
- What behaviors are expected in context?
- What protocols or mechanisms enable the activity?
- What variability is legitimate?
- What failures, misuse, adversary behavior, or anomalies may occur?

### Status

**Research-supported direction:** Context, system purpose, authentic problems, and structural relationships matter.

**Design Studio judgment:** NADF should organize technical knowledge so that protocols and tools remain connected to system purpose and observable behavior.

**Unresolved:** Whether `enterprise activity` should become a formal organizing object or primary architecture root.

## 5.2 Concern B — Knowledge and Representation

NADF must support coherent representations of:

- systems;
- relationships;
- communication behavior;
- protocols and functions;
- causal dependencies;
- expected patterns;
- observables;
- evidence relationships;
- analyst questions;
- and relevant operational context.

### Status

**Research-supported direction:** Structured, causal, relational, and revisable representations support expertise and reasoning.

**Design Studio judgment:** NADF requires coherent and traceable knowledge representations.

**v0.2 does not require one monolithic shared formal knowledge model.**

The prior principle **“One shared knowledge model”** is therefore not carried forward in its original mandatory singular form.

v0.2 proposes the narrower principle:

> **Coherent, governed, and traceable knowledge representations should reuse shared concepts and relationships where practical, while allowing multiple fit-for-purpose views or models when one representation would be insufficient or excessively constraining.**

### Unresolved

- whether a formal ontology is required;
- whether one authoritative semantic core is needed;
- how multiple representations would stay consistent;
- how model ownership and versioning would work;
- whether any model becomes authoritative for downstream generation.

## 5.3 Concern C — Analyst Cognition, Reasoning, and Performance

NADF must explicitly address how analysts:

- notice relevant information;
- build and apply mental models;
- explain observations;
- generate and compare plausible explanations;
- determine what evidence matters;
- interpret telemetry;
- manage uncertainty;
- reach judgments;
- communicate;
- and revise models after new evidence or outcomes.

### Status

**Research-supported direction:** Analytical reasoning, evidence use, uncertainty, structural and causal models, prediction, and model revision are central to expertise.

**Design Studio judgment:** Analytical reasoning should be treated as a cross-cutting NADF dimension rather than a single isolated lesson topic.

### R002 qualification

Any specific lifecycle terminology or claim materially dependent on R002 remains qualified pending any future authorized evidence remediation.

## 5.4 Concern D — Development and Learning

NADF must define framework-level constraints for how expertise is developed while leaving curriculum implementation to the Curriculum Studio.

### Research-supported direction

The evidence materially supports a family of approaches emphasizing:

- guidance;
- scaffolding;
- explicit models;
- worked examples where appropriate;
- authentic and contextualized problems;
- scenarios and cases;
- deliberate and varied practice;
- feedback;
- reflection;
- troubleshooting;
- progressively greater independence;
- model revision.

### Design Studio judgment

v0.2 proposes the following framework-level learning constraints:

1. Novice learning should not rely primarily on minimally guided discovery.
2. Tools should be used in service of conceptual understanding and analyst performance, not as substitutes for them.
3. Scaffolding should be reduced as capability develops.
4. Practice should increasingly require explanation, prediction, evidence use, and adaptation.
5. Learning should include opportunities to revise incorrect or incomplete models.

These constraints do not require every module to use every instructional method.

## 5.5 Concern E — Assessment and Evidence of Competence

NADF must assess more than factual recall or correct tool execution.

### Research-supported direction

The evidence supports assessing integrated performance through tasks involving some combination of:

- observation;
- explanation;
- troubleshooting;
- prediction;
- evidence use;
- investigation;
- communication;
- transfer;
- model revision.

### Design Studio judgment

v0.2 proposes that NADF assessment be based on **evidence of integrated analyst performance**.

No single assessment instrument, rubric, maturity threshold, or scoring model is approved by this proposal.

Reasoning may be assessed only through designed observable evidence such as:

- task performance;
- explanations;
- external representations;
- evidence selection;
- alternative explanations;
- predictions;
- written or oral assessments;
- model revision.

The architecture must avoid treating verbosity, stylistic conformity, tool familiarity, or agreement with one instructor-preferred thought process as proof of competence.

## 5.6 Concern F — Supporting Models, Artifacts, and Implementations

NADF may use many supporting artifact types, including:

- modules;
- labs;
- assessments;
- PCAPs;
- packet walkthroughs;
- telemetry exercises;
- scenarios;
- instructor guides;
- student materials;
- TOMs;
- COMs;
- capstones;
- future generated artifacts.

These are not assumed to occupy the same structural level.

No universal one-to-one relationship is established among:

- modules;
- labs;
- assessments;
- TOMs;
- COMs.

Any future mandatory coupling rule requires explicit architectural governance.

---

# 6. Research-Supported Architectural Directions Strengthened in v0.2

## 6.1 Expertise rather than recall or tool operation

**Disposition: Strengthened.**

The original direction is materially reinforced by R001–R003.

NADF should continue to target integrated network-analyst performance rather than define success primarily through:

- memorization;
- protocol trivia;
- command recall;
- procedural completion;
- or tool operation.

The exact competency taxonomy remains unresolved.

## 6.2 Structured, causal, and revisable mental models

**Disposition: Strengthened and clarified.**

The prior principle **“mental models before memorization”** is retained, but v0.2 clarifies that mental models should be:

- structured;
- relational;
- causal where appropriate;
- testable against observations;
- revisable;
- and fit for purpose.

v0.2 rejects any interpretation in which a learner is expected to internalize one static, universally correct mental picture of a complex system.

## 6.3 Analytical reasoning as cross-cutting

**Disposition: Strengthened, with R002 qualification.**

Analytical reasoning should cross technical subject areas.

However, v0.2 does not adopt one rigid universal analytical procedure.

## 6.4 Evidence, uncertainty, and model revision

**Disposition: Strengthened, with R002-dependent details qualified.**

NADF should distinguish among:

- observation or data;
- interpretation;
- evidence;
- finding;
- assessment or judgment;
- decision or recommendation.

It should also teach analysts to identify:

- assumptions;
- evidence gaps;
- telemetry limitations;
- alternative explanations;
- uncertainty;
- and what additional evidence could change the judgment.

Exact terminology and mandatory procedural treatment remain subject to later design and governance.

## 6.5 Guided and scaffolded development

**Disposition: Strengthened.**

Guidance, scaffolding, authentic practice, feedback, and progressive independence are retained as framework-level developmental directions.

The Curriculum Studio remains responsible for implementation.

## 6.6 Authentic and practice-rich learning

**Disposition: Strengthened.**

NADF learning should increasingly require analysts to perform meaningful work rather than merely recognize definitions or follow demonstrations.

Authenticity should not be interpreted as immediate unassisted complexity for novices.

## 6.7 Integrated analyst assessment

**Disposition: Strengthened as a principle; implementation deferred.**

Assessment should gather evidence of integrated performance.

Specific:

- rubrics;
- scoring rules;
- validity standards;
- mastery thresholds;
- and maturity levels

remain unresolved.

## 6.8 Tool-neutral architectural identity

**Disposition: Strengthened and qualified.**

NADF architecture should not be bound to a single vendor or product.

Tool neutrality does not mean tool absence.

Future implementation may require:

- minimum telemetry capabilities;
- representative tool profiles;
- platform-specific labs;
- or implementation baselines.

Those requirements are not defined in v0.2.

---

# 7. Research-Informed Architectural Judgments in v0.2

The following are Design Studio judgments. They are not presented as direct research conclusions.

## 7.1 NADF should use multiple architectural concerns rather than force one root object now

v0.2 proposes that NADF proceed without selecting one universal root object at this stage.

This judgment is based on the current state:

- expertise development is strongly supported as the framework purpose;
- context and system purpose matter;
- relational and causal representations matter;
- analytical reasoning matters;
- learning and assessment matter;
- but research does not establish `enterprise activity`, `communication`, `analyst work`, or another object as the correct universal root.

Therefore:

> **v0.2 does not designate `enterprise activity` or any other object as the canonical architecture root.**

This is a temporary architectural posture, not a claim that a root object can never be useful.

## 7.2 The historical architecture formulations should be treated as distinct views, not silently merged into one hierarchy

v0.2 proposes the following treatment:

### Model-category formulation

Treat as a **portfolio view** describing categories of models or architectural products.

### Conceptual-layer formulation

Treat as a **concern and traceability view** showing important domains of architectural attention.

### Reality-to-detection formulation

Treat as a **conceptual flow view** illustrating how operational reality may become observable evidence and downstream analytical or detection activity.

This is a v0.2 Design Studio interpretation for synthesis.

It does not claim that this was the original historical intent of those formulations.

None of the three is designated as the single canonical architecture hierarchy in v0.2.

If this treatment is accepted as durable architecture, it may warrant an explicit future decision.

## 7.3 Analytical reasoning should use common functions, not a rigid universal sequence

R002 identifies recurring analytical functions.

v0.2 proposes to retain those functions as a **provisional working model**, not a mandatory sequence.

The provisional functions are:

1. problem framing;
2. candidate explanation or hypothesis generation;
3. evidence planning;
4. evidence collection and preservation where applicable;
5. evidence evaluation and sensemaking;
6. judgment, action, and communication;
7. learning and model revision.

These functions may:

- overlap;
- repeat;
- occur in different orders;
- be abbreviated during rapid work;
- or be expanded during deliberate investigation.

They should not be treated as a seven-step checklist that all analysts must execute identically.

Because this model is materially dependent on R002, its status remains qualified pending any future authorized evidence remediation.

## 7.4 Development should be treated as a continuum before discrete levels are adopted

Research supports change from:

- greater dependence on explicit guidance and procedures;
- toward stronger models, discrimination, pattern recognition, self-monitoring, and adaptive judgment.

v0.2 proposes that NADF recognize this developmental continuum.

v0.2 does **not** adopt:

- a fixed number of maturity levels;
- named levels;
- mastery thresholds;
- or a universal progression ladder.

Those remain later architectural questions.

## 7.5 “Normal before abnormal” should be narrowed

The prior principle is not carried forward as an absolute universal sequencing rule.

v0.2 replaces it with:

> **Expected behavior before unexplained deviation, when the task requires anomaly interpretation.**

This means learners should develop enough contextual understanding of expected behavior to reason about deviations, while recognizing that:

- environments vary;
- normality is contextual;
- expected behavior can be uncertain;
- malicious and legitimate behaviors can overlap;
- and some learning may begin with a failure, anomaly, or incident as the motivating problem.

The architectural intent is to prevent analysts from treating every unfamiliar observation as malicious and to prevent instruction from teaching a false universal baseline.

## 7.6 Concepts should precede independent tool use, not all tool exposure

The prior direction is narrowed.

v0.2 proposes:

> **Novices should not be expected to learn complex network analysis primarily through independent, minimally guided tool use.**

Early tool use may be appropriate when it is:

- guided;
- conceptually anchored;
- purpose-driven;
- and integrated with explanation.

The architecture does not require a tool-free conceptual phase.

## 7.7 Knowledge representation should prioritize coherence and traceability over singularity

The prior **“one shared knowledge model”** principle is replaced.

v0.2 proposes:

> **Use shared concepts and relationships where they improve coherence and traceability, but permit multiple fit-for-purpose representations until a stronger architectural case exists for a single formal model.**

This reduces the risk of prematurely freezing:

- ontology;
- granularity;
- artifact structure;
- curriculum structure;
- or generation assumptions.

## 7.8 Communication stories should remain a candidate representation pattern, not a core governed object

The research supports:

- contextualized cases;
- meaningful representations;
- narrative or scenario structures;
- system and causal relationships.

It does not establish the NADF-specific construct `communication story`.

v0.2 therefore retains communication stories as a candidate representation pattern that may connect:

- actors;
- purpose;
- systems;
- communications;
- expected behavior;
- observables;
- analyst interpretation.

However, v0.2 does not make `communication story` a mandatory architectural object.

Its definition, granularity, schema, and relationship to other representations remain unresolved.

## 7.9 TOM and COM should remain outside the mandatory core architecture for now

TOM and COM are preserved as existing project concepts.

v0.2 does not make either one:

- mandatory for every module;
- mandatory for every lab;
- mandatory for every assessment;
- or a required core architecture component.

Their potential value is acknowledged, but their:

- purpose;
- authority;
- schema;
- coupling;
- relationship;
- and governance

remain unresolved.

## 7.10 Model-driven generation should be treated as an aspiration and feasibility hypothesis

The prior motto:

> Model reality once. Generate learning from the model.

is preserved as historical design intent.

It is not carried forward as a validated architectural requirement.

v0.2 replaces the hard requirement with:

> **Model important knowledge explicitly, reuse it where practical, and require evidence of feasibility before committing NADF to model-driven generation as core architecture.**

Whether model-once/generate-many becomes:

- a core architectural requirement;
- an optional capability;
- a tooling strategy;
- or a deferred engineering concern

remains unresolved.

---

# 8. Proposed v0.2 Core Principles

The following principles are proposed for Orchestrator review.

## 8.1 Reality and context matter

Technical facts should be connected to:

- systems;
- purposes;
- behavior;
- constraints;
- and operational context.

## 8.2 Expertise is integrated performance

NADF should develop the analyst's ability to:

- observe;
- explain;
- investigate;
- evaluate evidence;
- judge;
- communicate;
- and learn.

## 8.3 Mental models must be structured and revisable

Learners should build models that support:

- explanation;
- prediction;
- comparison;
- troubleshooting;
- and revision.

## 8.4 Analytical reasoning is cross-cutting

Reasoning should be developed across technical subject areas rather than isolated in one analytical-method lesson.

## 8.5 Observations are not automatically evidence

Analysts should learn to explain why an observation matters to a question, explanation, or judgment.

## 8.6 Uncertainty should be made visible

Analysts should identify:

- limitations;
- assumptions;
- alternatives;
- missing evidence;
- and confidence appropriately.

## 8.7 Guidance should precede independence

Novices require structured support, but support should progressively reduce as capability develops.

## 8.8 Expected behavior should be contextual

Analysts need models of expected behavior, but NADF should not teach a single universal definition of normal.

## 8.9 Tools serve analyst development

Tools are necessary implementation environments, but they should not define NADF's architectural identity.

## 8.10 Knowledge representations should be coherent and traceable

NADF should favor reusable shared concepts where useful without prematurely requiring one monolithic model.

## 8.11 Assessment should gather evidence of integrated performance

Correct answers alone are not sufficient evidence of expertise.

## 8.12 Architecture should constrain implementation without becoming curriculum

The Design Studio defines cross-cutting architecture and standards.

The Curriculum Studio implements learning experiences within those constraints.

Engineering implements repository and technical changes only when authorized.

---

# 9. Disposition of Prior Baseline Proposals

| Prior proposal | v0.2 disposition | Rationale |
|---|---|---|
| P-001 — Mission and outcome | **Strengthen** | R001–R003 materially support integrated expertise beyond recall and tool operation. |
| P-002 — Reality-first orientation | **Retain and qualify** | Context and meaningful problems are supported; the exact prior sequence is not established as a universal spine. |
| P-003 — Normal before abnormal | **Narrow and restate** | Retained as contextual expected-behavior-before-deviation, not a universal strict sequence. |
| P-004 — Shared knowledge model | **Do not carry forward in current singular form** | Replace mandatory singularity with coherent, governed, traceable representations; formal model architecture remains unresolved. |
| P-005 — Enterprise activity model | **Retain as unresolved candidate** | Context and purpose matter, but `enterprise activity` is not established as root or mandatory object. |
| P-006 — Communication stories | **Retain but narrow** | Preserve as a candidate representation pattern, not a mandatory governed core object. |
| P-007 — Analyst competency model | **Strengthen at broad capability level; defer taxonomy** | Multidimensional expertise is supported; complete taxonomy and levels remain unresolved. |
| P-008 — Analytical reasoning as cross-cutting | **Strengthen with R002 qualification** | Strong design direction; exact lifecycle and terminology remain qualified and unresolved. |
| P-009 — Mental models and systems thinking | **Strengthen and clarify** | Retain as structured, causal, revisable, fit-for-purpose models rather than static doctrine. |
| P-010 — Learning architecture | **Strengthen as framework-level constraints** | Guided, scaffolded, authentic, model-based, practice-rich development is well supported directionally; exact methods remain Curriculum Studio choices. |
| P-011 — Assessment architecture | **Strengthen principle; defer operational architecture** | Integrated performance is the target; rubric, scoring, validity, and thresholds remain unresolved. |
| P-012 — Generated learning and practice artifacts | **Retain as possible outputs; reject universal coupling** | Artifact diversity remains useful, but no one-to-one coupling is established. |
| P-013 — TOM and COM supporting models | **Defer core architectural status** | Existing research may inform them but does not establish their project-specific role. |
| P-014 — Tool and vendor neutrality | **Retain and qualify** | Architecture should not be product-bound; practical minimum capabilities remain unresolved. |
| P-015 — Architecture before curriculum implementation | **Retain as governance boundary** | Current studio separation is explicit; it should not be retroactively projected onto all historical work. |

---

# 10. Proposals No Longer Carried Forward in Their Prior Form

## 10.1 One shared knowledge model as a mandatory singular architecture

**Prior form:** One shared knowledge model.

**v0.2 treatment:** Not carried forward as a mandatory singular solution.

**Replacement direction:** Coherent, governed, traceable knowledge representations with shared concepts where useful.

## 10.2 Normal before abnormal as an absolute sequencing rule

**Prior form:** Normal before abnormal.

**v0.2 treatment:** Not carried forward as a universal strict sequence.

**Replacement direction:** Build sufficient contextual expectations to reason about deviations; treat normality as environment- and task-dependent.

## 10.3 A rigid canonical analytical lifecycle

**Prior form at risk:** Treating a synthesized lifecycle as one mandatory step-by-step method.

**v0.2 treatment:** Not carried forward.

**Replacement direction:** A provisional set of recurring analytical functions that may iterate, overlap, or vary by mode of work.

## 10.4 Enterprise activity as an implied default architecture root

**Prior form at risk:** Treating `enterprise activity` as the primary root before governance.

**v0.2 treatment:** Not carried forward as a default root.

**Replacement direction:** Retain enterprise activity as a candidate organizing concept pending definition and governance.

## 10.5 Communication story as an assumed core governed object

**Prior form at risk:** Treating `communication story` as a required architecture object because it appears in the historical model set.

**v0.2 treatment:** Not carried forward as mandatory.

**Replacement direction:** Candidate representation pattern pending definition and architectural justification.

## 10.6 TOM and COM as implicitly integrated with all learning units

**Prior form at risk:** Universal or one-to-one coupling with modules, labs, or assessments.

**v0.2 treatment:** Not carried forward.

**Replacement direction:** Preserve artifact independence unless a future governed decision establishes a specific relationship.

## 10.7 Model-once/generate-many as a core requirement

**Prior form:** A shared model reliably generates many downstream artifacts.

**v0.2 treatment:** Not carried forward as a core architectural requirement.

**Replacement direction:** Reuse explicit knowledge where practical; defer generation architecture until feasibility is demonstrated.

---

# 11. Unresolved Architectural Questions

## UAQ-001 — Does NADF need a single architecture root?

Current v0.2 posture: **No root selected.**

Possible future candidates include:

- enterprise activity;
- communication;
- analyst work;
- operational problem;
- another construct;
- or a deliberately multi-view architecture with no single root.

## UAQ-002 — What role should enterprise activity play?

Unresolved:

- definition;
- boundaries;
- granularity;
- relationship to system purpose;
- relationship to workflows;
- relationship to communication stories;
- relationship to curriculum organization.

## UAQ-003 — What knowledge-representation architecture should NADF use?

Unresolved:

- one semantic core;
- multiple coordinated models;
- ontology;
- graph;
- schema;
- document-based representations;
- versioning;
- authority;
- traceability rules.

## UAQ-004 — Should communication stories become a governed object?

Unresolved:

- purpose;
- schema;
- granularity;
- relationship to scenarios;
- relationship to protocol exchanges;
- relationship to enterprise activity;
- whether the term is necessary.

## UAQ-005 — Should NADF adopt a common analytical model?

v0.2 supports recurring functions but does not approve a canonical lifecycle.

Unresolved:

- terminology;
- degree of prescription;
- relationship to rapid versus deliberate work;
- exceptions;
- tool and worksheet implications;
- R002 remediation dependency.

## UAQ-006 — What constitutes the network analyst competency architecture?

Unresolved:

- competency domains;
- completeness;
- role boundaries;
- proficiency descriptions;
- relationship to tasks;
- relationship to assessment;
- relationship to team interfaces.

## UAQ-007 — Should NADF use explicit developmental levels?

Research supports developmental change.

Unresolved:

- whether discrete levels are necessary;
- how many levels;
- what they measure;
- thresholds;
- whether levels describe people, tasks, or performances.

## UAQ-008 — What is the assessment architecture?

Unresolved:

- constructs;
- evidence requirements;
- task design;
- rubric structure;
- scoring;
- validity;
- reliability;
- transfer;
- mastery claims.

## UAQ-009 — What is the minimum tool and telemetry baseline?

Unresolved:

- minimum capabilities;
- platform assumptions;
- vendor neutrality;
- implementation profiles;
- portability requirements.

## UAQ-010 — What are the architectural roles of TOM and COM?

Unresolved:

- purpose;
- audience;
- authority;
- schema;
- coupling;
- governance;
- relationship to threat intelligence;
- relationship to learning;
- relationship to validation and emulation.

## UAQ-011 — What is the durable relationship among historical architecture views?

v0.2 proposes a portfolio/concern/flow interpretation.

That interpretation remains a proposal pending governance.

## UAQ-012 — What are the explicit NADF scope boundaries?

v0.2 keeps the network analyst role primary.

Unresolved:

- interfaces with adjacent roles;
- team-level competencies;
- ownership of detection engineering;
- ownership of threat hunting;
- ownership of incident-response functions;
- where NADF stops.

## UAQ-013 — What promotion criteria move a proposal into accepted architecture?

Unresolved:

- evidence threshold;
- Design Studio synthesis threshold;
- governance review;
- decision record requirements;
- validation requirements;
- versioning rules.

---

# 12. Deferred Evidence, Provenance, and Feasibility Dependencies

## DFD-001 — R001 metadata and repository provenance

The substantive R001 research artifact is available and was accepted for reconciliation.

Remaining issues concern:

- formal title metadata;
- visible identifier metadata;
- version metadata;
- repository path;
- preferred long-term repository representation.

**Disposition:** Metadata/provenance issue only. No new research required.

**Routing:** Orchestrator when normalization or ingestion is authorized.

## DFD-002 — R002 evidence remediation

R002 remains useful as a design input, but selected claims require:

- citation reconciliation;
- source-quality improvement;
- claim-to-source validation.

**Disposition:** Deferred pending explicit Orchestrator authorization.

**Effect on v0.2:** R002-dependent conclusions remain qualified.

## DFD-003 — Network-specific validation of a common analytical model

The current analytical model is substantially synthesized from cross-disciplinary evidence.

**Disposition:** Deferred.

Potential future work may be warranted if NADF intends to make a common lifecycle canonical or use it for high-consequence assessment and doctrine.

## DFD-004 — Comprehensive competency validation

R001–R003 identify relevant dimensions but do not establish a complete authoritative network-analyst competency taxonomy.

**Disposition:** Deferred unless the Orchestrator assigns role/standards research or other validation work.

## DFD-005 — Developmental-level validation

Research supports developmental change but not specific NADF levels or thresholds.

**Disposition:** Deferred until the architecture determines whether discrete levels are necessary.

## DFD-006 — Normal/expected-behavior boundary conditions

Research supports coherent expectations but not one universal network-analysis sequencing rule.

**Disposition:** The principle is narrowed in v0.2; additional targeted validation may be assigned later if needed.

## DFD-007 — Assessment validity

Validated network-specific instruments for reasoning, mental models, uncertainty, and integrated analyst performance remain limited.

**Disposition:** Defer strong mastery claims and validated scoring architecture until sufficient evidence and validation work exist.

## DFD-008 — Knowledge-model architecture

Research supports structural and causal representations but does not establish one optimal architecture.

**Disposition:** Requires Design Studio definition before any research or engineering work is automatically justified.

## DFD-009 — Model-driven generation feasibility

No reviewed evidence establishes the feasibility of the NADF model-once/generate-many hypothesis.

**Disposition:** Deferred.

Potential future work may include an explicitly authorized engineering feasibility prototype after minimum model boundaries are defined.

## DFD-010 — TOM and COM architecture

Research may inform these models but does not establish their NADF-specific role.

**Disposition:** Deferred until purpose and boundaries are defined.

## DFD-011 — Tool and telemetry assumptions

Research supports avoiding tool-centric identity but does not determine practical minimum capabilities.

**Disposition:** Deferred pending architectural definition and possible later research or implementation analysis.

## DFD-012 — Team interfaces and role boundaries

R001–R003 do not determine the correct boundary between the network analyst and adjacent roles.

**Disposition:** Deferred unless scope ambiguity becomes blocking or the Orchestrator assigns targeted work.

## DFD-013 — R003 associated-analysis provenance

No separately authoritative R003 Research Analysis Report was established in the reconciliation inputs.

**Disposition:** No recreation is authorized or required merely to fill the gap.

Historical recovery may occur only if the Orchestrator determines that such an artifact should exist and recovery is necessary.

---

# 13. Consequential Decision Candidates

The following may eventually require explicit architectural decisions if the Orchestrator determines that the choices are durable and consequential.

No ADR is created or drafted here.

## CDC-001 — NADF architectural identity

**Candidate choice:** Adopt NADF as an expertise-development architecture for the network analyst role.

**Why consequential:** It shapes competency, learning, assessment, tooling, and scope.

## CDC-002 — Architecture root or deliberate multi-view posture

**Candidate choice:** Select one root object or explicitly adopt an architecture that does not require one universal root.

**Why consequential:** It affects model structure, traceability, and downstream implementation.

## CDC-003 — Relationship among historical architecture views

**Candidate choice:** Accept, modify, or reject the v0.2 proposal to treat them as portfolio, concern, and flow views.

**Why consequential:** It determines how historical architecture is preserved and how future artifacts map to it.

## CDC-004 — Knowledge-representation architecture

**Candidate choice:** Determine whether NADF uses one authoritative semantic model, multiple coordinated models, or another approach.

**Why consequential:** High downstream coupling and difficult reversibility.

## CDC-005 — Common analytical model

**Candidate choice:** Determine whether recurring analytical functions become canonical NADF architecture.

**Why consequential:** Could constrain curriculum, assessments, TOM/COM, tools, and doctrine.

**Condition:** R002-dependent foundations remain qualified pending any future authorized remediation.

## CDC-006 — Competency architecture

**Candidate choice:** Approve the structure, scope, and authority of the network analyst competency model.

**Why consequential:** Drives curriculum and assessment boundaries.

## CDC-007 — Developmental progression

**Candidate choice:** Determine whether NADF uses explicit framework-wide developmental levels.

**Why consequential:** Affects sequencing, assessment, credentialing, and claims of mastery.

## CDC-008 — Assessment architecture

**Candidate choice:** Define the constructs and evidence standards used to judge analyst competence.

**Why consequential:** Determines what NADF ultimately claims to develop and measure.

## CDC-009 — TOM and COM roles

**Candidate choice:** Define whether TOM and COM are core models, optional supporting models, or separate team artifacts.

**Why consequential:** Could create cross-artifact and cross-studio coupling.

## CDC-010 — Tool and telemetry baseline

**Candidate choice:** Define minimum implementation capabilities while preserving transferability.

**Why consequential:** Affects portability and practical feasibility.

## CDC-011 — Model-driven generation

**Candidate choice:** Determine whether generation from architectural models is a core requirement, optional capability, or separate engineering strategy.

**Why consequential:** Significant architecture and engineering coupling.

## CDC-012 — Scope and adjacent-role interfaces

**Candidate choice:** Define where the network analyst role ends and how NADF interfaces with adjacent roles.

**Why consequential:** Prevents uncontrolled scope expansion or critical omission.

---

# 14. Major Changes from the Prior Architecture Baseline

## 14.1 Research support is now explicit

The prior baseline preserved research relationships and gaps.

v0.2 incorporates the accepted R001–R003 reconciliation and explicitly distinguishes:

- strong directional support;
- partial support;
- qualified support;
- unsupported project-specific structure;
- and architectural judgment.

## 14.2 The architectural core is now clearer

v0.2 proposes a stable core centered on:

- integrated network-analyst expertise;
- structured and revisable mental models;
- analytical reasoning;
- evidence and uncertainty;
- guided development;
- authentic practice;
- integrated assessment;
- tool-neutral architectural identity.

## 14.3 One shared knowledge model is no longer treated as a mandatory singular solution

The prior direction is narrowed to:

- coherence;
- governance;
- traceability;
- reuse of shared concepts where useful;
- multiple fit-for-purpose representations when necessary.

## 14.4 Enterprise activity is no longer treated as an implied default root

It remains a candidate organizing concept.

No universal root is selected in v0.2.

## 14.5 Communication stories are narrowed

They remain a potentially useful representation pattern but are not treated as a required core object.

## 14.6 Normal before abnormal is restated

The absolute slogan is replaced with a contextual principle concerning expected behavior and unexplained deviation.

## 14.7 Concepts before tools is clarified

The concern is minimally guided independent tool use, not all early tool exposure.

## 14.8 Analytical lifecycle is reframed

Recurring functions are retained as a provisional working model.

A rigid universal sequence is not adopted.

R002-dependent claims remain qualified.

## 14.9 Developmental change is retained without adopting maturity levels

v0.2 recognizes progression toward more independent and adaptive performance but does not create level names or thresholds.

## 14.10 Assessment direction is strengthened while scoring architecture remains deferred

Integrated performance becomes a clearer architectural target.

Specific instruments and validity claims remain unresolved.

## 14.11 TOM and COM remain non-mandatory

v0.2 preserves them without making them universal components of modules, labs, or assessments.

## 14.12 Model-once/generate-many is moved from architectural ambition toward deferred feasibility

The historical motto is preserved as provenance.

It is not a core requirement in v0.2.

## 14.13 Historical architecture formulations are given a proposed relationship

v0.2 proposes to treat them as:

- portfolio view;
- concern/traceability view;
- conceptual flow view.

This is a Design Studio synthesis, not a historical fact or accepted architecture.

---

# 15. Unresolved Questions Remaining After v0.2

The most important unresolved questions are:

1. Does NADF need a single architecture root?
2. What exact role should enterprise activity play?
3. What knowledge-representation architecture should NADF use?
4. Should communication stories become a governed architectural object?
5. Should a common analytical model become canonical?
6. What is the complete network analyst competency architecture?
7. Should NADF use explicit developmental levels?
8. What evidence and validity standards define assessment?
9. What minimum tool and telemetry baseline is necessary?
10. What are the architectural roles and relationship of TOM and COM?
11. Should the proposed relationship among the historical architecture views become durable architecture?
12. What are the precise network analyst scope boundaries and adjacent-role interfaces?
13. What governance criteria promote a Design Studio proposal into accepted architecture?
14. Should model-driven generation become a core requirement, optional capability, or separate engineering concern?

---

# 16. Potential Future Decision Candidates

The highest-priority future decision candidates are:

1. **Architectural identity and scope**
2. **Architecture root or deliberate multi-view posture**
3. **Knowledge-representation architecture**
4. **Relationship among historical architecture views**
5. **Common analytical model**
6. **Competency architecture**
7. **Developmental progression**
8. **Assessment architecture**
9. **TOM/COM architectural roles**
10. **Tool and telemetry baseline**
11. **Model-driven generation**
12. **Adjacent-role interfaces**

These are decision candidates only.

No ADR is created or drafted by v0.2.

---

# 17. Evidence or Feasibility Work That May Require Orchestrator Assignment

The following work may require future Orchestrator assignment if it becomes necessary to move architecture forward.

## 17.1 R001 metadata and repository normalization

Purpose:

- normalize title, identifier, version, path, and long-term representation.

This is provenance work, not new research.

## 17.2 R002 evidence remediation

Purpose:

- reconcile citations;
- improve source quality;
- validate claim-to-source relationships.

This work is not initiated by v0.2.

## 17.3 Network-specific analytical-method validation

Potential purpose:

- determine whether the provisional analytical functions generalize sufficiently to network-analysis practice;
- identify modes, exceptions, and failure conditions.

## 17.4 Competency and role-boundary work

Potential purpose:

- test completeness of the competency scope;
- define adjacent-role interfaces;
- prevent uncontrolled scope expansion.

## 17.5 Assessment-validity work

Potential purpose:

- determine which performance evidence supports defensible claims of analyst competence;
- validate scoring and interpretation.

## 17.6 Expected-behavior boundary work

Potential purpose:

- refine the relationship among expected behavior, environmental variability, anomaly interpretation, and adversary behavior.

## 17.7 Tool and telemetry baseline work

Potential purpose:

- identify the minimum practical capabilities required for implementation while preserving architectural transferability.

## 17.8 TOM and COM clarification

Before additional research or Engineering work is automatically warranted, the Design Studio must first clarify:

- intended purpose;
- users;
- boundaries;
- relationship;
- and candidate authority.

## 17.9 Knowledge-model feasibility work

Potential purpose:

- compare one semantic core with multiple coordinated representations;
- evaluate traceability and governance needs.

This should follow clearer architectural requirements.

## 17.10 Model-driven generation feasibility work

Potential purpose:

- test whether a minimal approved model can reliably support more than one downstream artifact type without excessive coupling or loss of context.

This requires explicit authorization and should not begin merely because the historical motto exists.

---

# 18. Proposed Architecture Baseline v0.2 Summary

NADF Architecture Baseline v0.2 proposes that the framework move forward with a stronger and narrower core.

## Stronger core

The evidence materially supports continuing to build NADF around:

- development of integrated network-analyst expertise;
- structured, causal, and revisable mental models;
- analytical reasoning across technical domains;
- explicit evidence use and uncertainty;
- guided and scaffolded development;
- authentic and practice-rich learning;
- feedback and model revision;
- integrated analyst performance;
- transferability beyond one tool.

## Narrower structural commitments

v0.2 does not require:

- one canonical shared knowledge model;
- one architecture root;
- `enterprise activity` as the root;
- `communication story` as a mandatory object;
- one rigid analytical lifecycle;
- fixed developmental levels;
- one assessment rubric;
- TOM or COM as mandatory architecture;
- universal artifact coupling;
- model-once/generate-many as a core requirement;
- one historical architecture view to dominate the others.

## Current Design Studio judgment

The Design Studio proposes a **multi-concern, expertise-development architecture** in which:

- operational reality provides context;
- knowledge representations make systems and relationships explicit;
- analytical reasoning turns observations into evidence and judgment;
- development builds increasingly adaptive performance;
- assessment gathers evidence of integrated competence;
- supporting artifacts remain implementation mechanisms rather than automatically becoming the architecture itself.

This proposal is intentionally sufficient to clarify the current architectural direction without pretending that unresolved structural choices have been settled.

---

# 19. Return to Orchestrator

**Design Studio disposition:** Proposed NADF Architecture Baseline v0.2 is complete for Orchestrator architectural review.

The Orchestrator should determine the next governance action.

This proposal does not:

- approve itself;
- create or draft an ADR;
- authorize Engineering changes;
- modify `docs/framework/`;
- authorize curriculum implementation;
- initiate R002 evidence remediation;
- initiate new research;
- or resolve future consequential decisions beyond the Design Studio judgments explicitly proposed in this document.
