# Design Studio Handoff: NADF Architecture Baseline

- **Date:** 2026-07-10 (repository-ingestion working date)
- **Prepared by:** NADF Design Studio
- **Source conversation reference:** Candidate: `Network Analyst Training Builder` and subsequent NADF design discussions; exact baseline-source boundary is a provenance gap
- **Repository issue:** Not available — provenance gap

## Metadata

| Field | Value |
|---|---|
| Transfer title | NADF Architecture Baseline — Design Studio Transfer |
| Working repository-ingestion date | 2026-07-10 |
| Working timezone | America/Boise |
| Historical source date | **[PROVENANCE GAP — not independently established in the available repository record]** |
| Source studio | NADF Design Studio |
| Historical source context | Existing NADF architecture-baseline work developed before this repository transfer |
| Candidate source conversation | `Network Analyst Training Builder` and subsequent NADF design discussions; exact baseline-source boundary requires provenance confirmation |
| Prepared by | NADF Design Studio |
| Repository status | Raw Design Studio transfer; unapproved architectural proposal |
| Review status | Structured for repository ingestion and governance review only |
| Architecture approval status | **Not approved** |
| ADR status | **No ADR created by this transfer** |

> **Governance warning:** This document is a raw transfer from the NADF Design Studio. It records historical architectural substance, interpretations, proposals, unresolved questions, and research relationships for review. It does not constitute approved, adopted, canonical, validated, or final NADF architecture. No consequential architectural proposal recorded here is approved merely because it is preserved in the repository.

The repository-ingestion working date of **2026-07-10, America/Boise** is not asserted to be the historical creation date of the architecture baseline.

## Purpose

This transfer preserves the existing substance of the NADF Architecture Baseline while making its evidentiary, interpretive, architectural, and governance status explicit.

It is intended to:

- preserve the historical design direction without rewriting it as an approved framework;
- distinguish source-supported statements from interpretations, proposals, assumptions, and unresolved questions;
- record the relationship of the baseline to the already-existing prior research artifacts R001, R002, and R003 without inventing a clean dependency chain;
- expose architectural questions and evidence gaps that must be resolved before consequential concepts are promoted into approved framework documentation;
- provide a stable Design Studio record from which later research, governance, curriculum, and engineering work may proceed.

This transfer does **not**:

- approve the NADF architecture;
- create an ADR;
- redefine or replace R001, R002, or R003;
- resolve consequential architectural questions;
- modify curriculum;
- direct repository implementation beyond ingestion of this transfer;
- establish a mandatory dependency sequence among prior research artifacts.

## Sourced Observations

### Source-Supported Statements

The following are treated as source-supported statements about existing NADF artifacts or previously recorded project intent.

1. `NADF Charter v0.1` states that NADF exists to develop network analysts who can observe, interpret, investigate, and communicate enterprise network activity by constructing robust mental models rather than memorizing isolated protocols, tools, or procedures. It characterizes NADF as an architecture for developing expertise rather than merely a collection of lessons.

2. The charter identifies proposed architectural model categories including:
   - analyst competency models;
   - knowledge models;
   - enterprise activity models;
   - communication stories;
   - learning architecture;
   - assessment architecture; and
   - generation specifications.

3. The charter also records ten historical design principles:
   1. Reality is the source of truth.
   2. Mission before mechanics.
   3. Concepts before protocols.
   4. Normal before abnormal.
   5. Mental models before memorization.
   6. Observables before detections.
   7. Guidance before independence.
   8. One shared knowledge model.
   9. Adopt standards. Invent only at the seams.
   10. Architecture before implementation.

4. A prior research artifact associated in project history with the R001 body of work addresses instructional and learning-science approaches relevant to network analyst development, including guided inquiry, cognitive apprenticeship, model-based reasoning, simulation, conceptual change, deliberate practice, and the risks of minimally guided or tool-centric learning. The exact formal R001 title, identifier-bearing source file, and repository path are not established by this transfer and remain a provenance gap.

5. R002 is an existing prior research artifact titled **Analytical Reasoning and Investigative Methodologies Across Professional Disciplines**. Its analysis identifies an iterative analytical pattern involving problem framing, candidate explanations, evidence planning, evidence collection and interpretation, uncertainty management, judgment and communication, and learning. The R002 analysis also identifies citation-quality and traceability concerns requiring remediation before unqualified doctrinal use.

6. R003 is an existing prior research artifact titled **Mental Models, Systems Thinking, and Network Cognition**. It addresses mental models, structural knowledge, systems thinking, model-based reasoning, expert cognition, multiple representations, causal reasoning, and network-specific research gaps. It explicitly states that its analysis supports evidence-based NADF design without presupposing a specific curricular architecture.

7. Existing governance instructions require the architecture baseline to remain an unapproved proposal, require separation of facts, interpretations, proposals, unresolved questions, and potential decision points, and prohibit converting unsupported design assertions into repository truth.

## Interpretations

