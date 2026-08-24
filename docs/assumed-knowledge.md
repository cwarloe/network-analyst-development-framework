# What the lessons assume and never teach

Derived 2026-08-21 by extracting every technical term used in lessons 02, 03, 04, 06 and 07, pulling its first occurrence with context, and reading each one to see whether the lesson defines it or relies on the reader already knowing.

This exists to answer one question: **is the prerequisite gap a two-page primer or a course?** The answer is neither of the extremes — it is about 35 concepts in four clusters, and one of the four is much cheaper to close than the rest.

## Learner model

The [course](../COURSE.md#entry-assumptions) is paced for an experienced general-IT practitioner entering a first dedicated analysis role, with broad but uneven prior networking or cybersecurity exposure and no assumed analysis or tooling experience. That primary learner is a design target rather than an admission requirement. Less-experienced learners may need optional, just-in-time support for specific gaps identified below.

This inventory still does not establish which terms stop real learners. It distinguishes assumptions in the text from observed learner difficulty; actual use must determine which support is necessary.

## What "broad but uneven" actually means

The learner model says prior knowledge is uneven. This section says what the unevenness looks like in practice, because it determines the *shape* of any support and not just its content.

### Certification study does not close these gaps

A learner arriving with Security+ or equivalent self-study typically holds the relevant material as **recall**: 443 is HTTPS, TCP has a three-way handshake, DNS resolves names. Every one of those is true and none of them is what the lessons need, which is a **usable causal model** — enough structure to predict what should happen next and notice when it does not.

This is not a hypothetical. It is the premise of [the prologue](../narrative/00-prologue.md), whose narrator has studied on his own time and describes what he studied as *"lists — ports, protocols, attack names, the shapes of things that were bad"*, then fails his first ticket anyway. [`BOOK-1.md`](../BOOK-1.md) gives the same profile to Ethan deliberately.

**So a certification is the wrong gate, and a prequel built to deliver certification-shaped knowledge would reproduce the problem rather than fix it.** The holes are not in the facts. They are in whether the facts connect to anything.

### The holes are few, specific, and not the same for everyone

From the cluster analysis below, four items are load-bearing — meaning a learner without them cannot complete a named task, rather than merely finding it harder:

| | What is missing | Where it blocks | Type |
|---|---|---|---|
| 1 | **Layer** as a mechanism | Lesson 02's work-product question 3, which is the lesson's own stated thesis | Model |
| 2 | **Client / server / initiator** | Lesson 02's narration task; the learner copies fields instead | Model |
| 3 | **`SYN` / `ACK` / `FIN` as flags**, not as a named sequence | Lesson 06's `REJ` against `S0` | Model |
| 4 | **Packet against frame** | Nothing specific; produces steady low-grade confusion | Vocabulary |

All four are *models* rather than definitions, except the last. That matters: a glossary entry reading *"layer: a level of the protocol stack"* leaves lesson 02's question 3 exactly as unanswerable as before.

**And different learners are missing different ones.** Eight years of helpdesk usually supplies ports and client/server and no layer model. A NOC background usually supplies layers and no capture experience. Certification study supplies vocabulary for all four and a working model of none. A fourth profile turns up often enough to name: **methodology without the operational floor** — someone trained on how an investigation is supposed to go, who has had a taste of security work without holding a seat in it and never worked a helpdesk. That background supplies the reasoning moves and not the substrate the moves operate on, which is close to the inverse of the helpdesk profile.

The gaps are non-linear, which is the single most important constraint on how support gets delivered.

### The profile the self-check is worst at finding

The other three profiles fail the [self-check](../lessons/self-check.md) legibly. An answer comes out thin, or stops, or reaches for a memorised sequence, and the check says so.

The methodology-first profile does not fail that way, and the reason is structural. The self-check asks the reader to *produce* an explanation and then **"compare the shape of yours against the shape described."** Shape is exactly what that background supplies. The answer arrives properly hedged, distinguishes what is established from what is assumed, and reads as usable — while the mechanism underneath it may be absent. Items 3 and 5 are the two that still bite, because both ask for a mechanism and no methodological move substitutes for one: *why a fresh source port each time*, and *what each flag means on its own* rather than where it sits in a sequence.

This matters more than the other profiles do, because of what the course asks people to hand in. The work products are argued prose, and fluency in that genre is the thing this learner already has. So the failure mode is not a thin record — it is a **well-formed record resting on a wrong mechanism**, which is harder to catch in review than a thin one, and the review guides deliberately do not score. It is the strongest argument in the file for why *Check* is not optional in Observe → Explain → Predict → Check → Revise: it is the only step that tests the mechanism against evidence instead of testing the reasoning against itself.

**Recorded from one person's self-description, not from observation.** It is the author's own profile, offered while taking the self-check, and it is a hypothesis about a category rather than a measurement of one. The prediction it makes — items 3 and 5 discriminate for this profile where 1, 2 and 7 will not — is checkable in [the run template](../lessons/run-records.md#the-template) and has not been checked.

### Finding out which holes a given person has

[`lessons/self-check.md`](../lessons/self-check.md) covers the four load-bearing items plus three adjacent ones. It asks the reader to produce an explanation rather than recognise a term, because that is the only reliable way to separate recall from a working model, and it routes most findings to *no action* — a gap on something the course develops is the reason the lesson exists, not a deficiency to repair beforehand.

Taken before a run and recorded in [the run template](../lessons/run-records.md#the-template), it is also the cheapest available evidence on the question this file cannot answer from the text: which of these assumptions actually stop somebody.

### Consequences for delivery

**A linear prequel is the wrong shape for non-linear gaps.** It makes every learner sit through the parts they already hold. That is not merely inefficient — for material a learner already understands, added instruction is associated with *worse* outcomes rather than neutral ones (the expertise reversal effect). A prequel that helps the helpdesk learner can actively cost the NOC learner.

**Support must be self-selected, small, and independent.** Four short modules any of which can be skipped, rather than one sequence.

**A prequel must not pre-teach Book 1's scheduled content.** [Episode 2](../BOOK-1.md) targets *"hosts, services, ports, sessions, layers as reasoning aids"* and Episode 5 targets *"practical session states, refusal versus silence."* Items 1 and 3 above are therefore scheduled instruction, and support that delivers them in advance duplicates and pre-empts a lesson rather than unblocking one. The support version has to be strictly smaller: the mechanism, not the reasoning built on it.

### A live tension worth naming

Item 2 is currently taught twice, unequally. [Lesson 02](../lessons/02-reading-a-conversation.md) *states* it — *"`client` is whoever opened the connection"* — and [Episode 2](../narrative/01-who-is-talking-to-whom.md) has the learner *derive* it, from who sent the first `SYN`.

The definition therefore exists outside the narrative, which satisfies the rule in [`BOOK-1.md`](../BOOK-1.md#primary-learner-and-accessibility) that no required prerequisite may live only in a narrative chapter. The **practice** does not. Whether a stated definition is sufficient where the narrative supplies a derivation is exactly the sort of question a first run answers and reading cannot.

## The measurement that started it

Distinct technical terms per lesson:

| Lesson | Terms |
|---|---|
| 01 | 9 |
| **02** | **19** |
| 03 | 23 |
| 04 | 22 |

The vocabulary load roughly doubles between lesson 01 and lesson 02. [R005](research/R005-instructional-design-review.md) suspected the overload was in 02–04 from the instructional side, without counting anything. The count agrees.

## What the lessons already teach properly

Worth stating first, because it is more than expected and it bounds the problem. Each of these is defined in place, at the point of use, well enough that a reader who did not know it arrives knowing it:

`handshake` · `teardown` · `CNAME` · `A record` · `TTL` · `SOA` · `NXDOMAIN` vs `NODATA` · `anycast` · `self-signed` · `certificate authority` · `SNI` · `x509` · `issuer`/`subject` · `MTU` · `fragment` · `retransmission` · `status code` · `jitter` · `beaconing` · the *meaning* of `RST`

DNS in particular is taught almost completely. Lesson 03 needs very little in front of it.

## Cluster A — What a conversation is

Assumed from lesson 02 onward, never defined anywhere.

`port` · `ephemeral port` · `IP address` · `TCP` · `UDP` · `packet` vs `frame` · `layer` · `protocol` · `payload`

**This is the load-bearing cluster.** Lesson 02's entire thesis is that *"did it work?"* is a question per layer and the layers can disagree — and **the word "layer" is never explained.** A reader without it cannot have the insight the lesson is built to produce.

`packet` and `frame` are used interchangeably throughout and never distinguished, which is a reliable source of quiet confusion.

## Cluster B — TCP's moving parts

`SYN` · `ACK` · `FIN` (as flags, not as labels)

Lesson 02 names them — *"Frames 1–3, the handshake. SYN, SYN-ACK, ACK"* — and explains what the **sequence** proves. It never says what a SYN **is**: a bit in a header meaning *I would like to open a connection*. A reader can follow the lesson's argument while holding these as opaque tokens, which works until lesson 06 asks them to tell `REJ` from `S0` and the distinction is entirely about which flag came back.

## Cluster C — The application layer

`HTTP` · `GET` / `POST` · `User-Agent` · `Content-Length` · `URI` · `virtual host` · `TLS` · `ClientHello` / `ServerHello` · `cipher` · `ChangeCipherSpec` · `Application Data` · `fingerprint` · `certificate`

HTTP is never introduced; it simply appears in raw request text and in field names. That mostly works, because HTTP reads like English — but `Content-Length` becomes load-bearing evidence in lesson 06's truncation case, and a reader who has skimmed past it there has nothing to reason with.

TLS is heavier. Lesson 04 opens on `ClientHello` and `cipher 0xc030` and assumes both. `Application Data` is explained as *"TLS record type 23"*, which answers jargon with jargon.

## Cluster D — The toolchain, and the surprise

`pcap` · `Wireshark` · `tshark` · `Zeek` · `Security Onion` · `Hunt` · `Kibana` · `Elasticsearch` · `conn.log` · `dissect`

> **Closed 2026-08-21.** Lesson 02 now opens with *Six sentences about the tools, before any of them show up* — the pipeline from capture to Wireshark to Zeek to Security Onion to Hunt, the two-views framing, and the field-rename wrinkle. The rest of this section is the finding as it stood.

**This is the cheapest gap to close and the one nobody had noticed.**

The course's central working pattern is *log first, packets second* — go to the log to find the conversation, go to the capture to read it. But a reader is never told what a log **is** in this context, what produced it, or how the four tools relate. Lesson 02's "Requires" line names Wireshark, tshark and Zeek and then begins, and by the second section the reader is in Hunt or Kibana looking at documents Elasticsearch indexed.

Nothing anywhere says: a capture is a file of packets; Wireshark and tshark read it; Zeek reads the same file and writes summary logs instead; Security Onion runs Zeek and puts those logs in Elasticsearch; Hunt and Kibana are how you search them. **Six sentences.** Without them, the reader cannot tell which tool they are supposed to be imagining at any given moment, and the field-name mapping in [`lessons/field-names.md`](../lessons/field-names.md) has no frame to hang on.

## Size verdict

About 35 concepts. Not a two-page primer, and not two years of service desk either.

The clusters are not equal:

| Cluster | Size | Cost to close |
|---|---|---|
| ~~**D — toolchain**~~ | ~10 | ~~Six sentences~~ — **done** |
| **B — TCP flags** | 3 | A short paragraph, or a diagram |
| **A — what a conversation is** | ~9 | A real primer. This is the genuine prerequisite |
| **C — application layer** | ~13 | Partly closeable in place; TLS is the heavy end |

## What this does not settle

**Which of these actually stops a learner.** This is a list of what the text assumes, produced by reading the text. It is not evidence about readers.

Lesson 02 alone assumes nineteen terms, and it is unlikely that all nineteen matter equally — some will turn out to be inferable from context and some will stop someone dead. Only watching a real reader hit lesson 02 will separate them, and the list to watch is now written down rather than guessed at.

Recorded in [the roadmap](../ROADMAP.md) as an input to that run, not as a work item.
