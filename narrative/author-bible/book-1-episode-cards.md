# Book 1 Episode Cards — v0.1
## Working title: *Learning to See*

These cards sit between the Book-level Snowflake and individual scene cards.

Each episode card defines:

- approximate story time;
- opening image;
- Ethan's entering state;
- episode objective;
- participants;
- operational question;
- conflict engine;
- reveal order;
- key analytical move;
- character/relationship movement;
- technical handoff;
- closing beat;
- continuity changes;
- unresolved debt.

Technical specifics remain subordinate to validated lesson/capture artifacts.

---

# Episode 1 — The Word in the Ticket

## Story time
**Day 11 at Harrowmere.**

## Opening image
Ethan at his workstation, newly trusted with a ticket of his own, rereading the title before he opens the evidence.

The title already says something like:

> Possible unauthorized access attempt — internal file service.

He feels the small satisfaction of finally being given “real analyst work.”

## Ethan entering state
Confident enough to want to perform expertise; still anxious enough to borrow confidence from labels.

## Episode story objective
Break the equation:

> technical recognition + confident wording = analysis.

## Primary participants
- Ethan
- Dana
- optional brief Owen presence

## Operational question
What does the evidence actually establish about the reported internal-file-service activity?

## Conflict engine
The inherited ticket interpretation fits several visible facts well enough to feel obvious.

Ethan is not fabricating anything. He is **organizing evidence around someone else's conclusion without noticing**.

## Reveal sequence
1. Ticket title/description.
2. Ethan inspects evidence.
3. He drafts or says “probing” / “unauthorized attempt.”
4. Dana asks where the evidence says that.
5. Ethan searches for the field/packet/event carrying the claim.
6. It does not exist.
7. Ticket language is exposed as an earlier person's interpretation.
8. Ethan rewrites the claim in bounded form.

## Key analytical move
Separate:

- observation;
- interpretation;
- judgment;
- recommendation.

## Key character beat
Ethan expects correction to mean Dana supplies the right answer.

Instead, Dana gives him responsibility for reconstructing the claim.

## Relationship movement
**Dana → Ethan:** slight trust gain because he revises.  
**Ethan → Dana:** first crack in “she knows and is testing me.”  
**Ethan → Owen:** answer shortcut remains attractive.

## Technical handoff
Reuse/adapt Lesson 01 material. No technical expansion beyond validated evidence.

## Closing beat
Ethan rereads the ticket title after rewriting his assessment.

The exact same words now look less like evidence and more like **something a person said**.

## Continuity added
- Internal file/sync service enters story world.
- Tickets become recognized evidence artifacts with provenance problems.
- Ethan begins retaining a claim-transition note/template.

## Debt handed forward
If he cannot simply use labels, he needs to learn how to explain what the machines were actually doing.

---

# Episode 2 — Who Is Talking to Whom?

## Story time
**Several days later; late Week 2 or early Week 3.**

## Opening image
Ethan has a packet/log view on screen and is confidently listing IPs, ports, and status fields while Leah waits for an answer to a much simpler-sounding question.

## Ethan entering state
More careful about claims, but still assumes technical fields become explanation when arranged correctly.

## Episode story objective
Move from **field recognition** to **purposeful system narration**.

## Primary participants
- Ethan
- Dana
- Leah
- Owen briefly if useful

## Operational question
Did the Harrowmere client reach the internal service, and did the application request succeed?

## Conflict engine
The phrase “it worked” means different things at different layers.

Ethan wants one binary answer.

Leah needs two.

## Reveal sequence
1. Leah asks whether the application reached the service.
2. Ethan identifies TCP/80 success in the existing plaintext HTTP capture.
3. Leah asks whether the request itself worked.
4. Application response shows a refusal/403 on one exchange.
5. A comparison exchange shows transport + application success.
6. Dana asks Ethan to narrate both without jargon first.
7. Ethan maps actor → purpose → exchange → outcome.

## Key analytical move
Separate:

- transport success;
- application success;
- who initiated;
- who responded;
- what layer each conclusion belongs to.

## Key character beat
Leah becomes the first person outside security to expose that Ethan's technically correct answer is not yet **useful system meaning**.

## Relationship movement
**Leah → Ethan:** notices he can revise toward her operational question.  
**Ethan → Leah:** begins respecting application purpose as necessary context.  
**Owen → Ethan:** still easy/helpful, but Owen's “instant” answer becomes more understandable.

## Technical handoff
Use current Lesson 02 evidence/capture and its TCP success / HTTP refusal distinction.

## Closing beat
Ethan summarizes:

> “The client reached the service. The service refused the request.”

Leah says something simple such as:

> “That I can use.”

No praise speech needed.

## Continuity added
- File/sync service has purposeful client/server behavior.
- Leah's domain expertise enters the story.
- Ethan has a conversation/actor map artifact.