The following interpretations preserve the direction of the earlier design work but are not themselves established facts.

#### I-001 — NADF is intended as an expertise-development architecture

**Interpretation:** The historical baseline treats the primary design problem as development of network-analyst expertise rather than delivery of a conventional protocol syllabus or tool-training sequence.

**Basis:**
- the charter's stated mission;
- its distinction between architecture and lessons;
- the emphasis on mental models, enterprise activity, observation, analysis, and communication.

**Limit:** The exact operational definition of "expertise" and its measurable developmental stages have not yet been approved.

#### I-002 — Enterprise activity became an important candidate organizing object

**Interpretation:** Historical design work moved away from treating protocols as the primary organizing unit and toward organizing knowledge around why enterprise systems communicate, what problems or objectives those communications serve, and how protocols participate in observable activity.

**Basis:**
- the charter's inclusion of enterprise activity models and communication stories;
- historical Design Studio discussions that progressively emphasized reality, enterprise objectives, communications, systems, behaviors, evidence, and detection.

**Limit:** The baseline does not establish whether `enterprise activity` is the single architectural root object, one model among several, or a curriculum-facing organizational device.

#### I-003 — NADF seeks a reusable model-to-artifact relationship

**Interpretation:** The historical motto, `Model reality once. Generate learning from the model.`, implies an intended separation between reusable domain/knowledge models and downstream learning artifacts.

**Basis:**
- the charter's architectural-model categories;
- its list of potential generated artifacts.

**Limit:** No approved schema, ontology, generation contract, or repository representation is established by this transfer.

#### I-004 — The baseline contains multiple architectural views rather than one settled hierarchy

**Interpretation:** Prior design work used several related but non-identical formulations of the architecture. These formulations appear to represent different perspectives on the same problem, but their formal relationship was never conclusively governed.

**Known historical formulations include:**

- **Model-category view**
  - analyst competency models;
  - knowledge models;
  - enterprise activity models;
  - communication stories;
  - learning architecture;
  - assessment architecture;
  - generation specifications.

- **Conceptual-layer view**
  - philosophy;
  - competencies;
  - knowledge domains;
  - communication stories;
  - observables;
  - analyst decisions;
  - detection;
  - threat emulation.

- **Reality-to-detection view**
  - reality;
  - problems;
  - protocols;
  - conversations;
  - systems;
  - behaviors;
  - evidence;
  - detection.

**Limit:** These views must not be silently collapsed into a single canonical architecture. Their overlap, hierarchy, and intended use remain architectural questions.

## Architectural Proposals

Everything in this subsection is a **proposal**, not an approval.

### P-001 — Mission and Outcome

The Design Studio historically proposes that NADF develop network analysts who can:

- accurately observe network activity;
- explain what is occurring and why;
- connect communications to enterprise systems, objectives, and behaviors;
- investigate ambiguous or abnormal activity;
- distinguish observations from interpretations and conclusions;
- communicate defensible assessments;
- improve their mental models through evidence, practice, and feedback.

The historical baseline therefore proposes that analyst performance be evaluated by more than protocol recall or tool operation.

### P-002 — Reality-First Orientation

The Design Studio historically proposes that NADF begin with real system behavior rather than with an abstract sequence of protocol names.

The candidate logic is:

`real enterprise need or problem`
→ `systems and actors`
→ `communications and conversations`
→ `protocol mechanisms`
→ `observable behavior`
→ `evidence available to the analyst`
→ `analysis and judgment`
→ `possible detection, response, or improvement`

This sequence preserves the historical principle of **mission before mechanics** but remains a candidate architectural relationship.

### P-003 — Normal Before Abnormal

The Design Studio historically proposes that learners build models of expected system and protocol behavior before being asked to identify malicious, failed, or anomalous behavior.

This is consistent with the historical design principle but requires further specification regarding:

- what constitutes a sufficient model of normal behavior;
- how variability is represented;
- how "normal" differs across environments;
- how to avoid teaching a false universal baseline.

### P-004 — Shared Knowledge Model

The Design Studio historically proposes a shared knowledge model from which multiple learning and analytic artifacts could be derived.

Candidate content may include relationships among:

- enterprise objectives and problems;
- systems and roles;
- protocols and protocol functions;
- communications or conversations;
- behaviors and expected sequences;
- observables;
- telemetry sources;
- evidence;
- analyst questions and decisions;
- detections;
- threat behaviors;
- exercises and assessments.

The exact ontology, schema, boundaries, and authoritative representation remain unresolved.

### P-005 — Enterprise Activity Model

The Design Studio historically proposes an enterprise activity model that represents why systems communicate and what operational objective a communication supports.

Candidate examples of activity categories might eventually include authentication, name resolution, service discovery, resource access, administration, synchronization, management, and other enterprise communication functions.

This transfer does not approve any taxonomy of enterprise activities.

### P-006 — Communication Stories

The Design Studio historically proposes communication stories as a way to represent network behavior as meaningful interactions rather than isolated packets or fields.

