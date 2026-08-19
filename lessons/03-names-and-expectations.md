# Lesson 03 — Names and Expectations

## At a glance

- **Part of:** [the course plan](../COURSE.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-19
- **Capability targets:** OC-3, OE-1
- **Evidence families:** EF-2, EF-3
- **Time:** about 2 hours
- **Requires:** [`assets/pcaps/03-dns.pcap`](../assets/pcaps/03-dns.pcap), and Wireshark or `tshark`. Zeek is useful but optional — its output is reproduced in the text.
- **Assumes:** [Lesson 02](02-reading-a-conversation.md). You can narrate a conversation from a capture.

## Why this lesson exists

This is the first lesson where you build an expectation rather than read an event, and it is deliberately placed before anything about threats.

The reason is in the course's design: **an analyst who cannot describe healthy traffic cannot justify calling anything unhealthy.** Every "suspicious DNS" finding you will ever make is a claim about deviation, and a claim about deviation is worthless until you can say, specifically, from what.

DNS is the right place to learn this because DNS looks alarming when you first watch it closely. Addresses change under you. Answers contradict each other. Records expire in seconds. Names resolve through four other names before producing anything. Almost all of that is completely normal, and this lesson is mostly about finding that out the hard way — by predicting what you will see, then checking.

## The capture

Real queries against a real public resolver (1.1.1.1), captured live by [`lab/generate-captures.py`](../lab/generate-captures.py). The answers are whatever the internet actually returned on the day it ran. Nothing here was arranged to make a point; the points are what turned up.

Sixteen frames, eight query/response pairs. Start with the whole picture:

```
tshark -r assets/pcaps/03-dns.pcap -T fields -e frame.number -e dns.flags.response \
       -e dns.qry.name -e dns.qry.type -e dns.resp.ttl -e dns.cname -e dns.a
```

## What Security Onion would show you

Same workflow as lesson 02: the log first, the packets second. Search for this host's DNS and you get one document per lookup. In Security Onion's field names:

```
dns.query.name                       dns.query.type_name  dns.response.code_name  dns.answers.name                                 dns.ttls
www.github.com                       A                    NOERROR                 github.com, 140.82.113.3                         3600, 60
en.wikipedia.org                     A                    NOERROR                 dyna.wikimedia.org, 208.80.153.224               11342, 180
www.example.com                      A                    NOERROR                 104.20.23.154, 172.66.147.243                    300, 300
www.example.com                      AAAA                 NOERROR                 2606:4700:10::6814:179a, 2606:4700:10::ac42:93f3  300, 300
outlook.office365.com                A                    NOERROR                 outlook.cloud.microsoft,
                                                                                  acdcatm.outlook.mira.tm.svc.cloud.microsoft,
                                                                                  outlook.ms-acdc.office.com,
                                                                                  mdw-efz.ms-acdc.office.com,
                                                                                  52.96.164.146, 52.96.79.50,
                                                                                  52.96.164.130, 52.96.79.146                     289, 286, 60, 58, 8, 8, 8, 8
nonexistent-host-fbc19.example.com   A                    NOERROR                 —                                                —
www.github.com                       A                    NOERROR                 github.com, 140.82.112.4                         1277, 60
en.wikipedia.org                     A                    NOERROR                 dyna.wikimedia.org, 208.80.153.224               15928, 180
```

Security Onion adds two fields here that Zeek does not write, and both matter:

- **`dns.resolved_ip`** holds only the answers that are valid IP addresses, with the CNAMEs stripped out. For `outlook.office365.com` that is four addresses, not eight mixed records.
- **`dns.query.length`** is the character length of the query name. It exists so you can search on it, which becomes the point of [lesson 07](07-when-its-suspicious.md).

Now look at what `dns.response.code_name` does across those eight documents. **Every one says NOERROR** — including the one with no answers at all.

A Kibana search for successful lookups, written the obvious way as `dns.response.code_name:NOERROR`, returns eight of eight here. Seven of them resolved. One did not. The field an analyst instinctively reaches for does not distinguish them, and the field that does — `dns.answers.name` — is the one that gets left out of the dashboard because it is wide and ugly.

Hold that. It comes back later in the lesson with the packets behind it.

> **Running Zeek yourself?** `zeek -C -r assets/pcaps/03-dns.pcap` writes `dns.log` using Zeek's names — `query`, `qtype_name`, `rcode_name`, `answers`, `TTLs` — and without `dns.resolved_ip` or `dns.query.length`, which Security Onion computes during ingest. [The mapping is here](field-names.md).

## A name is not an address

Frame 1 asks for `www.github.com`. Frame 2 answers:

```
www.github.com    type CNAME, ttl 3600   -> github.com
github.com        type A,     ttl 60     -> 140.82.113.3
```

Two records, not one. The first says *that name is really this other name*. The second says *and that one is at this address, for the next 60 seconds*.

Three things are worth extracting from four lines of output:

**The answer has a shelf life.** TTL 60 is not decoration. It is the origin telling every resolver on earth how long this answer may be reused. Sixty seconds is short, and short is a design choice: it means the operator intends to be able to move this service quickly.

**The two records expire at different rates.** The alias is good for an hour; the address is good for a minute. That asymmetry is the normal shape of a service that stays at the same name while moving between machines. When you see it, you are looking at infrastructure designed to change.

**Nothing here tells you the client connected.** A DNS answer is a question answered, not a connection made. Lesson 02's capture would tell you that. This one cannot, and conflating the two is one of the most common errors in DNS-based reporting.

## The same question, five seconds later

Frames 13 and 14 ask the identical question again, 5.5 seconds after the first:

```
frame 2   (t=0.014s)   github.com  A  ttl 60    -> 140.82.113.3
frame 14  (t=5.529s)   github.com  A  ttl 60    -> 140.82.112.4
```

**The address changed.** Same name, same resolver, five seconds apart, different answer — and the TTL had not even expired.

Sit with that before reading on, because your instinct about it matters more than the explanation. If a detection rule fires on "host resolved the same name to two different addresses in under a minute," this is what it fires on, and there is nothing wrong here at all. Large services answer from pools. Which member you get depends on the resolver node, the time, and load. **Address instability for a name like this is the expected behavior, not the deviation.**

Now look at the CNAME TTLs across the same two frames:

```
frame 2   (t=0.014s)   www.github.com  CNAME  ttl 3600
frame 14  (t=5.529s)   www.github.com  CNAME  ttl 1277
```

And at `en.wikipedia.org`, frames 4 and 16:

```
frame 4   (t=0.434s)   en.wikipedia.org  CNAME  ttl 11342
frame 16  (t=5.849s)   en.wikipedia.org  CNAME  ttl 15928
```

The github TTL fell by more than the elapsed time. The wikipedia TTL **went up**.

A TTL is supposed to count down. A TTL that increases looks, on its face, like tampering — and if you have ever seen a threat-hunting article about DNS manipulation, that is roughly the shape of the indicator. What actually happened is that `1.1.1.1` is anycast: the two queries were answered by different cache nodes, holding the same record at different points in its life. Neither node is wrong. There is no single countdown to observe, because there is no single cache.

**This is the lesson's core.** Two observations that a rule would flag — an address that changed inside its TTL, and a TTL that ran backwards — are both ordinary. Not because anomalies do not matter, but because *you cannot tell which anomalies matter until you know what normal looks like in detail*, and normal is stranger than it appears from a diagram.

## Answers that are not addresses

Frames 11 and 12 ask for `nonexistent-host-fbc19.example.com`. Read the response carefully:

```
Flags: 0x8180  Standard query response, No error
    .... .... .... 0000 = Reply code: No error (0)
Questions: 1
Answer RRs: 0
Authority RRs: 1

Authoritative nameservers
    example.com: type SOA, class IN, mname elliott.ns.cloudflare.com
        Time to live: 1800
```

**No error. Zero answers.**

The response code is `NOERROR`, which reads like success, and the answer section is empty, which is the opposite of success. What arrived is an SOA record in the authority section — the zone's own statement of who is authoritative, and how long you may cache the fact that there is nothing here.

Two different things get confused at this point, and the distinction is worth carrying:

- **NXDOMAIN** (`dns.response.code: 3`) — that name does not exist.
- **NOERROR with zero answers** — the name exists in the zone but has no record of the type you asked for. Commonly called NODATA.

This capture shows the second. An analyst who searches `dns.response.code_name:NOERROR` to find successful lookups counts this as a success. An analyst who also checks `dns.answers.name` does not.

The habit generalises well beyond DNS: **a status field and an outcome are different things.** Lesson 02 made the same point with a 403 inside a perfectly successful TCP connection.

## Chains

Frames 9 and 10 ask for `outlook.office365.com`. The answer is eight records deep:

```
outlook.office365.com                              CNAME  ttl 289  -> outlook.cloud.microsoft
outlook.cloud.microsoft                            CNAME  ttl 286  -> acdcatm.outlook.mira.tm.svc.cloud.microsoft
acdcatm.outlook.mira.tm.svc.cloud.microsoft        CNAME  ttl 60   -> outlook.ms-acdc.office.com
outlook.ms-acdc.office.com                         CNAME  ttl 58   -> MDW-efz.ms-acdc.office.com
MDW-efz.ms-acdc.office.com                         A      ttl 8    -> 52.96.164.146
MDW-efz.ms-acdc.office.com                         A      ttl 8    -> 52.96.79.50
MDW-efz.ms-acdc.office.com                         A      ttl 8    -> 52.96.164.130
MDW-efz.ms-acdc.office.com                         A      ttl 8    -> 52.96.79.146
```

Four aliases before an address, four addresses at the end, and a TTL of **eight seconds**.

An eight-second TTL means the operator wants to re-steer this client almost continuously. The name you asked for and the name that finally carried an address share no common suffix — `office365.com` at the top, `office.com` at the bottom, `cloud.microsoft` in the middle. Any rule that assumes the resolved name resembles the queried name breaks here, on entirely legitimate traffic from one of the largest mail services in the world.

## Your work product — a baseline

Write **one page** describing expected DNS behavior for the environment this capture came from. Not a summary of the capture: a description of normal that someone else could use to judge whether a future observation deviates.

Use the capture to ground every claim, and answer these inside it:

1. **What is the observed range of TTLs, and what does the spread tell you?** The capture holds values from 8 seconds to 15,928. Explain what a very short TTL and a very long TTL each imply about the service behind the name.
2. **Which of these would you expect to be stable over a day, and which would you expect to change?** Cover: the queried name, the CNAME target, the A record, the number of A records, and the TTL. Justify each from the capture.
3. **`www.example.com` was asked for both A and AAAA** (frames 5–8). Compare the two answers. What would you conclude if a host queried only one of them? What would you conclude if the two disagreed about how many addresses exist?
4. **Write three detection ideas that this capture proves would be noisy**, and for each, name the frames that would trigger it falsely.
5. **Write one thing in this capture that you would want to look at more closely if you saw it on your own network**, and say precisely what additional evidence would settle it. This is not a trick — there is a defensible answer — but your reason has to be about the observation, not about the vendor.
6. **State what a DNS log cannot tell you** about whether anything actually happened as a result of these lookups. Be specific about which source would, and name the field you would search there.

## Reviewing your own work

- Every claim in your baseline: which frame supports it? A baseline built on what you already believed about DNS is not a baseline, it is a memory.
- Did you write "the address changed, which is suspicious" anywhere? Frames 2 and 14 say otherwise. Did you write "the address changed, which is normal for this kind of service"? Then say which kinds, and how you would tell the difference.
- For question 4, are your three noisy detections actually distinct, or three phrasings of the same one?
- Did you claim anywhere that a lookup means a connection? Go back and check. It is the easiest error in this lesson to make and the hardest to notice.
- Eight seconds and 15,928 seconds are both normal in this one capture. Does your baseline accommodate both, or did you write a rule that one of them breaks?
- Would this baseline still be useful in three months? If it depends on specific addresses, no. If it describes shapes and relationships, probably.

## What this lesson does not do

The capture is eight lookups from one client against one public resolver. That is enough to demonstrate the shapes; it is nowhere near enough to baseline a real environment, which would need volume, time, and every resolver in use.

It does not cover DNS over TLS or DNS over HTTPS, where these lookups would not be visible to a network sensor at all. That is lesson 04's territory and lesson 05's problem.

It does not cover tunneling, exfiltration over DNS, or algorithmically generated domains. Those are lesson 07, and they are deliberately after this one — recognizing a wrong shape requires knowing the right one.

It does not define proficiency, scoring, or completion. One baseline from one capture is a single sample.
