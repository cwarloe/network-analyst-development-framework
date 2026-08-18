# NADF Governance & Contributor Guide

## Purpose

The Network Analyst Development Framework (NADF) is an operational training architecture designed to build analyst reasoning, structured mental models, and practical troubleshooting capabilities. Governance exists to keep training content technically accurate, instructionally effective, and simple to maintain.

The active governing documents are:

- [NADF Active Training Architecture Baseline](NADF-Architecture-Baseline.md)
- [NADF Project Status & Roadmap](docs/project/NADF-Project-Status.md)
- This governance guide

Existing research, architectural decision records (ADRs), and dated Design Studio artifacts are retained as historical records and supporting context. They do not supersede the active training architecture baseline.

## Roles

- **Maintainer:** Oversees repository health, merges pull requests, and maintains active baseline alignment.
- **Contributor:** Authors or updates modules, packet walkthroughs, lab exercises, scenarios, and framework documentation.
- **Peer Reviewer:** Evaluates contributions for technical accuracy and training value.

## 3-Step Decision & Update Workflow

All changes to framework documentation, training modules, or lab exercises follow a simple, lightweight workflow:

**Draft & Propose** → **Practical Peer Review** → **Merge & Adopt**

1. **Draft & Propose:** Any contributor creates a standard pull request proposing new training modules, exercise setups, or framework updates. No prior formal pre-authorization or ADR is required to begin drafting.
2. **Practical Peer Review:** A peer reviewer evaluates the pull request for:
   - **Technical Accuracy:** Are the packet captures, telemetry details, and protocol behaviors correct?
   - **Training Value:** Does the contribution build analyst mental models, troubleshooting capabilities, and evidence-based reasoning?
3. **Merge & Adopt:** The maintainer merges the pull request. Merging updates the active training baseline or its implementing materials, as applicable, unblocking use in curriculum, lab creation, and student delivery.

ADRs are optional for consequential decisions where preserving the rationale, alternatives, and consequences is useful. Existing ADRs remain historical records.

## Core Guidelines

- **Focus on Actionable Value:** Avoid over-engineered administrative processes, unnecessary approval gates, or complex citation tracking.
- **Technical Integrity:** Do not commit credentials, sensitive information, or broken exercise configurations.
- **Iterative Improvement:** Refine curriculum materials through real-world instruction and student feedback.
