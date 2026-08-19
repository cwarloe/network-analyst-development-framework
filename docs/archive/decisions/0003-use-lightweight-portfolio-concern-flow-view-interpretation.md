# ADR-0003: Use a lightweight portfolio, concern, and flow view interpretation

- **Status:** accepted
- **Accepted:** 2026-07-12
- **Date:** 2026-07-12
- **Owners:** Integrated NADF Project Director / Design Studio (proposal); NADF Maintainer (disposition)
- **Related decisions:**
  - [ADR-0001: Adopt NADF as an expertise-development architecture centered on the network analyst role](0001-adopt-expertise-development-network-analyst-architecture.md)
  - [ADR-0002: Adopt a deliberate multi-view architecture posture without a universal root](0002-adopt-deliberate-multi-view-architecture-posture.md)
- **Related proposal:**
  - [NADF Architecture Baseline v0.2 — Proposed](../design-studio/2026-07-11-nadf-architecture-baseline-v0.2-proposed.md)

## Context

ADR-0002 establishes that NADF uses multiple governed, fit-for-purpose views and does not require a universal root. It deliberately leaves the actual view set and the relationship among inherited architecture formulations unresolved.

Architecture Baseline v0.2 preserves three historical formulations:

- a model-category formulation describing architectural components and artifact categories;
- a conceptual-layer formulation describing concerns and traceability; and
- a reality-to-detection formulation describing a conceptual flow from operational reality toward evidence and detection.

Treating these as competing hierarchies would recreate the single-root problem ADR-0002 rejected. Turning them into a formal metamodel would also add governance and maintenance cost before the project has defined its knowledge, competency, assessment, or implementation architecture.

The immediate need is smaller: provide a stable, understandable way to navigate the inherited formulations without making them mandatory structures or creating new process.

## Decision drivers

- Preserve the deliberate multi-view posture established by ADR-0002.
- Make the inherited formulations understandable without forcing them into one hierarchy.
- Avoid mandatory artifacts, schemas, classifications, handoffs, or approval stages.
- Keep the interpretation easy to revise or supersede.
- Prevent the flow view from becoming a canonical analytical lifecycle by implication.
- Prevent the portfolio view from becoming a required artifact checklist.
- Prevent the concern view from becoming an ontology or universal traceability schema.
- Maintain enough clarity to identify contradictions or missing relationships when they materially affect a decision.

## Options considered

### Option 1 — Lightweight complementary view interpretation

Use portfolio, concern, and flow as descriptive labels for three complementary ways of reading NADF architecture. Apply them only when they improve understanding or decision traceability.

This option adds shared language without requiring a formal model or new workflow.

### Option 2 — Formal view metamodel

Define required view types, schemas, mappings, authority rules, and conformance checks.

This could provide precision later, but it is premature and would create substantial formal overhead without established requirements.

### Option 3 — Select one inherited formulation as authoritative

Make one formulation primary and subordinate the others.

This would simplify navigation but conflict with ADR-0002 and prematurely privilege one concern.

### Option 4 — Leave the relationship entirely unresolved

Preserve all three formulations without shared interpretation.

This avoids immediate work but allows recurring confusion about whether the formulations compete, overlap, or supersede one another.

## Proposed decision

Adopt **Option 1: a lightweight complementary view interpretation**.

Use the following navigational meanings:

- **Portfolio view:** helps identify what kinds of architectural capabilities, models, records, or supporting artifacts are present or under consideration.
- **Concern view:** helps identify which architectural concerns are addressed and where material relationships or traceability may be needed.
- **Flow view:** helps explain a conceptual progression through operational context, problems, communications, systems, behaviors, evidence, analysis, and detection.

These views are complementary lenses, not competing hierarchies.

### Minimal operating rules

- Use a view label only when it materially improves clarity.
- An artifact may support more than one view or no named view.
- Do not require every artifact to be classified.
- Do not create a document solely to satisfy a view label.
- Do not introduce a separate review, approval, handoff, or conformance stage for view usage.
- Do not infer authority from a view label; lifecycle status and accepted ADRs establish authority.
- Resolve consequential conflicts through the normal ADR process; handle routine wording and mapping improvements as reversible documentation changes.
- Allow the labels and mappings to evolve when a later decision provides a clearer model.

### Explicit non-decisions

This ADR does **not**:

- define a formal metamodel, ontology, schema, or taxonomy;
- make any view a universal root or source of truth;
- require three views in every artifact or implementation;
- accept every item historically listed within a formulation;
- define required mappings among artifacts;
- define a canonical analytical lifecycle or sequence;
- define the knowledge-representation architecture;
- define competencies, progression, assessment, TOM/COM roles, tooling, or curriculum;
- authorize framework or engineering implementation; or
- promote Architecture Baseline v0.2 wholesale into accepted framework architecture.

## Consequences

### Positive consequences

- The inherited formulations gain a coherent relationship with minimal process cost.
- Contributors can discuss architecture from different useful perspectives without inventing a universal hierarchy.
- The interpretation is easy to revise because it does not impose schemas or implementation contracts.
- ADR-0002 becomes operationally understandable without creating governance machinery.
- Future decisions can introduce stronger mappings only when actual risk or dependency justifies them.

### Negative consequences and risks

- Lightweight labels may be applied inconsistently.
- Overlap among views may remain ambiguous in some cases.
- The interpretation provides navigation, not formal consistency guarantees.
- Additional traceability rules may still be needed for high-consequence models later.

These risks are acceptable because routine inconsistencies are reversible and consequential conflicts remain governed by ADRs.

## Validation plan

While proposed, verify that ADR-0003:

- describes the inherited formulations without turning them into mandatory architecture;
- adds no required artifact, schema, handoff, or approval stage;
- remains consistent with ADR-0001 and ADR-0002;
- preserves the explicit non-decisions in Architecture Baseline v0.2; and
- does not authorize implementation.

If accepted, validate the interpretation through ordinary use. Revisit it only when it causes material ambiguity, contradiction, or unnecessary work.

## Revisit triggers

Revisit this decision if:

- recurring ambiguity prevents consequential decisions;
- a governed knowledge or traceability architecture requires stronger view definitions;
- one or more labels no longer help users navigate the architecture;
- a later decision establishes a different view set; or
- a later ADR supersedes or deprecates this interpretation.

## Scope confirmation

ADR-0003 proposes one lightweight decision:

> Interpret the inherited formulations as complementary portfolio, concern, and flow views, without making them mandatory structures or adding process stages.
