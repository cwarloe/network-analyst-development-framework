# Book 1 — Learning to See

This is the working architecture for turning the current nine-lesson course into a longitudinal 14-episode first book. It does not supersede the written lessons. They remain usable now and are the technical source material from which the book will be built.

Book 1 is complete when a learner can take a bounded unfamiliar network-analysis problem, frame the question, explain expected behavior, make and check predictions, select evidence, compare explanations, revise a model, reach a proportionate judgment, and hand off work another person can use. It does not claim mastery or cover all of network analysis.

The active [capability model](docs/capability-model.md), [evidence model](docs/evidence-model.md), and the Standing Qualifications in [the architecture baseline](docs/architecture.md) still govern claims and exercise design.

## The recurring move

Across the book, the learner repeatedly performs:

> Observe → Explain → Predict → Check → Revise → Decide → Reflect

The narrative creates a consequential problem and the desire for a better model. The lesson names, explains, and tests that model. The exercise produces inspectable evidence of performance. Model revision happens throughout the book rather than appearing for the first time in the capstone.

The story and lesson do not need a mechanical one-chapter/one-lesson rhythm. An episode may put prediction before instruction, interrupt a case with practice, or return to a prior work product. The technical lesson must remain usable without the fiction.

## Primary learner and accessibility

Book 1 is paced for a learner like Ethan: an experienced general-IT practitioner entering a first dedicated analysis role, with broad but uneven networking or cybersecurity knowledge from certification study, self-study, workplace exposure, or a combination. No prior network-analysis experience or familiarity with the course's tools is assumed.

This is a design target, not an entry gate. A computer-confident learner with less IT or networking experience may still use Book 1 with optional, just-in-time support. Support may supply missing reference knowledge, technical models, representation mappings, or tool orientation; it must not supply the interpretation, prediction, judgment, or work product the episode is intended to develop. The narrative remains optional, so no required prerequisite may exist only in a narrative chapter.

## Persistent environment and cast

The story takes place at **Harrowmere Equipment Group**, a multi-site manufacturer and distributor of industrial equipment. Recurring hosts, services, domains, changes, owners, sensor locations, retention limits, and known gaps accumulate history rather than resetting between episodes.

- **Ethan Mercer** is a 27-year-old developing analyst with several years of civilian IT support experience and broad but uneven certification/self-study knowledge. He initially believes experts know more answers. His Book 1 development is learning to construct trustworthy, correctable judgments.
- **Dana Shah** is the senior analyst who mentors Ethan. She tells when reference knowledge is missing, directs retrieval when finding reliable information matters, models invisible reasoning when needed, and asks when the reasoning itself is the learning target. Her help fades until Ethan supplies his own questions and checks.
- **Nia Alvarez** is the Security Operations Manager. She owns priority, escalation, and operational decisions and needs consequence, cost, uncertainty, and recommendation rather than packet exposition.
- **Owen Kline** is an experienced analyst whose speed rests on compressed experience and Harrowmere history. He provides comparison and practical discrimination without becoming a rival or second mentor.
- **Priya Raman** is the Senior Network Engineer. She supplies paths, policy, infrastructure intent, and change history, but not the whole analytical answer.
- **Leah Moreno** is the Enterprise Applications Lead. She supplies application and system purpose, expected workflows, dependencies, and business consequences that packets cannot provide.
- **Cal Rowan** is the Security Engineer. He owns significant parts of the telemetry, detection, search, and automation machinery that determines what evidence analysts can retrieve.

These are instructional functions as well as character functions. Their organizational roles are author canon; information advantages and limitations may deepen in prose, but the roles should not drift to satisfy an individual scene.

## Author knowledge and reader knowledge

The author may know the real cause of an incident, why Dana chooses an intervention, what a character has not disclosed, and which later evidence will overturn Ethan's model. Ethan and the reader may use only the evidence available at that point.

Backstory is author knowledge unless it earns space by affecting an analytical decision, assumption, relationship, or longitudinal consequence. A conclusion is reviewed against the evidence then available, not the hidden answer.

## Episode architecture

### Part I — What an analyst does

#### 1. The Word in the Ticket

