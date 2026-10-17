# Who Is Talking to Whom?

## At a glance

- **Part of:** [the narrative track](README.md) · read after [lesson 01](../lessons/01-what-the-analyst-is-for.md) and before [lesson 02](../lessons/02-reading-a-conversation.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Time:** about 10 minutes
- **Requires:** nothing. No tooling, capture, or account.
- **Creates the question:** What does it mean to explain a network conversation rather than recognize fields in it?

> Every technical value in this chapter comes from [`assets/pcaps/02-conversation.pcap`](../assets/pcaps/02-conversation.pcap), the same capture used in [lesson 02](../lessons/02-reading-a-conversation.md).

---

I came back to Dana with six sentences.

The first two were observations. The next three were interpretations. The last one stated that I did not have enough evidence to decide whether the request was expected or harmful.

I had rewritten them until every line sounded as if it had been assembled by an audit committee. I was proud of them anyway.

Dana read the sheet through once.

“This is better.”

It was the first unqualified approval she had given me all week, and I made the immediate mistake of relaxing.

She tapped the first sentence with the tip of her pen.

“What happened?”

I read it aloud to her: “The workstation made two TCP connections to the internal file service. Both completed normally.”

“That is what the log line states,” Dana said evenly. “I’m asking what actually happened on the wire.”

“Right.” I hesitated, waiting for the question to turn into something easier. When it didn't, I tried again. “The first request succeeded with a 200 OK, and the second was forbidden.”

“Better,” she said. “What did the first one request?”

“An export endpoint, followed by an administrative users endpoint.”

“And what did the export contain?”

I looked down at the Zeek connection log (`conn.log`), as if the answer might have quietly appeared in the terminal while we were talking. The row listed IP addresses, port numbers, durations, byte counts, protocol, and connection state. It did not contain an export.

“I don’t know,” I said.

“Then how do you know it was an export?”

“From the URI path in the HTTP log,” I said.

“The URI path only proves that an engineer named an endpoint `export`,” Dana said. “Did the service actually export any data?”

“It returned an HTTP `200 OK` status.”

“That answers a different question,” she said. “A two-hundred OK only tells you the web server accepted the request and sent a response. It doesn't tell you what was in the payload.”

I could feel my six carefully polished sentences getting weaker as they sat on the desk.

“You told me to separate what I observed from what I thought.”

“You did that part correctly,” she said, handing the page back. “Now I’m asking whether you understand what you saw.”

There are moments at the beginning of a technical career when you discover that two skills you had grouped together are entirely different abilities. Until that morning, I thought rigorous phrasing and technical understanding were simply two sides of being thorough. Dana had separated them with one question.

I had written a flawless grammatical description of a conversation I could not explain.

“So I need to look at the raw packets,” I said.

“Maybe you do,” Dana replied. “What is it you think the packets will give you?”

“The Zeek connection log summarizes bytes and status, but it doesn't show me the response body payload. The packets will actually have the payload.”

“In this environment, with unencrypted internal traffic, yes, they will,” she noted.

I caught the qualification. “Only in this environment?”

“Hold onto that question for when we talk about TLS,” she said. “Today we have plaintext.”

She pulled up the [[packet_capture|Wireshark packet capture (`.pcap`)]] on her secondary monitor, opened the file, and stepped aside so I had the keyboard.

The Wireshark packet list displayed a stack of colored rows. I recognized the IP addresses from the Zeek log. I recognized the TCP protocol indicators. I saw `SYN`, then `SYN, ACK`, then `ACK`, and felt a sudden flare of relief because this was one of the textbook diagrams I had spent months memorizing.

“That's the [[tcp_handshake|TCP three-way handshake]],” I said, pointing at the first three packets.

“It is,” Dana said. “Now, what does that handshake actually tell you?”

“That the connection succeeded.”

“Be specific. Which layer of the connection succeeded?”

I paused. She hadn't asked me to define a SYN packet; I had memorized the definition back when I was studying for certifications. She was asking what a completed handshake gave me the right to claim about the network.

“It tells me the transport layer connected,” I said slowly. “The client reached the server's IP address and port, and the server was listening and answered back.”

“Good,” Dana said. “Does that handshake tell you whether the HTTP request succeeded?”

“No. The client hasn't even sent the request yet.”

“Does it tell you whether the client was authenticated or authorized?”

“No.”

“Does it tell you that this is the correct server the client meant to talk to?”

“It only proves that whatever machine is sitting at that IP address accepted the TCP connection.”

Dana nodded. “Keep that distinction in your pocket. It will save you a surprising amount of wasted time.”

Someone stopped beside the desk. She carried a laptop under one arm and had the contained impatience of someone who had already explained the same problem to three other people that morning.

“Dana, are you looking at the Reporting Platform ticket?”

“Ethan is.”

That neatly transferred the impatience to me.

Dana introduced us. Leah Moreno owned the application side of the Reporting Platform. I recognized her voice from a conversation I had overheard during my first week; this was the first time we had spoken directly. I had filed her away as someone who knew what application traffic was supposed to look like. I had not understood how much hard-won context that description concealed.

“Did the finance export complete?” Leah asked.

I looked at the `200 OK` in the log, and then glanced at Dana. She gave me nothing.

“The request to the export endpoint received a successful HTTP status code,” I said carefully.

Leah waited, looking at me with an unblinking stare.

“That isn’t what I asked.”

“No,” I admitted.

“Did the export complete?”

I looked back at the Wireshark packet list, feeling the uncomfortable gap between an HTTP response header and application reality. “I don’t know yet.”

It sounded weaker out loud than it had in my head.

Leah didn't look annoyed; if anything, she seemed relieved not to be given a false reassurance. “All right. What do you know for certain?”

I pointed at the opening frames. “A client opened a TCP connection to the file service. The server completed the handshake. The client sent an HTTP GET request to the export endpoint, and the service returned a `200 OK`.”

“And?”

“And I haven’t read the response payload yet.”

“Good,” Leah said. “Because that endpoint does not return the export.”

I looked up at her.

“It returns a summary for one page,” she explained. “The actual data export runs through an entirely different workflow.”

Dana asked, “How would he have known that from the network data?”

“From the response body,” Leah said. “Or from asking me. But definitely not from the endpoint name.”

Different people can say the exact same words in ways that produce completely different reactions. When Dana said *not from the endpoint name*, it sounded like an instructional guideline. When Leah said it, it sounded like the production environment didn't care what assumptions I had brought to work.

Dana right-clicked the HTTP packet and selected Follow TCP Stream. We inspected the first [[tcp_stream|TCP stream]]. The payload was a short JSON object. It referenced a finance export, indicated that it covered 1,284 rows, and specified the file format. It was a metadata description of work, not the work itself.

My six sentences had confidently called that first request “a successful export.”

That was not what the evidence showed. The evidence showed that the service had successfully returned a summary record.

“So the transport network worked,” I said, “and the HTTP request succeeded, but I still can’t say the export itself took place.”

Leah nodded once. “Now you’re asking my question.”

She left us with the ticket still open on the screen.

Once Leah headed back toward the development pods, I turned back to the capture to examine the second connection.

The Zeek log showed the same source IP address and destination IP address, but the client was using a different [[ephemeral_port|ephemeral source port]]—42886 instead of 42876. The HTTP User-Agent string matched identically. This time, the client requested `/api/v2/admin/users`, and the server returned a `403 Forbidden`.

“It’s the same client,” I said.

Dana tilted her head slightly, waiting.

“It has the same source IP address and the same User-Agent string,” I added, trying to support the claim.

“Those are observations,” Dana said. “They make it plausible that the same client software generated both requests, but they don't prove it. Multiple processes or users behind a NAT or sharing a workstation can originate from the same IP address.”

“And the client used a different source port,” I noted, pointing at the numbers. “Because the operating system opened a fresh socket, these are technically two distinct TCP connections.”

“Exactly,” Dana said. “So you have to stop speaking about ‘the connection’ as if this entire ticket were a single event.”

Dana pulled her chair closer. “Now walk me through the first conversation from start to finish.”

I started with the handshake, because I knew the protocol terms.

She stopped me immediately. “Don't just recite packet names. Tell me what the two machines actually did.”

I took a breath and started over.

“A client initiated contact with the internal file service.”

“How do you know which host was the client?”

I checked which IP sent the initial SYN frame.

“It started the connection by sending the opening SYN.”

“Good. Continue.”

“It asked for the first page of a finance export summary. The service returned a JSON payload describing 1,284 rows. Then the service initiated a clean teardown to close the connection.”

“Now walk me through the second conversation,” Dana said.

I looked at the packets, knowing where the traps lay, but realizing that recognizing fields wasn't the same as narrating an event. At the transport layer, the TCP connection established and tore down cleanly. At the application layer, the server rejected the administrative request with a 403 Forbidden. The source IP address was identical, but the client negotiated a new ephemeral port. The User-Agent string matched, and the server closed both sessions after responding.

Each fact was straightforward in isolation, but my mind kept wanting to stitch them together into an unverified story about a malicious user, a compromised workstation, or a rogue script.

“I need to reconstruct the sequence strictly in order,” I said. “First the transport establishment, then the application request, and then the teardown.”

“Right,” Dana agreed. “And at every step, make sure you know which network layer is answering the question. Don't let an endpoint name or a status code do your thinking for you.”

Dana pushed her chair back and stood up. “That ought to keep you occupied for the afternoon.”

“Are you going to tell me what that software was actually doing?” I asked.

“Leah might tell both of us eventually,” she said with a faint smile. “But before that happens, I want to see if you can explain what the traffic shows without forcing the application owner to correct assumptions you smuggled into the report.”

She walked back toward her desk.

I opened a clean document and laid the evidence for the two conversations side by side.

This time, I didn't reach for familiar jargon or guess at human intentions.

I began with which host spoke first.

---

**What happens next.** [Lesson 02](../lessons/02-reading-a-conversation.md) opens the same capture and asks you to narrate both conversations: who contacted whom, what happened at the transport and application layers, what the packets add to the log, and what neither source can establish.
