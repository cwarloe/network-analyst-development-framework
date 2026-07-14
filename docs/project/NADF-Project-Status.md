# NADF Project Status

## Document Control

- **Document owner:** NADF Orchestrator / Chief Program Manager
- **Maintained by:** NADF Orchestrator / Chief Program Manager
- **Last updated:** 2026-07-12
- **Repository status:** Current through accepted ADR-0003
- **Review status:** Capability Model v0.1 and Assessment Evidence Model v0.1 proposed for practical use
- **Project phase:** Architecture development and practical validation ([repository README](../../README.md))
- **Next scheduled review:** Unknown — not yet scheduled

## Purpose

This living document coordinates NADF work across specialized studios and repository activities. It tracks operational project state and records workstreams, dependencies, blockers, and next actions.

This document does not approve architecture, replace architectural decision records (ADRs), replace research evidence, redefine curriculum, or promote proposals into accepted project truth. Approved architecture, evidence, ADRs, and curriculum artifacts remain governed by their respective repository locations and lifecycle rules.

## Lifecycle and Status Vocabulary

The repository defines these authoritative lifecycle terms for specific record types:

- ADRs: `proposed`, `accepted`, `superseded`, and `deprecated` ([governance](../../GOVERNANCE.md)).
- Evidence records: `candidate`, `assessed`, `superseded`, and `retracted` ([evidence index](../research/EVIDENCE_INDEX.md)).
- Research confidence: `High`, `Moderate`, `Low`, and `Unknown` ([research protocol](../research/PROTOCOL.md)).

The repository does not currently define a general operational status vocabulary. Until governance establishes one, this document may use the provisional coordination labels `Not Started`, `Active`, `Awaiting Input`, `In Review`, `Blocked`, `Complete`, and `Deferred`. These labels describe coordination state only. In particular, `Complete` does not mean that architecture is approved or accepted.

## Current Project Phase

- **Current phase:** Architecture development and practical validation ([repository README](../../README.md))
- **Phase objective:** Sequence consequential architectural decisions from the governed baseline proposal through accepted ADRs
- **Entry conditions:** ADR-0001, ADR-0002, and ADR-0003 accepted; Architecture Baseline v0.2 preserved as the governed Design Studio proposal
- **Exit conditions:** Unknown — not yet established in a source record
- **Current assessment:** [ADR-0001](../decisions/0001-adopt-expertise-development-network-analyst-architecture.md) is NADF's first accepted architectural decision. Architecture Baseline v0.2 remains the governed Design Studio baseline proposal and is not accepted wholesale as framework architecture.
- **Known dependencies:** The working models remain proposed; completeness, proficiency, assessment validity, reviewer consistency, and role boundaries remain unresolved

## Active Workstreams

| Workstream | Owner | Current objective | Status | Dependencies | Blockers | Next action | Source or tracking reference |
|---|---|---|---|---|---|---|---|
| Program coordination | Integrated NADF Project Director | Turn accepted architecture into useful working models | Active (provisional) | Accepted ADR-0001 through ADR-0003 | None recorded | Apply the capability-to-task-to-evidence chain in practical work | [Assessment Evidence Model v0.1](../design-studio/2026-07-13-nadf-assessment-evidence-model-v0.1-proposed.md) |
| Design Studio | Integrated NADF Design Studio | Develop and test usable capability and evidence models | Active (provisional) | Accepted ADRs and qualified R001–R003 evidence | Completeness and external validation remain unresolved | Formalize further only where use exposes a material need | [Capability Model v0.1](../design-studio/2026-07-12-nadf-network-analyst-capability-model-v0.1-proposed.md) |
| Research | Unknown | Maintain the assessed R001–R003 evidence record and qualifications | Complete (provisional) | Recovered reconciliation provenance | R002 citation and claim-to-source remediation remains deferred | Perform no further research without assignment | [Evidence index](../research/EVIDENCE_INDEX.md) |
| Curriculum Studio | Unknown | No curriculum implementation authorized | Deferred (provisional) | Accepted framework architecture | No framework architecture has been accepted | Await approved architecture | [Orchestrator review](../design-studio/2026-07-11-nadf-architecture-baseline-v0.2-orchestrator-review.md) |
| Repository / Codex | Codex | Maintain the integrated project workspace and source-backed repository state | Active (provisional) | Accepted decisions and approved repository tasks | None recorded | Keep current-state records aligned with accepted decisions | [Current state](../../governance/current-state.md) |
| Validation and quality review | Unknown | Preserve evidence and acceptance qualifications | Awaiting Input (provisional) | Future architectural decisions and validation assignments | No validation assignment recorded | Await explicit assignment | [Architecture Baseline v0.2](../design-studio/2026-07-11-nadf-architecture-baseline-v0.2-proposed.md) |

