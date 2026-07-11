# Network Analyst Development Framework

The Network Analyst Development Framework (NADF) develops Network Analysts who operate effectively as members of a cyber defense team.

The Design Studio owns the architecture. Research reports provide the evidence base, and the Curriculum Studio implements the approved architecture. This repository is the system of record for reviewed evidence, traceable claims, architectural decision records, and approved documentation. It does not treat unreviewed design discussion as settled architecture.

TOMs, COMs, PCAPs, scenarios, and datasets are reusable assets. They are not required components of every module.

## Project status

**Phase:** research and repository initialization

No framework architecture has been approved yet. Proposed architecture should enter through an issue or pull request and cite supporting evidence.

## Repository map

- `docs/research/`: research questions, evidence, and syntheses
- `docs/decisions/`: accepted and proposed architectural decision records (ADRs)
- `docs/framework/`: approved framework documentation
- `docs/design-studio/`: dated transfers from the separate Design Studio
- `curriculum/`: Curriculum Studio implementation artifacts
- `assets/`: reusable scenarios, TOMs, COMs, PCAPs, telemetry, detections, and job aids
- `governance/`: decisions, change logs, and quality reviews
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

Except where otherwise noted, this project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](LICENSE).

You may share and adapt the material with attribution for noncommercial purposes. If you distribute adapted material, you must license it under the same terms. Commercial use is not granted by this license and requires separate permission from the copyright holder.
