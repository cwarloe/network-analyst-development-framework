# Harrowmere before Ethan — Shared Organizational and Relationship Timeline v0.1

**Design rule:** Dates are relative to Ethan's arrival until technical/narrative continuity requires exact calendar dates. Most of this history is author-only. The organization should feel accumulated, not staged for training.

## Year -5: The environment begins accumulating the history Ethan will inherit

### H-01 — Nia moves from senior practitioner/team lead into security-operations management
Nia is still technically hands-on and initially continues solving the hardest incidents herself. The team rewards this because incidents resolve faster. This begins the “get Nia on the bridge” habit that later becomes a leadership dependency problem.

**Relationship effects:** Nia begins working closely with Priya on infrastructure-impacting incidents. Priya learns Nia will listen to consequence rather than demand visible action.

### H-02 — Priya helps lead a major multi-site network standardization
Harrowmere cleans up routing, segmentation, remote-site connectivity, and firewall policy after years of growth. The project succeeds and establishes Priya's reputation for deliberate design and disciplined change.

**Residual debt:** several “temporary” exceptions are carried forward because production cannot tolerate immediate cleanup. They are documented unevenly.

### H-03 — Leah becomes a key owner of Harrowmere's finance/inventory integration ecosystem
A patchwork of ERP, file exports, scheduled jobs, service accounts, internal APIs, vendor SaaS, and warehouse integrations becomes her responsibility. She begins building the institutional workflow knowledge no topology diagram fully contains.

**Relationship effect:** Priya and Leah become regular collaborators because almost every application change has network consequences and almost every network change has application dependencies.

## Year -4: Trust forms through ordinary failures, not dramatic breaches

### H-04 — The “retired” integration that was not retired
A legacy finance/warehouse integration believed to be decommissioned wakes after a primary workflow failure. It makes unexpected outbound connections through a dormant fallback path.

Leah initially says the integration no longer exists. Priya says the old path should not be reachable. Telemetry proves both assumptions incomplete.

**Lessons carried forward:** inactive ≠ nonexistent; intended retirement ≠ executable removal; configuration/documentation can both be stale.

**Relationship effect:** Priya and Leah become more willing to say “that's what I think” rather than “that's what is.”

### H-05 — Owen joins Harrowmere
Owen arrives with strong network/infrastructure experience and quickly becomes useful during messy operational cases. His ability to collapse a problem with one discriminator earns trust from Nia, Priya, and Leah.

**System effect:** “Ask Owen” starts becoming a legitimate shortcut.

### H-06 — Owen and Priya resolve the first major path/behavior disagreement
Priya's architecture indicates one path; captured traffic shows another. They discover a failover/exception path inherited from H-02's standardization work.

**Relationship effect:** They learn to disagree safely. “Configured” and “observed” become distinct concepts in their shorthand.

### H-07 — Nia's first clear indispensability warning
A high-pressure incident resolves quickly only after Nia takes over. Everyone praises the result. Months later a similar case stalls while she is unavailable.

**Private realization:** Nia solved the first incident but preserved the system that made her necessary.

## Year -3: Dana's formative error and the team's epistemic culture begin changing

### H-08 — Dana arrives or becomes the recognized senior analytical lead
Dana is already technically strong and develops a reputation for separating observation from explanation. She and Owen respect one another quickly but have visibly different reasoning tempos.

### H-09 — The Dana/Nia formative analytical error
A technically familiar pattern appears during an ambiguous event. Dana develops a coherent explanation, searches within it, and communicates it with more confidence than the evidence warrants. Nia makes a reasonable operational decision based on Dana's stated confidence. Later evidence materially changes the explanation.

**Not a catastrophe.** The event matters because the process was almost good enough to hide the epistemic flaw.

**Dana learns:** the better her explanation, the more disciplined testing must become; confidence changes other people's justified actions.

**Nia learns:** uncertainty belongs in the decision package, not in the analyst's private head.

