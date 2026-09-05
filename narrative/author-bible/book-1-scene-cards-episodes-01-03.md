# Book 1 scene cards — Episodes 1–3

## Status

First scene-level test slice for *Learning to See*. These cards preserve the existing draft chapters and define their internal architecture; they do not authorize invented technical evidence. Learner-facing values and reveals come from the linked committed artifacts.

The first three episodes move Ethan through one continuous developmental sequence:

> inherited interpretation → purposeful narration → testable prediction

---

# Episode 1 — The Word in the Ticket

## Scene 1.1 — The title arrives first

- **Approximate time/location:** Day 11, morning; Ethan's workstation in the security operations area.
- **POV:** Ethan, first person.
- **Scene goal:** Establish why a competent beginner would sincerely adopt the ticket's interpretation before noticing he has done so.
- **Who wants what:** Ethan wants a clean first piece of real analyst work and evidence that Dana can trust him with ownership. The ticket's author wanted suspicious activity assessed and has already compressed that concern into the title.
- **Obstacle/conflict:** Ethan recognizes only a small subset of the available fields. The familiar words `admin` and `403 Forbidden`, combined with the loaded title, offer relief from uncertainty and a ready-made causal story.
- **Information entering the scene:** Ethan has had ten mostly successful days; he knows Harrowmere vocabulary, has seen the tools, and has not yet made a consequential judgment. The ticket contains the two validated conversations from `02-conversation.pcap`.
- **Reveal sequence:**

1. The title says “Possible unauthorized access attempt — internal file service.”
2. The evidence presents twenty-six pieces of information, most of which Ethan cannot yet interpret fluently.
3. He recognizes a successful export-summary request, an admin URI, and a `403`.
4. The ticket language and recognized facts appear to corroborate one another.
5. Ethan converts that fit into “Someone's probing the admin API.”

- **Analytical/cognitive turn:** No corrective turn yet. The important movement is that Ethan mistakes recognition plus agreement with inherited framing for independent analysis.
- **Choice/decision:** He takes the “probing” assessment to Dana rather than first tracing each word to evidence.
- **Relationship movement:** Ethan treats Dana as the evaluator of an answer he believes he has completed. Owen remains the imagined easier route, though he need not appear.
- **Technical artifact/handoff needed:** The exact ticket language and evidence values already used in [`00-prologue.md`](../00-prologue.md), all grounded in [`02-conversation.pcap`](../../assets/pcaps/02-conversation.pcap). No new field, timestamp, or packet claim.
- **Reader knows before vs. after:** Before, Ethan is eager and inexperienced. After, the reader can see that his conclusion is plausible and evidence-adjacent—not dishonest or foolish—but has not been independently established.
- **What remains author-only:** Dana has already identified premature interpretation aided by vocabulary as Ethan's early risk. Ethan's Day 10 success has made the confidence of this mistake possible.
- **Exit condition/closing beat:** Ethan tells Dana, “Someone's probing the admin API.” She does not answer immediately.
- **Continuity facts established:** Day 11; HarrowSync agent string; internal file/sync service; tickets mix observation and interpretation; Ethan wants ownership.
- **Debt passed to the next scene:** The word *probing* must acquire provenance.

## Scene 1.2 — Show me the word

- **Approximate time/location:** Continuous with Scene 1.1; Dana's desk, then Ethan's screen.
- **POV:** Ethan.
- **Scene goal:** Make claim provenance visible without having Dana replace Ethan's conclusion with her own.
- **Who wants what:** Ethan wants Dana to confirm or efficiently correct his assessment. Dana wants Ethan to locate the boundary between what he observed and what he inherited.
- **Obstacle/conflict:** Every observed fact can be arranged beneath “probing,” so Ethan initially experiences the interpretation as though it were another field in the record.
- **Information entering the scene:** Two requests from the same source and destination, four tenths of a second apart; one `200`, one `403`; the ticket's stronger language.
- **Reveal sequence:**

1. Dana asks what Ethan saw and what he thought.
2. Ethan repeats the observed facts and the probing claim as one package.
3. Dana asks where the word *probing* came from.
4. Ethan searches the evidence for it.
5. He traces his word to the title's phrase “unauthorized access attempt”; the literal word “probing” is his own paraphrase, not a field or a word in the title.
6. He recognizes that his analysis began inside someone else's interpretation.

