# The narrative track

A story that runs alongside the lessons. Ethan Mercer is a developing analyst at Harrowmere Equipment Group, mentored by Dana Shah. The working book architecture and full recurring cast are in [Book 1 — Learning to See](../BOOK-1.md).

**It is not a replacement for anything.** The lessons carry the technical content and the work products. These chapters exist to create the question the lesson answers, so a learner arrives already wanting to know.

## Why this exists

Not for engagement. For **time**.

[R005](../docs/research/R005-instructional-design-review.md) found the architecture has no time dimension. [R007](../docs/research/R007-nice-role-mapping.md) found the same gap from the role side — the NICE Defensive Cybersecurity role does trend analysis, posture reporting and continuous monitoring, and every NADF lesson is a single frozen moment. [R008](../docs/research/R008-longitudinal-judgment.md) went looking for how other fields close it and found medicine's longitudinal integrated clerkships — same patients, same supervisors, over months — carrying the strongest evidence of the six fields surveyed. Its top recommendation was a persistent environment recurring across incidents.

Prose spans time for free. *"Three weeks ago you told me this was fine"* is a sentence a story can say and a single-incident lesson cannot. That is the argument for this track, and it is the only one that would justify the writing cost.

## Rules

These are constraints, not style preferences. Breaking them makes the story contradict the course.

**1. Support fits the gap. The junior owns the conclusion.** [Lesson 01](../lessons/01-what-the-analyst-is-for.md) breaks the habit of confirming a conclusion handed down by someone else. Dana tells when reference knowledge is missing, directs reliable retrieval when that is the task, models otherwise invisible reasoning, and asks when reasoning is the learning target. She permits productive struggle and intervenes when it becomes random or unsafe. Her support fades as Ethan demonstrates readiness; questioning is not a substitute for teaching.

**2. The mentor is wrong in front of the junior, and revises out loud.** [Lesson 09](../lessons/09-capstone-encrypted-outbound-traffic/README.md) is about revising a model when evidence contradicts it. A mentor who is never wrong teaches that experts are oracles. One who says *"no, that's wrong, what I just said"* teaches the actual subject.

**3. Every number is real.** Read out of the committed captures, not invented. When a chapter shows a duration or a byte count, it came from `tshark` or Zeek. This is what makes the handoff work: the learner opens the same file two chapters later and the numbers are still there.

**4. Every beat does analytical work.** There is a well-replicated finding — the *seductive details* effect — that interesting-but-irrelevant material added to instruction reliably **hurts** learning while making readers rate it higher. Readers cannot detect it from the inside. So detail earns its place by carrying an analytical point or it comes out. Characters may have author-only backstories, but a detail reaches the reader only when it affects an analytical decision, assumption, relationship, or longitudinal consequence.

> **Confidence note.** Rule 4 rests on a literature this project has not verified against sources — the build environment cannot reach them. It is stated as a design constraint because the downside is asymmetric: writing lean costs nothing if the effect is smaller than believed.

**Exception (seductive details).** A personal cost to Ethan, a relationship that moves, or a Book 0 habit that helps or misleads him is not a seductive detail. Those details earn their place even when they do not change an analytical decision in the same beat. This settles NADF rule 4 against Portland cost-and-canon rule 5 (every chapter charges Ethan a personal cost). Do not use this rule to strip the residue of Book 0.

**5. Episodes share work with lessons rather than duplicating it.** Chapters do not add competing exercises. The technical lesson owns the work product and feedback. Narrative may establish a prediction or initial claim when the lesson preserves and tests it.

**6. The narrator never understands more than the reader.** If he reads a log fluently, a reader who cannot is being told they are behind before they start. He should be lost in the same places, name what he did not follow, and be told it does not matter yet. This is the cheapest defence against the material feeling abrupt, and it costs a sentence rather than a primer.


## Cost and canon rules (shared with Portland Desk)

NADF adopts Portland Desk's cost and canon rules 1-14. The numbering matches the Portland [Learning Narrative Framework](https://github.com/cwarloe/learning-narrative-kit/blob/main/docs/craft/learning-narrative-framework.md). Link that document rather than copying it, so the numbers cannot drift. The short forms below are a reminder; the framework is the source.

These rules sit alongside the NADF-only rules above. They do not replace them.

