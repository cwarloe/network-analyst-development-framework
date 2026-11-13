# Instructions for AI assistants working in this repository

## What this project is

Training material for network analysts. The deliverable is **lessons someone can actually sit down and do** — everything else exists only to serve that.

Read [README.md](README.md), [COURSE.md](COURSE.md), and [ROADMAP.md](ROADMAP.md) before starting. That is the whole context.

## The rule that matters most

**This project has been damaged by over-process.** It once had a governance guide, three named roles, an ADR workflow, decision registers, design-studio handoffs, and a peer-review gate — for a repository maintained by one person. It accumulated 5,000 lines of documentation around 275 lines of training material.

So: **do not add process.** No new governance documents, no decision records, no status registers, no templates, no conformance checks, no directories for things that do not exist yet. If you think a new process document is needed, you are almost certainly wrong.

When in doubt, write a lesson instead.


## Craft rules (shared with Portland Desk)

NADF adopts Portland Desk's cost and canon rules 1-14. Numbering matches the Portland [Learning Narrative Framework](https://github.com/cwarloe/learning-narrative-kit/blob/main/docs/craft/learning-narrative-framework.md). Link that document; do not copy it into this repo. Short forms also live in [narrative/README.md](narrative/README.md). If a rule changes in the framework, the number here still refers to that rule.

1. No promotion, raise, or forgiveness offsets any cost charged to Ethan in the same or the previous chapter. A relationship that moves through an action, with nothing said, is not a refund; a speech, promotion, or restored status is.
2. Each act has one incident that belongs to someone else (Ethan hears about it secondhand) and one thing Ethan saves that does not matter.
3. No narrator foreshadowing.
4. A carry-forward must change action. A grudge may not be restated in more than two chapters without moving.
5. Every chapter charges Ethan a personal cost that nobody refunds.
6. Ethan's standing struggles, named in the Portland bible, drive his wrong turns.
7. No recurring character enters or exits with the same action, phrase, or device twice in an act. Each return opens on what changed since the last appearance.
8. Run `python3 tools/check_dates.py` before merge. Every `date-ok` marker gives a reason (`<!-- date-ok: why -->`). Anchors are in [narrative/author-bible/timeline.md](narrative/author-bible/timeline.md).
9. A cost counts only if it is in the narrative file.
10. Use a surname only on introduction or when it matters (formal report, email signature, a stern manager); otherwise first names.
11. No two characters in the same act enter with the same staging device (an object carried "like" something, a burst into the aisle, a phone ringing as the scene opens).
12. When two of these rules conflict, the lower number wins unless an exception is written in this repository (this file or [narrative/README.md](narrative/README.md)), not in a pull-request comment.
13. Identifiers (tickets, escalations, evidence tags, email addresses) agree with the timeline and cast. Ticket, escalation, and evidence IDs carry no year and use one increasing counter per prefix (`SEC0004021` for the SOC queue), unique and in chapter order.
14. Every named recurring character has one row in the [NADF cast registry](narrative/author-bible/cast-and-relationships.md#cast-registry-one-surname-per-character), and only that surname is used.

**NADF-only rules** in [narrative/README.md](narrative/README.md) still apply and do not replace 1-14: the junior owns the conclusion, the mentor revises out loud, every number is real (from the committed captures), episodes share work with lessons, and the narrator never understands more than the reader. The cover test and "fiction lives at lesson boundaries" also stay.

**Exception (seductive details).** A personal cost to Ethan, a relationship that moves, or a Book 0 habit that helps or misleads him is not a seductive detail. This settles NADF rule 4 (every beat does analytical work) against Portland rule 5. Write any further exception in this repo, not in a pull-request comment.

The date and ID checker is a narrative continuity check, not a new governance process. It is the NADF counterpart of Portland's `tools/check_dates.py`.

## What to preserve

- **The Standing Qualifications** in [docs/architecture.md](docs/architecture.md). Simplifying process does not license stronger claims. Specifically: no proficiency levels, scoring, mastery thresholds, or assessment-validity claims, anywhere.
- **The research** in [docs/research/](docs/research/). It is the evidence base and it is genuinely load-bearing.
- **The archive** in [docs/archive/](docs/archive/). Superseded, but it is the record of how the design was reached. Don't revive it, don't delete it.

## Before recording anything as unreachable

HTTP egress is restricted, and `curl` returning `000` does not mean a resource is unobtainable. **The session's git proxy serves anonymous clones of public repositories, including non-GitHub hosts.** Try `git ls-remote <url>` and a blobless clone (`git clone --depth 1 --filter=blob:none`, which lists a tree without downloading contents) before concluding anything.

This is not hypothetical. The NICE Framework was recorded as needing a manual download; it did not — [R007](docs/research/R007-nice-role-mapping.md) got the full current framework through a public clone after every HTTP path failed.

## Working practice

- **Land work on `main`.** The maintainer reviews from a phone, where hunting for a branch is miserable, and a pull request nobody merges is just another place for finished work to get lost — the same failure as lesson M1 stranded behind the governance guide, recreated with branches instead of documents. This is a one-person project with CI on the things that can actually break, and anything wrong can be reverted.
- Branch and open a pull request when the change is large enough that the diff is worth reading on its own, then **merge it yourself as soon as CI is green.** Do not hold a merge waiting for approval unless the maintainer asked you to, or the change is genuinely hard to reverse.
- **Markdown is the deliverable.** The maintainer reads it directly and does not want a rendered companion: no HTML build, no published web version. One source, no drift. The exception is a Beyond Bullet Points outline, which may be HTML or Markdown. All other deliverables stay Markdown only.
- One coherent commit where practical.
- Check relative links before pushing.
- Ask the maintainer only about genuine forks in the road: scope, audience, or anything hard to reverse. Not about mechanics.

## Reporting

Say what changed, what state the project is in, and what the next useful thing is. Nothing else.