- **Ethan:** eager, fact-heavy, and equating expertise with rapid recognition.
- **Problem/discomfort:** he reports that evidence shows “probing” when the word came from the ticket. Dana asks where the data says it.
- **Technical/capability target:** analyst purpose; analytical question; observation, interpretation, judgment, and recommendation; OE-2, IR-1, OE-1, CT-1.
- **Reuse:** the [prologue](narrative/00-prologue.md) and [lesson 01](lessons/01-what-the-analyst-is-for.md).
- **Build:** preserve the ambiguous miniature case; add an annotation exercise and one-paragraph assessment with traceable claim transitions; retain the work as the first portfolio artifact.
- **Payoff/continuity:** Dana revises one of her own inferences aloud. “Show me where the evidence says that” becomes a callback.
- **Deferred:** formal confidence, hypothesis comparison, and threat judgment.

#### 2. Who Is Talking to Whom?

- **Ethan:** more careful with labels but treating IPs, ports, and protocol names as explanations.
- **Problem/discomfort:** Leah asks whether an application reached its service. Ethan can name port 80 but cannot narrate the purposeful exchange. The existing capture is plaintext HTTP; encryption enters in Episode 6.
- **Technical/capability target:** hosts, services, ports, sessions, layers as reasoning aids; OC-1, OC-2, OE-1.
- **Reuse:** [lesson 02](lessons/02-reading-a-conversation.md).
- **Build:** map a diagram to a capture, narrate an exchange, and predict an event before reveal; vary the second exchange's surface details.
- **Payoff/continuity:** Ethan gives Leah an explanation she can recognize as system behavior. The application and hosts recur.
- **Deferred:** windowing, performance behavior, and deep TCP state analysis.

#### 3. Before You Look

- **Ethan:** able to explain completed exchanges but reasoning retrospectively.
- **Problem/discomfort:** Dana hides the next evidence and asks for a prediction. Ethan calls it guessing.
- **Technical/capability target:** model-derived prediction, assumptions, prediction/outcome comparison; IR-3, LR-1, early LR-2.
- **Reuse:** prediction prompts currently distributed through lessons 02–06.
- **Build:** staged reveals that preserve the learner's prediction, require an assumption check, and create a before/after revision trace. **Built:** [`lessons/e03-before-you-look/`](lessons/e03-before-you-look/README.md), on a new capture ([`e03-prediction.pcap`](assets/pcaps/e03-prediction.pcap)) rather than by consuming lesson 02's or lesson 06's cases.
- **Payoff/continuity:** Ethan learns that a checked wrong prediction is more useful than being unsurprised after seeing an answer.
- **Deferred:** formal hypothesis matrices and investigation plans.

### Part II — How normal systems behave

#### 4. Names Have Behavior

- **Ethan:** predicting simple exchanges but treating diagrams as directly observable sequences.
- **Problem/discomfort:** DNS activity is absent or differs by client despite the familiar resolution diagram.
- **Characters:** Dana and Priya contribute analytical questions and infrastructure context.
- **Technical/capability target:** resolver paths, caching, TTLs, repeated lookups, and legitimate variation; OC-2, OC-3, OE-1, LR-1.
- **Reuse:** [lesson 03](lessons/03-names-and-expectations.md).
- **Build:** client and resolver views, first/repeated lookup predictions, and a Harrowmere DNS baseline retained for later episodes.
- **Payoff/continuity:** missing packets stop meaning that a conceptual step did not occur.
- **Deferred:** DNSSEC, delegation depth, advanced anomalies, and longitudinal DNS analytics.

#### 5. Conversations Have Structure

- **Ethan:** understands purpose but reduces TCP to a handshake and a simple success/failure label.
- **Problem/discomfort:** refused, dropped, incomplete, and slow conversations all arrive as “it won't connect.”
- **Characters:** Owen, Priya, and Leah bring analytical, network, and application views; Dana makes Ethan locate the discriminating evidence.
- **Technical/capability target:** practical session states, refusal versus silence, response versus delivery, network versus application delay; OC-2, OC-4, OE-1, IR-3.
- **Reuse:** conversation material from lesson 02 and failure signatures from [lesson 06](lessons/06-when-it-breaks.md).
- **Build:** reuse REJ, S0, reset, and slow-but-correct cases; require the discriminating event or absence and a causal triage map.
- **Payoff/continuity:** Ethan resolves a network/application disagreement with evidence.
- **Deferred:** congestion control, windowing, transport tuning, and performance engineering.

#### 6. What Encryption Leaves Behind

