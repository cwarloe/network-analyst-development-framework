# Contributing

## Before opening a change

- Check the change against the [training architecture baseline](NADF-Architecture-Baseline.md). No prior authorization or ADR is required to begin drafting.
- Search existing issues and evidence entries.
- Open a research question for claims that require investigation.
- By submitting a contribution, you agree that it may be distributed under the repository's CC BY-NC-SA 4.0 license.

## Evidence requirements

Material claims must cite a stable source. Prefer standards, peer-reviewed research, official documentation, primary data, and reproducible experiments. Label practitioner experience and inference explicitly.

Every evidence entry must include provenance, access date, relevance, limitations, and a quality assessment. Do not present a proposal as an established fact.

## Pull requests

- Keep changes focused on one module, exercise, research question, or documentation concern.
- Link related issues and evidence IDs.
- Describe contrary evidence and unresolved uncertainty.
- Update indexes when adding evidence, decisions, or framework documents.
- Do not include secrets, private conversation transcripts, or restricted source material.

## Document conventions

- Use Markdown and relative links.
- Use ISO 8601 dates (`YYYY-MM-DD`).
- Give evidence records IDs such as `E-0001` and ADRs IDs such as `ADR-0001`.
- Use status values defined in the relevant template.
- Mark normative language deliberately: `MUST`, `SHOULD`, and `MAY` follow RFC 2119 meanings only when explicitly stated.

## Review standard

Review a contribution for two things: **technical accuracy** — are the captures, telemetry details, and protocol behaviors correct? — and **training value** — does it build analyst mental models, troubleshooting capability, and evidence-based reasoning?

Beyond that, a reviewer should be able to trace a material framework claim to evidence and see how its limitations were considered.