## Decision and ADR Register

[ADR-0001](../decisions/0001-adopt-expertise-development-network-analyst-architecture.md), [ADR-0002](../decisions/0002-adopt-deliberate-multi-view-architecture-posture.md), and [ADR-0003](../decisions/0003-use-lightweight-portfolio-concern-flow-view-interpretation.md) are accepted architectural decisions and are indexed in the [ADR index](../decisions/README.md).

| Item | Decision question | Status | Owner | Dependencies | ADR reference | Next action | Source |
|---|---|---|---|---|---|---|---|
| ADR-0001 | Adopt NADF as an expertise-development architecture centered on the network analyst role | accepted | NADF Project Director / Maintainer | Architecture Baseline v0.2 and qualified R001–R003 evidence | [ADR-0001](../decisions/0001-adopt-expertise-development-network-analyst-architecture.md) | Use the accepted identity to govern subsequent decisions | [ADR index](../decisions/README.md) |
| ADR-0002 | Adopt a deliberate multi-view posture without a universal root | accepted | Integrated NADF Project Director / Maintainer | ADR-0001 and Architecture Baseline v0.2 | [ADR-0002](../decisions/0002-adopt-deliberate-multi-view-architecture-posture.md) | Use the accepted posture to govern subsequent view decisions | [ADR index](../decisions/README.md) |
| ADR-0003 | Use a lightweight portfolio, concern, and flow interpretation | accepted | Integrated NADF Project Director / Maintainer | ADR-0001, ADR-0002, and Architecture Baseline v0.2 | [ADR-0003](../decisions/0003-use-lightweight-portfolio-concern-flow-view-interpretation.md) | Use the interpretation only when it materially improves clarity | [ADR index](../decisions/README.md) |

## Research Register

The evidence index records R001, R002, R002-RAR, R003, and RR-G2 as assessed ([evidence index](../research/EVIDENCE_INDEX.md)).

| Research ID | Question or report | Status | Evidence location | Synthesis status | Downstream dependency | Next action |
|---|---|---|---|---|---|---|
| R001–R003 and RR-G2 | Recovered research and Gate G2 reconciliation provenance | Assessed | [Provenance recovery](../research/2026-07-11-r001-r003-reconciliation-provenance-recovery.md) | Recovered with conditions | Architecture Baseline v0.2 and future decisions | Preserve qualifications; do not begin remediation without assignment |

## Curriculum Register

| Artifact ID | Artifact type | Title or scope | Status | Architecture dependency | Research dependency | Review status | Next action |
|---|---|---|---|---|---|---|---|
| Placeholder | Unknown | Unknown — no curriculum artifact recorded | Unknown | Unknown | Unknown | Unknown | Add only when an artifact has a source record |

## Repository and Ingestion Register