- **Ethan:** oscillating between “encrypted means unknowable” and “valid certificate on 443 means legitimate.”
- **Problem/discomfort:** Harrowmere sees encrypted outbound activity and needs a bounded answer.
- **Characters:** Dana, Leah, and Cal; Nia may appear when the bounded answer reaches an operational decision.
- **Technical/capability target:** HTTP/TLS visibility boundaries, handshake metadata, timing, volume, names, certificates, context, and source limits; OC-2, OE-4, JU-2.
- **Reuse:** [lesson 04](lessons/04-what-encryption-hides.md) and selected capstone evidence patterns.
- **Build:** similar-looking encrypted exchanges in different contexts; observable/inferable/undetermined distinctions; a next-evidence request.
- **Payoff/continuity:** Ethan gives Cal a useful answer that names what cannot be known.
- **Deferred:** advanced fingerprinting, certificate ecosystems, interception, QUIC, and deeper encrypted-traffic analytics.

#### 7. Expected Does Not Mean Identical

- **Ethan:** wanting one crisp numerical template for normal.
- **Problem/discomfort:** he builds a baseline from too little history and flags expected business-cycle behavior.
- **Characters:** Nia, Priya, and Leah; Dana reviews rather than conducts.
- **Technical/capability target:** legitimate variation, peer groups, windows, schedules, recurring activity, and baseline limits; OC-3, OE-4, LR-1.
- **Reuse:** baseline and comparison material from lessons 03 and 07 and the capstone.
- **Build:** a small multi-day dataset with role and schedule variation, a misleading global average, and a baseline statement with assumptions.
- **Payoff/continuity:** Ethan corrects and improves the model instead of concealing the error. The baseline recurs.
- **Deferred:** seasonality, drift, statistical detection, and measurement strategy.

### Part III — Evidence and investigation

#### 8. Where Are You Standing?

- **Ethan:** treating each source as if it describes the complete event.
- **Problem/discomfort:** Priya's architecture, a capture, a firewall log, and an endpoint account appear to contradict one another.
- **Characters:** Priya, Cal, and Leah; Dana may review without supplying the reconciliation.
- **Technical/capability target:** sensor placement, vantage point, capture/flow/log/endpoint scope, retention, and distortion; OE-4, OC-4.
- **Reuse:** the vantage-point half of [lesson 05](lessons/05-vantage-point-and-evidence.md).
- **Build:** one event from at least three viewpoints, a source map, apparent contradictions resolvable through placement, and a durable source-limits ledger.
- **Payoff/continuity:** “not seen” becomes meaningful only after “could this source have seen it?”
- **Deferred:** NAT, proxies, asymmetric routing, clock correction, and multi-site reconstruction.

#### 9. Ask the Evidence a Question

- **Ethan:** aware of limitations but gathering broadly before deciding what each source must answer.
- **Problem/discomfort:** under time pressure he requests everything. Nia asks what decision the delay improves while Cal makes the collection costs and source limits concrete.
- **Characters:** Nia, Cal, and Dana; Priya or Leah appears only if the selected evidence requires their domain context.
- **Technical/capability target:** evidence relevance, provenance, decision value, collection cost, prioritization, and stopping; OE-3–OE-5, IR-4.
- **Reuse:** the evidence-planning half of lesson 05 and the capstone's mixed-source design.
- **Build:** a source catalog with costs/delays, shared-provenance traps, prioritized requests, expected decision changes, and stop conditions.
- **Payoff/continuity:** Leah begins using Ethan to shape an investigation. Dana reviews his draft instead of generating it.
- **Deferred:** forensic acquisition, large-scale collection, evidence governance, and automation.

#### 10. When the Expected Thing Does Not Happen

- **Ethan:** planning well but becoming attached to his first causal account.
- **Problem/discomfort:** intermittent DNS failures and unusual queries tempt a security explanation until a prediction fails.
- **Characters:** Nia, Priya, Leah, and Dana; Owen may contribute a fast historical comparison without taking ownership.
- **Technical/capability target:** causal models, policy/path effects, fragmentation and MTU at explanatory depth, visible revision; OC-4, IR-2, IR-3, IR-6, LR-1, LR-2.
- **Reuse:** fragmentation and causal material from lesson 06 and the capstone transfer case.
- **Build:** preserve the initial model, reveal contradictory evidence, require an explained revision, bounded correction, and verification. Do not reward guessing “MTU.”
- **Payoff/continuity:** Ethan catches the model failure before Dana points it out.
- **Deferred:** routing changes, NAT, asymmetric paths, and complex performance faults.