- **Analytical/cognitive turn:** A ticket becomes a human evidence artifact with provenance, not a neutral container around machine facts.
- **Choice/decision:** Ethan returns to the evidence instead of defending the inherited label.
- **Relationship movement:** Dana's refusal to supply the answer begins to look less like withholding and more like returning ownership. Her trust rises slightly because Ethan revises rather than bluffs.
- **Technical artifact/handoff needed:** A claim-transition record with separate spaces for observation, interpretation, judgment, and recommendation, aligned to [Lesson 01](../../lessons/01-what-the-analyst-is-for.md).
- **Reader knows before vs. after:** Before, the ticket seems to corroborate Ethan. After, the reader knows the corroboration was partly circular.
- **What remains author-only:** Dana's own formative overconfidence and the history behind her sensitivity to inherited stories.
- **Exit condition/closing beat:** Ethan can name the mistake but still wants to know who performed the activity and whether it was bad.
- **Continuity facts established:** “Show me where the evidence says that” becomes shared language; Ethan's first durable artifact begins.
- **Debt passed to the next scene:** Removing one unsupported word does not yet produce a bounded explanation.

## Scene 1.3 — The expert revises too

- **Approximate time/location:** Minutes later; both at Ethan's workstation.
- **POV:** Ethan.
- **Scene goal:** Separate machine evidence from person/process inference and show expert revision before Ethan can recast Dana as an oracle.
- **Who wants what:** Ethan wants the correct story of the event. Dana wants him to identify what this source can establish and to retain responsibility for the remaining judgment.
- **Obstacle/conflict:** The evidence invites person-language, and Dana herself begins to extend the microsecond duration into a human-impossibility argument too quickly.
- **Information entering the scene:** The connection records contain addresses, ports, bytes, duration, states, URIs, status codes, and matching agent strings—but no user, process identity, or intent.
- **Reveal sequence:**

1. Dana asks Ethan to show the user; he cannot.
2. The duration appears to make manual action implausible.
3. Dana begins treating that timing as the explanation, then stops herself aloud.
4. Matching `harrow-sync/3.21` agent strings make one workflow plausible without proving process identity.
5. The earlier successful request broadens the context around the `403`.
6. Dana states that neither of them yet knows whether the behavior is harmful.
7. She gives Ethan four bounded questions and asks him to write observation separately from meaning.

- **Analytical/cognitive turn:** Source limits apply to senior analysts too; expertise includes interrupting a persuasive inference and revising it visibly.
- **Choice/decision:** Ethan accepts “not established” as the current answer and writes the six-sentence claim-transition note.
- **Relationship movement:** Ethan's model of Dana shifts: her questions may not conceal a finished answer. Dana sees that Ethan can tolerate correction without retreating or performing certainty.
- **Technical artifact/handoff needed:** Existing validated values only; the completed six-sentence response becomes the narrative bridge into Lesson 01 and the opening object of Episode 2.
- **Reader knows before vs. after:** Before, the remaining uncertainty looks like Ethan's technical deficiency. After, some of it is revealed as a real boundary in the available evidence.
- **What remains author-only:** The four questions anticipate later episodes and the full HarrowSync environment. Dana's public self-correction is shaped by her history with Nia, but that history is not disclosed.
- **Exit condition/closing beat:** Forty minutes later, Ethan has six difficult sentences with observation and interpretation separated on the page.
- **Continuity facts established:** Same address and agent string do not prove the same user or process; Dana has nine years of experience; the claim-transition note becomes Artifact A.
- **Debt passed to Episode 2:** Ethan can now write bounded claims about fields he still cannot narrate as purposeful system behavior.

---

# Episode 2 — Who Is Talking to Whom?

## Scene 2.1 — Six accurate sentences

- **Approximate time/location:** Several days later, late Week 2 or early Week 3; Dana's desk in the security operations area.
- **POV:** Ethan.
- **Scene goal:** Demonstrate that careful wording and technical understanding are distinct capabilities.
- **Who wants what:** Ethan wants his revised six sentences accepted as competent work. Dana wants to know whether he understands the event he has described accurately.
- **Obstacle/conflict:** Ethan's prose is bounded but treats endpoint names and status fields as self-explanatory. Each careful sentence can be true while the whole explanation lacks system meaning.
- **Information entering the scene:** The claim-transition note from Episode 1 and the same two conversations.
- **Reveal sequence:**

