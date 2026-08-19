# Lesson 07 — When It's Suspicious

## At a glance

- **Part of:** [the course plan](../COURSE.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-19
- **Capability targets:** IR-2, IR-4, IR-5, OC-3
- **Evidence families:** EF-3, EF-4, EF-6
- **Time:** about 2.5 hours
- **Requires:** [`assets/pcaps/07-suspicious.pcap`](../assets/pcaps/07-suspicious.pcap), and Wireshark or `tshark`. Zeek is useful but optional — its output is reproduced in the text.
- **Assumes:** [Lessons 02 through 06](02-reading-a-conversation.md). In particular lesson 06 — you have diagnosed benign faults and have alternatives available.

## Why this lesson comes last

Everything before this taught you what normal looks like and how ordinary things break. That was the preparation. The failure mode this lesson exists to prevent is **indicator-first labeling**: learning a list of suspicious shapes, matching against it, and reporting the match as a finding.

Shapes do not carry intent. Regular outbound connections are what malware command-and-control looks like, and they are also what a monitoring agent, a software update checker, a licence validator, a mail client, and a status page poller look like. An analyst whose only tool is shape recognition will flag all of them with equal confidence and be right by accident.

This capture is built so that the obvious reading is available, tempting, and insufficient.

## An honest note about this data

The traffic is real — real sockets, real DNS, real HTTP — but it was **generated in a lab to have particular shapes**, not captured from an actual intrusion. It teaches the reasoning. It does not teach you what any specific real adversary looks like, and you should not carry the specific values here into production expecting to match them.

[R004](../docs/research/R004-pcap-and-telemetry-sourcing.md) cleared the CIC and Stratosphere/CTU-13 corpora for use here, and working against genuine captured intrusion traffic is the natural next step for this lesson. That is a gap, and it is recorded in the [roadmap](../ROADMAP.md).

## The situation

> A weekly review flags one workstation, `192.0.2.10`, for "unusual outbound activity." No alert fired. Nothing is broken. A colleague has already looked and says it is "clearly beaconing."
>
> You have an hour of that host's traffic.

## Start in the log

```
zeek -C -r assets/pcaps/07-suspicious.pcap
```

`conn.log`, grouped by destination:

```
count  id.resp_h       id.resp_p  service  orig_bytes  resp_bytes
40     198.51.100.80   53         dns      96          125
11     198.51.100.60   80         http     139         116
9      198.51.100.70   80         http     134         116
1      198.51.100.90   80         http     61618       0
```

Four destinations, four very different patterns. Take them in turn, and resist naming any of them yet.

## The two that look identical

Connections to `198.51.100.60` and `198.51.100.70` arrive on a timer:

```
198.51.100.60    11 connections   mean interval 4.02s   stdev 0.048s   (1.2% variation)
198.51.100.70     9 connections   mean interval 4.96s   stdev 0.234s   (4.7% variation)
```

Both are regular. Both send about 135 bytes and receive about 116. Both use the same browser-like `User-Agent`. In `http.log`:

```
id.resp_h       method  host                              uri                      response_body_len
198.51.100.60   GET     cdn-metrics.example               /api/v1/tasks?id=8842    23
198.51.100.70   GET     updates.contoso-internal.example  /hb                      23
```

**Nothing in the shape separates these two.** Same method, same size class, same regularity class, same user agent, same response size. If you cluster this traffic by timing and volume, they land in the same cluster.

One of them is a workstation checking an internal update service for a heartbeat. The other is not. **The capture does not tell you which**, and any confidence you feel about which is which right now is coming from the hostnames — which is fine, but notice that it is coming from *context*, not from the beaconing.

Two traps worth naming explicitly:

**"Low jitter means malicious."** `198.51.100.60` varies by 1.2% and `198.51.100.70` by 4.7%, so the rule would pick the first. But plenty of legitimate software polls on a near-exact timer — cron-driven agents are more regular than this — and command-and-control frameworks have added deliberate jitter for years precisely to look like the second one. The rule is fragile in both directions.

**"It beacons, therefore it is C2."** Beaconing is a description of timing. It is a property shared by most well-behaved background software on any managed endpoint.

## The DNS stream

Forty queries to `198.51.100.80`, all TXT, every one a different name:

```
518ju0lyebhk9trcbmre07mvahtt8s1qirzf3px6w2o9afxo.d000.sync.cdn-metrics.example
x9w2vsyk05uhwfd2j79sn3xdgg4aevbjexfegcfqr9gentwl.d001.sync.cdn-metrics.example
n9vv2rvb973j0a3wnw85n9tceu7fbiucn0nqjxov1r87clgl.d002.sync.cdn-metrics.example
...
```

Forty queries, forty unique names, averaging 78 characters, with a 48-character random-looking leftmost label, a sequence counter, and TXT as the record type.

Compare this against the baseline you built in [lesson 03](03-names-and-expectations.md), which is exactly what that lesson was for:

| | Lesson 03 baseline | Here |
|---|---|---|
| Names | Repeat; caches serve them | Every one unique |
| Leftmost label | Short, meaningful (`www`, `en`) | 48 random characters |
| Record type | A and AAAA | TXT throughout |
| Caching | Benefits from it | Structurally defeats it |
| Direction of data | Answers flow to the client | Content is in the *question* |

That last row is the one that matters. In ordinary DNS the information you want comes back in the answer. Here the entropy is in the query, and unique names guarantee every query reaches the authoritative server. That is what a channel looks like when a name lookup is being used to carry data.

**And it still is not proof.** Legitimate systems do this. Anti-malware reputation lookups encode file hashes into query names. Some CDN and telemetry systems encode session identifiers the same way. The shape is genuinely ambiguous; what makes it worth pursuing is not the shape alone.

## The transfer

One connection to `198.51.100.90`:

```
method  host                  uri               request_body_len   resp_bytes
POST    cdn-metrics.example   /upload/session   61618              0
```

Roughly 60 KB outbound, nothing back. A single upload against a workstation's otherwise tiny traffic.

By itself: unremarkable. Workstations upload things. Crash reports, telemetry bundles, document saves, backups.

## The evidence that actually discriminates

Go back and read the `host` field across all three behaviours:

```
beacon      198.51.100.60   Host: cdn-metrics.example
dns         198.51.100.80   ...........sync.cdn-metrics.example
upload      198.51.100.90   Host: cdn-metrics.example
```

**Three different behaviours, three different IP addresses, one domain.**

A regular check-in, a high-rate DNS channel, and a bulk outbound transfer, all associated with `cdn-metrics.example`. Meanwhile `198.51.100.70` — the other beacon, the one that is shape-identical to the first — belongs to `updates.contoso-internal.example` and appears in nothing else.

This is the shift the lesson is built around. **The discriminating evidence is relational, not morphological.** Not "this beacon is more regular than that one," but "these three unrelated-looking behaviours converge on one domain, and that one does not." Convergence is much harder to produce accidentally than any individual shape, and much harder for an adversary to avoid than jitter.

It is also, note, exactly the kind of question the [lesson 03](03-names-and-expectations.md) baseline and the [lesson 05](05-vantage-point-and-evidence.md) evidence plan prepare you to ask. It is not a new trick. It is the earlier lessons pointed at a harder problem.

## What is still not established

Being honest about the remaining gap is most of the value of the assessment you are about to write:

- **Nothing here identifies a process, a user, or a file.** Every claim about *what* is doing this needs endpoint telemetry, which the network cannot supply — [lesson 05](05-vantage-point-and-evidence.md), and the same limitation that shaped [lesson 04](04-what-encryption-hides.md).
- **`cdn-metrics.example` could be a legitimate service.** Analytics and CDN vendors run beacons, encode identifiers into DNS, and receive uploads. The convergence pattern is *consistent with* one vendor's SDK doing three normal things.
- **The DNS payloads are opaque.** TXT answers were returned; this capture does not establish what they contained or what was encoded outbound.
- **One hour of one host is not a baseline.** You do not know whether other workstations do the same thing — which is the single cheapest next question and would settle a great deal.

## Your work product

Write an **assessment of about a page** of `192.0.2.10`'s traffic.

The structure is the requirement, and it is not optional:

**1. Observations.** All four destinations. Facts, frame- or log-traceable, no characterisation.

**2. The benign explanation, argued properly.** Write the strongest honest case that all of this is legitimate software. Not a token paragraph — make it good enough that a reasonable colleague could hold it.

**3. The malicious explanation, argued properly.** Same standard.

**4. Which you favour, with the specific evidence that moved you** and how confident you are. If the evidence does not move you far, say so and say what that means.

**5. What would settle it.** For each open question, the source that answers it, in priority order.

**6. What you would do in the next hour**, sized to the evidence you actually have.

Address these inside that structure:

1. Your colleague said it is "clearly beaconing." Respond to that specifically — is it true, and is it useful?
2. Explain why `198.51.100.70` is not in your finding, in a way that does not rely on the hostname sounding internal.
3. If you had only `conn.log` and no `http.log` or `dns.log`, what could you still say? This is a real scenario — it is what encrypted traffic looks like after [lesson 04](04-what-encryption-hides.md).
4. Give one plausible, specific benign product that would produce all three `cdn-metrics.example` behaviours, and say what evidence would rule it in or out.
5. The DNS queries defeat caching by design. Name a legitimate reason to do that.

## Reviewing your own work

- Is your benign section shorter than your malicious section? If so, you wrote a justification, not an assessment. Length is a rough proxy for how seriously you held it.
- Did you write the word "malicious," "attacker," or "exfiltration" as a fact anywhere? Check each one against [lesson 01](01-what-the-analyst-is-for.md): is it an observation, an interpretation, or a judgment, and is it labelled as what it is?
- On question 2 — if your entire reason for excluding `198.51.100.70` is that its hostname contains "internal," you have accepted an attacker-controllable string as evidence. What would you check instead?
- Did you distinguish "these three behaviours share a domain" from "these three behaviours are one campaign"? The first is in the capture. The second is an inference.
- Would your assessment survive `cdn-metrics.example` turning out to be a legitimate analytics vendor the marketing team signed up for? If it would be embarrassing, it was overclaimed — this is the same test [lesson 08](08-judgment-and-handoff.md) applies.
- Did you recommend an action proportionate to the evidence, or did you recommend the most decisive action available?
- What is your single cheapest next question? If it is not "do other workstations do this too," reconsider.

## What this lesson does not do

It does not train you against real adversary traffic. The shapes are lab-generated, and while the reasoning transfers, the specifics do not. Working the same method against CIC or Stratosphere data is the intended next step.

It does not cover encrypted C2, domain generation algorithms, protocol tunneling other than DNS, or living-off-the-land techniques where the traffic is generated by legitimate signed software.

It does not teach detection engineering. Everything here argues that shape-based rules are fragile; writing rules that survive that is a different discipline.

It does not define proficiency, scoring, or completion. One assessment of one hour of one host is a single sample.