A communication story may eventually connect:

- actors;
- intent or enterprise objective;
- systems;
- protocol interactions;
- expected sequence;
- observable evidence;
- analyst interpretation.

The term, structure, granularity, and relationship of communication stories to enterprise activities remain unresolved.

### P-007 — Analyst Competency Model

The Design Studio historically proposes an analyst competency model that describes what a network analyst must know and be able to do.

Historical design work suggests that competency may involve some combination of:

- technical and conceptual knowledge;
- observation;
- explanation;
- correlation;
- investigation;
- evidence evaluation;
- judgment;
- communication;
- learning and model revision.

No competency taxonomy, level structure, or assessment standard is approved by this transfer.

### P-008 — Analytical Reasoning as a Cross-Cutting Dimension

The Design Studio records as a proposal for further governance that analytical reasoning should cut across technical content rather than exist as an isolated lesson topic.

R002 is directly relevant to this proposal, but the precise NADF analytical lifecycle, terminology, required techniques, and progression structure remain subject to evidence review and governance.

### P-009 — Mental Models and Systems Thinking as Cross-Cutting Dimensions

The Design Studio records as a proposal for further governance that network knowledge should be organized to support structural, causal, dynamic, and predictive understanding rather than isolated fact accumulation.

R003 is directly relevant to this proposal.

The exact instructional and assessment consequences remain unresolved.

### P-010 — Learning Architecture

The historical baseline proposes a learning architecture that may use:

- explicit models and explanations;
- guided practice;
- progressively reduced scaffolding;
- worked examples;
- scenarios;
- laboratories;
- simulations;
- troubleshooting;
- reflection;
- repeated practice;
- feedback.

R001, R002, and R003 may all be relevant to different parts of this proposal, but the baseline does not establish a single research-to-architecture dependency chain.

### P-011 — Assessment Architecture

The historical baseline proposes that assessment should ultimately measure integrated analyst performance rather than only recall or correct tool operation.

Candidate assessment concerns include:

- accuracy of observation;
- quality of explanation;
- model accuracy;
- evidence use;
- reasoning quality;
- handling of uncertainty;
- communication;
- transfer to unfamiliar situations.

The dimensions, rubrics, maturity levels, scoring rules, and validity evidence remain unresolved.

### P-012 — Generated Learning and Practice Artifacts

The historical baseline proposes that approved architectural models could eventually inform or generate artifacts such as:

- HTML lessons;
- PCAP-generation scripts;
- PCAPs;
- Wireshark walkthroughs;
- Zeek and Security Onion labs;
- instructor guides;
- student workbooks;
- assessments;
- capstones;
- TOMs;
- COMs.

The existence of these artifact types does not imply that each module must contain every artifact type or that TOMs and COMs occupy the same structural level as modules, labs, or assessments.

No one-to-one relationship among modules, labs, assessments, TOMs, or COMs is established by this baseline transfer.

### P-013 — TOM and COM as Related but Distinct Supporting Models

Historical project work includes Threat Observable Models (TOMs) and Cyber Threat Emulation Observable Models (COMs).

This transfer preserves them as existing project concepts but does not define their final architectural status.

Open possibilities include their use as:

- analyst reasoning aids;
- threat-observable models;
- team coordination artifacts;
- exercise-planning artifacts;
- validation artifacts;
- curriculum-support artifacts.

Their schema, governance status, and relationship to the core NADF architecture require separate architectural treatment.

### P-014 — Tool and Vendor Neutrality

The Design Studio historically proposes that NADF teach transferable network-analysis capabilities rather than bind the framework to a specific product.

Tools such as Wireshark, Zeek, Security Onion, or other platforms may be used as implementation environments without becoming the architecture itself.

The degree of required tool baseline versus tool neutrality remains unresolved.

### P-015 — Architecture Before Curriculum Implementation

The historical baseline proposes a separation between:

- architecture and standards owned by the Design Studio;
- evidence development owned by the Research Studio;
- learning-experience implementation owned by the Curriculum Studio; and
- repository execution owned by the Engineering Workspace.

This governance relationship is now explicit project operating context, but this transfer does not retroactively imply that all historical architecture work followed the current process.

## Assumptions

The following assumptions are preserved or exposed for future validation.

| ID | Assumption | Status |
|---|---|---|
| A-001 | Network analyst expertise can be represented sufficiently to guide learning design and assessment. | Unvalidated architectural assumption |
| A-002 | A shared knowledge model can support multiple downstream learning artifacts without excessive loss of context. | Unvalidated architectural assumption |
| A-003 | Enterprise activity or communication purpose is a useful organizing layer for network analyst development. | Proposal requiring architectural and possibly empirical validation |
| A-004 | Normal behavior can be taught in a way that improves interpretation of abnormal behavior without creating overly rigid baselines. | Evidence and design question |
| A-005 | Analyst reasoning can be made sufficiently observable for meaningful assessment. | Partially research-related; operationalization unresolved |
| A-006 | Concepts and mental models should generally precede independent tool use for novices. | Research-relevant; exact instructional implications unresolved |
| A-007 | TOM and COM can integrate with NADF without becoming mandatory components of every learning unit. | Project-context assumption; architecture unresolved |
| A-008 | The initial framework can focus on the network analyst role while recognizing that analysts operate as members of teams. | Current scope assumption; team-role interfaces unresolved |

