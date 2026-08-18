# NADF Project Status & Roadmap

## Purpose

This document provides a single, consolidated view of active workstreams, priorities, and roadmap items for the Network Analyst Development Framework (NADF).

## Project Overview

NADF is in active development, focused on building high-impact, practical training modules, telemetry exercises, and scenario-based assessments for network analysts. The [NADF Active Training Architecture Baseline](../../NADF-Architecture-Baseline.md) is the single active governing training architecture baseline.

The [research record](../research/) remains NADF's standing evidence base. [ADRs](../decisions/) and [Design Studio artifacts](../design-studio/) are preserved as historical records of how the baseline was reached.

## Active Workstreams

| Workstream | Focus & objectives | Active task / next action |
|---|---|---|
| Core Framework & Governance | Maintain streamlined baseline and contributor workflows | Maintain the simplified 3-step PR workflow and avoid redundant registers and approval gates. |
| Curriculum Studio | Author hands-on training modules, packet walkthroughs, and scenario labs | Develop **C001 – Foundations of Network Analysis** as the current priority. |
| Practical Validation | Find out whether the working models describe real analyst work before scaling them | Run [PILOT-001](../../curriculum/pilots/encrypted-outbound-traffic/README.md) with at least one learner other than its author and record the result in [run records](../../curriculum/pilots/encrypted-outbound-traffic/run-records.md). |
| Lab & Telemetry Engineering | Create PCAP datasets, exercise environments, and telemetry configurations | Build authentic scenario PCAPs and lab environments using tools such as Security Onion, Wireshark, and Elastic. |
| Repository Maintenance | Maintain source-backed documentation and exercise artifacts | Keep repository documentation clean, aligned, and ready for immediate instructional use. |

## Near-Term Priorities

1. **Run PILOT-001 once, with someone other than its author.** This is a few hours of work and is the only check available on whether the capability and evidence models hold up against real use. C001 will scale whatever the pilot gets right or wrong, so it is worth knowing which before authoring at volume.
2. **C001 – Foundations of Network Analysis:** Develop the Curriculum Studio's current priority under the active training architecture baseline. Do not block authoring on the pilot; let the pilot's findings correct it.
3. **Settle PCAP and telemetry sourcing.** Authentic capture data and redistributable capture data are frequently not the same data. Determine which public corpora NADF may lawfully ship inside exercises and what must instead be generated in a lab. This shapes exercise design, so it wants answering before authoring at volume rather than after.
4. **Feedback Integration:** Incorporate instructor and student feedback from operational training deliveries to continuously improve materials.

## Recent Accomplishments

- Streamlined governance from a multi-studio enterprise-engineering process into a lightweight 3-step PR workflow.
- Consolidated multi-file registers into a single active project status roadmap.
- Established [NADF-Architecture-Baseline.md](../../NADF-Architecture-Baseline.md) as the single active governing training architecture baseline.
- Preserved existing research as the standing evidence base, and ADR and Design Studio artifacts as historical records.
- Retained the capability and assessment evidence models as active implementing models under the baseline.
