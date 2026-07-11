# Network Analyst Development Framework

An evidence-based research and documentation project for developing the Network Analyst Development Framework (NADF).

The architectural vision is developed separately in the Design Studio. This repository is the system of record for reviewed evidence, traceable claims, architectural decision records, and approved documentation. It does not treat unreviewed design discussion as settled architecture.

## Project status

**Phase:** research and repository initialization

No framework architecture has been approved yet. Proposed architecture should enter through an issue or pull request and cite supporting evidence.

## Repository map

- `docs/research/`: research questions, evidence, and syntheses
- `docs/decisions/`: accepted and proposed architectural decision records (ADRs)
- `docs/framework/`: approved framework documentation
- `docs/design-studio/`: dated transfers from the separate Design Studio
- `templates/`: reusable research and decision templates
- `.github/`: contribution and review workflows

## Working method

1. Define a research question before collecting sources.
2. Record each source in the evidence register with provenance and quality notes.
3. Separate sourced facts, interpretations, and proposals.
4. Synthesize evidence against a specific question.
5. Capture consequential decisions in ADRs.
6. Merge framework documentation only after evidence and decision links are reviewable.

See [Research protocol](docs/research/PROTOCOL.md), [Contributing](CONTRIBUTING.md), and [Governance](GOVERNANCE.md).

## Design Studio handoff

Design Studio outputs are inputs, not repository truth. Each handoff should be dated, identify its source conversation, list unresolved questions, and distinguish proposals from decisions. Use `templates/design-studio-handoff.md`.

## License

No license has been selected. Until one is added, copyright remains with the repository owner and reuse rights are not granted.
