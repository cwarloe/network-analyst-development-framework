# Governance

## Roles

- **Maintainer:** administers the repository, review process, releases, and accepted records.
- **Contributor:** proposes research, evidence, decisions, or documentation through issues and pull requests.
- **Reviewer:** evaluates traceability, source quality, internal consistency, and scope.
- **Design Studio:** develops architectural vision outside this repository; it is an input source and has no automatic decision authority here.

One person may hold multiple roles during the initial phase.

## Decision process

Consequential or difficult-to-reverse decisions require an ADR. ADRs begin as `proposed`, become `accepted` through maintainer-approved review, and may later be `superseded` or `deprecated`. Accepted records are not rewritten to conceal changed reasoning; a new ADR supersedes them.

Routine editorial changes may be merged without an ADR. Evidence quality disputes should be documented in the evidence record or synthesis rather than resolved by deleting contrary material.

## Repository integrity

- Protected information and credentials must not be committed.
- Retractions, broken links, and material source corrections must be recorded.
- Framework releases should identify the evidence and ADR baseline they contain.
- Governance changes use the normal pull request process and require explicit maintainer approval.
