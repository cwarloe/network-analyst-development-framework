# ADR-0002: Adopt a deliberate multi-view architecture posture without a universal root

- **Status:** accepted
- **Accepted:** 2026-07-12
- **Date:** 2026-07-12
- **Owners:** Integrated NADF Project Director / Design Studio (proposal); NADF Maintainer (disposition)
- **Related decisions:**
  - [ADR-0001: Adopt NADF as an expertise-development architecture centered on the network analyst role](0001-adopt-expertise-development-network-analyst-architecture.md)
- **Related evidence and proposals:**
  - [NADF Architecture Baseline v0.2 — Proposed](../design-studio/2026-07-11-nadf-architecture-baseline-v0.2-proposed.md)
  - [Architecture Baseline v0.2 — Orchestrator Review](../design-studio/2026-07-11-nadf-architecture-baseline-v0.2-orchestrator-review.md)
  - [R001–R003 Reconciliation and Provenance Recovery](../research/2026-07-11-r001-r003-reconciliation-provenance-recovery.md)
- **Related research questions:** R001, R002, and R003 as qualified in the evidence records

## Context

[ADR-0001](0001-adopt-expertise-development-network-analyst-architecture.md) establishes NADF as an expertise-development architecture centered on the network analyst role. It intentionally does not decide the architecture root, knowledge-representation architecture, relationship among historical architecture views, competency structure, assessment architecture, or implementation model.

Architecture Baseline v0.2 preserves several historical ways of organizing NADF:

- a portfolio or model-category view;
- a concern and traceability view; and
- a conceptual flow view from operational reality toward evidence and detection.

The baseline proposes a portfolio/concern/flow interpretation but does not govern that relationship as accepted architecture. It also records enterprise activity, communication, analyst work, and operational problems as possible organizing constructs without selecting any of them as a universal root.

Selecting a universal root now would force every later competency, knowledge, assessment, learning, tooling, and artifact concern to inherit one organizing assumption. The current evidence supports expertise development, structured and revisable knowledge, reasoning, authentic practice, evidence use, and integrated performance, but it does not establish one project-specific root object as uniquely correct.

The decision therefore concerns architectural posture only: whether NADF requires a universal root or deliberately permits multiple coordinated views. It does not determine the final view set or the internal structure of any view.

## Decision drivers

1. **Consistency with ADR-0001**
   The architecture must keep development of network-analyst expertise primary without treating one supporting artifact or domain model as the framework's identity.

2. **Avoidance of premature coupling**
   A universal root would strongly couple later decisions before competencies, knowledge representations, assessment, and role boundaries are defined.

3. **Fit-for-purpose representation**
   Operational context, analyst development, knowledge, reasoning, assessment, and traceability may require different representations.

4. **Explicit coherence**
   Multiple views must be deliberately coordinated rather than allowed to become unrelated document collections.

5. **Traceability**
   Later work must be able to identify the purpose, authority, scope, and relationships of each governed view.

6. **Reversibility**
   Deferring a universal root is easier to reverse than embedding an unsupported root throughout downstream architecture and implementation.

7. **Evidence discipline**
   The recovered research informs architectural qualities but does not prove a project-specific root or ontology.

8. **Separation of decisions**
   The posture decision should not silently decide the relationship among historical views or the knowledge-representation architecture.

## Options considered

### Option 1 — Deliberate multi-view posture without a universal root

NADF would not require every architectural concern to descend from one universal object. It would permit multiple governed, fit-for-purpose views, each with an explicit purpose, scope, authority, audience, and traceable relationship to other relevant views and accepted decisions.

#### Benefits

- Avoids making enterprise activity, communication, a knowledge model, or another construct authoritative before its boundaries are established.
- Supports different representations for operational, developmental, knowledge, assessment, and traceability concerns.
- Preserves ADR-0001's distinction between NADF's primary identity and its supporting content or artifacts.
- Reduces the cost of revising an individual view when evidence or requirements change.
- Allows later decisions to define coordination rules based on actual needs.

#### Risks

- Multiple views can fragment or contradict one another without clear governance.
- Traceability may require more explicit coordination than a single hierarchy.
- Contributors may confuse “no universal root” with “no architecture.”
- Duplicate concepts may emerge across views.
- Authority and conflict-resolution rules remain to be defined.

### Option 2 — Enterprise activity as the universal root

All major NADF structures would organize around enterprise purposes, activities, or workflows.

This could connect learning to operational mission, but enterprise activity is not sufficiently defined and may subordinate analyst cognition, development, assessment, and cross-context transfer to one organizational representation.

### Option 3 — Analyst work as the universal root

