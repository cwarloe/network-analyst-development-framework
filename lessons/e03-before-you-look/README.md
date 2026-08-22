# Episode 3 — Before You Look

## At a glance

- **Part of:** [the course plan](../../COURSE.md) · Book 1 [Episode 3](../../BOOK-1.md) · follows [`narrative/02-before-you-look.md`](../../narrative/02-before-you-look.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Capability targets:** IR-3, LR-1, LR-2
- **Evidence families:** EF-3, EF-8
- **Time:** about 90 minutes
- **Requires:** [`assets/pcaps/e03-prediction.pcap`](../../assets/pcaps/e03-prediction.pcap), and Wireshark or `tshark`. Zeek is useful but optional — its output is reproduced in the text.
- **Assumes:** [Lesson 02](../02-reading-a-conversation.md). You can narrate one completed conversation: who started it, what was asked, what came back, who closed it.

> This lesson works whether or not you read the narrative chapter. Nothing below depends on it.

## Why this lesson exists

After lesson 02 you can explain a conversation **you have already seen in full**. That is a real skill and it is narrower than it feels.

Explaining a completed conversation has a hidden property: the answer is on the screen while you build the explanation. You cannot tell, from the outside or from the inside, whether you understood the mechanism or described the outcome. Both produce a correct-sounding paragraph.

There is one way to tell the difference. **State what you expect before the evidence is visible, then look.**

That is what this lesson practises:

> **Explain → Predict → Check → Revise**

A prediction here is not a guess at a hidden answer. It is an **observable expectation derived from your current explanation and the assumptions underneath it**. A guess gives evidence nothing to disagree with. A prediction names a direction, a kind of event, and a condition — so that evidence can contradict a specific part of it, and you can tell which part.

Being wrong is not the failure mode. **Being unfalsifiable is.** The worked example below contains a prediction that is reasonable, derived correctly, and wrong — and the reasoning is still worth having, because the way it failed identifies exactly what to check next time.

## The one piece of mechanism you need

Only this much, and only because the exercise turns on it.

When bytes arrive at a machine, its networking software sends back an **acknowledgment** — a packet that says *these bytes arrived*. In Wireshark this shows as a packet with the `ACK` flag set and **zero bytes of payload**: a bare acknowledgment.

Three things follow, and they are the whole model for today:

- An acknowledgment is sent by the receiving machine's **networking software**, not by the program you are interested in.
- It therefore says **the bytes arrived**. It does not say the program read them, liked them, or is going to answer.
- It also does not say **the sender has finished sending.** A sender may transmit more.

That last point is the one people skip, and it is the one the worked example turns on.

> This is not lesson 02's point about a connection succeeding while a request is refused. That was about two layers disagreeing over *whether something worked*. This is narrower: an acknowledgment tells you nothing about whether the message is **complete**.

## About this evidence

The capture is synthetic — generated in a lab by [`lab/generate-captures.py`](../../lab/generate-captures.py) against real sockets, then rewritten into documentation address ranges. The protocol behaviour, timing and payloads are whatever the stack actually did; the addresses and the company are invented.

**What that means for transfer:** the *shapes* here occur constantly in real traffic. The specific byte counts, ports and hostnames do not generalise to anything. Do not carry the numbers out of this lesson; carry the moves.

Everything quoted below is derivable from the committed file. Check any of it.

---

## Worked example — a request that was not finished

Read this one through. It is a complete cycle, shown in full.

### The evidence available

One conversation, five frames so far:

```
tshark -r assets/pcaps/e03-prediction.pcap -Y "tcp.stream==0 && frame.number<=5" -T fields -e frame.number -e frame.time_relative -e ip.src -e tcp.dstport -e tcp.len
```

```
1	0.000000000	192.0.2.10	80	0
2	0.000173000	198.51.100.20	44101	0
3	0.000187000	192.0.2.10	80	0
4	0.000283000	192.0.2.10	80	163
5	0.000291000	198.51.100.20	44101	0
```

Columns: frame number, seconds since the capture started, who sent it, the port it was addressed to, and **bytes of payload**.

Frames 1 to 3 are the handshake — three packets, no payload, both directions proven. Frame 4 carries 163 bytes from the client. Read them:

```
POST /v1/inventory/batch HTTP/1.1
Host: inventory.harrowmere-internal.example
User-Agent: hsync-agent/1.4
Content-Type: application/json
Content-Length: 84
```

Frame 5 is the server's bare acknowledgment: it travels server-to-client and carries **zero bytes of payload**.

**Everything after frame 5 is hidden for now.**

### 1. Current explanation

A client opened a connection to an internal inventory service and sent a `POST` to `/v1/inventory/batch`. The server's networking software acknowledged receiving it. The application on the server has been handed a request to process.

### 2. Evidence basis

Frames 1–3 are a completed handshake, so both directions work. Frame 4 is client-to-server with 163 bytes and a readable HTTP request line. Frame 5 is server-to-client with the `ACK` flag and `tcp.len` of 0.

### 3. Material assumption

**The request the server received is complete.** Nothing in frames 1–5 confirms this. It is what makes the prediction below follow.

### 4. Observable prediction

> The next frame carrying application data will travel **from the server to the client**, and will contain an HTTP response — provided the application handles the request.

Three commitments, each separately checkable: **direction** (server to client), **kind** (an HTTP response), **condition** (the application handles it).

### 5. What would weaken or change this

- Data from the **client** instead — the request was not finished.
- A reset — something ended the conversation rather than answering it.
- A close with no response — the application declined to answer.
- Nothing further — an absence, which is not the same as any of the above.

### 6. The reveal

```
tshark -r assets/pcaps/e03-prediction.pcap -Y "tcp.stream==0 && frame.number>=6 && frame.number<=8" -T fields -e frame.number -e frame.time_relative -e ip.src -e tcp.dstport -e tcp.len
```

```
6	0.600604000	192.0.2.10	80	84
7	0.600646000	198.51.100.20	44101	0
8	0.600796000	198.51.100.20	44101	133
```

Frame 6 is **the client**, sending 84 more bytes, six tenths of a second later:

```
{"batch":"HG-7741","site":"portland","units":184,"submitted":"2026-08-22T09:41:07Z"}
```

The server's response does arrive — but in frame 8, not frame 6.

### 7. Expected against observed

The **direction** was wrong. The next data came from the client.

The **kind** and the **condition** were not tested at all. The response did eventually arrive and was an HTTP response, so nothing contradicted those — they were simply not yet in play.

This is worth separating carefully. One part of the prediction was contradicted. Two parts were merely deferred. A prediction that fails in one named part and holds in others is more useful than a vague one that cannot fail anywhere.

### 8. Revision

The explanation does not need replacing. The **assumption** does.

> A client opened a connection and sent a `POST` whose headers declared `Content-Length: 84`. It transmitted the headers first and the 84-byte body six tenths of a second later. The server acknowledged the headers on arrival, then acknowledged the body, then answered `201 Created`. A request may be delivered across more than one segment, so an acknowledgment does not establish that the request is complete.

Note what did not change: the server did answer, the application did handle it, and the conversation completed normally. **The model was sound. One assumption inside it was unchecked.**

### 9. What the evidence made available in advance

Look again at frame 4. It declares `Content-Length: 84` — the request is telling the server that 84 bytes of body are coming. The frame ends immediately after the blank line, with no body in it, and carries 163 bytes in total.

Those two facts together do not merely hint that the body was still to come. **They establish it.** The evidence needed to reject the prediction was on the screen before the prediction was made.

This is the useful residue. Not *"I was wrong"*, but *"there was a decisive fact in front of me and I did not read it as decisive."* That converts into a check that can be performed at a specific moment: **before predicting a response, confirm the request is complete.**

### 10. Remaining uncertainty

Why the client split the request across two segments is not determinable from this capture. It could be how the agent is written, a buffering effect, or a timing artifact. Nothing here settles it, and nothing here needs it settled.

---

## Guided practice — a conversation on an unfamiliar port

Different service, different server, different protocol. **The same move.**

You have one Security Onion connection record and nothing else:

```
source.ip            192.0.2.10
source.port          44103
destination.ip       198.51.100.30
destination.port     9110
network.transport    tcp
network.protocol     —
event.duration       0.301045
client.bytes         39
server.bytes         1105
connection.state     SF
```

`network.protocol` is empty. Zeek did not recognise the protocol, so it did not name one. That is an observation about Zeek, not about the traffic.

`connection.state: SF` means the conversation opened normally and both sides closed it normally — the same state lesson 02's two conversations carried.

**Before you look at the packets**, record all five of these. Prompts, not answers:

1. **Current explanation.** What is this conversation, in a sentence you would defend? The client sent 39 bytes and received 1,105 — what kind of exchange does that shape suggest?
2. **Evidence basis.** Which specific fields above support it?
3. **Material assumption.** You are about to predict who sends application data first. What are you assuming that the record does not state? Write the assumption itself, not the prediction.
4. **Observable prediction.** Name a **direction**, a **kind**, and a **condition**. Which side sends the first application data, roughly how much, and under what circumstance would that not hold?
5. **What would weaken or change it.** What would you have to see to know you were wrong?

Question 3 is the one to spend time on. Nearly everyone predicts this conversation correctly in shape and incorrectly in one specific respect, and the assumption behind the error is not usually visible until it is written down.

When all five are written, open **[reveal 1](reveal-1-guided.md)**.

---

## Your work product — the conversation that stops

A third conversation, on the same capture. Same client, same internal service as the worked example.

```
source.ip            192.0.2.10
source.port          44102
destination.ip       198.51.100.20
destination.port     80
network.transport    tcp
network.protocol     http
event.duration       0.000164
client.bytes         138
server.bytes         0
connection.state     S1
```

And the HTTP record for the same conversation:

```
http.method                GET
http.virtual_host          inventory.harrowmere-internal.example
http.uri                   /v1/inventory/summary
http.status_code           —
http.response.body.length  0
```

Two things to note before you start.

**`connection.state: S1`** means the connection was established and **was not seen to close**. It is not a fault code. Lesson 02's conversations were `SF` — opened and closed normally. This one opened and, in this record, does not end.

**`http.status_code` is empty.** Not zero, not an error — absent. Zeek writes what it saw.

### What to produce

A record with **all ten fields below**, written in this order. Fields 1 to 5 must be complete before you open the reveal, and **must still be readable afterwards.**

| | Field |
|---|---|
| 1 | **Current explanation** — what you think is happening |
| 2 | **Evidence basis** — the specific fields or frames it rests on |
| 3 | **Material assumption** — what you are taking as true that the evidence does not state |
| 4 | **Observable prediction** — direction, kind, condition |
| 5 | **What would weaken or change the explanation** |
| — | *stop here and open the reveal* |
| 6 | **Observed result** — what the evidence actually shows |
| 7 | **Meaningful difference** — which part of the prediction the evidence engaged, and which parts it did not touch |
| 8 | **Revised explanation** |
| 9 | **What remains unresolved** |
| 10 | **Specific learning need** — what you would check earlier next time |

**Do not edit fields 1 to 5 after the reveal.** If field 4 turns out to be wrong, leaving it wrong is the point — field 7 is where the difference gets written, and it has nothing to compare against if field 4 has been quietly improved. A revision trace that shows no revision is not evidence of accuracy; it is evidence of editing.

At least two different explanations of this record are defensible on the evidence given. Pick the one you actually hold and say why — do not hedge across all of them, and do not pick one because it feels safer.

Copy this and fill it in:

```
1. CURRENT EXPLANATION

2. EVIDENCE BASIS

3. MATERIAL ASSUMPTION

4. OBSERVABLE PREDICTION
   direction:
   kind:
   condition:

5. WHAT WOULD WEAKEN OR CHANGE IT

--- stop. open the reveal. do not edit anything above this line. ---

6. OBSERVED RESULT

7. MEANINGFUL DIFFERENCE
   engaged by the evidence:
   not tested by the evidence:

8. REVISED EXPLANATION

9. WHAT REMAINS UNRESOLVED

10. SPECIFIC LEARNING NEED
```

When fields 1 to 5 are written, open **[reveal 2](reveal-2-work-product.md)**.

Then use the **[review guide](review-guide.md)**.

---

## Reviewing your own work

The [review guide](review-guide.md) carries the full set. The three that matter most:

- Was your prediction specific enough that evidence could disagree with a **named part** of it?
- Did you distinguish **contradicted** from **not yet tested**? Those license different revisions.
- Did your revision explain **why** the model changed, or does it just restate the outcome?

## What this lesson does not do

It does not teach TCP. Sequence numbers, windows, retransmission, congestion behaviour and the full set of connection states are outside it, and one `S1` record is not a substitute for any of them.

It does not teach failure diagnosis. Telling a refused connection from a dropped one, a reset from a timeout, or a network delay from an application delay is [lesson 06](../06-when-it-breaks.md)'s subject, and this lesson deliberately contains no faults at all — every conversation here is working correctly.

It does not establish that you can now predict reliably. Three predictions on one synthetic capture is a small sample of one behaviour, and no score, level or threshold is defined anywhere in it.