#### 11. More Than One Explanation

- **Ethan:** able to revise but comparing alternatives informally.
- **Problem/discomfort:** recurring outbound traffic supports approved-agent, misconfiguration, unwanted-software, and malicious explanations.
- **Characters:** Dana and Owen; Leah or Cal may contribute one bounded source or discriminator.
- **Technical/capability target:** competing explanations, discriminating predictions, investigation sequence, confirmation bias, and convergence; IR-2–IR-4, OE-5, LR-2.
- **Reuse:** reasoning from lessons 06 and 07.
- **Build:** an explanation/prediction/evidence matrix with ambiguous support, one high-value discriminator, and an evidence-driven ranking change.
- **Payoff/continuity:** Ethan notices a relationship Dana has not yet seen; she verifies it rather than acting as an oracle.
- **Deferred:** multi-day case management, formal analytic techniques, emulation, and complex timelines.

### Part IV — Judgment

#### 12. Suspicious Compared with What?

- **Ethan:** technically stronger but still feeling pressure from the word “malicious.”
- **Problem/discomfort:** beacon-like connections, high-entropy DNS, and an upload are individually ambiguous but relationally convergent.
- **Characters:** Nia, Owen, Leah, and Cal; Dana does not conduct the analysis and may only review afterward.
- **Technical/capability target:** beaconing, DNS channel characteristics, transfer shapes, peer/history comparison, legitimate analogues, convergence; OC-3, IR-2, IR-4, IR-5, JU-1, JU-2.
- **Reuse:** [lesson 07](lessons/07-when-its-suspicious.md).
- **Build:** preserve shape-similar legitimate and concerning beacons; require ranking, a proposed rule, false-positive analysis, cross-source linkage, and confidence.
- **Payoff/continuity:** Ethan avoids both indicator-first certainty and empty agnosticism.
- **Deferred:** hunting, detection design, campaign analysis, and adversary-specific tradecraft.

#### 13. What Can You Responsibly Say?

- **Ethan:** able to investigate but tempted to compress mixed evidence into one verdict.
- **Problem/discomfort:** 94% of authentication failures used a recently changed path, making the change a leading but unverified explanation; a 6% residue has different possible causes.
- **Characters:** Nia, with Dana deliberately distant and Leah present only if workflow consequence requires her.
- **Technical/capability target:** proportionate judgment, confidence basis and breaker, reversibility, cost of waiting, stopping points, role boundaries, and audience adaptation; JU-1–JU-4, CT-1–CT-4.
- **Reuse:** [lesson 08](lessons/08-judgment-and-handoff.md).
- **Build:** preserve the 94%/6% case; require separate judgments, a technical handoff, a manager summary, identical claim strength, gaps, action, and stopping condition.
- **Payoff/continuity:** Nia can decide and Leah can act without either receiving false certainty. Dana does not edit the products before delivery.
- **Deferred:** executive politics, governance, metrics, detection priorities, and leadership systems.

#### 14. Decide Before You Disrupt

- **Ethan:** a credible developing analyst ready to run the complete loop without live mentoring.
- **Problem/discomfort:** encrypted outbound traffic follows an authorized update. The initially reasonable benign account is later contradicted.
- **Characters:** Ethan leads; Leah, Priya, Owen, Cal, and Nia supply or consume bounded parts. Dana is absent during the core performance.
- **Technical/capability target:** integrated mixed-source analysis, staged evidence, visible revision, proportionate response, handoff, transfer, and targeted learning; all six domains.
- **Reuse:** the existing [encrypted outbound traffic capstone](lessons/09-capstone-encrypted-outbound-traffic/README.md).
- **Build:** adapt the case to Harrowmere; retain the evidence stop point, initial and revised assessments, shared-exposure reinterpretation, role-specific action, transfer task, and Episode 1 comparison.
- **Payoff/continuity:** Ethan changes his mind visibly, coordinates rather than exceeds his role, and identifies his next learning need without Dana manufacturing it.
- **Deferred:** the incident's origin and historical scope for Book 2; detection, automation trust, metrics, and organizational learning for Book 3.

## Guidance fade

