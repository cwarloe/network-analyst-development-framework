# Lesson 02 — Reading a Conversation

## At a glance

- **Part of:** [the course plan](../COURSE.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-19
- **Capability targets:** OC-1, OC-2, OE-1
- **Evidence families:** EF-1, EF-2
- **Time:** about 2 hours
- **Requires:** [`assets/pcaps/02-conversation.pcap`](../assets/pcaps/02-conversation.pcap), and Wireshark or `tshark`. Zeek is useful but optional — its output is reproduced in the text. Everything else is in this file.
- **Assumes:** [Lesson 01](01-what-the-analyst-is-for.md). You can separate what you saw from what you concluded.

## Why this lesson exists

Lesson 01 was about not overstating. This one is about having something to state.

Before you can say that anything is unusual, you have to be able to say what happened — precisely, in order, with the parts labeled. Most bad analysis is not bad judgment applied to good observation. It is confident judgment applied to a conversation the analyst never actually read.

The unit you read is a **conversation**: one client, one server, one port pair, from open to close. Everything in this course is built on being able to narrate one.

## Six sentences about the tools, before any of them show up

You are about to meet five pieces of software in two paragraphs. Here is the whole relationship, once, so you are not assembling it from context later.

A **capture** — a `.pcap` file — is a recording of packets in order, exactly as they crossed one point on the network. **Wireshark** opens a capture and shows you every packet; **`tshark`** is the same program at the command line. **Zeek** reads that identical file and does something different: instead of showing you packets, it writes *summary logs* — one line per conversation, in files called `conn.log`, `http.log`, `dns.log`. **Security Onion** is a platform that runs Zeek continuously against live traffic and loads those logs into **Elasticsearch**, a search index; **Hunt** and **Kibana** are the two interfaces you search it with.

So there are two views of the same traffic: **the packets themselves, and Zeek's summary of them.** This whole course moves back and forth between those two views, and knowing which one you are looking at is most of the skill.

One wrinkle worth knowing now rather than being confused by later: Security Onion **renames Zeek's fields** as it ingests them. Zeek writes `id.orig_h`; Security Onion indexes it as `source.ip`. Same value, two names, depending on where in the pipeline you are standing. [`field-names.md`](field-names.md) is the mapping.

## Where this data came from

The capture in `assets/pcaps/` was generated in a lab by [`lab/generate-captures.py`](../lab/generate-captures.py). The traffic is real — a real client, a real server, a real TCP stack — and then the addresses were rewritten into documentation ranges so it reads as an ordinary internal exchange. Protocol behavior, timing and payloads are untouched.

It is checked two ways before it ships: Wireshark must dissect it cleanly, and Zeek must parse it into logs. See [the lab README](../lab/README.md) for why that second check is the one that matters.

## Start where you would actually start

In a Security Onion deployment you do not open Wireshark first. You start in Hunt or Kibana, looking at what Zeek already made of the traffic and Elasticsearch already indexed.

Search for this host's connections and you get one document per conversation. The fields, as Security Onion names them:

```
event.dataset      conn                    conn
log.id.uid         CwlV971jSsZWObrEKd      Cd2hCo1PXGfUinZyj2
source.ip          192.0.2.10              192.0.2.10
source.port        42876                   42886
destination.ip     198.51.100.20           198.51.100.20
destination.port   80                      80
network.transport  tcp                     tcp
network.protocol   http                    http
event.duration     0.004038                0.000184
client.bytes       151                     149
server.bytes       207                     144
connection.state   SF                      SF
```

Two conversations. Same client, same server, same service. Read the fields you will use for the rest of your career:

**Duration boundary:** the second record's `0.000184` seconds corresponds to the opening SYN through the client FIN. The final ACK follows nine microseconds later; first-to-last captured packet time is `0.000193` seconds. Do not substitute a log's duration boundary for the entire packet window.

- **`source.ip` / `source.port`** — who started it, and from which ephemeral port. Different port each time: **these are two separate conversations, not one.**
- **`destination.ip` / `destination.port`** — who was contacted, on which service port.
- **`connection.state: SF`** — normal establishment and normal teardown. Both sides said hello and both said goodbye. Security Onion also carries `connection.state_description`, which spells it out: *Normal SYN/FIN completion*.
- **`client.bytes` / `server.bytes`** — 151 out, 207 back; then 149 out, 144 back. Note the direction words: `client` is whoever opened the connection, which is not always the interesting party.
- **`log.id.uid`** — the identifier tying this document to every other log Zeek wrote about the same conversation. It is how you pivot. Zeek mints a fresh one every time it runs, so if you process this capture yourself your UIDs will not be the two above. Use whatever you get; the pivot is what matters, not the string.

Take that `log.id.uid` and search for it again. This time you get the HTTP document:

```
event.dataset                 http                            http
log.id.uid                    CwlV971jSsZWObrEKd              Cd2hCo1PXGfUinZyj2
http.method                   GET                             GET
http.virtual_host             files.harrowmere-group.example  files.harrowmere-group.example
http.uri                      /api/v2/export?page=1           /api/v2/admin/users
http.useragent                harrow-sync/3.21                harrow-sync/3.21
http.request.body.length      0                               0
http.response.body.length     90                              44
http.status_code              200                             403
http.status_message           OK                              Forbidden
```

Now put the two side by side, because the whole lesson is sitting in that comparison:

```
conn   connection.state:   SF     SF      <- both conversations completed normally
http   http.status_code:   200    403     <- one request succeeded, one was refused
```

**Security Onion is telling you two different things about the same second conversation, and both are true.** That is not a contradiction to resolve. It is two layers reporting on their own business, and the rest of this lesson is about learning to keep them apart.

> **Running Zeek yourself?** `zeek -C -r assets/pcaps/02-conversation.pcap` writes `conn.log` and `http.log` with Zeek's own field names — `id.orig_h` rather than `source.ip`, `conn_state` rather than `connection.state`. Same data, one stage earlier in the pipeline. [The mapping is here](field-names.md).

## Demonstration — Conversation One: Reading Beyond the Handshake

In [narrative episode 01](../narrative/01-who-is-talking-to-whom.md), Ethan thought he understood the first conversation because he recognized the three-way handshake. Then Leah Moreno asked: *"Did the finance export complete?"* Ethan had to admit that while the HTTP status code was `200 OK`, he hadn't actually read the response. 

Here is how an analyst reads a conversation end-to-end across both layers.

### Step 1: Read the Packet Flow in Order

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

Watch the three distinct phases:

* **Phase 1: The Transport Handshake (Frames 1–3):** `SYN` → `SYN, ACK` → `ACK`. This proves bidirectional path reachability between the two sockets.
* **Phase 2: The Application Exchange (Frames 4–7):** The client sends 151 bytes of HTTP request. Frame 5 is the **bare ACK**—the server TCP stack acknowledging receipt before the application processes it. In Frame 6, the application returns `200 OK`.
* **Phase 3: The Teardown (Frames 8–10):** The server initiates teardown (`FIN, ACK`) because the client sent `Connection: close`.

### Step 2: What the Packets Add to the Log

The log showed `client.bytes: 151` and `server.bytes: 207`. The packets reveal the actual dialog:

```
GET /api/v2/export?page=1 HTTP/1.1
Host: files.harrowmere-group.example
User-Agent: harrow-sync/3.21
...

HTTP/1.1 200 OK
Server: nginx/1.24.0
Content-Type: application/json
Content-Length: 90

{"report":"finance-export","rows":1284,"generated":"2026-08-19T09:14:22Z","format":"json"}
```

**The Demonstrated Heuristic:**  
* The transport layer succeeded (`SF`).
* The HTTP transaction succeeded (`200 OK`).
* But the business action did **not** export a file—it returned a *1-page metadata summary*.  
**One-sentence narration:** *A client running `harrow-sync/3.21` requested a metadata summary for page 1 of a finance export, and the service returned a 90-byte JSON payload describing 1,284 rows before closing the connection.*

---

## Guided Practice with Feedback — Conversation Two: The Log Deductions

Before touching Wireshark for Conversation Two, perform the deductions an analyst must make from the log alone in Hunt:

```
source.ip: 192.0.2.10    source.port: 42886
destination.ip: 198.51.100.20    destination.port: 80
connection.state: SF    event.duration: 0.000184s
http.method: GET    http.uri: /api/v2/admin/users
http.status_code: 403    http.status_message: Forbidden
```

Work through these four guided questions:

### 1. Does `connection.state: SF` mean the request succeeded?
* Formulate your answer for transport vs. application.
* **Feedback:** No. `SF` proves TCP delivery succeeded (SYN/FIN completed). It says nothing about whether the application served the data.

### 2. Is this the same conversation as Conversation One?
* Look at the socket pair.
* **Feedback:** No. Conversation One used ephemeral port `42876`; Conversation Two used `42886`. A new source port defines a completely separate TCP conversation.

### 3. The Duration Anomaly (0.000184 seconds)
* What does a total conversation duration of 184 microseconds tell you about the client?
* **Feedback:** A human cannot navigate to an admin page, type an address, or react in 0.18ms. This request was fired programmatically by an automated client.

### 4. What is still unknown from the log alone?
* What can neither `conn.log` nor `http.log` tell you?
* **Feedback:** The log cannot tell you why the server returned 403 (missing header? bad token? unmapped role?), or whether the client attempted authorization.

---

## Practice Application — Conversation Two: Packet Stream Dissection

Now open the capture in Wireshark or `tshark` and inspect Frames 11–20:

```
tshark -r assets/pcaps/02-conversation.pcap -Y "frame.number >= 11"
```

Draft a half-page technical assessment answering:

1. **Narrate the exchange in one sentence:** Who asked what of whom, and what came back? (Zero adjectives about probing or attacks).
2. **Prove refusal from the packets:** Cite the specific frame number and the exact response payload bytes.
3. **The Dual-Layer Split:** Explain why saying "the connection failed" is technically false, and state which layer succeeded and which layer refused.
4. **Who hung up first?** Identify whether the client or server sent the first `FIN`, and contrast with Conversation One.
5. **The Unobservable Boundaries:** Name at least two things this packet capture structurally cannot prove about authorization.

```
tshark -r assets/pcaps/02-conversation.pcap -Y "frame.number >= 11"
```

Or in Wireshark: right-click any frame from 11 onward → Follow → TCP Stream.

Write **half a page** that answers all of the following. Every answer is checkable against the file, so check it.

1. **Narrate the conversation** the way the first one was narrated above: one sentence, no judgment, naming who asked what of whom and what came back.
2. **Is this the same conversation as the first one, continued?** Justify your answer by pointing at a specific field, and name it as Security Onion would.
3. **You already know from `http.status_code` that this request was refused.** Prove it from the packets alone — name the frame and the bytes. Then answer, separately: did the TCP connection succeed? Say which specific evidence answers which question, and why one cannot substitute for the other.
4. **Who closed the connection, and does it differ from the first conversation?**
5. **The response was 144 bytes against the first response's 207.** Before looking, write down at least two explanations a smaller response could have. Then look, and say which one it was and what distinguished it. The point is the habit of generating alternatives before checking, not the answer.
6. **What did the client do differently between the two conversations?** There is more than one answer.
7. **What can you not determine from this capture?** Name at least three things. Be specific — "I don't know everything" is not an answer, but "I cannot tell whether this client is authorised to make this request, because authorisation state lives on the server and is not on the wire" is.

## The thing this lesson is really about

Question 3 is the lesson.

The second conversation completes perfectly. Handshake, request, response, clean teardown, `connection.state: SF` — by every measure at the transport layer, it worked. And the application said **403 Forbidden**.

Both statements are true, at different layers. An analyst who collapses them into one verdict will be wrong in one direction or the other:

- Read only `connection.state`, and you report a successful connection to a service. True, and it hides that access was refused.
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

---

## The 4DX In-The-Flow-of-Work Transfer System

Learning how to read two layers in a lab does not guarantee you will do it on shift when an executive is asking why an application is broken. The tendency to look at only one layer and guess the other is a cognitive default.

### 1. Pinned Desk Aid: The Transport vs. Application Diagnostic Split

Pin this rule to your monitor:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                     THE DUAL-LAYER DIAGNOSTIC SPLIT (BEFORE YOU ANSWER)                │
├─────────────────────┬─────────────────────────────────┬────────────────────────────────┤
│ LAYER               │ SOURCE FIELD / EVIDENCE         │ WHAT IT ANSWERS                │
├─────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ TRANSPORT LAYER     │ • `connection.state: SF`        │ "Did the network deliver?"     │
│ (TCP / Delivery)    │ • SYN / SYN-ACK / ACK Handshake │                                │
│                     │ • TCP Retransmissions / RSTs    │ YES: Network succeeded.       │
│                     │                                 │ NO: Delivery failed in transit.│
├─────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ APPLICATION LAYER   │ • `http.status_code: 200 / 403` │ "Did the app accept/process?"  │
│ (HTTP / Processing) │ • Server response payload body  │                                │
│                     │ • TLS Alert / Handshake Error   │ 200 OK: Application served it. │
│                     │                                 │ 403/500: App refused or broke. │
├─────────────────────┴─────────────────────────────────┴────────────────────────────────┤
│ RULE: Never answer "Did it work?" without naming which layer you are speaking about.   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. The Analyst's Daily 4DX Scorecard

```
WEEKLY 4DX SCORECARD — ANALYST: [ ____________ ]  WEEK OF: [ _________ ]

[ WIG / LAG TARGET ]: Zero misdiagnosed connection tickets; 100% layer separation.

[ LEAD MEASURE ]: % of triage tickets where Transport Status (Delivery) and Application
                 Status (Processing) are recorded as separate line items. (Target: 100%)

  DAY       CONVERSATIONS TRIAGED   DUAL-LAYER SEPARATED?   FRAME # PROOF ATTACHED?
  Mon               [   ]                   [   ]                    [   ]
  Tue               [   ]                   [   ]                    [   ]
  Wed               [   ]                   [   ]                    [   ]
  Thu               [   ]                   [   ]                    [   ]
  Fri               [   ]                   [   ]                    [   ]

  WEEKLY DUAL-LAYER COMPLIANCE: [ _____ / _____ ] = [ _____ % ]
```

### 3. The 5-Minute Friday Supervisor Huddle

Every Friday morning:
1. **Review the Scorecard (1 min):** Check total triage tickets vs. dual-layer split compliance.
2. **Review One Conversation Ticket (2 min):** *"On Ticket #4021, you reported 'connection succeeded'. Did you check the HTTP status code, or just `conn.log: SF`?"* Coach the distinction.
3. **Commitment for Next Week (2 min):** Agree on checking application status on all `SF` records before marking as benign.

---

<div class="bridge-card">
  <div class="bridge-label">Next Step in Curriculum</div>
  <div class="bridge-title">Chapter 02 (Story) — Before You Look</div>
  <p class="bridge-desc">You can now explain a result you can already see. But what happens when the next packet is hidden? Watch Dana challenge Ethan to commit to a prediction before the answer is visible.</p>
  <a href="#/narrative/02-before-you-look" class="bridge-btn">Continue to Chapter 02 →</a>
</div>

## What this lesson does not do

It does not establish that this traffic is normal or abnormal. Two conversations from one client is not a baseline, and lesson 03 is where expected behavior starts being built deliberately.

It does not teach you the tool. Wireshark's filter language, column layouts and stream reassembly are worth learning and this lesson does not attempt to cover them.

It does not define proficiency, scoring, or completion. One narrated conversation is a single sample.