1. **No refunds.** A promotion, raise, or act of forgiveness may not offset any cost charged to Ethan in the same or the previous chapter. A relationship that moves through an action, with nothing said, is not a refund. A speech, a promotion, or a restored status is.
2. **Not the center of the web.** Each act has at least one incident that belongs to someone else, which Ethan hears about secondhand, and at least one thing Ethan saves or prepares that turns out not to matter.
3. **No narrator foreshadowing.** Cut lines such as "it would matter more than I knew."
4. **Carry-forwards must change action.** A carry-forward counts only when it changes what someone does in a later scene. A grudge may not be restated in more than two chapters without moving.
5. **Every chapter charges Ethan a personal cost** in time, money, opportunity, or standing, and nobody refunds it. Costs to other people are welcome but do not replace it. See the seductive-details exception under NADF-only rule 4 above.
6. **Standing struggles.** Ethan's standing struggles are named in the Portland bible and they drive each of his wrong turns. Do not invent a new flaw for each chapter.
7. **No repeated entrances.** No recurring character enters or exits with the same action, phrase, or device twice in an act. Each return opens on what changed since the last appearance.
8. **Dates are checked.** Check every date and season against [narrative/author-bible/timeline.md](author-bible/timeline.md) before merge. Run `python3 tools/check_dates.py`. A `date-ok` marker must give its reason: `<!-- date-ok: back-reference to the June incident -->`.
9. **Narrative file only.** A cost counts only if it is in the narrative file.
10. **Names the way people use them.** Use a surname only on introduction or when it matters (a formal report, an email signature, a stern manager). Otherwise use first names.
11. **No shared staging devices.** No two characters in the same act enter with the same staging device: an object carried "like" something, a burst into the aisle, or a phone ringing as the scene opens.
12. **Rule conflicts.** When two cost and canon rules conflict, the lower-numbered rule wins unless an exception is written in this repository, in this file or in [AGENTS.md](../AGENTS.md). Do not leave an exception in a pull-request comment. (The seductive-details exception above is one such exception. Portland's own Exception 1, in the framework, still stands.)
13. **Identifiers are canon.** Every identifier that encodes a date, a name, or a sequence (ticket, escalation, evidence tag, email address) must agree with the timeline and the cast list. Ticket, escalation, and evidence IDs carry no year. The SOC queue uses its own prefix and a fixed-width yearless counter in the style `SEC0004021`, unique and in chapter order. `tools/check_dates.py` checks this.
14. **One surname per character.** Every named recurring character has one row in the [NADF cast registry](author-bible/cast-and-relationships.md#cast-registry-one-surname-per-character). Use only that surname. Book 0 names follow the Portland registry when they appear here.

The cover test and "fiction lives at lesson boundaries" stay in the section below. They are NADF-only rules and they do not collide with 1-14.

## Canon and disclosure

The author may know why Dana chooses an intervention, what another character has not disclosed, or which later evidence will overturn Ethan's model. Ethan and the reader may use only what has been revealed. Conclusions are evaluated against the evidence then available, not the author's hidden answer.

The recurring cast has distinct sources of partial knowledge: Nia Alvarez manages security operations and owns operational decisions; Owen Kline is the experienced analyst with deep institutional pattern knowledge; Priya Raman carries the network-engineering view; Leah Moreno carries system, application, and business-workflow purpose; and Cal Rowan engineers the telemetry, detections, and automation that shape what analysts can observe. None is an omniscient source or replacement mentor.

Dana's support fades across the book. She first supplies questions, then reviews Ethan's models, and is absent during the capstone's core performance. Ethan's errors must evolve with his capability rather than repeating the prologue's mistake.

## How the lessons reference this

Decided 2026-08-21, before any of it was built, so it is not re-argued later.

**Fiction lives at lesson boundaries, never inside the instructional body.** A chapter before, a chapter after. The lesson itself stays second-person, present tense, technical, all the way through. This is what stops a hard break into academic mode without letting the lessons go soft in the middle.

**Lessons reference events, not characters.** "The word in the ticket" is portable — it means something to a reader who skipped the story and lands as a callback for one who didn't. "Dana said" forces the lesson to stop and explain a character. Characters stay in these files.

**The cover test.** Hide any reference to the story. The lesson sentence must still work. If it doesn't, rewrite it. This is what keeps the promise the root README makes, that the lessons stand alone — and nothing automated can check it, so it is discipline rather than a gate.

**Story demonstrates, lesson names and tests.** The story provides the experience; the lesson provides the vocabulary and the practice. Where the story has already shown something, the lesson names it in half the words and spends the saved space on a check instead of a reveal. [Lesson 01](../lessons/01-what-the-analyst-is-for.md)'s Case A works this way: the prologue spent the reader's first encounter with a smuggled conclusion, so Case A asks them to find one rather than pointing at it.

**Watch for collisions.** The prologue duplicated Case A's punchline and neither the author nor the maintainer noticed until the seam was being designed. Every chapter needs checking against its neighbouring lesson's reveals, and that cost grows with each one written.

**One open question, deliberately unresolved.** Everything above assumes the lessons stay usable standalone. If that changes — if the story becomes required reading — the cover test disappears, the seams get considerably better, and the course becomes one thing instead of two. That is a defensible choice and it is the opposite of what is written down today. It should be decided on purpose, not by drift.

## Status

**Fifteen chapters** (Book 1 is 00-09, Book 2 is 10-14). The complete narrative track spans Ethan's development from day one through the independent capstone: separating observation from interpretation, reading conversations, predicting name behaviors, bounding claims under encryption, reconciling vantage contradictions, classifying conversation failure states, competing explanations, proportionate handoffs under pressure, and visible model revision.

| | Chapter | Leads into |
|---|---|---|
| 00 | [The Word in the Ticket](00-prologue.md) | [Lesson 01](../lessons/01-what-the-analyst-is-for.md) |
| 01 | [Who Is Talking to Whom?](01-who-is-talking-to-whom.md) | [Lesson 02](../lessons/02-reading-a-conversation.md) |
| 02 | [Before You Look](02-before-you-look.md) | [Episode 3 technical lesson](../lessons/e03-before-you-look/README.md) — built |
| 03 | [Names Have Behavior](03-names-have-behavior.md) | [Lesson 03](../lessons/03-names-and-expectations.md) |
| 04 | [What Encryption Leaves Behind](04-what-encryption-leaves-behind.md) | [Lesson 04](../lessons/04-what-encryption-hides.md) |
| 05 | [Where Are You Standing?](05-where-are-you-standing.md) | [Lesson 05](../lessons/05-vantage-point-and-evidence.md) |
| 06 | [Conversations Have Structure](06-conversations-have-structure.md) | [Lesson 06](../lessons/06-when-it-breaks.md) |
| 07 | [More Than One Explanation](07-more-than-one-explanation.md) | [Lesson 07](../lessons/07-when-its-suspicious.md) |
| 08 | [What Can You Responsibly Say?](08-what-can-you-responsibly-say.md) | [Lesson 08](../lessons/08-judgment-and-handoff.md) |
| 09 | [Decide Before You Disrupt](09-decide-before-you-disrupt.md) | [Lesson 09 Capstone: Encrypted Outbound Traffic](../lessons/09-capstone-encrypted-outbound-traffic/README.md) |

### Book 2 — The Hunter's Eye (Proactive Threat Hunting Track)

| | Chapter | Leads into |
|---|---|---|
| 10 | [The Silence of the Data Lake](10-the-silence-of-the-data-lake.md) | [Hunt 01 — The Falsifiable Hypothesis](../lessons/hunt-01-the-falsifiable-hypothesis/README.md) |
| 11 | [The Long Tail](11-the-long-tail.md) | [Hunt 02 — Least-Frequency Analysis](../lessons/hunt-02-least-frequency-analysis/README.md) |
| 12 | [The Heartbeat with a Stutter](12-the-heartbeat-with-a-stutter.md) | [Hunt 03 — Beaconing & Statistical Jitter](../lessons/hunt-03-beaconing-and-jitter/README.md) |
| 13 | [The Forest and the Trees](13-the-forest-and-the-trees.md) | [Hunt 04 — Domain & TLS Clustering](../lessons/hunt-04-domain-and-tls-clustering/README.md) |
| 14 | [The Hunter's Crucible](14-the-hunters-crucible.md) | [Hunt 05 — The Whole-Fleet Crucible (Capstone)](../lessons/hunt-05-the-whole-fleet-crucible/README.md) |


Vocabulary tables, At a glance blocks, and lesson bridge cards no longer sit in the chapter files. The table above and the [master glossary](../glossary.md) keep that map. A chapter should still read if every lesson title and number is stripped from it.

The prologue plants four questions Dana counts off. [Lesson 02](../lessons/02-reading-a-conversation.md) first establishes what the same two conversations show; owner evidence and history are still needed to determine intended and habitual behavior. The immediate payoff is reconstruction, not a baseline or an authorization judgment.

## Author-only continuity

The deep working canon is maintained in the [narrative author bible](author-bible/README.md). It contains the recurring cast and relationship web, Harrowmere history and page-one state, Book 1 Snowflake and causal matrix, all 14 episode cards, the provisional HarrowSync system bible, and the [Episodes 1–3 scene-card test slice](author-bible/book-1-scene-cards-episodes-01-03.md).

This material is intentionally much deeper than the reader-visible story. A detail belongs in prose only when it changes reasoning, relationship, continuity, or consequence.
