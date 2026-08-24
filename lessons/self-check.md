# What do you already have?

Optional. About fifteen minutes. **No score, no threshold, and nobody sees it but you.**

This is not a test and not an entry requirement. Nothing here gates anything. It exists because the course assumes a small number of things it never teaches, and because the most common way to be missing one of them is **not knowing you are missing it**.

## Why "do you know X?" does not work

If you have studied for a certification, or picked things up at work, you almost certainly recognise every term below. Recognition is not the thing the lessons need.

The lessons need these as **working models** — enough structure to predict what should happen next and notice when it does not. Recall and model feel identical from the inside, and the only reliable way to tell them apart is to try to produce an explanation and see what comes out.

So each item asks you to **write something** before you read on. Two sentences is enough. If you skip the writing and just read, the check does not work — you will recognise every answer and learn nothing about yourself.

That is the same move the course teaches, applied to you. [Episode 3](e03-before-you-look/README.md) makes the argument at length: an explanation you produce before seeing the answer is checkable, and one you assemble afterwards is not.

## How to take it

For each item: **write your answer, then read what follows it.** Compare the shape of yours against the shape described — not the wording.

Mark each one *had it*, *partly*, or *no*. Keep the list. That list is the only output.

---

## 1. Two things being true at once

> A parcel arrives at your door. The courier delivered it correctly and on time. Inside is a letter saying your application was refused.
>
> **Write:** what does each of those two facts establish, and what does neither establish?

**A usable answer** treats them as two separate systems with separate success conditions — the delivery worked, the decision went against you — and does not try to make one of them the "real" answer. It also notices that neither says anything about *why* the application was refused.

**If yours collapsed them** into a single verdict, or reached for which one "really" mattered, that is worth knowing. The course rests on holding two true statements about the same event without merging them, and it is the single most load-bearing habit in the sequence. **You do not need to fix this now** — it is what [lesson 02](02-reading-a-conversation.md) is built to develop, and arriving without it is normal.

## 2. Who started it

> Two machines have been talking. You have a record of the conversation.
>
> **Write:** how would you work out which one started it, and why does it matter which one did?

**A usable answer** names something *observable* — who sent the first thing, who asked and who answered — rather than a role assumed from what the machines are. On why it matters: the initiator is usually the one that decided to do something, which is usually the one you are investigating.

**If yours assumed the roles** from the names or addresses ("the workstation is obviously the client"), that is the gap. It is common and it is quiet, because the assumption is usually right and silently wrong exactly when it matters. Lesson 02 states the rule; [Episode 2](../narrative/01-who-is-talking-to-whom.md) has the character derive it, if you would rather see it worked.

## 3. Ports

> **Write:** what does a port number identify? And why does the same machine use a different one every time it makes a new connection?

**A usable answer** has a port identifying **which service or conversation on a machine**, not the machine itself — and the second half explains that the side making the call picks a fresh throwaway number each time, so that several conversations to the same place stay separate.

**If the second half was fuzzy**, that is the more useful gap. It is why two log lines with the same two addresses can be two different conversations, and it comes up from lesson 02 onward.

**The short version, if you want it now:** a machine has one address and many numbered doors. A service waits at a fixed door — 80, 443, 53. Anything calling out grabs an unused high-numbered door for that one conversation and releases it afterwards. The pair of doors is what makes each conversation distinct.

## 4. Packet and frame

> **Write:** are "packet" and "frame" the same thing? If not, what is the difference?

**A usable answer** either distinguishes them by level — a frame is what crosses one physical hop, a packet is what travels end to end — or honestly says *"people use them interchangeably and I have never been sure."*

**Both of those are fine.** This one is vocabulary rather than mechanism, and the honest answer is that the course itself uses the words loosely, as most practitioners do. It is here so that if you have been quietly unsure, you know it is the words that are slippery and not you.

## 5. The three-letter flags

> You have seen `SYN`, `ACK` and `FIN`.
>
> **Write:** what is each one *for*? Not the order they come in — what does each one mean when it appears?

**A usable answer** treats them as **signals with meanings** — roughly *I would like to start*, *I received what you sent*, *I am finished sending* — rather than as the names of steps in a memorised sequence.