1. Dana gives Ethan his first unqualified “This is better.”
2. She asks, “What happened?”
3. Ethan reads the accurate sentence rather than answering the question beneath it.
4. Questions about the endpoint and response expose that he has promoted a URI label and `200 OK` into “successful export.”
5. Ethan realizes he has written an accurate description of a conversation he cannot explain.

- **Analytical/cognitive turn:** Precision in claim strength does not automatically supply a causal or purposeful model.
- **Choice/decision:** Ethan asks for the packets rather than polishing the same sentence again.
- **Relationship movement:** Ethan briefly expects approval to end the work; Dana's next question shows that trust means deeper ownership, not fewer questions.
- **Technical artifact/handoff needed:** The six-sentence note and the current connection record. Packet access comes next from the committed Lesson 02 capture.
- **Reader knows before vs. after:** Before, Ethan's disciplined wording appears to have solved the first problem. After, the reader knows it solved only claim separation, not event explanation.
- **What remains author-only:** Dana is deliberately testing whether the improvement generalized beyond the form of the Lesson 01 artifact.
- **Exit condition/closing beat:** Dana opens the capture and moves aside.
- **Continuity facts established:** Earlier work products remain active; success creates the next blind spot rather than resetting Ethan.
- **Debt passed to the next scene:** Ethan must translate packet structure into defensible claims at the correct layer.

## Scene 2.2 — A handshake is not the request

- **Approximate time/location:** Continuous; Ethan's workstation.
- **POV:** Ethan.
- **Scene goal:** Convert a memorized handshake diagram into a bounded statement about what the evidence establishes.
- **Who wants what:** Ethan wants the relief of recognizing the three-way handshake. Dana wants him to state precisely what that pattern licenses and what it does not.
- **Obstacle/conflict:** Familiar terminology tempts Ethan to stop at naming the pattern. “The connection succeeded” remains ambiguous about which connection, which layer, and which outcome.
- **Information entering the scene:** The packet rows expose SYN, SYN-ACK, ACK and the two directions of communication.
- **Reveal sequence:**

1. Ethan identifies the three-way handshake.
2. Dana accepts the name but asks what it establishes.
3. Ethan bounds the claim to reachability and response in both directions.
4. Dana tests common overextensions: request success, authorization, and server identity.
5. Ethan distinguishes what the handshake supports from what later evidence must establish.

- **Analytical/cognitive turn:** Protocol knowledge becomes a reasoning tool only when tied to a claim boundary.
- **Choice/decision:** Ethan stops treating “connection succeeded” as a complete answer.
- **Relationship movement:** Dana tells rather than only asks when a missing layer distinction needs naming, keeping her mentoring from becoming ritualized questioning.
- **Technical artifact/handoff needed:** Frames and values from [`02-conversation.pcap`](../../assets/pcaps/02-conversation.pcap), as already documented in [Lesson 02](../../lessons/02-reading-a-conversation.md).
- **Reader knows before vs. after:** Before, a completed handshake feels like success. After, it establishes a narrower transport fact and leaves the application question open.
- **What remains author-only:** Dana is preparing Ethan to answer someone whose operational question does not map cleanly to a packet label.
- **Exit condition/closing beat:** Leah arrives carrying the Reporting Platform question.
- **Continuity facts established:** “At which layer?” enters Ethan's working vocabulary.
- **Debt passed to the next scene:** A stakeholder needs to know whether work completed, not whether TCP performed correctly.

## Scene 2.3 — Leah's question

- **Approximate time/location:** Continuous; Ethan's workstation, with Leah standing beside the desk.
- **POV:** Ethan.
- **Scene goal:** Establish Leah as a technically serious source of application/workflow context and force Ethan to answer the decision-relevant question.
- **Who wants what:** Leah wants to know whether the finance export completed so she can act on the workflow. Ethan wants to give a useful answer without repeating Episode 1's overclaim. Dana wants him to integrate—not defer to—Leah's bounded expertise.
- **Obstacle/conflict:** A `200 OK` from an endpoint named `export` sounds like successful completion, but the response may describe work rather than perform it. Ethan experiences “I don't know yet” as weak in front of a domain expert.
- **Information entering the scene:** Transport success, HTTP request/response status, URI, and the unread response body. Leah knows the Reporting Platform workflow.
- **Reveal sequence:**

