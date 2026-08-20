# R009 — What paired review can prove without a rubric

**Status:** assessed · **Date:** 2026-08-20 · **Prompt:** [`prompts/R009-reviewer-agreement.md`](prompts/R009-reviewer-agreement.md)

[R006](R006-literature-scan.md) put paired review third on its list and flagged the trap: trained raters with analytic rubrics reach weighted kappa around 0.79–0.83, the [capstone review guide](../../lessons/09-capstone-encrypted-outbound-traffic/review-guide.md) is deliberately not a rubric, and so a paired-review trial will produce a low number that means nothing unless what counts as a result is fixed beforehand.

The brief settles the measure and rejects nothing. What it does do is make the cost visible, and the cost is larger than this project assumed.

## Provenance

Commissioned from an external research model against the committed prompt, returned 2026-08-20. Findings and figures below are as supplied; sources were not read. The interpretation, the code list, the sample-size problem and the recommendation are this project's.

**Not independently verified.** The essay-marking figures are the load-bearing ones — the claim that non-rubric marking lands somewhere around 0.3–0.6 correlation, and much lower for inexperienced raters, is what makes a low result interpretable rather than alarming. Worth checking before it is quoted anywhere that matters.

## The instinct was right, and it has a name

R006 guessed that the useful question is whether two reviewers *notice the same things* rather than whether they reach the same verdict. That guess holds, and the brief supplies the vocabulary this project was missing.

The distinction is **global versus analytic** rating in performance assessment: a global rating is one overall judgment, an analytic judgment is a set of specific observations, and the two behave differently. "Did they notice the same issues" is not a rating problem at all — it is **intercoder reliability** from qualitative content analysis, where the question is precisely whether two coders apply the same codes to the same open-ended text.

That reframing matters more than it sounds. It moves the trial out of a literature where the absence of a rubric is a defect, and into one where coding open-ended prose against a shared taxonomy is the normal method.

**Confidence: high** that the mapping is correct. The brief could not find a specialised term for noticing-agreement in assessment specifically, and says so — it borrows the construct from content analysis rather than finding it named in place.

## The measure

Two levels, both chance-corrected.

| Level | Unit | Statistic | What it answers |
|---|---|---|---|
| **Verdict** | One work product | Cohen's kappa over 3 categories — acceptable as-is / acceptable with caveats / not acceptable | Sanity check: does the guidance support broadly aligned global judgment at all |
| **Issue** | Work product × issue code, flagged or not | Krippendorff's alpha (nominal), or kappa per code | The real question: did they see the same problems |

Jaccard similarity per work product — the overlap of the two sets of flagged issues divided by their union — is worth computing as a descriptive companion, because it is legible without a statistics background. It is not the reliability statistic and should not be reported as one.

Thresholds supplied: **≥0.80 good, 0.667–0.80 tentative, below 0.667 insufficient for strong claims.** These are content-analysis conventions, and this record adopts them as *stated in advance* rather than as *validated for this setting*.

**The verdict categories are an analysis artifact, not a change to practice.** No reviewer sees a scale, no learner sees a category, and nothing is scored. The brief is explicit that any numeric coding here is an ex post research artifact and cannot support a claim that anyone is proficient — which is the same limit the [Standing Qualifications](../capability-model.md) already impose from the other direction.

## The code list already exists

The brief proposes a generic taxonomy — observation/interpretation separation, missing alternative, uncalibrated confidence, unstated unknowns, scope mischaracterised. NADF does not need to adopt it, because the review guide's "look for" bullets are that list already, written from the design rather than imported.

Inverting them gives the codes directly:

| Code | Flagged when the work product… |
|---|---|
| **OI** | blurs observation into interpretation |
| **MA** | does not argue the benign or expected explanation seriously |
| **UC** | states confidence the evidence does not carry |
| **UD** | leaves what could not be determined unstated |
| **DV** | ignores the evidence with the highest decision value |
| **PR** | recommends action disproportionate to the confidence |
| **HO** | hands off without the timeline, scope and open questions an adjacent role needs |
| **RV** | replaces a conclusion silently instead of explaining the change |

Eight codes, each traceable to a bullet already in the guide and to the [evidence model](../evidence-model.md). Reviewers write their narrative exactly as now, then tick which of the eight they believe they raised. That is a taxonomy, not a rubric: no scale, no weights, no total.

**The stronger variant is post-hoc coding** — a second pass mapping free-text comments to the eight codes, so agreement rests on what was actually said rather than on whether a reviewer self-labelled it. Worth doing if two people are available for it, since differently-worded observations about the same underlying flaw are exactly the failure mode self-tagging hides.