## Debt handed forward
He can narrate after seeing the whole exchange. He still cannot say what should happen **before** he looks.

---

# Episode 3 — Before You Look

## Story time
**Week 3 or 4.**

## Opening image
Dana physically or digitally withholds the rest of a capture/log sequence.

Ethan can see enough to start explaining and keeps trying to scroll farther.

## Ethan entering state
Feels increasingly capable at retrospective explanation.

## Episode story objective
Turn explanation into a **risk-bearing prediction**.

## Primary participants
- Ethan
- Dana
- optional Owen contrast beat

## Operational question
Given what Ethan currently believes the synchronization exchange is doing, what observable behavior should come next?

## Conflict engine
Ethan thinks Dana is asking him to guess before she lets him see the answer.

The psychological conflict is stronger than the technical one.

## Reveal sequence
1. Ethan sees initial evidence.
2. Dana asks for explanation.
3. Ethan gives one.
4. Dana asks what he expects next.
5. Ethan resists: “I haven't seen it yet.”
6. Dana distinguishes prediction from guessing.
7. Ethan records assumption + expected observation + breaker.
8. Remaining evidence is revealed.
9. Some prediction is supported, revised, or simply untestable from available evidence.
10. Ethan preserves his original fields and appends the result and revision, rather than rewriting what he predicted.

## Key analytical move
Prediction must be:

- observable;
- tied to a model;
- dependent on named assumptions;
- capable of being weakened.

## Key character beat
Ethan discovers that being wrong **before evidence is revealed** feels much less threatening when wrongness produces information.

## Relationship movement
**Ethan → Dana:** begins seeing intent behind her questioning.  
**Dana → Ethan:** reduces one layer of structure.  
**Owen → Ethan:** if present, sees Ethan engaging the method rather than merely complying.

## Technical handoff
Use `lessons/e03-before-you-look/` and `e03-prediction.pcap`.

## Closing beat
Ethan voluntarily writes down one final prediction before Dana asks.

Dana notices but does not comment.

## Continuity added
Prediction/revision log becomes recurring artifact.

## Debt handed forward
Ethan assumes clean models should produce clean visible sequences. DNS will complicate that.

---

# Episode 4 — Names Have Behavior

## Story time
**Late Month 1.**

## Opening image
Ethan comparing two clients that appear to reach the same service differently: one has obvious DNS activity; the other seems not to resolve anything at all.

## Ethan entering state
Ready to predict, but still assumes conceptual steps should appear directly in evidence.

## Episode story objective
Teach that **expected conceptual behavior and observable evidence are not identical**.

## Primary participants
- Ethan
- Priya
- Dana

## Operational question
Why does name resolution appear differently across two otherwise related Harrowmere clients/workflows?

## Conflict engine
Ethan thinks one client “did DNS” and one did not.

Priya knows the resolver architecture/cache context can create both views legitimately.

## Reveal sequence
1. Ethan sees differing DNS evidence.
2. He proposes that one client skipped name resolution or behaved unusually.
3. Priya asks where the resolver is and what the client already knew.
4. Resolver/cache architecture is introduced only as needed.
5. Cold and repeated lookup evidence is compared.
6. Ethan predicts which observations would disappear after caching and from which vantage.
7. Comparison evidence supports the model.

## Key analytical move
Replace:

> “I didn't see DNS.”

with:

> “I did not observe a client lookup at this vantage during this window.”

## Key character beat
Priya checks a diagram/config/current state while answering.

Ethan notices this time.

He begins realizing experts **reconstruct relevant state** rather than carry everything in memory.

## Relationship movement
**Ethan → Priya:** intimidation shifts toward curiosity.  
**Priya → Ethan:** sees a novice capable of refining language after model correction.  
**Dana → background:** lets Priya own the domain knowledge.

## Technical handoff
Reuse Lesson 03 DNS/caching behavior as technically validated.

## Closing beat
Ethan writes “not observed” instead of “didn't happen.”

That wording matters.

## Continuity added
- Resolver/caching architecture joins Harrowmere system model.
- DNS expected-behavior artifact begins.

## Debt handed forward
If absence can mean many things, “connection failed” is also probably too blunt. Episode 5 follows.

---

# Episode 5 — Conversations Have Structure

## Story time
**Early Month 2.**

## Opening image
Several users or sites report essentially the same symptom:

> “It won't connect.”

Different teams are already leaning toward different owners.

## Ethan entering state
Better at modeling sequences but still overcompresses different failure states into “connectivity problem.”

## Episode story objective
Make causal differences visible inside similar user symptoms.

## Primary participants
- Ethan
- Owen
- Priya
- Leah
- Dana lightly

## Operational question
Which part of the system is failing in each case, and who should investigate next?

## Conflict engine
All cases look the same from the user perspective.

At the network/application level they differ materially.

