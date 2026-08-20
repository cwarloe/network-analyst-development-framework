# R006 — Literature scan against R005's five gaps

**Status:** assessed · **Date:** 2026-08-19 · **Supersedes parts of:** [R005](R005-instructional-design-review.md)

[R005](R005-instructional-design-review.md) reviewed the instructional design and listed five areas the project had never consulted. This scans them.

**The headline is that the literature revises R005 rather than confirming it.** Three of its four cheap recommendations turn out to be more conditional than it implied, and one is stronger than it claimed. R005 is left standing as written; this record is the revision, which is the behavior the course asks learners to demonstrate.

## 1. Outcome data on network and SOC analyst training — essentially absent

R005 suspected this. It is worse than suspected.

What exists is three things, none of which is what NADF needs:

- **Performance measurement of working analysts.** A Delphi panel with industry experts and Analytic Hierarchy Process produced the SOC Analyst Assessment Method (SOC-AAM), evaluated in two SOCs. This measures incumbents on the job. It does not evaluate a training intervention.
- **Security awareness training.** A large literature, and a different construct entirely — it measures whether employees click phishing links, not whether analysts reason better. Its outcome measures do not transfer to this problem.
- **Ethnographic work.** One study trained three students as SOC analysts, embedded them in different SOCs, and had them meet with an anthropologist. Useful for understanding SOC effectiveness; not an outcome study of a curriculum.

**No controlled outcome evidence for analyst-reasoning curricula was located.** NADF's design therefore rests entirely on transfer from adjacent domains — expertise development, analytical reasoning, mental models — which is what R001–R003 covered and is a defensible basis.

But it should be said out loud rather than left implicit, because it changes what the project can claim. The current Standing Qualifications say no external role standard has confirmed the model's completeness. They should also say that **no published outcome evidence exists for this kind of training in this domain, so NADF cannot be benchmarked against a field standard because the field has not established one.**

That is not a weakness unique to NADF. It is the state of the field, and being the project that says so plainly is a better position than implying otherwise.

> Confidence: **Moderate.** Absence of evidence found in a scan is weaker than a systematic review. A dedicated search of ACM/IEEE and the human-factors literature could still turn something up.

## 2. Retrieval practice — supported, with a caveat that lands directly on NADF

R005 called this the largest gap and recommended closed-book recall prompts. The effect is real: meta-analytic testing effects around **g = 0.50**, transfer effects around **d = 0.40**, and around **g = 0.50** in applied classroom settings. It is stronger when material is complex, when retrieval is effortful, and **when feedback is given during practice**.

Two findings complicate the recommendation.

**Some studies find retrieval no better than restudy for learning to apply rules and procedures.** Much of what NADF teaches is procedural judgment — how to frame, how to discriminate, how to size a claim. That is precisely the category where the advantage is least reliable.

**The moderator that matters most is feedback, and NADF does not have it.** Retrieval works best when the learner finds out whether they were right. In eight of nine lessons there is no second party to tell them. So the intervention would be deployed in the condition least favorable to it.

The recommendation is not withdrawn. It is downgraded from *do this* to *trial this and measure*, and it moves below the next item.

> Confidence: **High** on the effect sizes. **Low** that a bare recall prompt helps this material without feedback attached.

## 3. Predict-then-check is the stronger version of the same idea

R005 listed this third. It should be first among the retrieval-flavored changes.

[Lesson 06](../../lessons/06-when-it-breaks.md)'s predict-then-check step is effortful retrieval **with immediate feedback built in** — the learner commits to a prediction, then checks it against the capture, and the capture tells them whether they were right. That is the configuration under which retrieval practice performs best, and it is the one NADF can implement without a second person in the room.

It also produces the error signal that makes the whole thing work. A recall prompt with no answer key generates effort; a prediction checked against evidence generates a correction.

> Confidence: **Moderate-to-High.** The mechanism is well supported and NADF can actually satisfy its preconditions, which is more than can be said for the bare recall prompt.

## 4. Self-explanation may already be backfiring

This is the finding R005 did not anticipate.

Every lesson ends in "Reviewing your own work" — a set of self-explanation prompts. R005 treated these as a mild positive with moderate support.

The literature is less comfortable. **Additional self-explanation, particularly for novice learners, can be extraneous and increase cognitive load.** Prompt effectiveness interacts strongly with prior knowledge, and an expertise-reversal pattern applies: low prior-knowledge learners gain most from studying worked examples, while higher prior-knowledge learners gain most from generating explanations themselves.

NADF's stated target learner has **no analysis experience and no tooling background** — the low prior-knowledge end. And lessons 02, 03 and 04 already carry a new tool, new protocol content, two field vocabularies, and a new reasoning habit before the self-review section begins.

Prompt design mediates this. Focused, gap-filling prompts outperform open-ended ones. NADF's self-review questions are mostly specific and gap-directed rather than open, which is the better form. But this is now a live risk in the shipped material, not a hypothetical about a proposed addition.

**Watch for it in the first run:** if learners skip or abandon the self-review sections in 02–04 but complete them in 01, 08 and 09, load is the likely explanation rather than motivation.

> Confidence: **Moderate.** The interaction is well established; whether it bites at NADF's specific load level is untested.

## 5. Inter-rater reliability — the bar has to be set before the trial, not after

