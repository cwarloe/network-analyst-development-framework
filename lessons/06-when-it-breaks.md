# Lesson 06 — When It Breaks

## At a glance

- **Part of:** [the course plan](../COURSE.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-19
- **Capability targets:** OC-4, IR-2, IR-3, IR-5, IR-6
- **Evidence families:** EF-3, EF-4, EF-8
- **Time:** about 2.5 hours
- **Requires:** [`assets/pcaps/06-failures.pcap`](../assets/pcaps/06-failures.pcap), and Wireshark or `tshark`. Zeek is useful but optional — its output is reproduced in the text.
- **Assumes:** [Lessons 02 through 05](02-reading-a-conversation.md). You can narrate a conversation, describe expected behaviour, and plan what evidence to gather.

## Why this lesson exists

This lesson comes before the one about suspicious activity, deliberately, and the reason is worth stating plainly rather than leaving in the course plan.

**A misread firewall change and a covert channel look alike to someone who has only been taught to look for covert channels.** An analyst who has never systematically diagnosed a broken network has no benign explanations available — so every unexplained observation resolves toward the only category they know. That is not caution. It is a shortage of alternatives, and it produces confident, wrong escalations.

So this lesson is about failure. Four connections, one user complaint, four different causes, four different owners. None of them is an attack. Learning to tell them apart is what makes the next lesson honest.

## The situation

> Users report that the finance application "isn't working." Some say it hangs. Some say it errors immediately. One says it is "just slow." The application talks to four backend services. You have a capture of one client's attempts to reach all four.

That spread of descriptions is not users being unhelpful. It is the actual signature of four different faults, arriving as one ticket.

## Start in the log

```
zeek -C -r assets/pcaps/06-failures.pcap
```

`conn.log`, trimmed:

```
id.orig_p  id.resp_h       id.resp_p  service  duration  orig_bytes  resp_bytes  conn_state  history
41001      198.51.100.30   80         -        0.000011  0           0           REJ         1
41002      198.51.100.40   80         http     0.000471  67          441         RSTR        4
41003      198.51.100.50   80         http     4.000853  95          132         SF          5
41000      198.51.100.20   80         -        4.092267  0           0           S0          5
41000      198.51.100.20   80         -        2.015977  0           0           S0          2
41000      198.51.100.20   80         -        -         -           -           S0          1
```

Before reading further, look only at `conn_state` and try to name four different faults. Zeek has already done most of the discrimination for you — the column exists precisely because these outcomes are different, and learning to read it is worth more than any amount of packet staring.

- **`REJ`** — the connection was rejected.
- **`RSTR`** — it established, then the responder reset it.
- **`SF`** — normal establishment, normal teardown. Nothing failed.
- **`S0`** — a SYN was sent and nothing ever came back.

## Worked: the two that get confused

`REJ` and `S0` produce the same sentence from a user — *"it won't connect"* — and they are opposites.

**`198.51.100.30` — rejected.** Frames 1 and 2:

```
1   0.000000   192.0.2.10 → 198.51.100.30   41001 → 80 [SYN]
2   0.000011   198.51.100.30 → 192.0.2.10   80 → 41001 [RST, ACK]
```

Eleven microseconds. A packet reached the destination, something there examined it, and **that something answered.** The answer was no, but there was an answer. That tells you the host is up, the path works in both directions, and a specific decision was made — nothing listening on the port, or a firewall configured to reject rather than drop.

**`198.51.100.20` — dropped.** Frames 21 through 28:

```
21   6.002    41000 → 80 [SYN]
22   7.023    41000 → 80 [SYN]   +1.02s   [retransmission]
23   8.047    41000 → 80 [SYN]   +1.02s   [retransmission]
24   9.071    41000 → 80 [SYN]   +1.02s   [retransmission]
25  10.095    41000 → 80 [SYN]   +1.02s   [retransmission]
26  11.119    41000 → 80 [SYN]   +1.02s   [retransmission]
27  13.135    41000 → 80 [SYN]   +2.02s   [retransmission]
28  17.199    41000 → 80 [SYN]   +4.06s   [retransmission]
```

Eight SYNs, eleven seconds, **not one byte back.** The widening gaps are the client's stack backing off, assuming the network is congested and trying to be polite about it. Nothing ever answers.

The discrimination, and it is the most useful single distinction in network troubleshooting:

| | `REJ` | `S0` |
|---|---|---|
| What happened | Something answered | Nothing answered |
| What you know | Host reachable, path bidirectional, decision made | Delivery failed, in one direction or both |
| Where to look | Service and firewall configuration on that host | Routing, firewall DROP rules, the path itself |
| How long the user waits | Instant error | Long hang, then timeout |

**`REJ` proves the path works.** That is a large piece of free information, and it is the one most often thrown away. An analyst who reports "connection failed" for both has destroyed the difference between a configuration problem and a delivery problem.

## The one that gets misattributed

`198.51.100.50` returned `conn_state: SF`. Normal establishment, normal teardown, correct response. And a duration of **4.0 seconds**, which is why a user called it slow.

Look at where the time went:

```
11   2.0013   [SYN]
12   2.0013   [SYN, ACK]         <- 0.0000s. The path is instant.
13   2.0014   [ACK]
14   2.0016   GET /api/v2/export?page=1     95 bytes
15   2.0016   [ACK]              <- server acknowledges receipt immediately
16   6.0020   HTTP/1.1 200 OK   132 bytes   <- four seconds later
17   6.0020   [ACK]
18   6.0020   [FIN, ACK]
```

**Between frames 15 and 16 there are no packets at all.** Not a retransmission, not a window problem, not a dropped segment. Four seconds of nothing, and then a correct answer.

The network delivered the request in 200 microseconds and acknowledged it in seven. Then the application thought for four seconds.

This is the single most common misattribution in operations. "The network is slow" is a report about an experience, and the experience is real — but the evidence here says the network did its job in under a millisecond. Frame 15 is what proves it: the server's TCP stack acknowledged the request instantly, which means the request arrived, intact, and only then did the delay begin.

Being able to say *"the network delivered this in 0.2 milliseconds and the application took four seconds"* — and point at the frames — is worth more to a troubleshooting bridge than any amount of confident guessing.

## The one that half-worked

`198.51.100.40` returned `RSTR`. Frames 3 through 10:

```
6   1.0006   GET /report/full     67 bytes
8   1.0008   HTTP/1.1 200 OK ... 441 bytes
10  1.0009   [RST, ACK]           <- responder resets
```

A `200 OK` and then a reset. Read the response header in the capture: the server advertised `Content-Length: 5000` and delivered exactly 400 bytes of body — a 441-byte response of which 41 bytes are header — before tearing the connection down.

Two things worth extracting. **A `200 OK` is a promise, not a delivery** — the status line is sent before the body, so a successful status code says nothing about whether the transfer completed. And **truncation is visible if you look for it**: the advertised length and the delivered length disagree, which is checkable evidence rather than a hunch.

## What the log renders versus what happened

Go back to `conn.log` and count the `S0` rows. There are **three**, all from source port 41000, all to `198.51.100.20`.

There was **one** connection attempt.

Zeek closes a pending connection record after an inactivity period and opens a new one when retransmissions continue, so a single eleven-second SYN sequence is rendered as three rows. Neither Zeek nor the packets are wrong; they are answering different questions.

The consequence is concrete. A detection that counts `S0` connections per host per minute — a completely reasonable thing to build — will report three failed attempts where a user made one. Scale that across an outage and the numbers in your incident report are inflated by a factor nobody can reconstruct later.

**A log is a rendering of events under a set of rules, not the events.** Knowing the rules of your own logs is part of knowing your evidence, which is what [lesson 05](05-vantage-point-and-evidence.md) was about.

## Predict, then check

Do this before writing anything up, and write your predictions down first — the value is in being wrong on paper.

For each of the four servers, predict:

1. What the user's description of the symptom would be, in their words.
2. Which team owns the fix.
3. What one additional piece of evidence would most increase your confidence.

Then check your predictions against the capture, and **record every place you were wrong.** Revising a model when a prediction fails is the capability this lesson exists to build; getting the predictions right on the first pass is not the point and does not develop it.

## Your work product

Write a **diagnosis of about a page** for the ticket that says "the finance application isn't working."

It must contain:

1. **A statement of what is actually happening**, covering all four backends. One complaint, four faults, named separately.
2. **For each fault: the discriminating evidence.** Not "it looks like a firewall" — the frame numbers and the field that separates this explanation from its nearest alternative.
3. **At least two explanations you considered and rejected**, with what ruled them out. If you rejected nothing, you did not diagnose, you recognised.
4. **A statement about the network's role**, which is not the same for all four. Be precise about which faults are network faults and which are not.
5. **What you cannot determine from this capture**, and which source would settle it.
6. **The `S0` counting problem**, stated in a way a manager reading incident numbers would understand.

## Reviewing your own work

- Did you give `REJ` and `S0` different owners? If both went to "the network team," reread the table — one of them is proof the network is working.
- On the four-second delay: did you write "slow response" or did you write "the network delivered in 0.2 ms and the application took 4 s"? Only one of those ends the argument on the bridge.
- Which frame did you cite as proof that the request reached the slow server? If you did not cite frame 15, find it and see why it matters.
- For the `RSTR` case, did you notice the `Content-Length` disagreement, or did you accept the `200 OK`?
- Count your rejected alternatives. Two is the floor, and they should be plausible — rejecting "aliens" is not analysis.
- Did any of your predictions fail? If none did, either you checked before predicting, or your predictions were vague enough to survive anything. Both are worth catching.
- Would your write-up survive one of these faults turning out to be deliberate — a firewall rule someone added on purpose? Nothing here proves intent either way, and your language should reflect that.

## What this lesson does not do

It does not cover packet loss, latency injection, MTU problems, or path MTU discovery failure. Those need traffic impairment the current [capture lab](../lab/README.md) cannot produce — no `netem` — and they are a real gap in this lesson. Fragmentation and MTU black holes in particular are a classic failure class this material does not yet teach.

It does not cover routing faults, asymmetric paths, or anything requiring more than one vantage point. [Lesson 05](05-vantage-point-and-evidence.md) explains why one sensor cannot settle those.

Four connections from one client is a demonstration of four signatures, not a survey of how networks fail.

It does not define proficiency, scoring, or completion. One diagnosis is a single sample.
