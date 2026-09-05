# Before You Look

## At a glance

- **Part of:** [the narrative track](README.md) · read after [lesson 02](../lessons/02-reading-a-conversation.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Time:** about 8 minutes
- **Requires:** nothing. No tooling, capture, or account.
- **Creates the question:** How can a prediction expose whether an explanation is usable before the answer is visible?
- **Technical exercise:** [`lessons/e03-before-you-look/`](../lessons/e03-before-you-look/README.md) is built and uses [`e03-prediction.pcap`](../assets/pcaps/e03-prediction.pcap).

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

Owen Kline rolled his chair around the divider. I had already learned that asking Owen was the fastest route to an answer and the easiest way to miss how he got there.

“Is this the prediction thing?” he asked.

“Apparently.”

“Dana loves the prediction thing.”

“Owen hates the prediction thing,” Dana said.

“I hate writing it down,” Owen said.

“Why?”

Owen looked at me instead of answering Dana. “Because when the next packet is different, she won’t let you claim you meant something more general.”

“You usually did mean something more general,” Dana said. “Afterward.”

Owen moved closer to the screen. “What do we have?”

I told him: established connection, request delivered, server acknowledgment, no application response visible yet.

“It’ll respond,” Owen said.

Dana waited.

Owen sighed. “The next application data will travel from the server to the client.”

“Why?”

“Assuming the client has finished its request and the application handles it, I expect a response.”

“Does acknowledgment mean the application accepted the request?”

“No. It means the server’s TCP stack received the bytes.”

“So what assumption is underneath your prediction?”

Owen looked at the visible rows. “That these bytes constitute the complete request, and that the application is running and eventually handles it. The acknowledgment alone establishes neither.”

Dana looked at me.

I said, “That still sounds like guessing with extra steps.”

“A guess gives reality nothing to disagree with,” Dana said. “Owen just gave it three things. Direction: server to client. Kind: application data. Condition: the application handles the request. If the connection resets instead, which part changes?”

“The application may not have handled it.”

“Or?”

“Something else ended the connection.”

“And if there’s a long silence before a normal response?”

I thought about the bare acknowledgment in the earlier capture—the server saying *received* before it said *answered*.

“Then the request reached the server quickly, but whatever generated the response took longer.”

“Can you say why?”

“Not from that alone.”

Dana nodded. “Now you have a model that can be wrong in a useful way.”

Owen said, “This is the point where she makes you write it down.”

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

Owen laughed, but not at me.

“She got me with that one too,” he said.

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

**What happens next.** [`Episode 3 — Before You Look`](../lessons/e03-before-you-look/README.md) preserves your initial explanation and prediction before releasing the result. Its purpose is not to reward guessing the next packet. It makes the difference between expectation and observation visible, then requires a reasoned revision.