## Reveal sequence
1. Four superficially similar reports.
2. Ethan initially groups them.
3. Owen asks a cheap discriminator: response or silence?
4. Priya distinguishes active refusal from path/drop.
5. Leah distinguishes transport success from application delay/failure.
6. Evidence reveals REJ/S0/RSTR/slow-but-correct style differences.
7. Ethan builds a causal triage map.
8. One case is routed differently because of his analysis.

## Key analytical move
Use **discriminating observations** to separate:

- active refusal;
- silence;
- reset after establishment;
- application delay.

## Key character beat
For the first time Ethan watches several experts disagree while all making valid statements from different models.

He stops asking:

> “Which one of them is right?”

and starts asking:

> “Which part is each describing?”

## Relationship movement
**Owen → Ethan:** sees real reasoning emerging.  
**Priya → Ethan:** trusts him more because he stops lazily blaming network.  
**Leah → Ethan:** sees him connecting packets to workflow failure.  
**Ethan → team:** first hint that expertise is distributed.

## Technical handoff
Use validated failure signatures. Keep MTU/fragmentation out for Episode 10.

## Closing beat
A user ticket says “network problem.”

Ethan changes the category only after checking the discriminator.

Small behavioral payoff.

## Continuity added
- Multiple sites/workflows around recurring environment.
- Causal triage map artifact.

## Debt handed forward
Ethan is getting good at reading visible structure. Encryption now removes part of it.

---

# Episode 6 — What Encryption Leaves Behind

## Story time
**Mid Month 2.**

## Opening image
An encrypted outbound flow from a familiar Harrowmere system looks clean and inscrutable at the same time.

Ethan stares at a TLS record that gives him far less than he wants.

## Ethan entering state
Believes visible structure enables good reasoning; now evidence becomes intentionally sparse.

## Episode story objective
Teach **bounded inference under encryption** without sliding into either helplessness or overtrust.

## Primary participants
- Ethan
- Cal
- Leah
- Dana

## Operational question
Is this encrypted outbound activity consistent with an approved vendor/application workflow, and what remains unknowable from network evidence alone?

## Conflict engine
Two attractive shortcuts:

- encrypted = unknowable;
- valid-looking TLS/443 = legitimate.

Both are wrong.

## Reveal sequence
1. Ethan sees encrypted flow.
2. He notes expected port/name/certificate-like context.
3. Cal shows that visibility differs by TLS version/source/pipeline.
4. Leah explains what the approved workflow should do.
5. Dana asks what each source can actually establish.
6. Ethan separates observable / inferable / undetermined.
7. He names one additional source that could materially change the answer.

## Key analytical move
Construct a bounded claim whose confidence comes from **relational context**, not encrypted payload visibility.

## Key character beat
Cal corrects a tool-centric assumption:

> “That's what the field says the pipeline produced. That's not the same as what the packet contained.”

Ethan remembers it.

## Relationship movement
**Cal → Ethan:** sees him beginning to ask provenance questions.  
**Leah → Ethan:** trusts his restraint.  
**Nia → Ethan:** may receive first concise bounded summary indirectly/directly.

## Technical handoff
Reuse Lesson 04 TLS 1.2/1.3 visibility differences.

## Closing beat
Ethan writes “cannot determine from this source” without feeling that he has failed.

## Continuity added
- Legitimate encrypted vendor/cloud behavior enters recurring baseline.
- Evidence-pipeline transformation becomes explicit.

## Debt handed forward
Ethan now wants enough historical data to define what “expected” really looks like. Episode 7 gives him the chance.

---

# Episode 7 — Expected Does Not Mean Identical

## Story time
**Late Month 2 / early Month 3.**

## Opening image
Ethan has assembled several days of Harrowmere traffic and built a neat graph.

It looks convincing.

It is also misleading.

## Ethan entering state
More mature, more confident, and ready to build a generalizable baseline.

## Episode story objective
Create Ethan's **first real operational win** while teaching that expected behavior depends on peer group, role, schedule, and context.

## Primary participants
- Ethan
- Leah
- Priya
- Nia
- Dana as reviewer

## Operational question
Is a recurring sync/transfer pattern at one site/role anomalous enough to warrant escalation?

## Conflict engine
The global view makes it look unusual.

The contextual view may make it expected—or reveal the reverse.

## Reveal sequence
1. Ethan presents a global average or simple baseline.
2. Leah asks about business date/schedule.
3. Priya asks about site/role/path.
4. Ethan partitions the data.
5. A meaningful pattern emerges.
6. He forms a prediction tied to a specific workflow.
7. Application/job evidence verifies the prediction.
8. Nia asks for the decision implication.
9. Ethan provides a bounded recommendation.

## Key analytical move
Define a baseline as:

> expected behavior for **this population, during this condition, over this window**.

Not “normal traffic.”