| Episodes | Dana | Ethan |
|---|---|---|
| 1–3 | Stops closure, supplies the next question, models correction | Answers prompts and starts recording predictions |
| 4–6 | Asks for expectations and limits; supplies missing reference facts | Builds explanations but needs assumptions exposed |
| 7–9 | Reviews Ethan's draft models and plans | Arrives with context, model, and proposed next step |
| 10–11 | Waits; challenges after Ethan acts | Detects failed predictions and compares explanations |
| 12–13 | Available as reviewer, not conductor | Conducts and communicates; asks specific review questions |
| 14 | Absent during core performance | Runs the loop, revises, hands off, and identifies a learning need |

Other characters must not become substitute answer-givers. Each has partial knowledge or a real decision to make.

## Existing material map

| Current material | Book 1 use | Treatment |
|---|---|---|
| Prologue | Episode 1 | Adapt names and setting; preserve its analytical move |
| Lesson 01 | Episode 1 | Reuse substantially |
| Lesson 02 | Episodes 2–3 and 5 | Split conversation reading from prediction; retrieve later in failure analysis. Episode 3 is built and reuses none of lesson 02's evidence — see [the note below](#episode-3-evidence-note) |
| Lesson 03 | Episodes 4 and 7 | Reuse DNS model; extend baseline across time |
| Lesson 04 | Episode 6 | Reuse substantially; connect to recurring update environment |
| Lesson 05 | Episodes 8–9 | Split vantage point from evidence planning |
| Lesson 06 | Episodes 5 and 10 | Split observable failure signatures from causal model revision |
| Lesson 07 | Episodes 7, 11, and 12 | Seed baseline and alternatives; retain suspicious-traffic synthesis |
| Lesson 08 | Episode 13 | Reuse substantially |
| Lesson 09 capstone | Episode 14 | Adapt to Harrowmere and earlier continuity; preserve staged revision and transfer |

### Episode 3 evidence note

Episode 3 uses a new capture rather than lesson 02's or lesson 06's. Reusing lesson 02's conversations would have revealed that lesson's work product, and reusing lesson 06's failure cases would have consumed the fault taxonomy that lesson exists to teach. The Episode 3 capture contains **no faults at all** — all three conversations behave correctly — so the prediction work happens on ordinary traffic and lesson 06's subject stays intact.

New construction is concentrated in Episode 3's repeated prediction/revision, Episode 7's longitudinal baseline, Episode 8's multi-vantage evidence, and Episode 11's explicit competing-explanation work. Existing lessons should not be destructively rewritten until their replacement episode has a technically validated exercise.

## Narrative–technical handoff

Before building an episode, Narrative Studio and Curriculum/Engineering Studio agree on these facts in the episode's working notes or lesson draft; no separate form or governance file is required:

1. Ethan's entering knowledge and the misconception being exposed.
2. The operational question and decision consumer.
3. What evidence Ethan and the learner initially receive.
4. The prediction or claim they must commit to before later evidence.
5. The technical model the instruction must make usable.
6. The objective evidence the artifact must demonstrate, including source limits.
7. The learner work product and feedback/revision mechanism.
8. Ethan's exiting capability state and the next continuity debt.
9. Harrowmere facts changed or established by the episode.
10. Advanced content deliberately left outside Book 1.

ChatGPT owns character state, scene architecture, cognitive discomfort, controlled revelation, prose, and narrative continuity. Claude Code owns lessons, exercises, captures, logs, supporting artifacts, technical validation, and environment continuity. Either side should reject a handoff that cannot be represented honestly in the evidence.

## Book 1 completion and later books

Book 1 ends with Ethan able to produce reasoning that is visible, testable, revisable, and useful. It does not end with him identifying every threat or mastering every network mechanism.

**Book 2 — Learning to Investigate** can deepen TCP and performance, routing, NAT, proxies, VPNs, tunnels, richer DNS/TLS behavior, endpoint/network correlation, timelines, changing baselines, longer cases, and adversary behavior mixed with legitimate activity.

**Book 3 — Learning to Judge** can deepen hunting and detection assumptions, false positives and negatives, risk, evidence sufficiency, dashboards and metrics, tool acquisition, automation and AI, organizational incentives, incident coordination, and mentoring systems.

## Production gate

Build Episodes 1–3 as the first combined narrative/lesson slice. Run at least one resulting lesson with a learner before producing fourteen chapters of prose or replacing all nine working lessons. The architecture is a working baseline, not evidence that the sequence is validated.