**Relationship effect:** their trust increases because both revise rather than blame.

### H-10 — “Enough to act?” becomes shared language
Dana and Nia begin explicitly separating “enough evidence to do X” from “enough evidence to claim Y.” This becomes part of Harrowmere's emerging analytical culture.

### H-11 — Owen's answer-provider status hardens
Nia repeatedly uses Owen for hard cases because it works. Junior staff learn to bring ambiguous problems to him. Owen explains answers, often well, but his invisible reasoning remains invisible.

**Latent problem:** organizational performance looks stronger than capability distribution actually is.

## Year -2: Cal changes what Harrowmere can observe—and exposes new failure modes

### H-12 — Cal joins or moves into security engineering
Cal improves telemetry, Security Onion pipelines, enrichment, and analyst tooling. Owen and Cal quickly form the “this is annoying; automate it” partnership.

### H-13 — The first celebrated automation
Cal automates repetitive enrichment that analysts previously performed manually across several systems. It saves real time without replacing judgment.

**Important author rule:** This success is why Cal's automation optimism is rational, not caricatured.

### H-14 — The noisy production detection
A rule that works beautifully in development floods production because legitimate Harrowmere behavior shares the target shape.

Cal and Owen tune it aggressively. Alert volume drops dramatically.

### H-15 — The tuning miss
Later review finds a meaningful case was also suppressed by the tuning. No disaster is required; the lesson is enough.

**Cal learns:** lower alert count is not automatically better detection; false negatives are less visible than false positives.

**Dana/Cal relationship:** Dana increasingly asks what a detection actually establishes before Cal operationalizes it.

### H-16 — Priya and Cal discover a sensor-placement blind spot
A sensor was placed where “most” traffic passed, but failover moved traffic elsewhere during an operational event. Harrowmere briefly possessed confident telemetry about only one path.

**Shared lesson:** observability has topology; redundancy must be considered in sensor design.

## Year -1: Organizational memory, metrics, and application context become explicit problems

### H-17 — Leah and Cal's silent integration degradation
A vendor API changes. A security/application integration continues running successfully but quietly stops returning one category of data. No obvious alarm fires because the process itself remains green.

**Lesson:** a system can fail by continuing to operate while producing incomplete information.

**Relationship effect:** Leah begins asking “who owns this eighteen months from now?” when Cal proposes new integrations.

### H-18 — The security-effectiveness dashboard
Leadership reasonably asks whether security operations are improving. Cal helps construct metrics such as alert volume, closure time, backlog, detection count, and automated triage.

The dashboard is useful at first.

Over time, teams begin adapting behavior to improve the measures: quicker closure, noisy-rule suppression, more easily counted automations, more detection rules.

No one cheats. The measurement system shapes behavior.

**Nia notices first organizationally; Cal notices technically.** They begin distinguishing activity metrics from capability/effectiveness questions.

### H-19 — Leah's month-end normalization error
A large transfer occurs during a known month-end workflow. Leah contextualizes the timing correctly but overextends the context to explain magnitude. Later they discover duplicate/runaway processing.

**Lesson:** context can explain one dimension while leaving another anomalous.

### H-20 — Owen's old workaround returns as technical debt
A successful historical workaround remains in practice after its rationale disappears. An upgrade changes the surrounding assumptions and the workaround becomes harmful.

Owen hears his own name used as justification: “We leave that disabled because Owen said so.”

**Lesson:** a correct fix without preserved reasoning becomes cargo cult.

## Months -9 to -3: The team begins intentionally changing how expertise is distributed

### H-21 — Dana pushes mentoring from answer transfer toward reasoning visibility
Dana starts asking Owen and others to distinguish when a junior needs a factual answer from when the junior needs to construct the reasoning. Owen initially sees some of this as unnecessary slowing.

### H-22 — Owen's first deliberately bad imitation of Dana
A junior asks a factual question. Owen answers, “What do you think?” The learner clearly does not have the reference knowledge.

Dana later points out that questions are not inherently good teaching.

