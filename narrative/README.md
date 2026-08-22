# The narrative track

A story that runs alongside the lessons. Ethan Mercer is a developing analyst at Harrowmere Equipment Group, mentored by Dana Shah. The working book architecture and full recurring cast are in [Book 1 — Learning to See](../BOOK-1.md).

**It is not a replacement for anything.** The lessons carry the technical content and the work products. These chapters exist to create the question the lesson answers, so a learner arrives already wanting to know.

## Why this exists

Not for engagement. For **time**.

[R005](../docs/research/R005-instructional-design-review.md) found the architecture has no time dimension. [R007](../docs/research/R007-nice-role-mapping.md) found the same gap from the role side — the NICE Defensive Cybersecurity role does trend analysis, posture reporting and continuous monitoring, and every NADF lesson is a single frozen moment. [R008](../docs/research/R008-longitudinal-judgment.md) went looking for how other fields close it and found medicine's longitudinal integrated clerkships — same patients, same supervisors, over months — carrying the strongest evidence of the six fields surveyed. Its top recommendation was a persistent environment recurring across incidents.

Prose spans time for free. *"Three weeks ago you told me this was fine"* is a sentence a story can say and a single-incident lesson cannot. That is the argument for this track, and it is the only one that would justify the writing cost.

## Rules

These are constraints, not style preferences. Breaking them makes the story contradict the course.

**1. The mentor asks. The junior concludes.** [Lesson 01](../lessons/01-what-the-analyst-is-for.md) is built to break the habit of confirming a conclusion you were handed. A wise character explaining things teaches deference — the exact habit the course exists to remove. Dana's job is to ask the question and leave.

**2. The mentor is wrong in front of the junior, and revises out loud.** [Lesson 09](../lessons/09-capstone-encrypted-outbound-traffic/README.md) is about revising a model when evidence contradicts it. A mentor who is never wrong teaches that experts are oracles. One who says *"no, that's wrong, what I just said"* teaches the actual subject.

**3. Every number is real.** Read out of the committed captures, not invented. When a chapter shows a duration or a byte count, it came from `tshark` or Zeek. This is what makes the handoff work: the learner opens the same file two chapters later and the numbers are still there.

**4. Every beat does analytical work.** There is a well-replicated finding — the *seductive details* effect — that interesting-but-irrelevant material added to instruction reliably **hurts** learning while making readers rate it higher. Readers cannot detect it from the inside. So detail earns its place by carrying an analytical point or it comes out. Characters may have author-only backstories, but a detail reaches the reader only when it affects an analytical decision, assumption, relationship, or longitudinal consequence.

> **Confidence note.** Rule 4 rests on a literature this project has not verified against sources — the build environment cannot reach them. It is stated as a design constraint because the downside is asymmetric: writing lean costs nothing if the effect is smaller than believed.

**5. Episodes share work with lessons rather than duplicating it.** Chapters do not add competing exercises. The technical lesson owns the work product and feedback. Narrative may establish a prediction or initial claim when the lesson preserves and tests it.

**6. The narrator never understands more than the reader.** If he reads a log fluently, a reader who cannot is being told they are behind before they start. He should be lost in the same places, name what he did not follow, and be told it does not matter yet. This is the cheapest defence against the material feeling abrupt, and it costs a sentence rather than a primer.

## Canon and disclosure

The author may know why Dana chooses an intervention, what another character has not disclosed, or which later evidence will overturn Ethan's model. Ethan and the reader may use only what has been revealed. Conclusions are evaluated against the evidence then available, not the author's hidden answer.

The recurring cast has distinct sources of partial knowledge: Nia Alvarez is a peer analyst; Owen Kline carries the network-engineering view; Priya Raman carries system and application purpose; Leah Moreno consumes analysis for incident response; and Cal Rowan owns operational decisions. None is an omniscient source or replacement mentor.

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

**Three chapters.** The first production slice now carries the learner from separating observation and interpretation, through reading a conversation, to the need for prediction and visible revision. The Episode 3 technical exercise is intentionally still a handoff debt rather than being authored in the narrative track.

| | Chapter | Leads into |
|---|---|---|
| 00 | [The Word in the Ticket](00-prologue.md) | [Lesson 01](../lessons/01-what-the-analyst-is-for.md) |
| 01 | [Who Is Talking to Whom?](01-who-is-talking-to-whom.md) | [Lesson 02](../lessons/02-reading-a-conversation.md) |
| 02 | [Before You Look](02-before-you-look.md) | Episode 3 staged prediction and revision exercise — assigned, not yet authored |

The prologue plants four questions Dana counts off, and the first two are answered by [lesson 02](../lessons/02-reading-a-conversation.md)'s work product — which is the same `403` the chapter opens on. That is the intended shape: the story owes the lesson a debt the lesson collects.
