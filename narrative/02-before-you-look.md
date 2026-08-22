# Before You Look

## At a glance

- **Part of:** [the narrative track](README.md) · read after [lesson 02](../lessons/02-reading-a-conversation.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Time:** about 8 minutes
- **Requires:** nothing. No tooling, capture, or account.
- **Creates the question:** How can a prediction expose whether an explanation is usable before the answer is visible?
- **Technical debt:** The staged evidence exercise that follows this chapter is assigned to Curriculum/Engineering Studio and is not yet authored.

---

After working through the two conversations from my first ticket, I could reconstruct what Dana had made me do.

On those conversations, with the completed evidence in front of me, I could point to the handshake and say that both directions worked. I could point to the `403` and keep the application refusal separate from the transport connection underneath it. If somebody asked who closed first, I knew where to look.

That was real progress. It was also narrower than it felt.

I had learned to explain a result I could already see, in a case I had already worked. I had not learned how to use the same model when the next part was missing.

Dana found the problem before I did.

She put an unfamiliar capture on my screen and hid everything below the first exchange.

“What happens next?”

“How would I know?”

“You’ve been explaining what happens next all morning.”

“After it happens.”

“Yes.”

I looked at what she had left visible. A client had established a connection and sent a request. The server had acknowledged receiving it. Nothing on the screen showed the application response.

“The server responds,” I said.

“With what?”

“I don’t know.”

“Then what do you know?”

“The next application data should come back from the server.”

“Should?”

“If it processed the request.”

“Good. What else could happen?”

“It could close the connection. Reset it. Not answer.”

“Those are possibilities. Which one do you expect?”

“I still don’t know.”

Dana folded her arms. “You’re treating uncertainty as a reason not to commit to anything.”

“Because the answer is under your hand.”

“The answer is always under somebody’s hand. A later packet. A server log. A system owner. Tomorrow morning. If you wait until it arrives before saying what your explanation expected, you can make every result sound inevitable.”

I did not like that, which usually meant I had understood it.

Nia Alvarez rolled her chair around the divider. I had spoken to her twice since joining Harrowmere. Both times she had been friendly in a way that made it impossible to tell whether she was helping me or collecting material.

“Is this the prediction thing?” she asked.

“Apparently.”

“Dana loves the prediction thing.”

“Nia hates the prediction thing,” Dana said.

“I hate writing it down.”

“Why?”

Nia looked at me instead of answering Dana. “Because when the next packet is different, she won’t let you claim you meant something more general.”

“You usually did mean something more general,” Dana said. “Afterward.”

Nia moved closer to the screen. “What do we have?”

I told her: established connection, request delivered, server acknowledgment, no application response visible yet.

“It’ll respond,” Nia said.

Dana waited.

Nia sighed. “The next application data will travel from the server to the client.”

“Why?”

“Because the client sent a complete request to a listening service and the server acknowledged it.”

“Does acknowledgment mean the application accepted the request?”

“No. It means the server’s TCP stack received the bytes.”

“So what assumption is underneath your prediction?”

Nia looked at the hidden part of the screen. “That the application is running and eventually handles what the network stack delivered.”

Dana looked at me.

I said, “That still sounds like guessing with extra steps.”

“A guess gives reality nothing to disagree with,” Dana said. “Nia just gave it three things. Direction: server to client. Kind: application data. Condition: the application handles the request. If the connection resets instead, which part changes?”

“The application may not have handled it.”

“Or?”

“Something else ended the connection.”

“And if there’s a long silence before a normal response?”

I thought about the bare acknowledgment in the earlier capture—the server saying *received* before it said *answered*.

“Then the request reached the server quickly, but whatever generated the response took longer.”

“Can you say why?”

“Not from that alone.”

Dana nodded. “Now you have a model that can be wrong in a useful way.”

Nia said, “This is the point where she makes you write it down.”

Dana gave me a blank page.

At the top she had put four headings:

**Current explanation.**

**Prediction.**

**Result.**

**Revision.**

The last two were empty.

“I can just tell you,” I said.

“You can tell me after I move my hand.”

“And you won’t believe that was my answer before?”

“I will believe you. You will believe you. That’s the problem.”

Nia laughed, but not at me.

“She got me with that one too,” she said.

I wrote:

> The client established a two-way connection and delivered a request to the server. I expect the next application data to come from the server to the client if the application handles the request. A TCP acknowledgment alone does not predict whether that response will indicate success.

Dana read it.

“What would make you revise?”

“A reset. A close with no response. No response at all.”

“Those are different results. Would they all produce the same revision?”

I started to say yes, then stopped. A reset was an event. Silence was an absence from one observation point. They did not carry the same information.

“No.”

“Write that part too.”

I did.

The explanation on the page looked embarrassingly cautious. It also looked checkable. For the first time, I could see exactly what the next evidence might damage.

Dana rested her hand on the hidden rows.

“Ready?”

I was not. That was different from having no prediction.

“Yes.”

---

**What happens next.** The technical exercise must preserve your initial explanation and prediction before releasing the result. Its purpose is not to reward guessing the next packet. It is to make the difference between expectation and observation visible, then require a reasoned revision.