**Team learning:** Tell / Retrieve / Ask / Model / Let struggle / Intervene begins to emerge informally as a useful distinction.

### H-23 — Nia changes assignment language
Instead of “Owen, take it,” she increasingly says, “You own it; Owen is available.”

This produces some short-term inefficiency but begins reducing answer dependency.

### H-24 — Priya starts using telemetry as design verification
After several configured-vs-observed discrepancies, Priya begins proactively asking analysts to confirm whether traffic actually used the intended path after selected changes.

**Development:** observability begins moving from security add-on toward infrastructure design feedback.

### H-25 — Leah begins treating analyst telemetry as application feedback
Unexpected network behavior reveals recurring application behavior that application monitoring did not expose. Leah increasingly sees security/network analysts as collaborators who can teach her about her own platform.

## Page-one-minus-weeks: The state Ethan inherits

### H-26 — Harrowmere is competent but imperfect
The organization is not broken and not a model shop. It has:
- generally good change discipline with legacy exceptions;
- useful telemetry with known and unknown gaps;
- experienced people with institutional knowledge;
- application workflows more complex than their documentation;
- security tooling that genuinely helps and occasionally misleads;
- metrics that answer some questions and tempt broader conclusions;
- technical debt produced by formerly sensible decisions.

### H-27 — Dana and Nia agree the next analyst should be developed differently
They do not design Ethan as an experiment. Rather, prior experience has convinced them that Harrowmere needs analysts whose reasoning is inspectable and transferable, not merely people who can memorize tools or depend on senior practitioners.

### H-28 — Owen is still the easiest shortcut
The developmental culture has begun changing, but “ask Owen” still works. This is exactly why Ethan will be tempted by it.

### H-29 — Priya, Leah, and Cal already know their own domains are incomplete views
They have all been burned by confusing intent, configuration, instrumentation, or context with reality. None has fully eliminated the habit.

### H-30 — Ethan arrives into a living system
The organization already contains old jokes, known exceptions, half-forgotten incidents, successful migrations, scars, trust patterns, dashboards, workarounds, and unresolved debts.

He initially interprets that accumulated expertise as: **these people know everything.**

Book 1 gradually teaches him the opposite, more useful truth:

> **These people know how to construct reality together without pretending any one of them possesses it.**

---

# Page-one author state (seed for next Snowflake pass)

- **Ethan:** wants to prove he belongs; assumes expertise = immediate answers.
- **Dana:** intends to develop reasoning but knows she can over-question and has her own pattern biases.
- **Nia:** wants independent analysts while still operating under real clocks; she helped create the answer-provider culture she now wants to change.
- **Owen:** genuinely likes Ethan and will instinctively solve things for him.
- **Priya:** sees a smart novice with vocabulary but not yet the map underneath it.
- **Leah:** expects another security analyst to ask her whether something is “normal” as though normal were a field she can fill in.
- **Cal:** recognizes someone likely to be overimpressed by dashboards and tools because Cal once was too.

## Active organizational debts at page one

1. Some legacy path/configuration exceptions from prior standardization remain.
2. Application integrations contain historical behavior no single current diagram captures.
3. Observability coverage is materially useful but not complete.
4. Security metrics have begun influencing behavior and need continued scrutiny.
5. Owen remains a significant bus-factor/tacit-knowledge concentration.
6. Dana's mentoring method is strong but not yet a standardized or perfected teaching system.
7. Harrowmere has good practitioners but no omniscient source of truth.

---

# Next Snowflake work

1. Expand **page-one world state** into a full matrix: what each character believes about each other, active tensions, current systems, current technical debts, and what each calls “normal.”
2. Convert the existing 14 instructional episodes into a true **Book 1 story snowflake** with escalating narrative causality, reversals, relationship changes, and climax—not merely lesson-adjacent fiction.
3. Build character-arc matrix across major story movements.
4. Build episode/scene cards.
5. Only then write substantial prose.


---