## Evidence State of Major Baseline Concepts

| Architectural concept | Evidence state | Current Design Studio treatment |
|---|---|---|
| NADF as expertise-development architecture | Supported by charter intent; empirical basis distributed across prior research | Preserve as historical intent; architecture still unapproved |
| Mental models before memorization | Research-relevant through R001 and R003 | Supported directionally; exact implementation unresolved |
| Mission before mechanics | Historical design principle | Proposal requiring operational definition |
| Normal before abnormal | Historical design principle with plausible research relevance | Proposal; evidence and boundary conditions require review |
| One shared knowledge model | Historical architecture proposal | No established validation or approved schema |
| Enterprise activity as organizing object | Historical design evolution | Consequential proposal; relationship to other architecture views unresolved |
| Communication stories | Historical proposal | Provenance and structural-definition gaps |
| Analytical lifecycle | Strongly relevant to R002 | Candidate architectural spine, not approved |
| Developmental progression | Suggested by R002 and broader project work | Candidate model; no approved levels |
| Systems thinking and model-based reasoning | Strongly relevant to R003 and prior research | Candidate cross-cutting design dimension |
| Guided, scaffolded, practice-rich learning | Relevant to prior R001-associated research artifact | Candidate learning-architecture principle |
| Reasoning-centered assessment | Relevant to R002 and R003 | Candidate assessment principle; validity work required |
| Generation from shared models | Historical architecture ambition | Major technical and architectural feasibility gap |
| TOM/COM integration | Existing project concept | Architectural relationship unresolved |
| Tool/vendor neutrality | Historical design direction | Degree of required tooling unresolved |

## Risks and Limitations

1. **Historical consolidation risk:** The baseline was developed iteratively across conversations. A repository transfer can falsely make that evolution look more deliberate, linear, or settled than it was.

2. **Research retrofitting risk:** R001, R002, and R003 existed in relation to the developing framework, but not all baseline concepts were necessarily derived from those reports. Later research relevance must not be mistaken for original causal provenance.

3. **Architecture-view conflation risk:** The model-category, conceptual-layer, and reality-to-detection formulations may represent different views rather than competing full architectures. Their relationship has not been formally defined.

4. **Premature ontology risk:** A shared knowledge model may be useful, but premature schema design could freeze weak assumptions about entities, relationships, granularity, or curriculum structure.

5. **Curriculum leakage risk:** Architectural statements can become de facto curriculum requirements before governance decisions are made.

6. **Tool-centric drift risk:** Downstream implementation environments may become mistaken for framework requirements.

7. **Research quality risk:** At least some prior research artifacts contain source-traceability or evidence-quality limitations that must be addressed before high-consequence claims are treated as settled.

8. **Assessment-validity risk:** A reasoning-centered framework requires valid ways to observe and score reasoning without merely rewarding verbosity, conformity to one thought process, or instructor preference.

9. **Role-boundary risk:** A framework focused on the network analyst role may still require explicit interfaces with adjacent team roles without expanding into an undefined all-cyber workforce framework.

## Decisions Requested

The following are possible future governance gates only. They are not ADRs and are not decisions.

1. **Architecture-root gate:** Determine whether NADF requires one primary organizing object and, if so, whether that object is enterprise activity, network communication, analyst work, or another construct.

2. **Architecture-view gate:** Determine how the model-category, conceptual-layer, and reality-to-detection views relate.

3. **Knowledge-model gate:** Decide whether a shared formal knowledge model is required and what governance applies to its schema.

4. **Analytical-method gate:** Decide whether NADF adopts a common analytical lifecycle, and if so, its terminology, scope, and flexibility.

5. **Competency-model gate:** Decide the structure and authority of the analyst competency model.

6. **Progression gate:** Decide whether NADF uses explicit developmental stages or another progression model.

7. **Assessment gate:** Decide what evidence of analyst performance is required and how reasoning is assessed.

8. **Learning-architecture gate:** Decide which instructional principles become framework requirements versus Curriculum Studio implementation options.

9. **TOM/COM gate:** Decide the architectural role and governance status of TOM and COM.

10. **Tool-baseline gate:** Decide whether the framework specifies minimum tools or telemetry capabilities while remaining vendor neutral.

11. **Generation gate:** Decide whether model-driven content generation is a core architectural requirement, an optional implementation capability, or a future engineering concern.

12. **Framework-promotion gate:** Determine when sufficient research support, provenance, and accepted governance decisions exist to promote selected content into approved framework documentation.

