# R005 — Does this design actually produce analysts?

**Status:** assessed · **Date:** 2026-08-19 · **Confidence:** see per-claim

A review of NADF's instructional methodology against what the learning-science literature supports, and of the architecture against what it would take to know whether it works.

> **Corroborated by [R007](R007-nice-role-mapping.md).** Finding 1 below says the architecture has no time dimension. R007 later mapped the capability model against the NICE Defensive Cybersecurity role and found that its trend-analysis, posture-reporting and continuous-monitoring statements have no NADF counterpart — the same structural absence, reached from the role side by an unrelated method. Two independent routes to one gap is the strongest signal either record carries. [R008](R008-longitudinal-judgment.md) then asked how other fields close it, and found medicine's longitudinal clerkships and meteorology's forecast verification the two structures with real evidence behind them.
>
> **Partly superseded by [R006](R006-literature-scan.md).** R005 named five literature gaps; R006 scanned them and the results revised this record's recommendation order rather than confirming it. Three of the four cheap recommendations below are more conditional than stated here, and the self-review sections this record treated as a mild positive turn out to carry a real load risk for novices. R005 is left as written; R006 is the revision.

Written after all nine lessons existed and before any of them had been used. That timing matters: the findings below are about design, not about performance, because no performance data exists yet.

## What the methodology actually is

NADF never names its instructional model in one place. Reconstructed from the [baseline](../architecture.md), the [capability model](../capability-model.md), the [evidence model](../evidence-model.md), and the lessons as built, it is:

| Element | Where it lives | Closest named tradition |
|---|---|---|
| Modeling → coaching → fading | Principle 5; the 01–04 / 05–07 / 08–09 scaffold bands | Cognitive apprenticeship |
| Worked example → guided → unaided | Lesson 01's Case A/B/C structure | Worked-example effect with faded guidance |
| Whole authentic cases from the first hour | Every lesson's work product | Case- and scenario-based learning |
| Schema before discrimination | Principle 4, and lesson 06 preceding 07 | Expected-behavior-first sequencing |
| Reasoning taught through content, not beside it | Principle 3 | Domain-embedded reasoning instruction |
| Assessment by work product, not test | Principle 7, the whole evidence model | Performance assessment |

That combination is coherent and unusually disciplined. Almost every element traces to a **sourced finding** in the [provenance matrix](2026-07-11-r001-r003-reconciliation-provenance-recovery.md), particularly PC-02 (guidance, scaffolding, worked examples, progressive independence) and PC-04 (structured, revisable mental models).

**The design is not the problem.** What follows is about what the architecture does not address at all.

## Finding 1 — The architecture has no time dimension

Seven principles. Six concerns. Seven analytical functions. **None of them says anything about when learning happens, how often, or whether anything is revisited.**

The course is a single pass. Each lesson is done once, produces one work product, and is never returned to. Nothing is retrieved from memory; every fact needed is on the page in front of the learner.

Dunlosky et al. (2013) reviewed ten learning techniques and rated exactly two as **high utility**: *practice testing* and *distributed practice*. Both generalize across ages, abilities, materials, and criterion tasks. Neither appears anywhere in NADF — not in the principles, not in Concern D, not in any lesson.

This is the largest gap between what the evidence base supports and what the architecture builds. It is also the cheapest to close, because it does not require new lessons (see recommendations).

> Confidence: **High** that the techniques are well supported and absent here. **Moderate** that adding them helps this specific population — the evidence is largely from academic learning of declarative material, and NADF teaches procedural judgment on authentic tasks, where retrieval practice is less studied.

## Finding 2 — Nothing in the design can detect learning

The [Standing Qualifications](../architecture.md) refuse proficiency levels, thresholds, scoring, and validity claims. That refusal is honest and, at this stage, correct — the project has not earned those claims.

But it has a consequence that should be stated plainly: **there is currently no mechanism by which NADF could observe that a learner improved.**

The [run records](../../lessons/run-records.md) instrument measures whether the *models* describe real analyst work — coverage, observability, discrimination, friction. It does not measure the learner. A run could go perfectly and produce no evidence that anyone learned anything.

The gap is not "we should add scoring." It is that *outcome* and *validity* are different questions, and the project has correctly deferred validity while accidentally deferring outcome with it. Detecting change does not require a rubric, levels, or a passing standard. It requires the same task twice.

> Confidence: **High.** This is a property of the artifacts, not an inference.