1. Leah asks whether the finance export completed.
2. Ethan answers that the request received a successful HTTP status.
3. Leah distinguishes that claim from her question.
4. Ethan states what he knows and what he has not inspected.
5. Leah explains that the endpoint returns a page summary, not the actual export.
6. The response body establishes a summary describing 1,284 rows.
7. Ethan revises: network and HTTP request succeeded; export completion remains unestablished.

- **Analytical/cognitive turn:** Application purpose is not contained in the endpoint name, and context from an owner is valuable evidence rather than a substitute for observed behavior.
- **Choice/decision:** Ethan retains the unknown instead of claiming completion or handing the judgment wholesale to Leah.
- **Relationship movement:** Leah moves from “application person” to a holder of workflow evidence Ethan needs. Leah sees that Ethan can narrow a claim when her system model complicates it.
- **Technical artifact/handoff needed:** Existing response body and validated row count; no invented Reporting Platform behavior beyond the draft.
- **Reader knows before vs. after:** Before, the endpoint name and `200` appear to answer Leah. After, the response is known to be a successful summary while the larger business outcome remains open.
- **What remains author-only:** Leah has previously been wrong when intent and actual application behavior diverged; that scar informs her precision but is not disclosed.
- **Exit condition/closing beat:** Leah leaves after Ethan can finally state her question accurately.
- **Continuity facts established:** Leah owns application/workflow context; HarrowSync has multiple workflow stages; a component can succeed without the business process completing.
- **Debt passed to the next scene:** Ethan must narrate both conversations without turning shared fields into an unsupported single actor or story.

## Scene 2.4 — Begin with who spoke first

- **Approximate time/location:** Immediately after Leah leaves; Ethan's workstation.
- **POV:** Ethan.
- **Scene goal:** Produce a purposeful, layer-aware narration of both conversations and make it usable to someone outside packet analysis.
- **Who wants what:** Ethan wants the actual explanation Dana has withheld. Dana wants him to construct it from sequence, roles, evidence, and limits.
- **Obstacle/conflict:** Same source/destination addresses and user-agent invite singular language, while different source ports and separate handshakes establish distinct conversations. Packet names keep competing with actor-and-purpose narration.
- **Information entering the scene:** Full packet order, both application responses, matching user-agent, two source ports, and Leah's workflow clarification.
- **Reveal sequence:**

1. Ethan calls the activity “the same client,” then bounds this to same source address and matching agent string.
2. He recognizes two distinct connections.
3. Dana asks for the first conversation without packet names.
4. Ethan identifies initiator, service, request, response, and closer.
5. He starts the second conversation and encounters the same temptation to turn correlations into person/process certainty.
6. He chooses a side-by-side actor map and begins with who spoke first.

- **Analytical/cognitive turn:** Technical fields become meaningful through ordered relationships among actors, layers, purposes, and outcomes—not through a larger inventory of correct labels.
- **Choice/decision:** Ethan constructs the explanation himself instead of asking Leah or Dana what the software “really” did.
- **Relationship movement:** Dana gives him the work rather than the answer. Ethan sees that Owen's speed may rest on learnable causal compression rather than magic recall.
- **Technical artifact/handoff needed:** Conversation/actor map that leads directly into [Lesson 02](../../lessons/02-reading-a-conversation.md).
- **Reader knows before vs. after:** Before, the ticket looks like one suspicious event. After, it is two conversations with separate transport and application outcomes plus unresolved actor/process attribution.
- **What remains author-only:** The conversation map will become Artifact B and later support the wider HarrowSync system model.
- **Exit condition/closing beat:** Ethan opens a blank page and begins with who spoke first.
- **Continuity facts established:** Leah's bounded role; two conversations; transport/application distinction; shared identifiers support but do not prove actor continuity.
- **Debt passed to Episode 3:** Ethan can explain completed evidence after seeing it all; his model has not yet borne the risk of predicting unseen evidence.

---

# Episode 3 — Before You Look

## Scene 3.1 — The hidden rows

