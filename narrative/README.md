# The narrative track

A story that runs alongside the lessons. A new analyst at Contoso and a mentor called Dana, one chapter before each lesson, ending where the lesson begins.

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

**4. Every beat does analytical work.** There is a well-replicated finding — the *seductive details* effect — that interesting-but-irrelevant material added to instruction reliably **hurts** learning while making readers rate it higher. Readers cannot detect it from the inside. So detail earns its place by carrying an analytical point or it comes out. Dana has no backstory. Nobody has a difficult marriage.

> **Confidence note.** Rule 4 rests on a literature this project has not verified against sources — the build environment cannot reach them. It is stated as a design constraint because the downside is asymmetric: writing lean costs nothing if the effect is smaller than believed.

**5. Chapters do not have their own exercises.** The lessons already end in work products. A chapter ends by handing off to one.

## Status

**One chapter, deliberately.** The prologue exists so the voice and the rules can be judged against something real before anyone commits to eight more. Nine chapters of fiction written before a single lesson has been run with a person would repeat the pattern this project spent July undoing.

| | Chapter | Leads into |
|---|---|---|
| 00 | [The Word in the Ticket](00-prologue.md) | [Lesson 01](../lessons/01-what-the-analyst-is-for.md) |

The prologue plants four questions Dana counts off, and the first two are answered by [lesson 02](../lessons/02-reading-a-conversation.md)'s work product — which is the same `403` the chapter opens on. That is the intended shape: the story owes the lesson a debt the lesson collects.