| Artifact | Intended path | Lifecycle state | Source | Repository status | Required review | Next action |
|---|---|---|---|---|---|---|
| NADF project status | `docs/project/NADF-Project-Status.md` | Merged | Initial project-status request | Merged through pull request #1 | Complete through normal pull request workflow | Maintain as source-backed project coordination changes occur |
| R001–R003 reconciliation provenance recovery | `docs/research/2026-07-11-r001-r003-reconciliation-provenance-recovery.md` | Assessed | Recovered Gate G2 package | Merged through pull request #5 | Complete through normal pull request workflow | Preserve recorded conditions |
| Evidence index update | `docs/research/EVIDENCE_INDEX.md` | Assessed | R001–R003 provenance recovery | Merged through pull request #5 | Complete through normal pull request workflow | Maintain evidence lifecycle records |
| Architecture Baseline v0.2 Orchestrator review | `docs/design-studio/2026-07-11-nadf-architecture-baseline-v0.2-orchestrator-review.md` | Accepted with conditions as a governed proposal | NADF Project Orchestrator disposition | Merged through pull request #6 | Complete through normal pull request workflow | Use as the governing source for next-decision preparation |
| Architecture Baseline v0.2 proposed | `docs/design-studio/2026-07-11-nadf-architecture-baseline-v0.2-proposed.md` | Accepted with conditions as a governed proposal | NADF Design Studio synthesis and Orchestrator disposition | Merged through pull request #6 | Complete through normal pull request workflow | Do not treat as accepted framework architecture |
| ADR-0001 | `docs/decisions/0001-adopt-expertise-development-network-analyst-architecture.md` | accepted | Maintainer-accepted architectural decision | Recorded through the ADR-0001 acceptance change | Complete through normal pull request workflow | Govern subsequent architecture decisions without broadening explicit non-decisions |
| ADR-0002 | `docs/decisions/0002-adopt-deliberate-multi-view-architecture-posture.md` | accepted | Maintainer-accepted architectural decision | Recorded through the ADR-0002 acceptance change | Complete through normal pull request workflow | Govern subsequent view decisions without resolving explicit non-decisions |
| ADR-0003 | `docs/decisions/0003-use-lightweight-portfolio-concern-flow-view-interpretation.md` | accepted | Maintainer-accepted architectural decision | Recorded through the ADR-0003 acceptance change | Complete through normal pull request workflow | Apply as lightweight navigation without adding process |
| Capability Model v0.1 | `docs/design-studio/2026-07-12-nadf-network-analyst-capability-model-v0.1-proposed.md` | proposed working model | Accepted ADRs and existing R001–R003 evidence | Proposed through the capability-model change | Practical evaluation | Do not treat as a validated taxonomy or assessment standard |
| Assessment Evidence Model v0.1 | `docs/design-studio/2026-07-13-nadf-assessment-evidence-model-v0.1-proposed.md` | proposed working model | Capability Model v0.1 and two validation slices | Proposed through the assessment-evidence change | Practical evaluation | Do not treat as a scoring rubric or validated assessment system |

## Risks and Blockers

| ID | Risk or blocker | Category | Severity | Owner | Mitigation or required action | Downstream impact |
|---|---|---|---|---|---|---|
| R-001 | R002-dependent conclusions remain qualified because citation alignment, source quality, and claim-to-source traceability require future remediation | Evidence | Unknown | Unknown | Preserve qualifications; remediate only with explicit Orchestrator authorization | Limits doctrinal and high-consequence architectural claims |
| R-002 | Architecture Baseline v0.2 is not accepted wholesale as framework architecture, and ADR-0001 does not authorize implementation | Governance | Unknown | NADF Project Director / Maintainer | Continue governing consequential choices through focused ADRs | Blocks framework and curriculum implementation |

## Cross-Studio Handoffs

| From | To | Deliverable | Purpose | Status | Acceptance criteria | Tracking reference |
|---|---|---|---|---|---|---|
| Research / recovered Gate G2 package | Design Studio | R001–R003 reconciliation provenance recovery | Constrain and inform Architecture Baseline v0.2 | Complete (provisional) | Qualifications preserved in the baseline | [Provenance recovery](../research/2026-07-11-r001-r003-reconciliation-provenance-recovery.md) |
| Design Studio | NADF Orchestrator | Architecture Baseline v0.2 proposal | Obtain a governed disposition | Complete (provisional) | Accepted with conditions only as the governed baseline proposal | [Orchestrator review](../design-studio/2026-07-11-nadf-architecture-baseline-v0.2-orchestrator-review.md) |

