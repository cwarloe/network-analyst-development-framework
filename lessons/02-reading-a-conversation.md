# Lesson 02 — Reading a Conversation

## At a glance

- **Part of:** [the course plan](../COURSE.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-19
- **Capability targets:** OC-1, OC-2, OE-1
- **Evidence families:** EF-1, EF-2
- **Time:** about 2 hours
- **Requires:** [`assets/pcaps/02-conversation.pcap`](../assets/pcaps/02-conversation.pcap) and Wireshark, or `tshark` at a terminal. Everything else is in this file.
- **Assumes:** [Lesson 01](01-what-the-analyst-is-for.md). You can separate what you saw from what you concluded.

## Why this lesson exists

Lesson 01 was about not overstating. This one is about having something to state.

Before you can say that anything is unusual, you have to be able to say what happened — precisely, in order, with the parts labelled. Most bad analysis is not bad judgment applied to good observation. It is confident judgment applied to a conversation the analyst never actually read.

The unit you read is a **conversation**: one client, one server, one port pair, from open to close. Everything in this course is built on being able to narrate one.

## Where this data came from

The capture in `assets/pcaps/` was generated in a lab by [`lab/generate-captures.py`](../lab/generate-captures.py). The traffic is real — a real client, a real server, a real TCP stack — and then the addresses were rewritten into documentation ranges so it reads as an ordinary internal exchange. Protocol behaviour, timing and payloads are untouched.

It is checked two ways before it ships: Wireshark must dissect it cleanly, and Zeek must parse it into logs. See [the lab README](../lab/README.md) for why that second check is the one that matters.

## Start where you would actually start

In a Security Onion deployment you do not open Wireshark first. You start in Hunt or Kibana, looking at what Zeek already made of the traffic. Zeek's `conn.log` is the index of every conversation it saw:

```
ts                   uid                id.orig_h    id.orig_p  id.resp_h       id.resp_p  proto  service  duration    orig_bytes  resp_bytes  conn_state
1755589200.000000    CHhAvVGS1DHFjwGM9  192.0.2.10   42876      198.51.100.20   80         tcp    http     0.000688    151         207         SF
1755589200.401037    ClEkJM2Vm5giqnMf4h 192.0.2.10   42886      198.51.100.20   80         tcp    http     0.000554    149         144         SF
```

Two conversations. Same client, same server, same service. Read the columns you will use for the rest of your career:

- **`id.orig_h` / `id.orig_p`** — who started it, and from which ephemeral port. Different port each time: **these are two separate conversations, not one.**
- **`id.resp_h` / `id.resp_p`** — who was contacted, on which service port.
- **`conn_state: SF`** — normal establishment and normal teardown. Both sides said hello and both said goodbye.
- **`orig_bytes` / `resp_bytes`** — 151 out, 207 back; then 149 out, 144 back.

Already there is something worth noticing, and it is worth stopping on before you read any further: **the second conversation got a smaller response than the first.** That is an observation. It is not yet anything else.

## The shape of a conversation

Open the capture. The first ten frames are one complete conversation:

```
No.  Time      Source          Destination     Info
1    0.000000  192.0.2.10      198.51.100.20   42876 → 80 [SYN] Seq=0 Win=65495
2    0.000017  198.51.100.20   192.0.2.10      80 → 42876 [SYN, ACK] Seq=0 Ack=1
3    0.000031  192.0.2.10      198.51.100.20   42876 → 80 [ACK] Seq=1 Ack=1
4    0.000075  192.0.2.10      198.51.100.20   GET /api/v2/export?page=1 HTTP/1.1
5    0.000079  198.51.100.20   192.0.2.10      80 → 42876 [ACK] Seq=1 Ack=152
6    0.003966  198.51.100.20   192.0.2.10      HTTP/1.1 200 OK  (application/json)
7    0.003977  192.0.2.10      198.51.100.20   42876 → 80 [ACK] Seq=152 Ack=208
8    0.004019  198.51.100.20   192.0.2.10      80 → 42876 [FIN, ACK] Seq=208 Ack=152
9    0.004038  192.0.2.10      198.51.100.20   42876 → 80 [FIN, ACK] Seq=152 Ack=209
10   0.004053  198.51.100.20   192.0.2.10      80 → 42876 [ACK] Seq=209 Ack=153
```

Three phases, and you should be able to point at each one:

**Frames 1–3, the handshake.** SYN, SYN-ACK, ACK. This is the part that proves a two-way path exists. A SYN with no SYN-ACK means your packet arrived nowhere, or the answer could not get back — and those two are very different problems that look identical from here.

**Frames 4–7, the exchange.** The client sends 151 bytes of request. Frame 5 is worth its own sentence: it is a **bare ACK carrying no data**, the server saying *received* before it says *answered*. Receipt and response are separate events. When someone reports that a service "didn't respond," the difference between no ACK and an ACK with no reply tells you which half of the system to look at.

**Frames 8–10, the teardown.** FIN, FIN, ACK — and notice **the server sent the first FIN.** The client asked for the connection to be closed (`Connection: close`) and the server obliged after answering. Who hangs up first is a real signal, and it is one of the first things that changes when something is wrong.

## What the packets add that the log did not

The Zeek log told you 151 bytes went out. The packets tell you what they were:

```
GET /api/v2/export?page=1 HTTP/1.1
Host: files.contoso-internal.example
User-Agent: contoso-sync/3.2
Accept: application/json
Connection: close
```

And the answer:

```
HTTP/1.1 200 OK
Server: nginx/1.24.0
Content-Type: application/json
Content-Length: 90
X-Request-Id: 7f3a91c2

{"report":"finance-export","rows":1284,"generated":"2026-08-19T09:14:22Z","format":"json"}
```

This is the pivot, and it is the working pattern for everything that follows: **the log tells you a conversation happened and roughly what shape it was; the packets tell you what was said.** You go to the log to find the conversation. You go to the capture to read it.

Narrated in one sentence: *a host called `contoso-sync/3.2` asked an internal file service for page 1 of a finance export, and the service returned a 90-byte JSON summary describing 1,284 rows.*

That sentence contains no judgment. It is what happened.

## Your work product — the second conversation

Frames 11–20 are the second conversation. Read them yourself and write a description of it.

```
tshark -r assets/pcaps/02-conversation.pcap -Y "frame.number >= 11"
```

Or in Wireshark: right-click any frame from 11 onward → Follow → TCP Stream.

Write **half a page** that answers all of the following. Every answer is checkable against the file, so check it.

1. **Narrate the conversation** the way the first one was narrated above: one sentence, no judgment, naming who asked what of whom and what came back.
2. **Is this the same conversation as the first one, continued?** Justify your answer by pointing at a specific field.
3. **Did the TCP connection succeed?** Did the request succeed? These are two questions. Answer them separately and say which evidence answers which.
4. **Who closed the connection, and does it differ from the first conversation?**
5. **The response was 144 bytes against the first response's 207.** Give at least two different explanations for a smaller response, and say what in the capture distinguishes them.
6. **What did the client do differently between the two conversations?** There is more than one answer.
7. **What can you not determine from this capture?** Name at least three things. Be specific — "I don't know everything" is not an answer, but "I cannot tell whether this client is authorised to make this request, because authorisation state lives on the server and is not on the wire" is.

## The thing this lesson is really about

Question 3 is the lesson.

The second conversation completes perfectly. Handshake, request, response, clean teardown, `conn_state: SF` in Zeek's log — by every measure at the transport layer, it worked. And the application said **403 Forbidden**.

Both statements are true, at different layers, and an analyst who collapses them into one verdict will be wrong in one direction or the other:

- Read only the Zeek `conn_state`, and you report a successful connection to a service. True, and it hides that access was refused.
- Read only the HTTP status, and you report a failure. True, and it hides that the network delivered everything correctly and the refusal was a deliberate decision by the application.

"Did it work?" is not one question. It is a question per layer, and the layers can disagree. Getting into the habit of asking *which layer are you asking about* is worth more than any amount of protocol memorisation.

This is also lesson 01's distinction arriving in technical form. *The connection completed* is an observation. *The request was refused* is an observation. *Someone is probing for admin access* is an interpretation, and this capture does not contain enough to support it.

## Reviewing your own work

- Read your narration back. Does any word in it assert intent, authorisation, or wrongdoing? Cross those out and see whether the sentence still says something.
- For each claim, name the frame number it rests on. A claim with no frame behind it is a guess wearing a uniform.
- Did you answer question 3 with two separate answers, or did you merge them? If you merged them, go back — that is the whole lesson.
- On question 5, did you actually check the response body, or did you infer from the byte count? The file will tell you. Inferring when the answer is available is a habit worth catching early.
- Did any of your "cannot determine" items turn out to be determinable if you looked harder? That is a good failure. Note which, and what made you assume it was unavailable.
- If a colleague read your description with no access to the capture, could they say what happened? Could they say what you were unsure of?

## What this lesson does not do

It does not establish that this traffic is normal or abnormal. Two conversations from one client is not a baseline, and lesson 03 is where expected behaviour starts being built deliberately.

It does not teach you the tool. Wireshark's filter language, column layouts and stream reassembly are worth learning and this lesson does not attempt to cover them.

It does not define proficiency, scoring, or completion. One narrated conversation is a single sample.