## Editorial and Provenance Statement

This transfer performs editorial normalization for structure, classification, and governance visibility.

It does not claim that:

- the historical baseline existed as one complete document in this exact form;
- every proposal originated at the same time;
- later research caused earlier design ideas;
- R001, R002, and R003 form a linear dependency chain;
- the architecture is approved;
- any future ADR outcome is predetermined.

Where exact historical source boundaries, dates, repository paths, or claim-to-source relationships cannot be established, the transfer records a provenance or evidence gap rather than inventing one.

## Unresolved Questions

| ID | Architectural question | Why it matters | Current evidence state | Research relevance | Current status | Possible future governance gate |
|---|---|---|---|---|---|---|
| AQ-001 | What is the primary unit or organizing object of NADF architecture? | Determines how knowledge, curriculum, assessment, and generation models relate. | Multiple historical proposals; no approved answer. | R001–R003 may constrain but do not by themselves answer the architecture question. | Open | Architecture-root gate |
| AQ-002 | How do `enterprise activity`, `communication story`, `protocol`, `system`, and `behavior` relate? | These concepts appear central but their hierarchy and cardinality are undefined. | Historical design substance only. | R003 may inform structural and systems-model considerations. | Open | Knowledge-model gate |
| AQ-003 | Are the model-category, conceptual-layer, and reality-to-detection formulations separate views of one architecture or competing alternatives? | Prevents silent consolidation of historically distinct formulations. | Provenance confirms multiple formulations; relationship unsupported. | Primarily architectural; research may inform terminology. | Open | Architecture-view gate |
| AQ-004 | Does NADF require one shared formal knowledge model? | Affects reuse, traceability, content generation, and governance complexity. | Historical proposal; no validated schema. | R003 relevant to structural knowledge; ontology-specific research may still be required. | Open | Knowledge-model gate |
| AQ-005 | What constitutes an `enterprise activity`? | Necessary before the concept can organize content or models. | No approved taxonomy or definition. | May require research into enterprise architecture, networking practice, and knowledge representation. | Open | Architecture-root or knowledge-model gate |
| AQ-006 | What is a `communication story`, and how is it different from a workflow, sequence, scenario, transaction, or protocol exchange? | Prevents ambiguous or redundant model objects. | Historical proposal with terminology gap. | R003 may support narrative and model-based representation but does not define NADF terminology. | Open | Terminology/knowledge-model gate |
| AQ-007 | What competencies define the network analyst role? | Required for scope, assessment, curriculum boundaries, and progression. | Prior project research exists, including R001, but exact traceability is incomplete in this transfer. | R001 directly relevant; other standards research may be required. | Open | Competency-model gate |
| AQ-008 | What is the relationship between technical knowledge and analytical reasoning? | Determines whether reasoning is a separate domain, a cross-cutting dimension, or both. | R002 provides substantial relevance; architecture not decided. | R002 directly relevant. | Open | Analytical-method gate |
| AQ-009 | Should NADF use a common analytical lifecycle? | Could provide a shared reasoning structure across labs and investigations but risks over-standardization. | R002 proposes a candidate lifecycle; evidence quality requires remediation in parts. | R002 directly relevant. | Open | Analytical-method gate |
| AQ-010 | Should NADF define developmental stages or maturity levels? | Affects sequencing, assessment, scaffolding, and competency claims. | Candidate progressions exist; none approved. | R002 and R003 relevant; direct validation may still be needed. | Open | Progression gate |
| AQ-011 | How should mental models and systems thinking be operationalized in architecture? | Prevents the terms from becoming vague slogans. | R003 provides substantial conceptual support and research gaps. | R003 directly relevant. | Open | Knowledge-model and assessment gates |
| AQ-012 | What does `normal before abnormal` require in practice? | Could shape sequencing across the entire framework. | Historical principle; boundary conditions unresolved. | R001 and R003 relevant; network-specific validation may be needed. | Open | Learning-architecture gate |
| AQ-013 | What evidence should demonstrate analyst competence? | Determines whether NADF can make defensible performance claims. | R002 and R003 identify candidate dimensions and methods; no approved assessment architecture. | R002 and R003 directly relevant. | Open | Assessment gate |
| AQ-014 | How should uncertainty, alternative explanations, and confidence be represented? | Central to defensible analysis but can add complexity or false precision. | R002 strongly relevant; exact implementation unresolved. | R002 directly relevant. | Open | Analytical-method and assessment gates |
| AQ-015 | What is the role of laboratories, scenarios, simulations, and PCAPs in the architecture? | Prevents delivery methods from being mistaken for architectural components. | R001-associated research supports guided and simulation-based approaches; no approved structural role. | R001 relevant. | Open | Learning-architecture gate |
| AQ-016 | What relationship, if any, must exist among a module, lab, and assessment? | Affects curriculum architecture without necessarily belonging to the core domain model. | Not established by the baseline. | Primarily Curriculum Studio implementation after architecture constraints are known. | Open; downstream | Learning-architecture gate if system-wide |
| AQ-017 | What architectural role do TOMs play? | TOM may be a reasoning model, threat model, observable model, learning scaffold, or combination. | Existing project concept; final status unresolved. | R002 may be relevant to reasoning fields; threat-model research may also be needed. | Open | TOM/COM gate |
| AQ-018 | What architectural role do COMs play? | COM may connect emulation, observables, mitigation, validation, and team workflow. | Existing project concept; final status unresolved. | R002 may inform validation loops; additional CTE research may be required. | Open | TOM/COM gate |
| AQ-019 | Must every learning unit use TOM or COM? | Prevents accidental one-to-one coupling between distinct artifact types. | No support for a universal requirement. | Little direct research relevance until TOM/COM purpose is defined. | Open; default should remain non-mandatory absent decision | TOM/COM gate |
| AQ-020 | How vendor-neutral should NADF be, and what minimum tool or telemetry assumptions are permissible? | Affects transferability and implementation feasibility. | Historical direction favors neutrality; minimum capabilities unresolved. | Standards and workforce research may be relevant. | Open | Tool-baseline gate |
| AQ-021 | Can one shared model reliably generate multiple artifact types? | Central to the historical model-once/generate-many ambition. | Architectural and engineering hypothesis; no validation established. | Research may help with knowledge representation; engineering prototyping likely required. | Open | Generation gate |
| AQ-022 | What evidence threshold is required before a baseline proposal becomes framework architecture? | Necessary to prevent both unsupported adoption and paralysis caused by missing repository links. | Governance distinction exists conceptually but requires operationalization. | Research Studio evidence assessment is relevant; governance decision required. | Open | Framework-promotion gate |
| AQ-023 | How should team context affect a framework currently focused on the network analyst role? | Analysts operate with others, but expanding scope could dilute the current role focus. | Current project scope emphasizes the network analyst role while acknowledging team context. | Team cognition research may eventually be relevant. | Open | Scope gate if consequential |
| AQ-024 | What is explicitly outside NADF scope? | Required to prevent architecture from expanding into all networking, cybersecurity, incident response, or workforce development. | Baseline exclusions are under-specified. | Primarily architectural and governance work. | Open | Scope gate |