## Finding 3 — Feedback is self-review for eight of nine lessons

Every lesson except the capstone ends in "Reviewing your own work." The capstone is the only one with a review guide written for a second party.

The evidence model states the problem itself: *"Feedback and model revision require an observable change across time, not a claim that learning occurred."* EF-8 — feedback, revision, and transfer — is structurally unreachable in eight of nine lessons, because there is no feedback in them.

Self-review has real value for metacognition and the questions in these lessons are well constructed. But a novice asked *"did you separate observation from judgment?"* has to detect an error using the same faculty that produced it. That is the weakest position self-assessment can be in.

This is [COURSE.md](../../COURSE.md)'s open question 2 — self-guided or instructor-led — and it is more consequential than it looks. It is not a delivery-mode preference; it decides whether a whole capability domain is reachable.

> Confidence: **High** on the structural claim. **Moderate** on severity — well-designed self-explanation prompts do help, and Dunlosky rates self-explanation moderate utility.

## Finding 4 — Guidance fades on a schedule, not on evidence

Principle 5 says support reduces *"as capability develops."* The course reduces it at fixed lesson boundaries: worked through 04, guided-independent 05–07, unaided 08–09.

A fixed schedule is a reasonable default and possibly the only practical one for self-guided material. But it is an assumption doing load-bearing work, and it is worth naming as one. The expertise-reversal literature holds that heavy guidance stops helping and begins to hinder once a learner has enough schema — so the *right* fading point differs per learner, and this design cannot detect it.

The course's own entry assumption compounds this: it targets someone with no analysis experience and no tooling background, while [run-records](../../lessons/run-records.md) suggests running the capstone with experienced analysts. Those two audiences want different fade points from the same material.

> Confidence: **Moderate.** Expertise reversal is well established in worked-example research; whether it bites at NADF's scale and duration is untested.

## Finding 5 — Prediction appears once and should be everywhere

[Lesson 06](../../lessons/06-when-it-breaks.md) asks the learner to predict what they will see, write it down, check, and record where they were wrong. It is the only place in nine lessons that does this.

That single step is doing several well-supported things at once: it is retrieval practice, it is generation, and it creates the error signal that makes feedback usable. It is also the only mechanism in the course that produces LR-1 evidence outside the capstone.

It costs about ten lines of text per lesson.

> Confidence: **High** that this is underused. **Moderate** on effect size in this context.

## Finding 6 — Practice is blocked, not interleaved

All DNS in one lesson, all TLS in another, all failure modes in a third. Blocked practice.

The course's central skill is **discrimination** — refused versus dropped, benign beacon versus malicious beacon, normal-looking-strange versus actually-strange. Interleaving is theorized to help precisely with discrimination, because it forces the learner to select the right comparison rather than apply the one currently in front of them.

Recording this as an option rather than a recommendation, deliberately: Dunlosky rates interleaved practice **moderate** utility, not high, with benefits that generalize across some variables and limited evaluation in educational contexts. It would also fight Principle 4's sequencing. A blocked-then-interleaved hybrid — teach each shape in isolation, then a mixed set — is the version worth testing, not a wholesale reordering.

> Confidence: **Low-to-Moderate.** Theoretically attractive, empirically thinner than the other findings here, and in tension with an existing principle.

## Finding 7 — No external role standard has been checked

The Standing Qualifications say it directly: *"no external role standard or practitioner population has confirmed its completeness."*

That is a checkable gap and it has been left open. The NICE Framework publishes a **Cyber Defense Analyst** work role with Task, Knowledge and Skill statements, free and public. Mapping NADF's 27 capability statements against that role's TKS statements is roughly a day of work and produces one of three results, all useful:

- broad correspondence, which is the first external support the capability model has ever had;
- NADF statements with no NICE counterpart, which are candidates for architectural judgment being mistaken for role reality;
- NICE statements with no NADF counterpart, which are coverage holes.

The last category is the one worth wanting. A framework built from learning-science research and design judgment, without a role inventory, will have holes exactly where the designer's intuition was thin.

> Confidence: **High** that this is worth doing. Its result is unknown, which is the point.

## What I may have made worse

The [Security Onion field-name change](../../lessons/field-names.md) is correct — it teaches the vocabulary an analyst actually uses. It also means lessons 02, 03, 04, 06 and 07 now carry **two** field vocabularies, since a learner running Zeek locally sees native names and the lesson shows Security Onion names.

