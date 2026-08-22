# R008 — How other fields teach judgment across time

**Status:** assessed · **Date:** 2026-08-20 · **Prompt:** [`prompts/R008-longitudinal-judgment.md`](prompts/R008-longitudinal-judgment.md)

[R005](R005-instructional-design-review.md) found the architecture has no time dimension. [R007](R007-nice-role-mapping.md) found the NICE role's trend, posture and continuous-monitoring statements have no NADF counterpart. Same gap, two unrelated methods. This asked how other fields solve it.

The brief came back with more usable structure than expected, and one recommendation this record declines.

## Provenance

Commissioned from an external research model against the committed prompt, returned 2026-08-20. Findings and citations below are as supplied; the interpretation, the convergence analysis, and the disagreement in the last section are this project's.

**Not independently verified.** Sources were not read. The strongest claims — the medical continuity evidence and the perceptual-training effect sizes — are the ones worth checking before anything expensive is built on them.

## What the fields actually do

| Field | Structure | Evidence strength |
|---|---|---|
| **Medicine** | Longitudinal integrated clerkships — same patients, same supervisors, months. Also 3–4 visit simulated longitudinal cases | **Strongest available.** LIC students meet or exceed block-rotation students on knowledge and skills, with better tolerance of uncertainty. Kirkpatrick levels 2–3. A dose–response pattern: more continuity, stronger effect |
| **Aviation** | Line-Oriented Flight Training — one 3–4 hour session, multiple legs, evolving conditions | Attitude change (L2) and observed behaviour change in simulators and line audits (L3). Accident rates too rare for causal attribution |
| **Meteorology** | Continuous forecast verification against outcomes, fed back to forecasters | Observational but long-run: human forecasters beat models by 20–40% on some thresholds across decades, partly attributed to verification feedback |
| **Quality control** | Control charts, trend rules, CUSUM/EWMA for small sustained shifts | Method mathematically validated. **Training-effect evidence much weaker** |
| **Audit** | Analytical procedures across periods, required by standards | Institutionalized and regulator-backed. Training research sparse |
| **Process safety** | HRO practice, precursor and near-miss analysis, normalization-of-deviance case work | Rich conceptually. A 2023 systematic review found **no empirically tested interventions** |

### The cognitive question, answered better than expected

Detecting gradual change is genuinely hard — change blindness is worst when transitions are slow, because motion cues are absent, and the task requires encoding, holding, comparing and deciding, each of which can fail under load.

But it is trainable, in several sensory domains, at modest dose:

- Perceptual training cut just-noticeable differences by roughly half, with measurable change in early visual cortex.
- Auditory change-detection training with feedback improved sensitivity, **reduced the "nothing changed" bias**, and generalized to novel stimuli.
- Seven days of visual change-detection training produced ~50% improvement with transfer to other visual tasks.

That middle finding is the interesting one for this project. The bias being corrected — defaulting to *nothing has changed* — is the same disposition lesson 06 attacks when it teaches that fragment loss leaves no trace shaped like a fault, and lesson 03 attacks when it shows a TTL running backwards is normal.

## Where this converges with what the project already found

Three of the brief's five recommendations restate findings this project reached independently. That is worth stating plainly, because agreement across unrelated methods is the only external corroboration available.

**The verification tracker is [R006](R006-literature-scan.md)'s top two recommendations, unified.** R006 ranked *predict-then-check* first because it is retrieval with feedback built in, and *same task twice* second because nothing else could detect that a learner improved. The brief's cross-lesson judgment log — record the decision, record the confidence, record the expected time horizon, reveal ground truth later, accumulate a personal hit-and-miss record — is both of those at once, running across the whole course instead of inside one lesson. It is strictly better than either, and it comes from meteorology rather than from learning science.

**Multi-episode conversion is what the capstone already does.** Staged evidence, a revision task, an explicit instruction to compare the initial and revised models. R006 recommended a second transfer exposure before the capstone; the brief recommends the same move, and describes the capstone's own structure while doing it.

**No cybersecurity evidence exists.** The brief could not find studies evaluating longitudinal judgment training for SOC analysts, and notes that cyber training research measures point-in-time detection accuracy and response time. That matches [R006](R006-literature-scan.md)'s finding exactly, from a different search. Two independent scans failing to find the same literature is reasonable grounds to believe it is not there.

## One recommendation this record declines

