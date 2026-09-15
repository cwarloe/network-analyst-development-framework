# NADF Governance & Contributor Guide

## Purpose

The Network Analyst Development Framework (NADF) is an operational training architecture designed to build analyst reasoning, structured mental models, and practical troubleshooting capabilities. Governance exists to keep training content technically accurate, instructionally effective, and simple to maintain.

## Roles

- **Maintainer:** Oversees repository health, merges pull requests, and maintains active baseline alignment.
- **Contributor:** Authors or updates modules, packet walkthroughs, lab exercises, scenarios, and framework documentation.
- **Peer Reviewer:** Evaluates contributions for technical accuracy and training value.

## 3-Step Decision & Update Workflow

All changes to framework documentation, training modules, or lab exercises follow a simple, lightweight 3-step workflow:

`[1. Draft & Propose]` → `[2. Practical Peer Review]` → `[3. Merge & Adopt]`

1. **Draft & Propose:** Any contributor creates a standard Pull Request (PR) proposing new training modules, exercise setups, or framework updates. No prior formal pre-authorization or Architecture Decision Record (ADR) is required to begin drafting.
2. **Practical Peer Review:** A peer reviewer evaluates the PR against two practical criteria:
   - **Technical Accuracy:** Are the packet captures, telemetry details, and protocol behaviors correct?
   - **Training Value:** Does the contribution build analyst mental models, troubleshooting capabilities, and evidence-based reasoning?
3. **Merge & Adopt:** The maintainer merges the PR. Merging directly updates the active training baseline, unblocking immediate use in curriculum, lab creation, and student delivery.

## Core Guidelines

- **Focus on Actionable Value:** Avoid over-engineered administrative processes, unnecessary approval gates, or complex citation tracking.
- **Technical Integrity:** Do not commit credentials, sensitive information, or broken exercise configurations.
- **Iterative Improvement:** Refine curriculum materials through real-world instruction and student feedback.

## Related

Shorter day-to-day contribution notes also live in [CONTRIBUTING.md](CONTRIBUTING.md).
