# NADF timeline (author-only anchors)

Internal continuity anchors for Book 1 and Book 2. This file is not learner-facing. Do not print the working start date in chapter prose. Book 0 facts (ages, jobs, employer, Nia, Leah, Dana) come from the Portland Desk timeline and bible; this file does not replace them.

Portland sources (do not copy them here):

- [PORTLAND_TIMELINE.md](https://github.com/cwarloe/learning-narrative-kit/blob/main/docs/research/PORTLAND_TIMELINE.md)
- [PORTLAND_AUTHOR_BIBLE.md](https://github.com/cwarloe/learning-narrative-kit/blob/main/docs/research/PORTLAND_AUTHOR_BIBLE.md) (section 1.3)

`python3 tools/check_dates.py` reads the chapter table below.

## Standing anchors

- Year 4 is 2026.
- Book 1 opens in August, Year 4. The offer from the parent company, Harrowmere Equipment Group, is already in the past when the prologue begins. The story starts mid-stride, eleven days into the job, with no on-page offer scene. Ethan does not apply again; Book 0 already ended on the submitted application.
- **Working start date (internal only):** about 9 August Year 4 (2026-08-09). This is the implied first day on this floor and badge, eleven days before the prologue ticket. Keep "eleven days on this floor" in the prose and do not print this date. The checker uses it as an anchor, not as a chapter timestamp.
- The prologue's first ticket is already stamped 2026-08-20 in the current chapter file.
- Ethan is 23 at the open and turns 24 in September of Year 4.
- **Security+:** Ethan holds Security+ when Book 1 opens. He earned it just after Book 0 Episode 12, off the page. Treat it as a floor, not a skill. The paper does not help in the first real hunt; that is for the prologue to show, not for this file to invent.
- **Ticket IDs:** yearless, monotonic, fixed-width counters with a SOC prefix, in the style `SEC0004021`. They run in their own sequence, increasing by chapter, with no year and no reuse. The checker accepts that prefix. The prologue uses `SEC0004021`. Chapters 01-14 still use the short form `SEC-4021`; later chapter PRs should migrate those IDs. Do not introduce a year into a ticket or evidence ID.
- Ethan works for the parent, one floor above PROC, still in the Portland area. He never relocates.
- Leah Moreno moved up to the parent's Enterprise Applications team a few weeks ahead of him. They know each other; they are not close. A first ticket together is fine. A first meeting is not.
- Nia Alvarez is Security Operations Manager in Portland at the open. In Book 0 Episode 12 she was still in Chicago, on the bridge only.
- Dana Shah was, in Book 0, only a signature on a ticket reply (Episode 09, signed D. Shah). Their first working conversation is the prologue.

## Chapter calendar

Book 1 is chapters 00-09. Book 2 is chapters 10-14. Fifteen narrative files in all.

Only pin a month when it is already decided. Book 2 months are not decided; do not invent them. Book 1 stays in August, Year 4, unless a later row pins a new month.

| Chapter | Book | Calendar | Notes |
|---|---|---|---|
| Ch 00 | 1 | August Year 4 | Prologue. First ticket stamped 2026-08-20. Eleven days on this floor, not eleven days at Harrowmere. |
| Ch 01 | 1 | August Year 4 | First ticket with Leah; not a first meeting. |
| Ch 02 | 1 | August Year 4 | |
| Ch 03 | 1 | August Year 4 | |
| Ch 04 | 1 | August Year 4 | |
| Ch 05 | 1 | August Year 4 | |
| Ch 06 | 1 | August Year 4 | |
| Ch 07 | 1 | August Year 4 | |
| Ch 08 | 1 | August Year 4 | |
| Ch 09 | 1 | August Year 4 | End of Book 1. |
| Ch 10 | 2 | not pinned | Book 2 begins. Do not invent a month. |
| Ch 11 | 2 | not pinned | |
| Ch 12 | 2 | not pinned | |
| Ch 13 | 2 | not pinned | |
| Ch 14 | 2 | not pinned | End of Book 2. |

Chapters 01-09 currently repeat `2026-08-22` in their frontmatter. That date is a copied placeholder, not a claim that each chapter happens on that Saturday, and several of those chapters already name other weekdays in the body. Leave the prose alone in this change; a later chapter PR should give each file an honest date or drop the copied one.

## Checker command

From the repository root:

```
python3 tools/check_dates.py
```

The checker fails on month or ISO-date drift against this table, on a weekday that disagrees with a `YYYY-MM-DD` date on the same line, on ticket or evidence IDs that carry a year or collide, and on a registered first name paired with the wrong surname. It accepts `SEC0004021` and, until the chapters are migrated, the short form `SEC-4021`. A `date-ok` marker must give a reason: `<!-- date-ok: back-reference to the June incident -->`.