That is defensible and honestly documented, but it is added extraneous load on lessons that already combine a new tool, new protocol content, and a new reasoning habit. If early runs show learners struggling in lessons 02–04, the field-name duality is a candidate cause and should be tested before the reasoning content is blamed.

> Confidence: **Low.** Speculative until someone runs it.

## Recommendations, ranked by value over cost

| | Change | Cost | Addresses |
|---|---|---|---|
| 1 | **Same task twice.** Have the learner do lesson 01's Case C at the start and again after the capstone, unaided both times, and keep both. No rubric, no score — just two artifacts to compare. | One paragraph | Finding 2 |
| 2 | **Opening recall prompt** on lessons 03–09: reconstruct something from an earlier lesson from memory before reading on. Closed book, thirty seconds. | ~10 lines each | Finding 1 |
| 3 | **Predict-then-check** in every lesson, as lesson 06 already does. | ~10 lines each | Findings 1, 5 |
| 4 | **Paired review** in the run protocol: two people review one work product independently, then compare. Disagreement is the finding. | Protocol note | Findings 2, 3 |
| 5 | **Stage evidence in one mid-course lesson** so revision-under-new-evidence is not capstone-only. Lesson 07 is the natural host. | Moderate rewrite | Findings 3, 5 |
| 6 | **Map the capability model to NICE Cyber Defense Analyst.** | ~1 day | Finding 7 |
| 7 | **Blocked-then-interleaved trial** — a mixed discrimination set after lesson 07. | New material | Finding 6 |

Items 1 through 4 are cheap, address the two highest-confidence findings, and none of them requires deciding anything the project has deliberately deferred. **None adds scoring, levels, or validity claims.**

## Research still needed

**On this project's own material** — none of it requires a literature review, and all of it beats more reading:

1. Run a lesson. Still the precondition for everything.
2. **Inter-rater reliability** on the capstone review guide: two reviewers, one work product, independently. If they disagree substantially, the evidence model does not yet discriminate, and that is the single most important thing to learn early.
3. **Change detection** via recommendation 1.
4. **Think-aloud** through lesson 02 or 06, to locate where load actually spikes rather than guessing.

**Literature the project has not consulted.** R001–R003 covered expertise development, analytical reasoning, and mental models. They did not cover:

1. **Spacing and retrieval practice** in procedural and judgment-heavy domains — the direct evidence for Finding 1, and the place where NADF's population differs most from the studied ones.
2. **Self-explanation prompt design** — cheap to add, moderate support, directly relevant to Finding 3.
3. **Performance-assessment reliability** — how comparable judgments of open-ended work products are made without collapsing into rubric scoring. Bears on whether EF families can ever discriminate.
4. **Transfer** — the stated goal of lesson 09 and the thing the whole architecture is for, with exactly one exposure and no literature behind the design of that exposure.
5. **Any published outcome data on SOC or network analyst training.** R002 already flagged that network-specific evidence is thin. If it is genuinely absent, that is worth knowing and stating, because it means NADF's design rests on transfer from adjacent domains — which is defensible, and which should be said out loud rather than left implicit.

## What this review does not establish

It reviews design against literature. It contains no evidence about whether NADF works, because none exists yet. Every finding here is a prediction about what will matter, and predictions from design review are exactly the kind of claim the lessons themselves teach learners to hold loosely.

The first real run may show that none of this is the binding constraint.

## Sources

- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). *Improving Students' Learning With Effective Learning Techniques: Promising Directions From Cognitive and Educational Psychology.* Psychological Science in the Public Interest, 14(1), 4–58. Utility ratings cited above are from this monograph: practice testing and distributed practice rated high; elaborative interrogation, self-explanation and interleaved practice rated moderate; summarization, highlighting, keyword mnemonic, imagery for text, and rereading rated low.
- NICE Framework Cyber Defense Analyst work role, published via NICCS and the DoD Cyber Workforce Framework. Note that the taxonomy moved from KSAT to TKS (Tasks, Knowledge, Skills) in the current revision.
- NADF's own [R001–R003 reconciliation](2026-07-11-r001-r003-reconciliation-provenance-recovery.md), particularly conclusions PC-02, PC-03, PC-04, PC-07, PC-08 and PC-09.

Secondary summaries were used to locate the Dunlosky utility ratings; the monograph itself was not read in full for this review. Treat the ratings as correctly attributed and the surrounding interpretation as this reviewer's.