All major structures would organize around the work performed by the network analyst.

This aligns closely with ADR-0001 but risks collapsing knowledge, developmental change, assessment evidence, and operational context into a task structure before the competency and role-boundary decisions exist.

### Option 4 — Operational problems as the universal root

All major structures would organize around the problems network analysts must recognize or resolve.

This supports authentic performance but may make the architecture overly scenario-dependent and does not by itself organize knowledge, progression, assessment, or reusable concepts.

### Option 5 — Continue without an explicit posture

NADF would defer both a universal root and a governed multi-view commitment.

This preserves short-term flexibility but allows incompatible organizing assumptions to accumulate without an explicit coherence requirement.

## Proposed decision

Adopt **Option 1: a deliberate multi-view architecture posture without a universal root**.

NADF will not require all architectural concerns, models, records, or implementation artifacts to descend from one universal root object.

NADF may use multiple fit-for-purpose architectural views when they are needed to represent distinct concerns. A governed view must eventually state, in proportion to its consequence:

- its purpose;
- its scope and boundaries;
- its intended users;
- its authority and lifecycle state;
- the concepts or concerns it represents;
- its relationship to accepted decisions;
- its required traceability to other views; and
- how conflicts or overlaps are identified.

The absence of a universal root does not permit disconnected or contradictory architecture. Coherence must be established through explicit relationships, shared definitions where appropriate, accepted decisions, and traceability rules rather than assumed inheritance from one root.

No historical view becomes accepted architecture merely because this posture permits multiple views.

### Explicit non-decisions

This ADR does **not** decide:

- the final number or names of NADF views;
- whether the historical portfolio, concern, and flow views are accepted, modified, or rejected;
- the role of enterprise activity;
- the role of communication stories;
- the knowledge-representation architecture;
- whether NADF uses an ontology, graph, schema, document model, semantic core, or coordinated models;
- the competency architecture;
- a canonical analytical lifecycle;
- developmental levels;
- assessment architecture;
- TOM or COM roles;
- minimum tooling or telemetry;
- model-driven generation;
- curriculum organization;
- framework implementation; or
- promotion of Architecture Baseline v0.2 into accepted framework architecture.

## Consequences

### Positive consequences

- Later architectural work can select representations appropriate to the concern being governed.
- NADF avoids embedding an unsupported universal root across downstream decisions.
- ADR-0001 remains the governing identity rather than being displaced by a supporting model.
- Historical views can be evaluated individually and relationally in a later focused decision.
- Knowledge-representation choices remain open until their requirements and authority are clearer.
- Revisions can remain localized when a view changes without requiring every concern to be remodeled.

### Negative consequences and risks

- NADF must define explicit coordination and traceability rules as views become governed.
- The architecture may become difficult to navigate if view purposes and boundaries are vague.
- Similar concepts may be represented differently across views.
- Conflict resolution cannot rely on position within one universal hierarchy.
- A later decision may still determine that a shared semantic core or other cross-view mechanism is necessary.

### Required follow-on work

If accepted, subsequent decisions should:

1. determine whether the proposed portfolio/concern/flow relationship among historical views should be accepted, modified, or rejected;
2. define the knowledge-representation architecture and any cross-view semantic authority;
3. establish traceability and conflict-management expectations proportionate to the governed views; and
4. preserve ADR-0001's primary focus on network-analyst expertise.

This follow-on work is not authorized or completed by this ADR.

## Validation plan

While proposed, review ADR-0002 for the following:

- it decides architectural posture without selecting the final view set;
- it does not accept the historical views by implication;
- it does not decide the knowledge-representation architecture;
- it remains consistent with ADR-0001;
- it preserves the R002 and provenance qualifications; and
- it does not authorize curriculum, framework, research, or engineering implementation.

If accepted, future consequential proposals should identify:

- which view or concern they affect;
- how they trace to accepted ADRs;
- whether they introduce overlap or conflict with another governed view; and
- whether they implicitly create a universal root contrary to this decision.

## Revisit triggers

Revisit this decision if:

1. later architecture demonstrates that one root is necessary for coherence, traceability, or implementation;
2. the multi-view posture produces persistent contradiction or unmanageable duplication;
3. an accepted knowledge-representation architecture requires a universal semantic root;
4. assessment or competency architecture cannot be governed coherently across views;
5. a future proposal would make enterprise activity, analyst work, operational problems, or another construct universally authoritative; or
6. a later ADR supersedes or deprecates this decision.

## Scope confirmation

ADR-0002 proposes one decision only:

> NADF should adopt a deliberate multi-view architecture posture without a universal root.

It does not select, accept, or implement the views themselves.