## Near-Term Priorities

### Highest-priority action

Apply the capability-to-task-to-evidence chain in the next real design task before adding formal structure.

### Next three actions

1. Use both working models in a real design task.
2. Revise only where use exposes a material problem.
3. Add scoring, levels, schemas, or validation work only for a demonstrated consumer.

### Waiting on

No maintainer input is currently required.

### Recently completed

- R001–R003 reconciliation provenance recovery merged through pull request #5.
- Architecture Baseline v0.2 disposition merged through pull request #6.
- Architecture Baseline v0.2 accepted with conditions as the current governed Design Studio baseline proposal.
- ADR-0001 accepted as NADF's first architectural decision.
- ADR-0002 accepted as NADF's deliberate multi-view architecture posture.
- ADR-0003 accepted as NADF's lightweight portfolio, concern, and flow interpretation.

### Deferred work

- Curriculum implementation.
- Framework implementation or promotion.
- Additional research and R002 remediation.
- TOM/COM architecture.
- Engineering implementation and model-driven generation.

These remain unauthorized by ADR-0001 and require separate direction or decisions.

## Update Protocol

The Orchestrator should update this file when:

- a workstream begins, changes state, becomes blocked, or completes;
- a handoff is issued or accepted;
- a research dependency changes;
- an ADR is proposed or accepted;
- a curriculum artifact enters or leaves review;
- repository ingestion changes an artifact's lifecycle state; or
- a significant risk, blocker, or dependency appears.

Updates must preserve links to the relevant repository evidence, issue, pull request, ADR, report, or handoff. Planned links must remain explicitly marked as unresolved or planned until the referenced record exists.

## Governance Guardrails

- Proposals are not decisions.
- Decisions require the repository's established governance process.
- Research claims require traceable evidence.
- Curriculum implements approved direction and does not establish architecture.
- Operational status does not imply architectural acceptance.
- The project-status file summarizes and coordinates; it does not supersede source records.
- Unknown information must remain explicitly unknown rather than inferred.

## Provenance

- **Initial creation date:** 2026-07-10
- **Initial author or agent:** Codex, acting on the source request
- **Source request:** User-provided request to create the initial NADF project-status artifact
- **Related issue or pull request:** Pull request #1

### Revision History

| Date | Author or agent | Change | Reference |
|---|---|---|---|
| 2026-07-10 | Codex | Created initial coordination artifact | Unresolved — pull request planned |
| 2026-07-12 | Codex | Reconciled project status with merged research provenance and Architecture Baseline v0.2 disposition records | Pull requests #5 and #6 |
| 2026-07-12 | Codex | Recorded accepted ADR-0001 and moved the project into architecture decision development | ADR-0001 acceptance change |
| 2026-07-12 | Codex | Prepared proposed ADR-0002 for a deliberate multi-view posture | ADR-0002 preparation change |
| 2026-07-12 | Codex | Recorded accepted ADR-0002 and returned the project to decision sequencing | ADR-0002 acceptance change |
| 2026-07-12 | Codex | Prepared proposed ADR-0003 for a lightweight portfolio, concern, and flow interpretation | ADR-0003 preparation change |
| 2026-07-12 | Codex | Recorded accepted ADR-0003 and returned the project to decision sequencing | ADR-0003 acceptance change |
| 2026-07-12 | Codex | Proposed Network Analyst Capability Model v0.1 and moved active work into practical model evaluation | Capability Model v0.1 change |
| 2026-07-13 | Codex | Proposed Assessment Evidence Model v0.1 from two capability-validation slices | Assessment Evidence Model v0.1 change |
