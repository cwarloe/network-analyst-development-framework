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

## Demonstration — The Anatomy of a Name: What Healthy Looks Like

In [Book 1 Episode 04](../BOOK-1.md#4-names-have-behavior), Ethan expects DNS to behave like the neat diagrams from his certification study: query leaves, resolver answers, address is cached, done. Then he watches real DNS traffic and discovers that normal behavior looks alarming if you have never watched it closely.

Here is how an analyst establishes expected behavior on live infrastructure.

### Step 1: A Name Is Not an Address

Frame 1 asks for `www.github.com`. Frame 2 answers:

```
www.github.com    type CNAME, ttl 3600   -> github.com
github.com        type A,     ttl 60     -> 140.82.113.3
```

Three critical facts visible in four lines:

1. **The answer has a short shelf life:** `TTL 60` is not decoration. It is the origin operator saying: *you may only reuse this address for 60 seconds because we steer traffic actively across server pools.*
2. **Asymmetrical Expiration:** The alias (`CNAME`) is good for an hour (3,600s); the physical server address (`A`) is good for 60 seconds. This is the normal signature of cloud-native infrastructure designed to flex.
3. **Lookup != Connection:** Receiving a DNS answer proves a name resolved. It does **not** prove the client ever connected. Conflating DNS lookups with established connections is one of the most pervasive false-alarm drivers in security reporting.

---

## Guided Practice with Feedback — Commit Before You Look

Frames 13 to 16 ask two of these exact same questions again, **5.5 seconds later**. 

Before opening the packets, write down your predictions:

1. **Address Stability:** Frame 2 gave `github.com` an A record with `TTL 60`. Only 5.5 seconds have elapsed. Same IP or different IP?
2. **CNAME TTL Countdown:** `www.github.com` started with `TTL 3600`. What value do you predict after 5.5 seconds?
3. **The TAMPERING Alarm Test:** `en.wikipedia.org` started at `TTL 11342`. If it returns with `TTL 15928`, what does that mean?

### The Feedback (Checking Data Against Expectations)

Now look at the actual capture data:

```
frame 2   (t=0.014s)   github.com  A  ttl 60    -> 140.82.113.3
frame 14  (t=5.529s)   github.com  A  ttl 60    -> 140.82.112.4
```

* **Observation 1: The IP address changed in 5 seconds!**  
  * **Feedback:** A junior analyst's reflex: *"DNS Cache Poisoning / Fast Fluxing Attack!"*  
  * **The Heuristic:** Completely false alarm. Major cloud providers balance load across anycast clusters. **Address instability is the expected normal behavior for high-scale public CDNs.**

```
frame 4   (t=0.434s)   en.wikipedia.org  CNAME  ttl 11342
frame 16  (t=5.849s)   en.wikipedia.org  CNAME  ttl 15928
```

* **Observation 2: The TTL ran backwards (went up by 4,500s)!**  
  * **Feedback:** An alert rule flags this as *"DNS Header Manipulation."*  
  * **The Heuristic:** In anycast resolver networks (like `1.1.1.1`), successive queries are routed to different physical resolver nodes. Node A cached the record 30 minutes ago; Node B cached it 5 minutes ago. There is no single universal countdown timer.

---

## Part-Task Automation Micro-Drills

Before drafting your baseline, build speed and pattern recognition on the two most common DNS alert failure modes in a SOC.

### Drill 3.1: CDN Pool Rotation vs. Fast-Flux Sorter (45 Seconds)

In a live queue, you will routinely see alerts for *"Rapid IP address resolution changes on endpoint."*

**Your Task:** Classify each of these 4 DNS behaviors as **Benign CDN / Anycast Steering** or **Potential Adversarial Fast-Flux**:

1. `Domain: cdn.cloudvendor.example` · TTL: `20s` · CNAME chain: `2 canonical aliases ending in akamaiedge.net` · IPs: 4 addresses in Microsoft ASN 8075.
   - [ Benign CDN / Anycast Pool | Potential Adversarial Fast-Flux ]
2. `Domain: login-portal-auth77.top` · TTL: `30s` · CNAME chain: `None` · IPs: 8 addresses across consumer residential broadband ISPs in Romania, Brazil, and Vietnam.
   - [ Benign CDN / Anycast Pool | Potential Adversarial Fast-Flux ]
3. `Domain: telemetry.os-updates.example` · TTL: `60s` · CNAME chain: `1 alias to trafficmanager.net` · IPs: 2 addresses in Fastly ASN 54113.
   - [ Benign CDN / Anycast Pool | Potential Adversarial Fast-Flux ]
4. `Domain: qx991a-update.biz` · TTL: `10s` · NS records: 5 distinct dynamic IP nameservers changing every 2 minutes · IPs: 10 non-contiguous residential IP pools.
   - [ Benign CDN / Anycast Pool | Potential Adversarial Fast-Flux ]

<details class="reveal-gate">
  <summary>🔍 Check Your Classification Key</summary>
  <div class="reveal-content">
    <ol>
      <li><strong>Case 1: Benign CDN / Anycast Pool.</strong> Known vendor CNAME chain, enterprise ASN, low TTL used for geographic load balancing.</li>
      <li><strong>Case 2: Potential Adversarial Fast-Flux.</strong> High-risk TLD, zero CDN infrastructure, disparate residential broadband ASNs (compromised botnet proxy nodes).</li>
      <li><strong>Case 3: Benign CDN / Anycast Pool.</strong> Valid trafficmanager routing, consistent enterprise CDN infrastructure.</li>
      <li><strong>Case 4: Potential Adversarial Fast-Flux.</strong> High nameserver churn (Double Fast-Flux), short TTLs, residential pools masking bulletproof hosting.</li>
    </ol>
  </div>
</details>

### Drill 3.2: The "NOERROR / NODATA" Trap Check (20 Seconds)

SIEM dashboards frequently filter on `dns.rcode: NOERROR` to measure successful resolutions. 

**Your Task:** Match each DNS response to its true diagnostic meaning:

1. `rcode: NOERROR`, `answers: 0`, `authoritative: 1 (SOA in authority)`
   - Meaning: [ Successful Resolution | NODATA (Name exists, record type does not) | Non-Existent Domain ]
2. `rcode: NXDOMAIN`, `answers: 0`
   - Meaning: [ Successful Resolution | NODATA (Name exists, record type does not) | Non-Existent Domain ]
3. `rcode: NOERROR`, `answers: 3`
   - Meaning: [ Successful Resolution | NODATA (Name exists, record type does not) | Non-Existent Domain ]

<details class="reveal-gate">
  <summary>🔍 Check Your DNS Response Key</summary>
  <div class="reveal-content">
    <ol>
      <li><strong>Response 1: NODATA (Name exists, record type does not).</strong> Example: querying for an IPv6 <code>AAAA</code> record on a domain that only has IPv4 <code>A</code> records. The domain is valid, but returns zero IP answers. <em>Treating this as 'resolution success' in a SIEM causes ghost connection tracking.</em></li>
      <li><strong>Response 2: Non-Existent Domain (NXDOMAIN).</strong> The authoritative server confirms the domain name does not exist.</li>
      <li><strong>Response 3: Successful Resolution.</strong> The resolver returned 3 valid resource records.</li>
    </ol>
  </div>
</details>

---

## Practice Application — Building the 1-Page Environment Baseline

Apply this method to Frames 5–12 in `assets/pcaps/03-dns.pcap` (covering `www.example.com`, `outlook.office365.com`, and `nonexistent-host-fbc19.example.com`).

Draft a 1-Page Environment Baseline answering all six prompts below. Use the capture to ground every claim:

1. **The `NOERROR` / Zero Answers Trap:** Inspect Frame 12. The response flag is `NOERROR`, but `Answer RRs: 0`. Explain why querying `dns.response.code: NOERROR` in a SIEM will falsely report this as a successful resolution.
2. **The 8-Second Steering Chain:** Inspect the 8-record chain for `outlook.office365.com` (Frames 9–10). Why does an 8-second TTL prove active routing rather than malicious fluxing?
3. **What is the observed range of TTLs, and what does the spread tell you?** The capture holds values from 8 seconds to 15,928. Explain what a very short TTL and a very long TTL each imply about the service behind the name.
4. **Which records would you expect to be stable over a day, and which would you expect to change?** Cover: the queried name, the CNAME target, the A record, the number of A records, and the TTL.
5. **Write three detection rules that this clean capture proves would be noisy**, and for each, name the frames that would trigger it falsely.
6. **The Conn.log Bridge:** Identify which specific log file and field in Zeek/Security Onion must be checked before you can report that a DNS query resulted in actual data transfer. State what a DNS log cannot tell you about whether a connection occurred.

## Reviewing your own work

- Every claim in your baseline: which frame supports it? A baseline built on what you already believed about DNS is not a baseline, it is a memory.
- Did you write "the address changed, which is suspicious" anywhere? Frames 2 and 14 say otherwise. Did you write "the address changed, which is normal for this kind of service"? Then say which kinds, and how you would tell the difference.
- For question 4, are your three noisy detections actually distinct, or three phrasings of the same one?
- Did you claim anywhere that a lookup means a connection? Go back and check. It is the easiest error in this lesson to make and the hardest to notice.
- Eight seconds and 15,928 seconds are both normal in this one capture. Does your baseline accommodate both, or did you write a rule that one of them breaks?
- Would this baseline still be useful in three months? If it depends on specific addresses, no. If it describes shapes and relationships, probably.

---

## The 4DX In-The-Flow-of-Work Transfer System

Learning what healthy DNS looks like in a lab prevents "false-positive alert fatigue" in a live SOC. Without daily tracking, junior analysts revert to flagging any rapid address change or TTL decrement anomaly as "DNS poisoning" or "malicious fluxing."

### 1. Pinned Desk Aid: The DNS Baseline & Sanity Matrix

Pin this to your monitor or keep it in your triage playbook:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        DNS TRIAGE: NORMAL VARIATION VS. TRUE THREAT                    │
├─────────────────────┬─────────────────────────────────┬────────────────────────────────┤
│ OBSERVATION         │ WHAT ROOKIES THINK              │ REALITY / OPERATIONAL BASELINE │
├─────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ Address changes in  │ "DNS Cache Poisoning / Fast     │ NORMAL: CDN / Anycast pool     │
│ < 60 seconds        │ Fluxing Attack!"                │ load balancing (e.g. GitHub).  │
├─────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ TTL counts up or    │ "Man-in-the-Middle tampering    │ NORMAL: Anycast resolvers      │
│ jumps around        │ with TTL headers!"              │ answering from separate nodes. │
├─────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ `NOERROR` with      │ "Successful DNS lookup! Domain  │ NODATA: Name exists, but requested│
│ zero answer records │ is valid."                      │ record type does not exist.    │
├─────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ DNS lookup seen     │ "Host connected to malicious    │ UNPROVEN: Lookup != Connection.│
│ in `dns.log`        │ external IP!"                   │ Check `conn.log` for handshake.│
├─────────────────────┴─────────────────────────────────┴────────────────────────────────┤
│ RULE: Never escalate DNS without checking: (1) Pool behavior, and (2) Handshake proof. │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2. The Analyst's Daily 4DX Scorecard

```
WEEKLY 4DX SCORECARD — ANALYST: [ ____________ ]  WEEK OF: [ _________ ]

[ WIG / LAG TARGET ]: Zero false-alarm DNS escalations; 100% baseline-verified tickets.

[ LEAD MEASURE ]: % of DNS-related alerts where CDN pool behavior and TCP handshake proof
                 were verified in `conn.log` BEFORE opening an escalation ticket. (Target: 100%)

  DAY       DNS ALERTS TRIAGED   POOL CHECKED?   CONN.LOG HANDSHAKE PROVED?
  Mon              [   ]             [   ]                 [   ]
  Tue              [   ]             [   ]                 [   ]
  Wed              [   ]             [   ]                 [   ]
  Thu              [   ]             [   ]                 [   ]
  Fri              [   ]             [   ]                 [   ]

  WEEKLY DNS BASELINE COMPLIANCE: [ _____ / _____ ] = [ _____ % ]
```

### 3. The 5-Minute Friday Supervisor Huddle

Every Friday morning:
1. **Review the Scorecard (1 min):** Check total DNS alerts triaged vs. pool & connection verification rate.
2. **Review One DNS Alert (2 min):** *"On Ticket #4088, an alert fired for 'Rapid IP resolution change'. Did you verify if the domain belongs to a known CDN pool before escalating?"*
3. **Commitment for Next Week (2 min):** Commit to checking `conn.log` to prove actual outbound connection before escalating any DNS alert.

---

<div class="bridge-card">
  <div class="bridge-label">Next Step in Curriculum</div>
  <div class="bridge-title">Chapter 04 (Story) — What Encryption Leaves Behind</div>
  <p class="bridge-desc">You now understand how names behave and why healthy DNS changes over time. But what happens when the session transitions into TLS? Watch Ethan and Dana confront encrypted payloads and discover what evidence remains visible.</p>
  <a href="#/narrative/04-what-encryption-leaves-behind" class="bridge-btn">Continue to Chapter 04 →</a>
</div>

## What this lesson does not do

The capture is eight lookups from one client against one public resolver. That is enough to demonstrate the shapes; it is nowhere near enough to baseline a real environment, which would need volume, time, and every resolver in use.

It does not cover DNS over TLS or DNS over HTTPS, where these lookups would not be visible to a network sensor at all. That is lesson 04's territory and lesson 05's problem.

It does not cover tunneling, exfiltration over DNS, or algorithmically generated domains. Those are lesson 07, and they are deliberately after this one — recognizing a wrong shape requires knowing the right one.

It does not define proficiency, scoring, or completion. One baseline from one capture is a single sample.
