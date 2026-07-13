# NADF Current State

## Current operational phase

**Architecture decision development.**

[ADR-0001](../docs/decisions/0001-adopt-expertise-development-network-analyst-architecture.md) establishes NADF's primary architectural identity and development target. [ADR-0002](../docs/decisions/0002-adopt-deliberate-multi-view-architecture-posture.md) now proposes a deliberate multi-view posture without a universal root; it is not yet accepted.

## Architecture state

- **First accepted architectural decision:** ADR-0001.
- **Primary identity:** NADF is an expertise-development architecture centered on the network analyst role.
- **Primary development target:** The network analyst.
- **Adjacent roles:** Interfaces unless a future decision explicitly expands NADF's primary scope.
- **Supporting elements:** Content, protocols, tools, procedures, labs, assessments, TOMs, COMs, scenarios, and reusable assets may support analyst development but do not define NADF's primary identity.
- **Governed Design Studio proposal:** [Architecture Baseline v0.2](../docs/design-studio/2026-07-11-nadf-architecture-baseline-v0.2-proposed.md) remains accepted with conditions as the governed Design Studio baseline proposal; it is not accepted wholesale as framework architecture.
- **Historical baseline:** [Architecture Baseline transfer dated 2026-07-10](../docs/design-studio/2026-07-10-nadf-architecture-baseline.md).

## Active work

- Sequence the next consequential architectural decision from Architecture Baseline v0.2.
- Maintain traceability from accepted decisions to the qualified R001–R003 evidence record.
- Review proposed ADR-0002 without treating its posture or any historical view as accepted architecture.

R001–R003 provenance recovery is complete. Its evidence and provenance qualifications remain binding.

## Next priority

Review and disposition proposed ADR-0002 while preserving its explicit non-decisions and all evidence qualifications.

## Paused or unauthorized work

ADR-0001 does not authorize:

- curriculum implementation;
- framework implementation or promotion;
- additional research or R002 evidence remediation;
- TOM/COM architecture;
- engineering implementation;
- model-driven generation work; or
- architecture synthesis or ADR drafting beyond an assigned decision.

## Binding constraints

- Research evidence, interpretation, architectural proposal, and accepted decision remain distinct.
- R002-dependent high-consequence claims remain qualified.
- Architecture Baseline v0.2 remains a governed proposal, not accepted framework architecture.
- ADR-0001 decides identity and primary target only; all explicit non-decisions in the ADR remain unresolved.
- ADR-0002 remains proposed and does not govern NADF unless accepted.
- Consequential architectural decisions require an ADR under [Governance](../GOVERNANCE.md).
- Curriculum implements accepted architecture and does not redefine it.

## Authoritative references

- [ADR-0001](../docs/decisions/0001-adopt-expertise-development-network-analyst-architecture.md)
- [ADR-0002](../docs/decisions/0002-adopt-deliberate-multi-view-architecture-posture.md)
- [ADR index](../docs/decisions/README.md)
- [Repository overview](../README.md)
- [Governance](../GOVERNANCE.md)
- [NADF Project Status](../docs/project/NADF-Project-Status.md)
- [Architecture Baseline v0.2](../docs/design-studio/2026-07-11-nadf-architecture-baseline-v0.2-proposed.md)
- [Architecture Baseline v0.2 Orchestrator Review](../docs/design-studio/2026-07-11-nadf-architecture-baseline-v0.2-orchestrator-review.md)
- [Evidence Index](../docs/research/EVIDENCE_INDEX.md)