## Key character beat — MIDPOINT
Nia acts differently because of Ethan's analysis.

No senior analyst translates it for him.

He is useful.

## Relationship movement
**Nia → Ethan:** first meaningful operational trust.  
**Owen → Ethan:** begins treating him as junior colleague if present afterward.  
**Dana → Ethan:** reviews rather than builds.  
**Ethan → self:** gains deserved confidence that later becomes a vulnerability.

## Technical handoff
Build/validate a small multi-day dataset and contextual baseline.

## Closing beat
Ethan saves the baseline with assumptions attached.

He feels proud of it.

He should.

## Continuity added
- Persistent baseline artifact.
- Business-cycle/site variation established.
- Ethan now has a genuinely successful analytical method he may later overtrust.

## Debt handed forward
The baseline increases his confidence. Episode 8 shows that even good baselines depend on vantage/source.

---

# Episode 8 — Where Are You Standing?

## Story time
**Early Month 3.**

## Opening image
Four screens appear to tell four different stories about the same event.

Ethan is annoyed because he thought adding sources was supposed to reduce ambiguity.

## Ethan entering state
Confident in baseline reasoning; assumes multiple good sources should converge cleanly.

## Episode story objective
Teach that sources are **situated observers**, not competing omniscient accounts.

## Primary participants
- Ethan
- Priya
- Cal
- Leah
- Dana optional/reviewer

## Operational question
What actually happened in one Harrowmere transaction/event when packet, firewall, application, and perhaps endpoint evidence differ?

## Conflict engine
The evidence seems contradictory.

Each source is accurate within its observation boundary.

## Reveal sequence
1. Ethan presents contradiction.
2. Cal asks how each source is generated.
3. Priya asks where each source sits relative to the traffic path.
4. Leah explains what an app log's “success” actually means.
5. Ethan maps vantage + responsibility.
6. The contradiction resolves into a multi-view event.
7. A remaining unknown persists because no source could see it.

## Key analytical move
Ask first:

> “Could this source have seen the thing I'm claiming it did not see?”

## Key character beat
Ethan realizes a source can be highly trustworthy and still **incapable of answering his question**.

## Relationship movement
**Priya/Cal/Leah → Ethan:** deeper cross-domain trust.  
**Ethan → sources:** moves from ranking “best” source to matching source to question.

## Technical handoff
Use multi-vantage event design from Lesson 05 architecture.

## Closing beat
Ethan adds a “could have observed?” column to his evidence notes.

## Continuity added
- Source/vantage ledger begins.
- Known observability blind spot enters continuity.

## Debt handed forward
Ethan now sees gaps everywhere and wants more data. Episode 9 disciplines that impulse.

---

# Episode 9 — Ask the Evidence a Question

## Story time
**Mid Month 3.**

## Opening image
Ethan has made a long list of logs, captures, endpoint data, tickets, and application records he wants to collect.

Nia looks at the list, then at the clock.

## Ethan entering state
Evidence-aware but increasingly completeness-seeking.

## Episode story objective
Turn “more evidence” into **decision-valued evidence selection**.

## Primary participants
- Ethan
- Nia
- Cal
- Leah or Priya as source owners
- Dana as light reviewer

## Operational question
Which evidence should be collected now to support a time-bounded Harrowmere decision?

## Conflict engine
Some evidence:

- expires quickly;
- takes hours to obtain;
- shares provenance with other evidence;
- will not change the next action.

Ethan wants comprehensive certainty.

Nia needs usable sufficiency.

## Reveal sequence
1. Ethan presents broad collection plan.
2. Nia asks which decision each source could change.
3. Several sources fail the test.
4. Cal identifies perishable evidence.
5. Leah/Priya identify retrieval costs/context.
6. Ethan reorders collection.
7. He defines a stop condition.
8. Team acts before complete evidence exists.

## Key analytical move
Every requested source must have:

- question;
- predicted discriminator;
- cost/time;
- decision impact.

## Key character beat
Ethan finally understands Nia's compressed questions as analytical, not managerial impatience.

## Relationship movement
**Nia → Ethan:** sees decision-aware thinking emerge.  
**Ethan → Nia:** respect deepens.  
**Dana → Ethan:** further fading.

## Technical handoff
Use evidence-planning architecture from Lesson 05.

## Closing beat
Ethan crosses two “nice to have” sources off his own list before Nia asks.

## Continuity added
- Evidence retention/perishability fact becomes canon.
- Evidence plan artifact enters toolbox.

## Debt handed forward
Ethan can now collect evidence efficiently—but still tends to organize collection around his leading explanation. Episode 10 exploits that.

---

# Episode 10 — When the Expected Thing Does Not Happen

## Story time
**Late Month 3 / early Month 4.**

## Opening image
A warehouse/finance sync process is failing intermittently.

The screen contains two things Ethan has learned to take seriously:

- a recent network/security policy change;
- strange-looking large DNS behavior.

This time, he has enough skill to make the wrong story look very good.

## Ethan entering state
Competent, trusted, and convinced explicit modeling/prediction largely protects him from beginner-style premature closure.

## Episode story objective
Deliver the **major setback**: Ethan becomes convincingly wrong.

## Primary participants
- Ethan
- Dana
- Priya
- Leah
- Nia
- Owen optional as second technical voice

## Operational question
What is causing the synchronization failures, and is the unusual DNS behavior a security concern or causal component?

## Conflict engine
A plausible security/causal explanation fits timing and visible evidence.

Ethan's baseline contains legitimate odd-looking DNS behavior, but the failure begins near a policy change.

He links them incorrectly.

## Reveal sequence
1. Operational failure appears.
2. Ethan identifies unusual DNS traffic.
3. Recent policy/change context emerges.
4. He proposes a client-side lookup-contention hypothesis, retaining the changed policy as an alternative; odd appearance alone does not establish tunneling.
5. Dana asks for a prediction that distinguishes client-side lookup contention from path-specific policy failure.
6. Ethan produces one, but his evidence plan still favors his leading model.
7. Priya/Leah test related paths/workflows.
8. Nia permits one reversible pause of the noncritical inventory agent on an affected client while Priya prepares a safe path-policy check; essential sync remains running and the test has a stated deadline.
9. The odd queries stop and pending lookups drain on the test client, but its resolution and sync failures persist. The bounded detour consumes support time while service remains degraded.
10. A rollback or comparison test restores service.
11. The agent resumes and unusual DNS behavior continues without the failures on the corrected path.
12. Ethan sees the model cannot explain both facts.
13. He states that his explanation fails.
14. Paired observations and effective policy establish dropped response fragments and unavailable TCP fallback. This explains the outage; it does not classify every unusual query as benign merely because rollback worked.

## Key analytical move
**Preserve and visibly kill a model when its prediction fails.**

## Key character beat
Ethan experiences the professional weight of having people act on his confidence.

## Relationship movement
**Dana → Ethan:** trust tested but preserved.  
**Priya/Leah → Ethan:** remember the cost, but respect ownership of revision.  
**Nia → Ethan:** does not take the work away.  
**Ethan → Dana:** first glimpse that Dana's rigor comes from having made analogous mistakes.