R005 recommended paired review as the cheapest validity evidence available. It is. But R005 did not say how to interpret the result, and without that the trial will be misread.

Trained raters using **detailed analytic rubrics** achieve pairwise weighted kappa in the range of roughly **0.79 to 0.83**. Studies typically use two to five raters; Cohen's kappa for two, Fleiss' for three or more.

NADF's [capstone review guide](../../lessons/09-capstone-encrypted-outbound-traffic/review-guide.md) is **deliberately not a rubric.** It is a set of things a reviewer should look for, written to avoid premature scoring machinery — which the evidence model states as an explicit design choice.

So a paired-review trial will very likely produce agreement well below 0.79, and **that would not demonstrate the evidence model is broken.** The literature notes that lower reliability is routinely accepted for open-ended formative assessment. Unrubricked review is not built to produce rater agreement; it is built to produce useful feedback.

Set the question before running it. The useful question is not *"do the reviewers agree?"* but **"do they notice the same things?"** — whether both flag the same weak claim, the same missing alternative, the same overstated conclusion. Agreement on *what is worth commenting on* is the property the evidence families claim to have. Agreement on a verdict is not something this instrument was designed to deliver.

> Confidence: **High** on the calibration point. This changes how the trial should be run.

## 6. Transfer — the capstone is attempting the achievable kind, once

Far transfer, across domains sharing little structure, largely does not occur; a century of research has not resolved the debate, and the practical answer in education is "not very much." Near transfer succeeds relatively often because source and target share **both surface features and underlying structure**. Far transfer fails when surface dissimilarity hides structural correspondence.

Locate the capstone on that scale. Its transfer case moves from an encrypted-outbound-traffic decision to a DNS fragmentation incident: same domain, different surface, **shared structure** — in both, an initial attribution rests on the appearance of the traffic and is overturned by history, comparison, and mechanism.

That is mid-range transfer, not far transfer, and it is the kind that does happen. Good news for the design.

The problem is quantity. Transfer is built by varied practice across contexts, and NADF provides **one** transfer exposure, at the very end, after every preceding lesson has been single-context. The structural weakness is not the capstone's design — it is that nothing before it varies the context at all.

This also connects to [R005](R005-instructional-design-review.md)'s finding that all four LR statements land only in the capstone. Same root cause, arriving from a different direction.

> Confidence: **Moderate-to-High.** The transfer literature is contested in its details and consistent in this general shape.

## A note added after R007

[R007](R007-nice-role-mapping.md) mapped the capability model against an external role standard after this record was written, and independently reached the gap [R005](R005-instructional-design-review.md) found from the instructional side: the role performs trend, posture and continuous-monitoring work across time, and every NADF lesson is a single moment. That corroboration is why "a second transfer exposure" below understates the problem — the issue is not only how many transfer exposures there are, but that the course has no unit of analysis larger than one incident.

## Revised recommendation order

Replacing R005's ranking:

| | Change | Why it moved |
|---|---|---|
| 1 | **Predict-then-check in every lesson** | Was third. It is retrieval *with* built-in feedback, the condition under which the effect is most reliable, and NADF can satisfy its preconditions unaided |
| 2 | **Same task twice** | Unchanged. Nothing else can detect that a learner improved |
| 3 | **Paired review, with the bar set first** — ask whether reviewers notice the same things, not whether they reach the same verdict | Unchanged in priority, materially changed in method |
| 4 | **A second transfer exposure before the capstone** | New. One exposure at the end is the structural weak point, and this is the same root cause as the LR concentration R005 found |
| 5 | **Closed-book recall prompts** | Demoted from second. Least reliable for procedural material, and NADF lacks the feedback that makes it work |
| — | **Watch lessons 02–04 for self-explanation load** in the first run | New. A risk in shipped material, not a proposed change |

## What this scan does not establish

It is a scan, not a systematic review. Effect sizes were read from meta-analytic summaries rather than primary studies, and the absence of analyst-training outcome data is an absence found by searching, which is weaker than an absence established by a structured review.

Nothing here is evidence about NADF. It is evidence about the conditions under which the techniques NADF uses tend to work, applied to NADF by argument. The first run remains worth more than this document.

## Sources

Located by search, August 2026. Effect sizes and characterizations are as reported in the sources named.

- **Retrieval practice:** meta-analytic reviews reporting testing effect g ≈ 0.50, transfer d ≈ 0.40, applied-classroom g ≈ 0.50; moderators of complexity, retrieval effort and feedback; and the finding that retrieval is not always superior to restudy for applying rules and procedures.
- **Self-explanation:** the instructional-fit hypothesis literature on prompt design (gap-filling versus mental-model revision), and findings that self-explanation can be extraneous and load-increasing for novice learners.
- **Inter-rater reliability:** performance-assessment reliability literature reporting pairwise quadratic weighted kappa ≈ 0.79–0.83 among trained raters using analytic rubrics, and the accepted practice of lower reliability thresholds for open-ended formative assessment.
- **Transfer:** Barnett & Ceci's taxonomy for far transfer and its nine dimensions; second-order meta-analytic work on near and far transfer in cognitive training.
- **SOC analyst measurement:** the SOC Analyst Assessment Method (SOC-AAM), developed via Delphi panel and Analytic Hierarchy Process and evaluated in two SOCs.
