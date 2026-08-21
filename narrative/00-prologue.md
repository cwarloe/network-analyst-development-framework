# Prologue — The Word in the Ticket

## At a glance

- **Part of:** [the narrative track](README.md) · read before [lesson 01](../lessons/01-what-the-analyst-is-for.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-20
- **Time:** about 10 minutes
- **Requires:** nothing. No tooling, no capture, no account.
- **Teaches:** nothing directly. It asks the question [lesson 01](../lessons/01-what-the-analyst-is-for.md) answers.

> Every number in this chapter is real, read out of [`assets/pcaps/02-conversation.pcap`](../assets/pcaps/02-conversation.pcap), which you will open yourself in [lesson 02](../lessons/02-reading-a-conversation.md). Nothing here is invented for effect.

---

I had been at Contoso eleven days when Dana let me take a ticket.

I want to be honest about what I thought the job was. I thought it was recognizing bad things. I had spent two years on a service desk in Portland resetting passwords and unsticking printers, and I had studied for this on my own time, and what I had studied was lists — ports, protocols, attack names, the shapes of things that were bad. I thought analysis was pattern-matching with a better vocabulary. I thought the people who were good at it had simply memorized more.

The ticket said:

> **Possible unauthorized access attempt — internal file service**

Underneath were two lines from a connection log, and I want to be accurate about how much of them I understood, because it was not much.

There were two addresses. There were two numbers I was fairly sure were ports. There were four more numbers I assumed were byte counts and one I assumed was a duration, except it was mostly zeros and I could not think of a unit that made it sensible. There was a column called `connection.state` containing the value `SF`, twice, and about that I had nothing at all.

Here is what I could actually read. Same workstation, same server, four tenths of a second apart. The first was a `GET` to an export endpoint and it came back `200 OK` with ninety bytes of JSON. The second was a `GET` to `/api/v2/admin/users` and it came back `403 Forbidden` with forty-four bytes.

`403 Forbidden` I knew. `admin` I knew.

So out of the thirty-odd pieces of information in front of me I built my answer out of the two I recognized. Then I read the title again and it agreed with me, and I felt the small hot satisfaction of knowing something.

I went and found Dana at her desk and said, "Someone's probing the admin API."

She didn't answer. She has a way of not answering that is not rude and is not friendly either. She just looks at you with mild interest, the way you'd look at a bird doing something unexpected, and waits.

After about four seconds of that I got uncomfortable enough to keep talking.

"There's a four-oh-three on `/api/v2/admin/users`. From a finance workstation. Four tenths of a second after a successful export."

"Those are three things you saw," she said. "What did you think?"

"…That someone's probing the admin API."

"Where did the word *probing* come from?"

I opened my mouth and closed it. I went back to my screen. It was not in the log. It was not in either of those two lines. It was in the ticket title, in the phrase *unauthorized access attempt*, and it had been sitting there before I opened the ticket, and I had spent four minutes assembling a case for a conclusion that somebody I'd never met had handed me on the way in.

That is the whole thing. Nobody tells you that on your first day. I want to be clear that I am not describing a mistake I made and then stopped making. I still do it. Everybody does it. The difference is that now I go looking for the word.

Dana came over and leaned on the back of my chair.

I told her I hadn't understood most of the columns, and braced for that to turn out to be the real problem.

She looked genuinely uninterested. "Which ones?"

I listed them. She stopped me about halfway down. "You'll have all of those inside a month and not one of them is the hard part. The hard part is the thing you just did with the word. I've been doing this nine years and I still do it."

Then: "All right. Somebody's poking at an admin endpoint. Who?"

"A user on a finance laptop."

"Show me the user."

I looked. The log had an address. It had a port number. It had how many bytes went each way and how long the whole thing lasted. It did not have a user. It did not have a person, or a process, or a name, or an intention. It had two machines and a number of bytes.

"It's not in there," I said.

"It's not in there," she agreed. "Keep that. It comes up constantly." She reached past me and put a finger on the column I hadn't been able to make sense of. "This one's seconds. Now — how long did the second one take?"

Nought point nought nought nought one eight four. I had to count the zeros twice. A hundred and eighty-four millionths of a second, from the first packet to the last.

"So," she said. "That's your person. Reading a page, deciding to try an admin URL, typing it in. In under a fifth of a millisecond." She stopped. "No. That's wrong, what I just said. I was about to walk you into it."

She was quiet for a second, and then: "Look at the agent string on both of them."

They were identical. `contoso-sync/3.2`. The same string on the successful export and on the `403`.

"So not someone," she said. "Something. And it's the same something that did the export four tenths of a second earlier and was allowed to. Which is a different question than the one the ticket asked, and I nearly got it wrong in front of you, so — that's the other thing to keep. I do this for a living and I still start from the story I walked in with."

I asked her what it actually was, then. Whether it was bad.

"I don't know," she said. "Neither do you. That's not a failure, it's just where we are." She counted them off on her fingers. "Is that service supposed to call that endpoint? Does it call it every time it syncs, or only today? Do the other forty finance machines do the same thing at the same time of day? And does anybody own that software well enough to answer?"

"How do I find out?"

"Some of it you can get from the traffic. Some of it you can't get from the traffic at any price, and knowing which is which is most of the job." She straightened up. "Here's what I actually want from you. Not an answer. Go write down what you *saw*, without any of the words the ticket gave you. Then, separately, write down what you think it might mean. Keep those two apart on the page. When they're apart, come find me."

It took me forty minutes and it was the hardest piece of writing I have ever done, and it was six sentences long.

---

**What happens next.** [Lesson 01](../lessons/01-what-the-analyst-is-for.md) is the thing Dana asked for — keeping observation, interpretation and judgment apart on the page. It takes about ninety minutes and needs no tools.

**If most of that log meant nothing to you, you read it correctly.** It meant nothing to him either, and Dana did not think that was the interesting part. Ports, byte counts, `connection.state`, the `SF` he had nothing at all about — those are a few weeks of exposure, and none of them was what went wrong on his first ticket.

The four questions Dana counted off are real questions with real answers, and you reach the first two in [lesson 02](../lessons/02-reading-a-conversation.md), where you open that capture yourself and read both conversations end to end. `SF` is explained there in a sentence. The `403` is waiting for you.
