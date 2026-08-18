# Network Analyst Development Framework

The Network Analyst Development Framework (NADF) is an expertise-development architecture centered on developing network analysts who operate effectively as members of a cyber defense team. The network analyst is its primary development target; adjacent cybersecurity roles are interfaces unless a future architectural decision explicitly expands NADF's primary scope.

The [NADF Active Training Architecture Baseline](NADF-Architecture-Baseline.md) is the single active governing training architecture baseline. The Curriculum Studio implements it, with **C001 – Foundations of Network Analysis** as its current development priority. Existing research, ADRs, and Design Studio artifacts are preserved as historical records and supporting context.

Content, protocols, tools, procedures, labs, assessments, TOMs, COMs, scenarios, PCAPs, datasets, and other reusable assets may support analyst development, but they do not define NADF's primary identity.

## Project status

**Phase:** active curriculum and practical exercise development

See the [project status and roadmap](docs/project/NADF-Project-Status.md) for current workstreams and priorities.

## Repository map

- [GOVERNANCE.md](GOVERNANCE.md): active contributor and decision workflow
- [NADF-Architecture-Baseline.md](NADF-Architecture-Baseline.md): single active governing training architecture baseline
- [docs/project/NADF-Project-Status.md](docs/project/NADF-Project-Status.md): active project status and roadmap

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
5. Optionally capture consequential decisions in ADRs when preserving rationale is useful.
6. Merge framework documentation only after evidence and decision links are reviewable.

See [Research protocol](docs/research/PROTOCOL.md), [Contributing](CONTRIBUTING.md), and [Governance](GOVERNANCE.md).

## Design Studio handoff

Design Studio outputs are preserved as historical context. They do not supersede the active training architecture baseline.

## License

Except where otherwise noted, this project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](LICENSE).

You may share and adapt the material with attribution for noncommercial purposes. If you distribute adapted material, you must license it under the same terms. Commercial use is not granted by this license and requires separate permission from the copyright holder.
