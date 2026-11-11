# R012: Spatial memory, recall with a check, and live-session design

**Status:** candidate · **Date:** 2026-11-11 · **Adapts:** "Cognitive & Spatial Technical Learning Architecture" (Charles Warloe, Google Drive, 2026-11-09)

This record adapts the maintainer's own field guide for technical training into this project's rules. The guide's full text and its reconstructed bibliography are archived, unedited, in learning-narrative-kit at [`research/memory-palace-spatial-learning/`](https://github.com/cwarloe/learning-narrative-kit/tree/main/research/memory-palace-spatial-learning). Read the original there. This record keeps only what survives comparison with [R005](R005-instructional-design-review.md), [R006](R006-literature-scan.md), [R008](R008-longitudinal-judgment.md), [R009](R009-reviewer-agreement.md), and the [Standing Qualifications](../architecture.md#standing-qualifications).

**The headline is that most of the guide agrees with what this project already does, and the parts that go further are either weakly supported or need a check added.** Four points needed a decision. The maintainer made them on 2026-11-11, and they are recorded below as the terms on which anything from the guide may enter a lesson.

## Provenance

- **The guide has no reference list.** It names Sweller and Paivio and a set of effects (method of loci, split attention, generation and retrieval, demonstration-performance, the "hollowed mind"). The archive's [`sources.md`](https://github.com/cwarloe/learning-narrative-kit/blob/main/research/memory-palace-spatial-learning/sources.md) reconstructs 58 sources those names point to, plus studies that test or qualify the guide's claims. Source numbers below ("LNK #6") refer to that file.
- **What "verified" means there.** The bibliographic record was confirmed against Crossref, arXiv, ERIC, Open Library, ADS, or the publisher. The full texts were not read. Effect sizes come from published abstracts. Bower (1970) is listed in the archive with a confirmed record but no DOI. It is not relied on here.
- **The comparison behind this record** was a read of this repository's R001 to R010, the evidence index, and the [technical-training-design skill](../../skills/technical-training-design/SKILL.md) against the guide, done 2026-11-10. It is interpretation, not new evidence about NADF.
- **The archive also carries [errata](https://github.com/cwarloe/learning-narrative-kit/blob/main/research/memory-palace-spatial-learning/errata.md)** for two of the guide's protocol metaphors (TCP RST and TLS SNI). Those corrections apply here.

## What the guide claims that this project does not carry

The guide says an AI-free final test shows that a learner is operationally competent, that a learner who fails it has not consolidated the underlying schema, and that its "integrity gate" secures durable learning. None of that carries over. [R009](R009-reviewer-agreement.md) and the Standing Qualifications are explicit: without a validated instrument nothing here can say that anyone has reached a level. An AI-free check shows what one learner did unaided on one task on one day. It is evidence for a reviewer to look at, not a verdict about the learner.

The guide's neuroscience explanations are also left out. "Retrieval consolidates fragile hippocampal engrams" and "physical movement reinforces associative neural pathways" are not established mechanisms (the archive found no source for either), and the teaching moves they decorate stand or fall on behavioral evidence alone.

The "10-minute attention span" is not used anywhere in this record as a reason for anything. Reviews of that claim find little support for it (LNK #44, #45).

## The four decisions

### 1. The memory palace is optional and only for ordered sequences

Use a fixed-position aid only where learners must recall things in order: layer order, the steps of a handshake, the order of a checklist. Build it on a plain labeled diagram, never on a story setting or a fictional workplace. End the unit with problems that do not use the diagram.

**Why.** The method of loci reliably helps people remember ordered lists. A meta-analysis of 13 trials found a medium effect on recall (g = 0.65), but most trials carried a high risk of bias (LNK #6), and a larger review found strong evidence of publication bias that shrinks the effect after correction (LNK #7). Nobody has tested it as a way to understand or transfer how a system works, which is what this course teaches. The repository's own transfer guidance points the other way for that goal: hold the deep structure constant and vary the surface hard ([skill](../../skills/technical-training-design/SKILL.md); [R006 §6](R006-literature-scan.md#6-transfer--the-capstone-is-attempting-the-achievable-kind-once)). Concrete detail has to fade toward an abstract rule, or the learner keeps the setting and loses the idea. A plain labeled diagram is already a step along that fade. A story world is not.

The guide's laminated desk "placemat" is really a labeled layer diagram, so it fits this rule once it stops being mandatory. A persistent course map has its own modest support as an advance organizer or concept map (LNK #57, #58), separate from the loci literature.

> Confidence: **Moderate** that loci help ordered recall, with the bias caveats above. **Unknown** for understanding systems. This record does not claim that a fixed diagram helps NADF learners; it permits one where order is the thing being learned.

### 2. Every recall exercise ends with a check against the source

The learner recalls or sketches first, without notes or AI. Then they open the reference (a diagram, a capture, the lesson text), mark what they missed or got wrong, and fix it. The guide's closed-notebook sketch drill is kept in this form only.

**Why.** [R006 §2](R006-literature-scan.md#2-retrieval-practice--supported-with-a-caveat-that-lands-directly-on-nadf) found retrieval least reliable for rules and procedures and strongest when feedback is given, and demoted a bare closed-book prompt to fifth place. The meta-analyses in the archive agree that feedback enlarges the testing effect (LNK #29, about g = 0.50; LNK #30, about g = 0.61). A sketch checked against a reference is predict-then-check, which R006 put first. Drawing from memory has its own recall benefit (LNK #34), so the sketch is worth keeping once the check is attached.

> Confidence: **High** on the effect of retrieval with feedback. **Low** for recall with no check on procedural material, which is why the check is required.

### 3. 10 / 25 / 15 is a per-hour guide, not a rule

For live, instructor-led sessions only: plan about 50 minutes of work and a break each hour. Within the hour, up to about 10 minutes of explaining and demonstrating, about 25 of guided practice with the instructor moving around and giving feedback, and about 15 of solo practice and review that ends in a check against the source. Across several hours or several concepts, apply the ratio loosely, hour by hour. The break each hour is the part to keep fixed.

**Why.** The reason is task sizing, not attention. The demonstrated task has to be small enough that a novice can do it right after seeing it. Experts underestimate how long that takes: a task an expert demonstrates in about 3 to 5 minutes may take a novice 9 to 12. Capping the demonstration keeps the expert honest about novice time and leaves most of the hour for practice. The instructor is a guide on the side who coaches at the learner's elbow, not a lecturer at the front, even though some explaining and demonstrating is always needed.

The direction is well supported. Active learning beat lecture on exams and failure rates across 225 studies (LNK #46), and the show, then guided, then solo order matches worked examples followed by fading guidance (LNK #36, #37; [skill](../../skills/technical-training-design/SKILL.md), three rungs per unit). The minute counts are not supported by any source the archive found. They are the maintainer's practitioner judgment, stated as such. The expert-versus-novice time gap is also the maintainer's estimate, not a measured figure.

This applies to instructor-led delivery. NADF lessons are mostly self-paced, so it does not change the lessons themselves.

> Confidence: **High** that short demonstration and mostly practice beats lecture. **Unknown** for the specific minutes, because no source was found; treat them as a planning heuristic.

### 4. A vivid metaphor must carry the mechanism and say where it breaks

Allow a mechanical or physical metaphor only when it works the way the real process does. Every metaphor gets one line stating where the comparison stops matching. Cut metaphors that only add color.

**Why.** Analogies teach when they map relations rather than surface features (LNK #42), and they plant misconceptions unless the teacher shows where they break (LNK #43). Interesting but irrelevant material reduces learning while readers rate it higher ([skill](../../skills/technical-training-design/SKILL.md), seductive details). The guide's spring-loaded valve for the TCP sliding window carries the mechanism. Its brake-cord picture of a TCP reset overstated the effect and is corrected in the archive's errata: a reset ends that one connection, not every session on the host. Each metaphor needs a technical check before it reaches a lesson.

> Confidence: **Moderate.** The misconception risk is well documented; how much a given metaphor helps is not.

## What else is worth keeping

These extend what the repository does without conflicting with it. Each is a candidate for a lesson, not a commitment.

| Idea from the guide | Adapted form | Evidence as the sources rate it | Where it is weak |
|---|---|---|---|
| Put labels on the diagram, not in a legend | Label each field or node on the picture itself; drop separate legends | **Strong.** Integrated text and diagrams beat separated ones, g = 0.63 across 58 comparisons (LNK #21, #22) | Labels the learner already knows become clutter (expertise reversal, LNK #16) |
| "Replace text with moving models" | Pair words with a labeled static diagram; animate only change over time that must itself be learned | **Strong** for words plus pictures (LNK #23). **Weak to moderate** for animation over a still image (LNK #24, #25) | The guide's "replace" is not supported; the words stay |
| Few interacting elements at once | Introduce header fields and flags singly before a live capture | **Strong** for the principle (LNK #13, #15) | The guide's "cognitive failure" past a fixed count is overstated |
| Audit a flawed AI-written answer | Give learners a plausible AI-written analysis with planted errors after guided practice; they find, explain, and fix them, then see the key | **Moderate.** Erroneous examples help mainly learners with prior knowledge (LNK #50); errors help when corrective feedback follows (LNK #51) | Too early, it confuses novices. Always reveal the key. A natural fit for [lesson 07](../../lessons/07-when-its-suspicious.md) or [lesson 08](../../lessons/08-judgment-and-handoff.md), untested there |
| AI-free practice | Keep starting tasks without search or AI, as [lesson 00](../../lessons/00-baseline-alert.md) already does | **Emerging,** resting mainly on one field experiment: unguarded GPT-4 raised practice scores and lowered later unaided exam scores, and a tutor-style version removed most of that harm (LNK #55). Other studies are a small preprint and self-report surveys (LNK #53, #54, #56) | Shows what a learner did unaided once. It is not a measure of the learner |
| Coach with questions, hands off the keyboard | In live sessions, ask where, what, and which tool instead of answering or taking over | **Moderate** for prompting over telling (LNK #47, #48) | The keyboard rule and the guide's 45-second visit limit have no source; short visits must not mean no help |

The supporting AI-and-learning summary in [`ai-and-cognitive-decline-synthesis.md`](ai-and-cognitive-decline-synthesis.md) carries more detail on the AI studies, with its own provenance note.

## What this record does not establish

Nothing here is evidence about NADF learners. It is evidence about conditions under which these techniques tend to work, applied to this project by argument, the same limit [R006](R006-literature-scan.md#what-this-scan-does-not-establish) states. The archive confirmed citations and read abstracts, not full texts, so the effect sizes are as reported in those abstracts. The minute counts, the expert-versus-novice estimate, and the coaching rules are practitioner judgment. No technique in this record supports a claim that a learner has reached any level.

## What would change this view

A study of fixed-position aids for understanding (not just recalling) technical systems would reopen decision 1. A trial in this course comparing a recall-then-check opener against no opener would show whether decision 2 earns its time. If learners in live sessions routinely cannot do the demonstrated task after seeing it, the demonstration is too large, which is the test decision 3 sets for itself.
