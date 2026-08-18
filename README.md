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

Contributions follow three steps: **draft and propose** a pull request, **practical peer review** for technical accuracy and training value, then **merge and adopt**. No prior authorization or ADR is required to begin drafting. See [Governance](GOVERNANCE.md) and [Contributing](CONTRIBUTING.md).

Research is a supporting process rather than the repository's main activity. When a contribution rests on a claim that needs investigation, frame the question first, record sources with provenance and quality notes, keep facts separate from interpretation, and synthesize against the question. See the [research protocol](docs/research/PROTOCOL.md).

## License

Except where otherwise noted, this project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](LICENSE).

You may share and adapt the material with attribution for noncommercial purposes. If you distribute adapted material, you must license it under the same terms. Commercial use is not granted by this license and requires separate permission from the copyright holder.
