# Instructions for AI assistants working in this repository

## What this project is

Training material for network analysts. The deliverable is **lessons someone can actually sit down and do** — everything else exists only to serve that.

Read [README.md](README.md), [COURSE.md](COURSE.md), and [ROADMAP.md](ROADMAP.md) before starting. That is the whole context.

## The rule that matters most

**This project has been damaged by over-process.** It once had a governance guide, three named roles, an ADR workflow, decision registers, design-studio handoffs, and a peer-review gate — for a repository maintained by one person. It accumulated 5,000 lines of documentation around 275 lines of training material.

So: **do not add process.** No new governance documents, no decision records, no status registers, no templates, no conformance checks, no directories for things that do not exist yet. If you think a new process document is needed, you are almost certainly wrong.

When in doubt, write a lesson instead.

## What to preserve

- **The Standing Qualifications** in [docs/architecture.md](docs/architecture.md). Simplifying process does not license stronger claims. Specifically: no proficiency levels, scoring, mastery thresholds, or assessment-validity claims, anywhere.
- **The research** in [docs/research/](docs/research/). It is the evidence base and it is genuinely load-bearing.
- **The archive** in [docs/archive/](docs/archive/). Superseded, but it is the record of how the design was reached. Don't revive it, don't delete it.

## Before recording anything as unreachable

HTTP egress is restricted, and `curl` returning `000` does not mean a resource is unobtainable. **The session's git proxy serves anonymous clones of public repositories, including non-GitHub hosts.** Try `git ls-remote <url>` and a blobless clone (`git clone --depth 1 --filter=blob:none`, which lists a tree without downloading contents) before concluding anything.

This is not hypothetical. The NICE Framework was recorded as needing a manual download; it did not — [R007](docs/research/R007-nice-role-mapping.md) got the full current framework through a public clone after every HTTP path failed.

## Working practice

- Branch, commit, open a pull request. Merge it yourself when it's routine — do not leave finished work sitting on a branch waiting for a review that isn't coming.
- Don't commit to `main` directly.
- One coherent commit where practical.
- Check relative links before pushing.
- Ask the maintainer only about genuine forks in the road: scope, audience, or anything hard to reverse. Not about mechanics.

## Reporting

Say what changed, what state the project is in, and what the next useful thing is. Nothing else.
