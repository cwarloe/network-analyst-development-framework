---
name: technical-training-design
description: >-
  Evidence base and design patterns for building training that develops
  judgment in a technical domain — curricula, courses, lessons, onboarding
  programmes, analyst or engineer development, certification paths. Use this
  whenever the user is designing, reviewing, or arguing about instructional
  material — how to teach a technical skill, how to structure lessons or
  exercises, whether training is working, how to assess open-ended written
  work, how to check that two reviewers agree, or how to develop expertise
  that plays out over time rather than in one sitting. Also use it when
  someone proposes a training intervention that sounds obviously right, since
  most of them are unsupported and this skill carries what actually is, with
  its confidence attached.
---

# Designing training that develops judgment

For technical domains where the goal is **judgment** — deciding what evidence means, holding competing explanations, knowing what you cannot yet claim — not recall or tool operation.

Distilled from a curriculum-development project that commissioned four literature reviews and then had to act on them. **The confidence markers below are load-bearing.** Most of this evidence is weaker than it sounds, and the failure mode this material exists to prevent is presenting a plausible-sounding intervention as a settled one.

## The stance

Two questions separate real instructional design from taste:

1. **What is this claim's evidence, and how strong is it actually?**
2. **What would tell me this isn't working?**

Almost every training intervention that feels obviously right is unsupported. Some are actively harmful. Ask for the evidence before building, and record what you find — including when the honest answer is "nobody has studied this."

## What is actually supported

**Strong.** Two techniques are consistently rated high-utility across the learning-science literature:

- **Practice testing** — retrieval, not re-reading. The strongest version builds feedback in: the learner commits to a prediction, then the material reveals whether they were right. *Predict-then-check* is retrieval with feedback attached and it needs no second person in the room, which makes it the highest-value change available to most projects.
- **Distributed practice** — the same material revisited across time rather than massed.

**Moderate.** Interleaving, self-explanation, elaborative interrogation. Worth using; not worth restructuring a course around.

**Weak.** Re-reading, highlighting, summarisation. These *feel* productive, which is exactly the problem.

> Confidence: high that the ranking is right; moderate on specifics. These ratings come from secondary summaries of the Dunlosky et al. (2013) monograph rather than the monograph itself.

**Worked examples, then fading guidance.** Novices learn more from studying a worked solution than from attempting the problem. That reverses as expertise grows — the *expertise reversal effect* — so guidance has to fade. Well supported.

**Seductive details hurt.** Interesting-but-irrelevant material added to instruction reliably *reduces* learning while making readers rate the material higher. Readers cannot detect this from the inside, and neither can authors. Every anecdote, illustration, and narrative flourish must carry an instructional point or come out.

> Confidence: moderate. Well-replicated in the literature but not independently verified in the project this came from. Treat as a design constraint anyway — writing lean costs nothing if the effect is smaller than believed.

## The structure this implies

**Three rungs per unit, not two.** Most technical training goes: worked walkthrough → do it yourself. That is one step from fully scaffolded to unaided, and it hides where the learner actually is.

| Rung | Guidance | Purpose |
|---|---|---|
| **Worked example** | Full. Shown start to finish | The demonstration |
| **Guided practice** | Prompts, no answer key | Where the learner finds out where they are |
| **Work product** | None | The evidence |

The middle rung is the one usually missing and the cheapest to add.

**Hold deep structure constant; vary surface hard.** The practice case must require the *same move* as the worked example on *deliberately unlike material*. If the practice case is the worked example with the nouns swapped, learners match phrasing instead of recognising the pattern — they will pass your exercise and fail the real thing.

**When the data allows no second case, ask a different question of the same data.** Predict before you look. State what this source cannot establish. That is a genuine practice rung and it costs nothing to produce.

**Fade guidance inside each unit, not only across units.** Fading only at unit boundaries means the right fade point differs by learner and the design cannot detect it. The middle rung is where the learner detects it themselves.

## Assessment: what you can and cannot claim

Read `references/assessment.md` before designing any review process, rubric, or reviewer-agreement check. Short version:

- **Without a validated instrument you cannot claim proficiency, mastery, or a level.** Any number you attach is a research artifact, not a measurement.
- **Ask whether reviewers noticed the same things, not whether they reached the same verdict.** That is *intercoder reliability* from qualitative content analysis, not rating reliability, and it behaves differently.
- **Trained raters with analytic rubrics reach weighted kappa ≈ 0.79–0.83.** Without a rubric, published results run from near-zero to moderate. The 0.79–0.83 figure is not a target a rubric-less design can be held to.
- **At small sample sizes, report descriptive overlap and decline to compute a coefficient.** State n and state that n is the reason. A kappa on five items invites exactly the over-reading that a no-scores design exists to prevent.
- **"Formative means reliability doesn't matter" is false.** Requirements scale with stakes, but there is no consensus threshold and no licence to ignore it.

## Judgment that plays out over time

Most training teaches single-moment decisions. Most technical judgment work is longitudinal — trends, drift, posture over weeks. If your curriculum has no unit of analysis larger than one incident, that is a real gap, and `references/longitudinal.md` covers how six other fields close it and how strong each one's evidence actually is.

The two structures worth stealing:

- **A verification tracker.** Record the decision, the confidence, and the expected time horizon; reveal ground truth later; let a personal hit-and-miss record accumulate. This is retrieval, feedback and distributed practice in one mechanism, and it comes from operational meteorology rather than from education research.
- **Multi-episode cases.** The same environment across several exposures, with an explicit revisit-your-own-earlier-judgment step.

Two cautions: no minimum dose is established, and effects from single-sitting interventions have been observed to decay within weeks without reinforcement.

## When the evidence does not exist

**Expect this.** In one project, three independent literature scans came back reporting that the specific question had never been studied for the target domain. That is the normal case for specialised technical fields, not a failure of searching.

What to do:

1. **Say so plainly.** "No evidence exists for this domain" is a finding and belongs in the record.
2. **Borrow across the domain boundary and label the borrowing.** Structures from medicine, aviation, or meteorology can be adapted — but the transfer claim is yours, not the literature's.
3. **Accept that you will have to run your own trials.** The alternative to a trial is not a literature answer, it is no answer.

## Process discipline

Five lessons that cost real rework:

**Validate against how the material will actually be consumed, not how it looks to you.** Something can read beautifully to its author and fail the moment it meets its real use. Find the downstream check that would catch that and run it.

**Adversarial re-reading finds what testing cannot.** In one pass over nine finished lessons, five defects surfaced that had passed every automated check — including a lesson contradicting itself, and a claim that told learners something was unknowable when it was sitting in a log the lesson had just told them to open. Schedule the read; it needs distance from the writing.

**Claims about what a tool shows must be re-run, not remembered.** The single most common defect class: an author describing output from memory. If a document quotes tool output, execute the command and diff it. This is automatable and worth automating.

**Queued recommendations go stale, and some were wrong when written.** Two recommendations in that project's own research records turned out to be wrong on inspection — one rested on a category error, one had already been superseded. Both looked actionable for weeks. Before acting on a recommendation, re-check it against the source it came from, not against the summary.

**And don't add process.** Small projects die of governance documents, decision registers, and review gates that no one has the capacity to operate. Record a lesson where someone will trip over it — in the file where the work happens — not in a register nobody reads.

## References

- `references/assessment.md` — reviewer agreement without a rubric: the measures, the statistics, the thresholds, the minimum design, and how to tell a rater problem from a task problem from an instrument problem.
- `references/longitudinal.md` — how six fields develop judgment across time, with evidence strength per field, and what is known about training change-detection.