The brief recommends short change-detection micro-drills — dashboard pairs with subtle differences, ten to twenty trials, immediate feedback.

**Its own Part 4 undercuts it.** The transfer question — whether low-level perceptual gains reach complex analytic judgment under domain load — is listed as *plausible but not experimentally verified*. The evidence cited is contrast discrimination, auditory flicker tasks, and visual conjunction search. None of that is reasoning about whether a beacon is malicious.

It also fights the architecture. The [capability model](../capability-model.md) states that capability means integrated performance, and that tool speed, command recall and interface familiarity are not substitutes for conceptual understanding. A decontextualized spot-the-difference drill is closer to the thing that model excludes than to the thing it measures. NADF could add it and would then be doing exactly what it tells learners not to do: acting on a shape that resembles the target rather than evidence that it is the target.

Recorded as the lowest priority, and if ever built, labelled as an unvalidated transfer bet rather than as capability development.

## What the project already has and did not notice

The brief's first recommendation is to establish a persistent environment appearing across several incidents. **Much of it already exists by accident:**

- `files.contoso-internal.example` is the same host in [lesson 02](../../lessons/02-reading-a-conversation.md) and [lesson 04](../../lessons/04-what-encryption-hides.md) — a plaintext API conversation, then the same service over TLS.
- Contoso appears in 02, 04 and 07, including as the certificate's organization.

> **Naming note, 2026-08-22.** The fictional company was renamed from Contoso to Harrowmere Equipment Group, and the host is now `files.harrowmere-group.example`. The continuity finding above is unchanged — it is the same host in the same two lessons — and the record is left as written rather than retrofitted.
- Portland recurs in 01, 04 and 05; Denver anchors 08.

So the recommendation is not *create continuity* but *stop hiding the continuity that is there*. Lesson 04 could say outright that it is the same service lesson 02 read in the clear, which makes the encryption point land harder — you watched this conversation, and now you cannot. That is close to free and it strengthens an existing lesson rather than adding one.

The capstone breaks the pattern with AcmeSync, and that is probably correct: a capstone testing transfer should not reuse the environment the course rehearsed in.

## The dose question is open and matters

Medicine shows a dose–response relationship — more continuity produces stronger effects — but **no minimum episode count is established**, and the short simulated versions report self-rated confidence rather than measured performance.

The minimum viable design would give NADF two multi-episode conversions out of nine lessons. Nobody knows whether two is enough to develop anything. That is an assumption, and it should be recorded as one rather than designed around.

A related finding cuts the same way: aviation fatigue training produced attitude effects that **decayed within weeks without reinforcement**. Whatever this course changes in a single sitting is unlikely to persist unreinforced — which is an argument for recurrence that R006 demoted on different grounds.

## Revised recommendation order

Merging R006's list with this one. Everything still waits on the first run.

| | Change | Source | Cost |
|---|---|---|---|
| 1 | **Make the existing continuity explicit.** Lesson 04 names the host lesson 02 already read | R008, and already half-built | Two sentences |
| 2 | **Cross-lesson judgment log with verification.** Decision, confidence, expected horizon; ground truth revealed later; personal hit-and-miss record accumulates | R008 + R006 #1 and #2 unified | ~5 min per lesson |
| 3 | **Convert one or two incidents to multi-episode**, with an explicit revisit-your-own-judgment step | R008 + R006 #4 | Moderate rewrite; costs breadth |
| 4 | **SPC-style trend tasks** — a small time series, one or two trend rules, investigate-or-monitor, immediate feedback | R008, genuinely new | ~5–10 min in 3–4 lessons |
| 5 | **Paired review with the bar set first** | R006 #3, awaiting R009 | Protocol note |
| 6 | **Closed-book recall prompts** | R006, demoted there and still demoted | ~10 lines each |
| 7 | *Change-detection micro-drills* | R008, **declined above** | — |

Item 4 is the only one that adds a genuinely new capability rather than restructuring what exists. It is also the one whose training-effect evidence is weakest, which is an uncomfortable pairing worth naming.

## What this does not establish

A literature scan by a model, unverified against sources. No evidence about NADF. The brief's own strongest caveat is that no field has demonstrated this for cybersecurity, so every structure here is borrowed across a domain boundary on the argument that the underlying judgment is similar — which is precisely the kind of transfer claim [lesson 09](../../lessons/09-capstone-encrypted-outbound-traffic/README.md) teaches learners to be careful about.