## Evidence Needed

## Relationship Principle

R001, R002, and R003 are existing prior research artifacts. This transfer does not recreate, renumber, redefine, or replace them.

Their relationship to the architecture baseline is **many-to-many and historically imperfectly traced**.

The transfer therefore does **not** assert:

`R001 → R002 → R003 → Architecture`

as a formal dependency chain.

A later report may inform an earlier design idea. Multiple reports may support different aspects of the same proposal. A baseline concept may also predate the research later found relevant to it.

## R001

**Identifier:** R001  
**Exact title:** **[PROVENANCE GAP — verify against the existing R001 artifact]**  
**Existing status:** Prior NADF research artifact; do not recreate or redefine.

**Historical project characterization:** Prior project analysis described R001 broadly as addressing what network analysts need to know. That characterization must be verified against R001 itself before it is treated as formal metadata.

**Observed research relevance from the associated prior research artifact:**

- guided rather than minimally guided learning;
- cognitive apprenticeship;
- authentic and problem-centered learning;
- worked examples and scaffolding;
- conceptual change;
- systems thinking and model-based reasoning;
- simulation and scenario-based practice;
- deliberate practice and mastery-oriented learning;
- concerns about tool-centric or unstructured discovery approaches.

**Baseline concepts potentially related to R001:**

- guidance before independence;
- concepts before protocols;
- mental models before memorization;
- learning architecture;
- lab and scenario design;
- progressive scaffolding;
- practice and feedback.

**Relationship classification:** Relevant prior evidence and design input; exact claim-to-source mapping unresolved.

**Gaps:**

- exact R001 title;
- repository path;
- formal Research Studio disposition;
- precise mapping from R001 findings to baseline proposals;
- distinction between direct evidence, synthesis, and design inference.

## R002

**Identifier:** R002  
**Title:** *Analytical Reasoning and Investigative Methodologies Across Professional Disciplines*  
**Existing status:** Prior NADF research artifact; do not recreate or redefine.

The existing R002 analysis identifies substantial relevance to:

- problem framing;
- candidate explanations or hypotheses;
- evidence planning;
- evidence collection and interpretation;
- uncertainty;
- judgment and communication;
- learning and model revision;
- novice-to-expert changes in reasoning;
- distinctions among data, evidence, findings, assessments, and decisions.

**Baseline concepts potentially related to R002:**

- analyst decisions;
- analytical reasoning as a cross-cutting dimension;
- observables becoming evidence;
- reasoning-centered assessment;
- analyst progression;
- TOM reasoning fields;
- COM validation loops.

**Relationship classification:** Strongly relevant research input with explicit evidence-quality and citation-traceability limitations recorded in the existing analysis.