**If you could produce the handshake order but not the individual meanings**, that is the specific gap this item exists to find, and it is extremely common in certification-shaped knowledge. It does not block anything early. It blocks in [lesson 06](06-when-it-breaks.md), where telling a refused connection from an ignored one depends entirely on *which* signal came back. **Do not go and study it now** — lesson 06 develops it, and it is more useful arriving there and meeting the distinction on real evidence.

## 6. TCP and UDP

> **Write:** what does using TCP get you that UDP does not, and what does that cost?

**A usable answer** names something about **delivery being tracked and put back in order**, and a cost in setup or delay. It does not need to be precise about mechanisms.

**If you named the difference but not the cost**, that is the recall-shaped version. Nothing in the course blocks on it, but it shows up as background whenever a design choice looks strange.

## 7. What an address tells you

> **Write:** you have an IP address that did something. What does it identify, and what are the ways it might not identify what you think?

**A usable answer** gets to *an address is not reliably a person, and often not reliably a machine* — because of shared addresses, translation at a boundary, reassignment over time, or a device with several.

**If your answer was confident that an address identifies a host**, that is worth marking. It is not developed until [lesson 05](05-vantage-point-and-evidence.md), and it is the most common source of overstated findings in real reports.

---

## What to do with your list

**Probably nothing.** That is the honest answer and it is not a dodge.

Items 1, 2, 5 and 7 are all developed by the course — that is what lessons 02, 05 and 06 are *for*. A gap on those is not a deficiency to repair before starting; it is the reason the lesson exists. Studying ahead would mean arriving at the lesson already holding the answer it is designed to make you derive, which is a worse experience and a worse outcome.

Items 3, 4 and 6 are not developed anywhere, and each has its short version written above. If one of those was a *no*, you have already closed it by reading the paragraph.

**The list itself is the point.** Knowing that you hold `SYN` as a step rather than a signal changes how you read lesson 06 — you will notice yourself reaching for the sequence, and that noticing is the thing.

### If it all came out clean

Worth pausing on, because there are two ways to get there.

The check separates **recall** from a **working model**. It does not separate a working model from **fluency** — being practised at explaining things well. If your background is stronger on method and process than on concrete mechanism, your answers will come out properly shaped either way: hedged in the right places, careful about what is established and what is assumed. That is a real skill and it is most of what the course is trying to build. It is also the one thing that can hide a missing mechanism from this check, because shape is what the check compares against.

Two items are worth a second pass, because both need a mechanism and nothing else substitutes:

- **Item 3.** The same machine opens three connections to the same server, all to port 443. Of the four numbers that identify a connection, how many differ between the three, and which ones? Write the count.
- **Item 5.** A machine sends a `SYN` and gets back a segment with `RST` and `ACK` set. Something else sends a `SYN` and gets back nothing at all. What is materially different about those two situations?

Item 3 you can settle from the paragraph already written above it. **Item 5 is deliberately not answered here** — if you cannot produce a confident account, that is the expected result and [lesson 06](06-when-it-breaks.md) is built on exactly that distinction. The point is only to notice which of the two you were.

## If you are running this with someone else

Ask them to take it before lesson 01 and keep the list. Then, in the [run record](run-records.md#the-template), note **which items they marked and whether the ones they marked *no* actually caused trouble.**

That is the only way to find out whether [the assumed-knowledge list](../docs/assumed-knowledge.md) describes real difficulty or only difficulty in the text. It currently records about thirty-five assumed concepts and **no evidence at all about which ones stop a person.**

## What this does not do

It does not measure anything. There is no score, no level, no threshold, and no interpretation of the pattern of your answers — the [Standing Qualifications](../docs/architecture.md) rule those out and nothing here is validated well enough to support them anyway.

It does not cover everything the lessons assume. [`docs/assumed-knowledge.md`](../docs/assumed-knowledge.md) lists the full inventory; this is the handful that are load-bearing, which is a judgment made by reading the lessons rather than by watching anyone use them.

And it cannot tell you whether you will find the course hard. Seven prompts is a very small sample of a person.
