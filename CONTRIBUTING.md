# Contributing

This is a one-person project. Follow the [working practice in AGENTS.md](AGENTS.md#working-practice): keep the work moving without an issue, assigned reviewer, or approval ceremony for every small change.

- For **small, reversible, preauthorized internal engineering or mechanical corrections**, run the applicable checks and land the change on `main`. No pull request is required solely to create a review ceremony.
- For **substantial changes where the diff is useful to inspect**, open a pull request and merge after CI succeeds. Do not wait for another person's approval unless the maintainer requested it or the change is hard to reverse.
- **Stop for a real decision**, including new lesson or story canon, change of scope or audience, sensitive material, public-facing editorial decisions, or licensing/security implications. A green test cannot make those decisions.

In every case, preserve the technical and instructional standards below.

## What gets reviewed

Two questions:

1. **Is it technically correct?** Protocol behavior, capture details, telemetry specifics.
2. **Does it build the reasoning?** A lesson should make someone think better, not memorize more.

## A few things that matter

- **Don't claim more than the evidence supports.** If a lesson asserts something about how analysts actually work, it should be traceable to the [research](docs/research/) or labeled as design judgment. See the Standing Qualifications in [docs/architecture.md](docs/architecture.md).
- **No scores, levels, or mastery thresholds.** Nothing here is validated enough to grade anyone, and adding a number implies otherwise.
- **Lessons end in a work product**, not a quiz.
- **No secrets, private transcripts, or capture data you don't have the right to redistribute.** The last one is a live question — see the [roadmap](ROADMAP.md).
- Markdown, relative links, ISO dates.

By contributing you agree your work may be distributed under the repository's CC BY-NC-SA 4.0 license.