## Technical handoff
Use the selected causal sequence in [HarrowSync's Episode 10 design](harrowsync-system-bible.md#episode-10-causal-sequence). Lesson 06's two surviving query fragments illustrate fragmentation; they do not demonstrate the proposed dropped-response incident, rollback, or business consequence. The capstone transfer supplies a written hypothetical case. New multi-vantage failure evidence must be validated before exact scene values are published. Do not reward guessing “MTU.”

## Closing beat
After the corrected model is established, Ethan looks at his original notes and does **not delete them**.

He writes:

> “Prediction failed here.”

## Continuity added
- Legitimate large DNS behavior is now historical Harrowmere context.
- Policy/fragmentation incident becomes future organizational memory.
- Dana's formative scar may be hinted.

## Debt handed forward
Ethan risks overcorrecting into permanent hedging and too many hypotheses. Episode 11 teaches useful alternatives.

---

# Episode 11 — More Than One Explanation

## Story time
**Several weeks later, Month 4.**

## Opening image
Ethan has four plausible explanations written down for recurring outbound activity and is reluctant to cross any of them out.

## Ethan entering state
Less overconfident; now somewhat afraid of committing too soon.

## Episode story objective
Teach that alternatives are useful only when they generate **different observable expectations**.

## Primary participants
- Ethan
- Dana
- Owen
- Cal and/or Leah

## Operational question
Which explanation best accounts for recurring outbound behavior associated with a Harrowmere host/service?

## Conflict engine
All explanations are superficially possible:

- approved agent;
- configuration error;
- unwanted software;
- malicious activity.

Keeping all four alive feels safe but becomes analytically inert.

## Reveal sequence
1. Ethan presents alternatives.
2. Owen asks which two actually explain the current evidence best.
3. Dana asks what each predicts.
4. Ethan constructs comparison matrix.
5. Cal/Leah supply one bounded source/context clue.
6. Ethan selects a high-value discriminator.
7. New evidence changes ranking.
8. Dana favors or mentions an explanation.
9. Ethan notices a mismatch/failed prediction in Dana's account.
10. Dana checks and revises.

## Key analytical move
Alternatives must **compete**.

The goal is not “consider all possibilities forever.”

## Key character beat
Ethan catches something Dana missed.

Dana says some version of:

> “You're right.”

The method becomes independent of the mentor.

## Relationship movement
**Ethan ↔ Dana:** moves toward collegial reasoning.  
**Owen → Ethan:** sees his eyes as useful.  
**Ethan → uncertainty:** learns commitment and revisability can coexist.

## Technical handoff
Build explicit explanation/prediction/evidence matrix; no new deep protocol topic.

## Closing beat
Owen asks Ethan:

> “Which one do you actually believe?”

Ethan answers with a ranking and breaker instead of “it depends.”

## Continuity added
A legitimate recurring outbound pattern is now well understood and can later serve as benign comparison.

## Debt handed forward
He can rank explanations. Episode 12 asks when a concerning one deserves action despite legitimate analogues.

---

# Episode 12 — Suspicious Compared with What?

## Story time
**Late Month 4 / early Month 5.**

## Opening image
A dashboard or query shows clean periodicity.

Early Ethan would have found that automatically suspicious.

Mid-book Ethan would have said “could be legitimate.”

Now he has to go farther.

## Ethan entering state
Capable of alternatives and explicit predictions; ready to exercise security judgment.

## Episode story objective
Move from anomaly recognition to **relational convergence and calibrated concern**.

## Primary participants
- Ethan
- Owen
- Leah
- Cal
- Nia

## Operational question
Is recurring outbound activity concerning enough to justify escalation/action?

## Conflict engine
Every individual feature has legitimate analogues:

- timing regularity;
- DNS structure;
- TXT traffic;
- transfer size;
- encryption.

Concern emerges from relationships among them.

## Reveal sequence
1. Periodic traffic appears.
2. Ethan identifies a known-good analogue.
3. Leah supplies legitimate workflow possibilities.
4. Cal correlates DNS/session/transfer evidence.
5. One destination/entity connects otherwise separate concerning behaviors.
6. Owen pushes Ethan to articulate strongest benign explanation.
7. Ethan predicts what evidence should exist if benign.
8. That context is absent or contradicted.
9. Ethan ranks concern above benign without claiming proof.
10. Nia asks what action is proportionate.

## Key analytical move
Suspicion is not a visual shape.

It is a judgment about how well explanations fit **relationships and context**.

## Key character beat
Ethan can now resist both:

- “beacon = C2” certainty;
- “anything could be legitimate” paralysis.

## Relationship movement
**Nia → Ethan:** sees usable security judgment.  
**Cal → Ethan:** begins regarding him as a partner in defining future detections.  
**Leah → Ethan:** trusts that legitimate context is seriously weighed.  
**Owen ↔ Ethan:** increasingly peer-like.

## Technical handoff
Reuse Lesson 07 style benign/concerning shape comparison and relational convergence.

## Closing beat
Ethan writes “concerning” rather than “malicious.”

Nia still acts.

This demonstrates that action does not require overclaiming.

## Continuity added
Benign and concerning pattern library now coexists.

## Debt handed forward
Ethan can form a judgment; Episode 13 makes him communicate a mixed one without losing distinctions.

---

# Episode 13 — What Can You Responsibly Say?

## Story time
**Month 5.**

## Opening image
Ethan has an analysis that is mostly clear and partly unresolved.

The hardest part is no longer finding facts.

It is deciding how to say them.

## Ethan entering state
Analytically capable; still underestimates how communication can alter claim strength.

## Episode story objective
Make **communication itself an analytical responsibility**.

## Primary participants
- Ethan
- Nia
- Dana deliberately distant
- Leah or another operational stakeholder

## Operational question
What should Harrowmere do when 94% of observed authentication failures used a recently changed path, while a small residual has different risk characteristics? The change is the leading operational explanation, not a demonstrated cause before rollback verification.

## Conflict engine
Stakeholders want a single headline.

Evidence supports:

- provisional operational explanation for the majority;
- minority residual security concern.

Compression can destroy this distinction.

## Reveal sequence
1. Ethan receives mixed case.
2. He separates the majority associated with the changed path from the residue, keeping causation provisional.
3. Residual context raises concern without evidence of success.
4. He drafts technical handoff.
5. He drafts manager summary.
6. Dana refuses/declines to pre-edit.
7. Ethan delivers directly to Nia.
8. Nia asks a breaker/decision question.
9. Ethan answers from his own analysis.
10. Nia decides.

## Key analytical move
Same evidence and claim strength across audiences; different detail.

## Key character beat
Dana's absence from editing is the mentoring event.

Ethan realizes only afterward that she deliberately let his communication stand.

## Relationship movement
**Nia → Ethan:** direct decision trust.  
**Dana → Ethan:** reviewer status recedes further.  
**Ethan → self:** communication becomes part of ownership.

## Technical handoff
Use Lesson 08's 94/6 case structure and two-audience work product.

## Closing beat
Nia says:

> “Okay. We'll do that.”

Ethan waits for Dana's correction.

None comes.

## Continuity added
Demonstrates transfer beyond recurring sync environment.

## Debt handed forward
People now trust Ethan's judgments enough that the final test is whether he can reverse one of **his own** when new evidence arrives.

---

# Episode 14 — Decide Before You Disrupt

## Story time
**Late Month 5 or Month 6.**

## Opening image
An authorized update is underway or just completed across a set of Harrowmere systems Ethan now knows well.

New encrypted outbound behavior appears.

At first glance it looks exactly like the sort of thing Book 1 has taught him not to panic about.

## Ethan entering state
Trusted developing analyst; capable of independent loop; no longer trying to prove he belongs every minute.

## Episode story objective
Full-loop capstone: **revise a reasonable trusted judgment under real decision pressure without Dana conducting the work**.

## Primary participants
- Ethan
- Nia
- Owen
- Priya
- Leah
- Cal
- Dana absent from core, returns later

## Operational question
Does the new post-update outbound behavior justify continued operation, staged investigation, or containment/interruption?

## Conflict engine
The benign explanation is genuinely strong at first.

Ethan's accumulated Book 1 knowledge supports it.

The danger is not ignorance.

It is attachment to a correct-looking model after contradictory evidence appears.

## Reveal sequence
1. Approved update context established.
2. Ethan sees familiar encrypted/periodic pattern.
3. Baseline/peer comparison supports benign interpretation.
4. Ethan states benign-leaning assessment **plus breaker and next evidence**.
5. Nia accepts continued staged operation while checks proceed.
6. Leah/vendor context reveals destination ownership mismatch.
7. Cal/endpoint/package evidence reveals artifact mismatch.
8. Peer comparison shifts meaning: all updated hosts share behavior; non-updated do not.
9. Unexpected module/persistence evidence strengthens concern if technically validated.
10. Ethan recognizes his earlier model has failed.
11. Brief internal hesitation: he already told Nia this looked benign.
12. He explicitly revises.
13. He coordinates bounded questions to each expert.
14. He recommends proportionate action.
15. Nia decides.
16. Work is handed to deeper incident investigation.
17. Dana later reviews, not rescues.

## Key analytical move
The same piece of evidence—peer similarity—changes meaning when the causal model changes.

This is the intellectual payoff of the entire book.

## Key character beat — CLIMAX
Ethan says some version of:

> “My earlier assessment no longer holds.”

No defensiveness.

No theatrical confession.

Just professional revision.

## Relationship movement
**Nia → Ethan:** trusts revision, not consistency.  
**Owen → Ethan:** peer-like technical exchange.  
**Priya → Ethan:** trusts his bounded questions.  
**Leah → Ethan:** sees him integrating context without surrendering judgment.  
**Cal → Ethan:** sees an analyst who can define capability needs.  
**Dana → Ethan:** returns to find the method operating without her.

## Technical handoff
Use the [selected update trust boundary and response owners](harrowsync-system-bible.md#12-update-lifecycle); preserve the separation between initial observations and later repository/endpoint findings. A defensible initial assessment need not lean benign if it weighs the same evidence and proposes proportionate action.

Adapt existing capstone evidence:
- vendor/domain contradiction;
- package/hash mismatch;
- valid automation credential misuse;
- unsigned module/persistence if retained;
- updated vs non-updated peer comparison;
- initial and revised assessments;
- proportionate handoff.

## Closing sequence

### Immediate operational close
Nia acts on Ethan's revised judgment.

### Analytical close
Ethan hands off:
- knowns;
- unknowns;
- scope questions;
- evidence preservation needs.

### Mentor close
Dana returns later.

Possible brief exchange:

> “Anything bother you?”

Ethan names the unresolved scope/credential question instead of defending the result.

### Final work beat
Later, Owen rolls over:

> “You got a second?”

Ethan looks.

> “What do we know?”

Owen gives observations.

Ethan:

> “If that's what we think it is, what else should be true?”

End near there.

## Continuity added
- Book 2 investigation questions established naturally.
- Ethan has completed Book 1 capability arc.
- Team relationships now operate as disciplined interdependence.

## Debt handed forward to Book 2
- origin;
- historical scope;
- credential use;
- timeline;
- expired/missing evidence;
- deeper endpoint/network reconstruction;
- incident investigation mechanics.

## Must NOT resolve
The full incident.

Book 1 ends when Ethan has produced a trustworthy judgment and usable handoff, not when Harrowmere knows everything.

---

# Episode Timing Map

A working rhythm:

| Episode | Approximate time |
|---|---|
| 1 | Day 11 |
| 2 | Week 3 |
| 3 | Week 4 |
| 4 | Late Month 1 |
| 5 | Early Month 2 |
| 6 | Mid Month 2 |
| 7 | Late Month 2 / early Month 3 |
| 8 | Early Month 3 |
| 9 | Mid Month 3 |
| 10 | Late Month 3 / early Month 4 |
| 11 | Month 4 |
| 12 | Late Month 4 / early Month 5 |
| 13 | Month 5 |
| 14 | Late Month 5 / Month 6 |

This gives Book 1 enough elapsed time for competence and relationships to grow plausibly.

Exact dates remain unset until artifact chronology requires them.

---

# Episode Participation Map

Avoid having the full cast appear constantly.

| Ep | Dana | Nia | Owen | Priya | Leah | Cal |
|---|---|---|---|---|---|---|
| 1 | Primary | — | Brief | — | — | — |
| 2 | Primary | — | Brief | — | Primary | — |
| 3 | Primary | — | Optional | — | — | — |
| 4 | Light | — | — | Primary | — | — |
| 5 | Light | — | Primary | Primary | Primary | — |
| 6 | Primary | Optional | — | — | Primary | Primary |
| 7 | Review | Primary | Optional | Primary | Primary | — |
| 8 | Optional | — | — | Primary | Primary | Primary |
| 9 | Review | Primary | — | Optional | Optional | Primary |
| 10 | Primary | Primary | Optional | Primary | Primary | — |
| 11 | Primary | — | Primary | — | Optional | Optional |
| 12 | —/Review | Primary | Primary | — | Primary | Primary |
| 13 | Deliberately distant | Primary | — | — | Optional | — |
| 14 | Absent core | Primary | Primary | Primary | Primary | Primary |

This preserves cast independence and makes Dana's fade visible.

---

# Episode Opening-Image Pattern

The openings should vary.

1. **Ticket** — inherited interpretation.
2. **Screen + stakeholder** — field list versus useful question.
3. **Hidden evidence** — resistance to prediction.
4. **Two clients** — missing DNS.
5. **Same symptom, different mechanisms.**
6. **Encrypted flow** — sparse evidence.
7. **Beautiful graph** — misleading baseline.
8. **Conflicting screens** — vantage.
9. **Long collection list + clock** — evidence cost.
10. **Operational failure + strange DNS** — seductive causal story.
11. **Too many hypotheses** — overcorrection.
12. **Clean periodicity** — anomaly ambiguity.
13. **Mostly explained case** — communication pressure.
14. **Familiar post-update behavior** — the dangerous comfort of recognition.

This prevents narrative sameness.

---

# Episode Closing-Beat Pattern

Closings should usually be **behavioral**, not explanatory.

1. Ethan rereads loaded ticket language differently.
2. Leah says the explanation is usable.
3. Ethan predicts before being asked.
4. Ethan writes “not observed.”
5. Ethan reclassifies a “network problem” only after evidence.
6. Ethan writes “cannot determine” without shame.
7. Ethan saves baseline + assumptions, proud.
8. Adds “could have observed?” column.
9. Crosses off unnecessary evidence himself.
10. Preserves failed model instead of deleting it.
11. Gives ranked explanation without hiding behind “depends.”
12. Writes “concerning,” not “malicious,” and action still follows.
13. Nia acts without Dana editing.
14. Ethan naturally asks Owen for observations and prediction.

The closing beats show the developmental arc without narration announcing it.

---

# Continuity Requirements Before Scene Cards

Before individual scene cards, the following need technical/world definition:

## A. Recurring system identity
We need a stable but original name for the finance/inventory/warehouse synchronization platform/service family.

Requirements:
- plausible enterprise name;
- not “Acme”/“Contoso” style;
- multiple components allowed;
- supports file/API/vendor/cloud behavior;
- name should not imply threat.

## B. Persistent technical topology
At author level only:
- major client/site classes;
- central service;
- resolver relationship;
- vendor/cloud component;
- relevant sensor/vantage locations;
- application owner;
- network ownership;
- Security Onion evidence path.

Not every subnet/IP yet.

## C. Baseline artifact schema
Define what Episode 7 baseline actually records so it can recur in 12/14.

## D. Episode 10 exact evidence staging
Technical validation must ensure:
- initial model is genuinely plausible;
- failed prediction is unmistakable;
- correction cannot be guessed from jargon alone.

## E. Episode 14 exact breaker sequence
Need a technically validated staged evidence packet preserving:
- reasonable benign initial assessment;
- multiple independent contradictions;
- peer-similarity reversal;
- proportionate decision without full attribution.

---

# Next Story-Design Step

We are now ready for **scene cards**, but I recommend one intermediate world-building task first:

> **Define the recurring Harrowmere synchronization environment as an author-level system bible.**

That system has become nearly another character.

We need to know:

- what it is for;
- which business processes depend on it;
- components;
- owners;
- schedules;
- legitimate variation;
- network path;
- vendor/external dependencies;
- known historical exceptions;
- what Ethan sees early versus later;
- which pieces are intentionally invisible from each evidence source.

Once that environment is stable, scene cards can use it without inventing topology on the fly and accidentally contradicting later technical exercises.


---