- **Approximate time/location:** Week 3 or 4, a quiet afternoon; Ethan's workstation or a nearby analysis/training desk.
- **POV:** Ethan.
- **Scene goal:** Make the limitation of retrospective explanation emotionally visible before prediction is introduced as the remedy.
- **Who wants what:** Ethan wants to apply his new conversation-narration skill to an unfamiliar capture. Dana wants evidence that his explanation can generate an expectation before the outcome is known.
- **Obstacle/conflict:** Dana hides the later rows. Ethan experiences this as artificial deprivation because he believes analysis begins after all available evidence is opened.
- **Information entering the scene:** Ethan can now distinguish transport and application outcomes in completed conversations. The new evidence shows an established connection, client request data, and a server acknowledgment, with the later exchange withheld.
- **Reveal sequence:**

1. Ethan starts explaining the visible exchange and tries to scroll farther.
2. Dana asks what happens next.
3. Ethan says he cannot know because it has not happened on his screen yet.
4. Dana asks what his current explanation would lead him to expect.
5. Ethan lists multiple possibilities to avoid privileging one.
6. Dana points out that an explanation that predicts everything gives later evidence nothing specific to test.

- **Analytical/cognitive turn:** Uncertainty does not remove the obligation to expose what a current model expects.
- **Choice/decision:** Ethan agrees to form a prediction without seeing the remaining rows.
- **Relationship movement:** Ethan initially reads Dana's withholding as a test; Dana keeps the focus on the model rather than his performance.
- **Technical artifact/handoff needed:** Narrative may describe only the general staged-evidence shape. Exact worked-example fields, bytes, timing, and reveal belong to [`lessons/e03-before-you-look/`](../../lessons/e03-before-you-look/README.md).
- **Reader knows before vs. after:** Before, Ethan's retrospective competence feels transferable. After, neither Ethan nor the reader knows whether that competence can survive a hidden outcome.
- **What remains author-only:** Dana is deliberately moving from explain to predict because Ethan has demonstrated readiness; this is fading support, not a trick.
- **Exit condition/closing beat:** Ethan gives a vague “the server responds,” and Dana asks for direction, kind, and condition.
- **Continuity facts established:** Dana can make evidence availability part of the learning design; Ethan's prior success is the reason for the new demand.
- **Debt passed to the next scene:** Prediction must become specific enough to be wrong in a named way.

## Scene 3.2 — Owen makes the reasoning visible

- **Approximate time/location:** Continuous; security operations area.
- **POV:** Ethan.
- **Scene goal:** Contrast Owen's compressed expertise with visible reasoning and show that experienced analysts also resist committing predictions to a record.
- **Who wants what:** Owen wants to help quickly and return to his work. Dana wants his expectation decomposed so Ethan can see the reasoning inside the fast answer. Ethan wants evidence that prediction is analytical practice rather than remedial theater for novices.
- **Obstacle/conflict:** Owen can state the likely next behavior immediately, which appears to confirm Ethan's original model of expertise. He dislikes writing it down because the written form removes retrospective flexibility.
- **Information entering the scene:** A completed connection, client request bytes, server bare acknowledgment, and no visible application response.
- **Reveal sequence:**

1. Owen recognizes the exercise and gives a quick expectation: the server will respond.
2. Dana asks for the observable direction and event kind.
3. She separates TCP acknowledgment from application handling.
4. Owen names the condition beneath his prediction: the application receives and handles a complete request.
5. Dana asks what a reset, silence, or additional client data would change.
6. Ethan sees that the fast answer contains assumptions and discriminators Owen did not initially externalize.

- **Analytical/cognitive turn:** Expert speed is compressed reasoning, not proof that reasoning artifacts are unnecessary. A prediction becomes useful when its direction, kind, condition, and breaker are visible.
- **Choice/decision:** Ethan stops using “Owen would just look” as an argument against prediction and agrees to preserve his own pre-reveal reasoning.
- **Relationship movement:** Owen remains admirable and useful rather than becoming Dana's negative example. Dana exposes his reasoning without belittling his speed; Owen's willingness to participate makes his expertise more teachable.
- **Technical artifact/handoff needed:** No exact reveal values in the narrative scene. The technical lesson supplies the distinction between a bare ACK and application response and stages the request-completeness issue.
- **Reader knows before vs. after:** Before, Owen's quick answer appears fundamentally different from Ethan's uncertainty. After, the reader can see the hidden assumptions that make the answer testable.
- **What remains author-only:** Owen's answer-provider history and Dana's longer effort to make team cognition visible.
- **Exit condition/closing beat:** Owen leaves Ethan with the admission that he dislikes writing predictions down too.
- **Continuity facts established:** Owen's speed is real; his reasoning can be externalized; Dana tells, asks, and models according to the gap rather than using one mentoring move universally.
- **Debt passed to the next scene:** Ethan must make and preserve his own prediction, not merely understand Owen's.