## The problem: the design costs more than the project has

The brief's minimum design is **two reviewers and 20–30 work products**, spanning multiple incidents and difficulty levels, blind-double-reviewed with no discussion until capture is complete. Krippendorff wants roughly 30 units for a stable alpha; fewer is possible with wider uncertainty.

**NADF has zero work products.** [Roadmap item 1](../../ROADMAP.md) is still *run one lesson with one person*. Twenty to thirty capstone products is on the order of twenty to thirty learners completing a 60–90 minute performance task, each reviewed twice, blind — which is a research programme, not a design check, and it is not happening before the first run.

So the honest position is a split:

- **Settled now, free:** the measure, the two levels, the eight codes, the thresholds, and the rule that verdict disagreement alone proves nothing. All of that can be written into the protocol today and costs nothing.
- **Not available now:** a reliability coefficient. At three or five work products, kappa and alpha are unstable enough that reporting a figure would be worse than reporting none — it would invite exactly the over-reading the whole no-scores position exists to prevent.

What a small first pass *can* yield is descriptive: which codes both reviewers raised, which only one did, and whether the disagreements cluster. That is a finding about the guide, and it is worth having. It is not reliability and must not be written up as reliability.

**A first paired review should report Jaccard overlap and the per-code table, and explicitly decline to compute kappa.** State n. State that n is the reason.

## How to read a low number, decided in advance

The brief's most useful contribution is a way to tell three causes apart, which R006 asked for and could not answer. Recorded here so the trial cannot be reinterpreted after its result is known.

| Pattern | Cause | What NADF should do |
|---|---|---|
| Issue agreement high, verdict agreement lower | **Not a problem.** Reviewers see the same flaws and differ on how many flaws is too many — legitimate variation in professional tolerance | Accept it. Report issues noticed, not verdicts |
| Both low | **The guidance is under-specified**, or the reviewers differ in experience. A finding about the instrument, not the learner | Refine the guide, or add worked examples and a calibration conversation — still without adding a rubric |
| Issue agreement low, verdict agreement high | Reviewers land in the same place by gestalt while noticing different things — common in general-impression essay marking | Treat as a signal about case design and reviewer prompts even though the verdicts look fine |
| Disagreement concentrated in particular work products | **The task**, not the guide or the reviewers. Ambiguous or under-specified prompts mark less reliably | Examine those cases qualitatively. Some incidents are genuinely multi-solution, which is a fact about the work |

The separator between rater and task effects is simple enough to apply by eye at any n: a **rater** effect is one reviewer flagging consistently more or fewer issues across *all* products, stable across tasks; a **task** effect is agreement collapsing on specific products regardless of reviewer.

## On formative reliability thresholds

R006's prompt asked whether "lower reliability is acceptable for formative work" is a real methodological position or a convenience. The answer is **both, with a sting**: reliability requirements genuinely scale with stakes, and low-stakes formative use genuinely tolerates less precision — but there is no consensus threshold, no published figure saying 0.5 is fine for formative written work, and the position in the measurement literature is *strive for as much reliability as purpose and cost allow*, not *formative means reliability does not matter*.

NADF's no-scores stance is not a way out of this. It removes the obligation to defend a score; it does not remove the obligation to show that two reviewers reading the same work are not diverging at random.

## What could not be determined

Reported honestly by the brief and repeated here because it is the shape of the answer:

- **No study mirrors this setting** — narrative professional judgment, no scores at all, issue-spotting as the primary outcome. Even "general impression" marking studies still assigned numeric grade bands.
- **No realistic kappa range exists for genuinely rubric-less professional assessment.** Reported results run from near zero to moderate with no consensus. The 0.79–0.83 figure R006 carried is well supported *for rubric-based* assessment and is not a target this project can be measured against.
- **No agreed reliability threshold for formative open-ended work.**

That is the third scan in a row — [R006](R006-literature-scan.md), [R008](R008-longitudinal-judgment.md), now this — to come back reporting that the specific question has not been studied. The pattern is consistent enough to plan around: this project will not find its methods pre-validated, and the alternative to running its own trials is not a literature answer, it is no answer.

## What this changes

[Roadmap item 4](../../ROADMAP.md) keeps paired review at position 5, unchanged in priority. What changes is that it is now specified: the codes exist, the statistic is named, the thresholds are set before the data, and the honest reporting rule at small n is written down. None of that required a rubric, which was the constraint worth protecting.
