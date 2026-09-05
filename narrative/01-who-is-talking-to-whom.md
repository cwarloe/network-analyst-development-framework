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

The first two were observations. The next three were interpretations. The last one said I did not have enough evidence to decide whether the request was expected or harmful.

I had rewritten them until every sentence sounded as if it had been assembled by a committee. I was proud of them anyway.

Dana read the page once.

“This is better.”

It was the first unqualified approval she had given me, and I made the mistake of relaxing.

She tapped the first sentence.

“What happened?”

I read it to her. “The workstation made two TCP connections to the internal file service. Both completed normally.”

“That’s what the line says.”

“Right.”

“What happened?”

I waited for the question to become a different question. It did not.

“The first request succeeded and the second was forbidden.”

“Better. What did it request?”

“An export, and then the admin users endpoint.”

“What did the export contain?”

I looked back at the connection log, as if the answer might have appeared while we were talking. The row had addresses, ports, durations, byte counts, protocol, and state. It did not have an export.

“I don’t know.”

“Then how do you know it was an export?”

“The URI.”

“The URI says somebody named an endpoint `export`. Did the service actually export anything?”

“It returned `200 OK`.”

“That answers a different question.”

I could feel the six sentences getting worse while they sat on the desk.

“You told me to separate what I saw from what I thought.”

“You did.” She handed the page back. “Now I’m asking whether you understand what you saw.”

There are moments at the beginning of a new job when you discover that two abilities you had grouped together are not the same ability. Until then, I thought careful wording and technical understanding were two parts of being precise. Dana had separated them with one question.

I had written an accurate description of a conversation I could not explain.

“So I need the packets,” I said.

“Maybe.”

“The connection log doesn’t have the response body.”

“Correct.”

“The packets do.”

“These do.”

I noticed the qualification. “Not always?”

“Keep that question. Not for today.”

She opened the capture and then moved aside before I could pretend I knew what I was looking at.

The display was a stack of colored rows. I recognized the addresses from the log. I recognized `TCP`. I saw `SYN`, then `SYN, ACK`, then `ACK`, and felt a small flare of relief because this was one of the diagrams I had memorized.

“Three-way handshake,” I said.

“Yes.”

I waited for the satisfaction to last longer than it did.

“What does that tell you?” she asked.

“The connection succeeded.”

“Which connection?”

“The first one.”

“At which layer?”

I stopped.

She had not asked what a SYN was. I knew what a SYN was. She had asked what the completed handshake allowed me to claim.

“The client could reach the server and the server could answer.”

“Good. Does it tell you the request succeeded?”

“No. The request hasn’t happened yet.”

“Does it tell you the client was authorized?”

“No.”

“Does it tell you this is the right server?”

“It tells me the server at that address answered.”

Dana nodded. “That distinction will save you a surprising amount of time.”

Someone stopped beside the desk. She had a laptop under one arm and the contained impatience of a person who had already explained a problem somewhere else.

“Dana, are you looking at the Reporting Platform ticket?”

“Ethan is.”

That transferred the impatience to me.

Dana introduced us. Leah Moreno owned the application side of the Reporting Platform. I recognized her voice from a conversation I had overheard during my first week; this was the first time we had spoken directly. I had filed her away as someone who knew what application traffic was supposed to look like. I had not understood how much work that description concealed.

“Did the finance export complete?”

I looked at the `200 OK` in the log. Then at Dana. She gave me nothing.

“The request to the export endpoint received a successful HTTP status,” I said carefully.

Leah waited.

“That isn’t what I asked.”

“No.”

“Did the export complete?”

I looked at the packet list again. “I don’t know yet.”

It sounded weaker out loud than it had in my head.

Leah did not seem offended by it. “All right. What do you know?”

I pointed at the first rows. “A client opened a TCP connection to the file service. The server answered. The client sent an HTTP request to the export endpoint. The service returned `200 OK`.”

“And?”

“And I haven’t read the response.”

“Good,” Leah said. “Because that endpoint does not return the export.”

I looked at her.

“It returns a summary for one page. The actual export is another workflow.”

Dana asked, “How would he have known that?”

“From the response body. Or from me. Not from the endpoint name.”

Different people can say the same thing in ways that produce different feelings. When Dana said *not from the endpoint name*, it sounded like a lesson. When Leah said it, it sounded like the system did not care what I had assumed.

We opened the first stream. The body was short JSON. It named a finance export, said it covered 1,284 rows, and identified the format. It was a description of work, not the work itself.

My six sentences had called the first request “a successful export.”

That was not what the evidence said. The evidence said the service successfully returned a summary.

“So the network worked,” I said, “and the HTTP request succeeded, but I still can’t say the export completed.”

Leah nodded. “Now you’re asking my question.”

She left us with the ticket still open.

I looked at the second connection. Same source address. Same destination address. Different source port. Same user-agent string. A request to `/api/v2/admin/users`. `403 Forbidden`.

“It’s the same client,” I said.

Dana tilted her head.

I tried again. “The same source address.”

Nothing.

“The same user-agent.”

“Those are observations.”

“They support it being the same software.”

“They do.”

“But they don’t prove it.”

“They don’t.”

I pointed at the two source ports. “And these are separate connections.”

“Yes.”

“So I need to stop talking about ‘the connection’ as if the whole ticket is one event.”

Dana pulled her chair over. “Tell me the first conversation.”

I started with the handshake, because I knew its name.

She stopped me. “Not the packet names. Tell me what the machines did.”

I started again.

“A client contacted the internal file service.”

“How do you know which one was the client?”

I looked at who sent the first SYN.

“It started the connection.”

“Good. Continue.”

“It asked for the first page of a finance export summary. The service returned JSON describing 1,284 rows. Then the service closed the connection.”

“Now the second.”

I could read enough of it to know where the traps were. That was not the same thing as being able to narrate it.

The connection was successful. The request was refused. The source address was the same. The source port was different. The user-agent matched. The server closed both conversations. Each statement was easy by itself. Together they kept trying to become a story about a person, a program, or an attack.

“I need to go through it in order,” I said.

“Yes.”

“And keep asking which layer each answer belongs to.”

“Yes.”

“And not use the endpoint name as an explanation.”

Dana stood. “That should keep you busy.”

“Are you going to tell me what the software was doing?”

“Leah may eventually tell both of us. But first I want to know whether you can tell her what the network shows without making her correct the parts you invented.”

She walked away.

I opened a blank page and put the two conversations side by side.

This time I did not begin with the words I recognized.

I began with who spoke first.

---

**What happens next.** [Lesson 02](../lessons/02-reading-a-conversation.md) opens the same capture and asks you to narrate both conversations: who contacted whom, what happened at the transport and application layers, what the packets add to the log, and what neither source can establish.