## Scene 3.3 — A model reality can disagree with

- **Approximate time/location:** Continuous; Ethan's workstation, with the hidden evidence still unrevealed.
- **POV:** Ethan.
- **Scene goal:** End the narrative at the moment Ethan voluntarily accepts risk-bearing prediction, creating a clean handoff to the learner exercise.
- **Who wants what:** Ethan wants a prediction cautious enough to be honest but specific enough to test. Dana wants a durable before/after trace that makes revision visible.
- **Obstacle/conflict:** Ethan tries to make the prediction safer by listing every possible result or speaking only after Dana reveals the answer. He also treats writing as an implicit claim of confidence.
- **Information entering the scene:** Current visible evidence, the server/network-stack distinction, possible alternative outcomes, and Owen's externalized assumptions.
- **Reveal sequence:**

1. Dana presents four fields: current explanation, prediction, result, revision.
2. Ethan objects that he can tell her the answer without writing it.
3. Dana explains that memory will quietly generalize the earlier claim after the reveal.
4. Ethan records an explanation, an observable server-to-client application-data prediction, and the condition that the application handles a complete request.
5. He distinguishes reset, close, silence, and additional client data as different challenges rather than one generic failure.
6. Dana asks whether he is ready for the reveal.
7. After Dana asks whether the outcomes imply the same revision, Ethan distinguishes them and records that distinction when she prompts him to write it. This is successful guided reasoning, not yet an unprompted habit.

- **Analytical/cognitive turn:** A written prediction is not a performance of certainty; it is a record of what the current model expected so later evidence can change the right part of it.
- **Choice/decision:** Ethan preserves the prediction and agrees not to edit it after the evidence arrives.
- **Relationship movement:** Ethan begins to see purpose behind Dana's questions. He supplies the distinction himself, but Dana still prompts its recording; later episodes must earn the transition to unprompted use.
- **Technical artifact/handoff needed:** Artifact C—the prediction/outcome/revision record—implemented in the ten-field work product in [`lessons/e03-before-you-look/`](../../lessons/e03-before-you-look/README.md), using [`e03-prediction.pcap`](../../assets/pcaps/e03-prediction.pcap).
- **Reader knows before vs. after:** Before, prediction feels like guessing under artificial constraint. After, it is a visible contract between an explanation and future evidence. The actual learner-facing result remains unrevealed in the narrative.
- **What remains author-only:** Which exact part of the learner's prediction will fail cannot be assumed; the lesson permits more than one defensible initial explanation. The author must not narratively pre-answer the staged exercise.
- **Exit condition/closing beat:** Ethan says he is not ready, recognizes that readiness is irrelevant to whether he has a prediction, and tells Dana, “Yes.”
- **Continuity facts established:** Prediction/revision becomes a recurring artifact; wrongness can produce information without becoming humiliation; explanations must expose material assumptions.
- **Debt passed to Episode 4:** Ethan now expects models to generate visible sequences. DNS and vantage will show that expected conceptual behavior and observed packets are not identical.

---

# Test-slice continuity check

By the end of Episode 3:

- Ethan has not become independent of the team; he has begun learning how to use people, artifacts, and sources without surrendering judgment.
- Dana has asked, told, and modeled revision. Ethan contributes reasoning, while recording the breaker still requires a prompt. She has not supplied a hidden canonical answer.
- Owen's speed remains genuinely valuable while his compressed reasoning becomes partially visible.
- Leah has established workflow meaning that packets cannot supply, without becoming the source of the analytical conclusion.
- Nia remains a manager and is not inserted into these scenes merely to keep the full cast present.
- Priya, Cal, and Nia remain offstage because Episodes 1–3 do not yet require their information advantages.
- HarrowSync has progressed from ticket label, to two purposeful conversations, to a repeatable exchange capable of supporting a prediction.
- The three durable artifacts are a claim-transition note, a conversation/actor map, and a prediction/outcome/revision record.
- No exact HarrowSync implementation beyond committed evidence has become reader-visible canon.