**Important governance caution:** The R002 analysis contains recommendations and proposed framework implications. Those recommendations are not automatically architecture decisions.

**Gaps:**

- citation remediation identified by the R002 analysis;
- validated claim-to-source map;
- decision on whether a common NADF analytical lifecycle should be adopted;
- network-specific validation of cross-disciplinary transfer.

## R003

**Identifier:** R003  
**Title:** *Mental Models, Systems Thinking, and Network Cognition*  
**Existing status:** Prior NADF research artifact; do not recreate or redefine.

R003 is relevant to:

- mental models;
- structural knowledge;
- causal reasoning;
- model-based reasoning;
- systems thinking;
- expert versus novice knowledge organization;
- prediction and mental simulation;
- multiple representations;
- cognitive flexibility;
- model revision;
- network-specific cognition and observability gaps.

**Baseline concepts potentially related to R003:**

- mental models before memorization;
- concepts before protocols;
- shared knowledge model;
- enterprise systems and relationships;
- communication stories;
- systems and behaviors;
- reasoning from observables;
- assessment of explanation, prediction, and troubleshooting.

**Relationship classification:** Strongly relevant research input, especially for cognitive and knowledge-model questions.

**Important governance caution:** R003 explicitly supports evidence-based framework design without presupposing a specific curricular architecture. It therefore does not independently validate any particular NADF hierarchy, ontology, or curriculum structure.

**Gaps:**

- network-specific empirical evidence remains limited in several areas;
- no approved translation from R003 concepts into NADF architecture;
- assessment and operationalization questions remain open.

## Cross-Artifact Relationship Matrix

| Baseline area | R001 relevance | R002 relevance | R003 relevance | Relationship status |
|---|---|---|---|---|
| Mission: develop capable network analysts | Likely relevant to learning design | Relevant to analyst practice | Relevant to expertise and cognition | Convergent relevance; no formal dependency chain |
| Competency model | Potentially relevant | Strongly relevant to analytical behaviors | Relevant to cognitive performance | Requires explicit synthesis |
| Knowledge model | Relevant to learning organization | Indirect | Strongly relevant | Architecture unresolved |
| Enterprise activity model | Indirect | Relevant where activity frames investigation | Relevant to systems and causal structure | Evidence relationship incomplete |
| Communication stories | Relevant to case/scenario learning | Relevant to framing and sensemaking | Relevant to narrative, models, and external representation | Concept under-defined |
| Analytical lifecycle | Indirect | Directly relevant | Complementary cognitive relevance | Candidate architecture question |
| Developmental progression | Relevant to scaffolding | Directly relevant | Directly relevant to expert-novice differences | Candidate model; not approved |
| Learning architecture | Directly relevant | Relevant to reasoning practice | Relevant to model formation and revision | Requires Design Studio synthesis |
| Assessment architecture | Relevant | Directly relevant | Directly relevant | Requires validity and governance work |
| TOM | Limited until purpose is defined | Potentially strong | Potentially relevant to model structure | Architectural role unresolved |
| COM | Relevant to simulation practice | Relevant to validation and learning loops | Relevant to model revision | Architectural role unresolved |
| Shared generation model | Possible relevance | Limited | Relevant to representation questions | Major architecture and engineering gap |

## Research Relationship Conclusion

The existing research record supports continued architectural investigation but does not remove the need for Design Studio judgment and governance.

The appropriate relationship is:

`Research findings and limitations`
→ `Design Studio synthesis and architectural questions`
→ `explicit governance decision where consequential`
→ `Curriculum Studio or Engineering implementation`

This is a governance relationship, not a claim that the historical baseline itself was originally created in that sequence.

## Provenance and Governance Gaps

## Gap-Type Definitions

For this transfer:

- **Evidence gap:** The support for a claim or proposal is absent, insufficient, conflicting, or not yet evaluated.
- **Provenance gap:** Relevant support or history may exist, but the exact source, date, repository path, or claim-to-source relationship is not traceable.
- **Governance gap:** A consequential proposal exists but has not been formally adjudicated through the required project process.
- **Interpretive gap:** Existing material permits multiple reasonable interpretations and the Design Studio has not resolved them.
- **Contradiction gap:** Two source statements or architectural formulations cannot both be applied as written without further reconciliation.

A missing repository link must not automatically be treated as lack of evidence. Conversely, the existence of research somewhere in project history must not automatically be treated as traceable support.

## Gap Register

| ID | Gap | Type | Severity | Required action before promotion to approved architecture |
|---|---|---|---|---|
| PG-001 | Exact historical creation date of the NADF Architecture Baseline is not independently established. | Provenance | Material | Recover source-conversation or dated artifact evidence. Do not substitute 2026-07-10 as the historical source date. |
| PG-002 | Exact source-conversation boundary for the baseline is not established. | Provenance | Material | Identify the conversation or artifact range that constitutes the historical baseline source. |
| PG-003 | The historical baseline was not preserved as one clearly versioned source document before this transfer. | Provenance | Material | Preserve available historical records without rewriting them into false linearity. |
| PG-004 | Exact repository path and formal status of `NADF Charter v0.1` must be verified during ingestion. | Provenance | Material | Link only to the existing repository artifact if found; do not invent a path. |
| PG-005 | Exact formal title and repository path of R001 are unresolved in this transfer. | Provenance | Material | Resolve against the existing R001 artifact without recreating or renaming it. |
| PG-006 | The claim-level relationship between R001 and the baseline is incomplete. | Provenance / evidence | Material | Create traceable synthesis or claim mapping where architecture depends on R001. |
| PG-007 | R002's existing analysis records citation-quality and citation-alignment concerns. | Evidence | Material | Complete the remediation already identified by the R002 process before using affected claims as settled doctrine. |
| PG-008 | R003 is highly relevant to mental-model architecture but does not validate a specific NADF architecture. | Governance / interpretation | Material | Conduct Design Studio synthesis before architectural adoption. |
| PG-009 | Multiple historical architecture formulations exist without a governed relationship. | Interpretive / governance | Blocking for canonical architecture; not blocking for raw transfer | Decide whether they are views, layers, mappings, or alternatives. |
| PG-010 | `Enterprise activity` has not been formally defined or approved as the architecture's primary organizing object. | Governance | Material | Resolve AQ-001 and AQ-005. |
| PG-011 | `Communication story` lacks a governed definition and relationship to other model objects. | Governance / terminology | Material | Resolve AQ-006 before schema or framework promotion. |
| PG-012 | The shared knowledge-model proposal has no approved schema or ontology. | Governance / evidence | Material | Research and design the representation before implementation commitments. |
| PG-013 | The analytical lifecycle is research-supported as a candidate but not approved as NADF architecture. | Governance | Material | Resolve AQ-009 through Design Studio synthesis and future governance. |
| PG-014 | No approved developmental progression or maturity model exists. | Governance | Material | Resolve AQ-010 before using levels as framework requirements. |
| PG-015 | No approved competency taxonomy exists. | Governance | Blocking for full framework approval | Resolve AQ-007 with traceable research and role scope. |
| PG-016 | No approved assessment architecture or validity standard exists. | Governance / evidence | Blocking for defensible mastery claims | Resolve AQ-013 and define validation expectations. |
| PG-017 | `Normal before abnormal` is a historical design principle but its limits are undefined. | Evidence / interpretation | Material | Define environment variability, baselining, and instructional implications. |
| PG-018 | The role of TOM in NADF architecture is unresolved. | Governance | Material | Resolve AQ-017 before treating TOM as mandatory framework structure. |
| PG-019 | The role of COM in NADF architecture is unresolved. | Governance | Material | Resolve AQ-018 before treating COM as mandatory framework structure. |
| PG-020 | No support exists for requiring every module to contain a TOM or COM. | Evidence / governance | Material | Preserve artifact independence unless a later decision establishes a relationship. |
| PG-021 | The relationship among modules, labs, and assessments belongs partly to curriculum architecture and is not fully defined by this baseline. | Governance boundary | Material | Design Studio should set only system-wide architectural constraints; Curriculum Studio should implement them. |
| PG-022 | Tool and vendor neutrality has not been reconciled with practical minimum telemetry and tool assumptions. | Governance | Material | Resolve AQ-020. |
| PG-023 | The model-once/generate-many concept has not been validated technically or architecturally. | Evidence / governance | Material | Define a minimum model and test generation feasibility before making it a framework requirement. |
| PG-024 | Framework promotion criteria are not operationalized at the claim or architecture-component level. | Governance | Material | Define the required combination of evidence, synthesis, review, and accepted decision for promotion. |
| PG-025 | Historical research relationships may be retroactively over-cleaned during repository ingestion. | Provenance risk | Material | Preserve uncertainty and many-to-many research relationships. |
| PG-026 | Current governance roles are clearer than the historical development process and must not be projected backward as if they always existed. | Provenance / governance | Material | Distinguish historical development from current operating governance. |
| PG-027 | Explicit NADF scope exclusions remain under-specified. | Governance | Material | Resolve AQ-024 before full architecture approval. |
| PG-028 | Team interfaces are acknowledged, but the architecture remains focused on the network analyst role. | Scope / governance | Material | Define interfaces without broadening scope unintentionally. |

## Current Governance Disposition

**Disposition:** Suitable for repository ingestion as a **raw Design Studio transfer with explicit unresolved questions and gaps**.

This disposition means only that the historical baseline can be preserved and reviewed in the repository.

It does **not** mean:

- the architecture is approved;
- any architectural component is canonical;
- an ADR has been accepted;
- R001, R002, or R003 has been superseded;
- research gaps have been closed;
- Curriculum Studio implementation is authorized for unresolved architectural proposals;
- Engineering Workspace implementation is authorized beyond ingestion of this transfer.

