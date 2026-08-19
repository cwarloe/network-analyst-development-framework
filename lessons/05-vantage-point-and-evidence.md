# Lesson 05 — Vantage Point and Evidence

## At a glance

- **Part of:** [the course plan](../COURSE.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-19
- **Capability targets:** OE-3, OE-4, OE-5
- **Evidence families:** EF-4, EF-5
- **Time:** about 2 hours
- **Requires:** nothing. Each case describes its environment. No capture data, tooling, or lab access.
- **Assumes:** lessons 01 through 04. You can read a conversation, describe expected behavior, and state what encryption prevents you from seeing.

## Why this lesson exists

"I looked and there was nothing there" is the single most expensive sentence in network analysis, because it is almost never what the analyst means. What they usually mean is "the sources I happened to check, over the window they happened to cover, at the sampling rate they happen to run, did not record anything I recognized."

Those are different claims. The first closes an investigation. The second describes a search.

By now you can interpret evidence in front of you. This module is about the step before that: deciding what evidence to go and get, in what order, and — the part that separates an analyst from a tool operator — knowing in advance what each source will not be able to tell you, so that its silence gets the weight it deserves and not more.

## Sources answer different questions

Every source class is a trade between fidelity, coverage, and how long it survives. None of them is the good one.

| Source | Answers well | Cannot answer | Typical failure mode |
|---|---|---|---|
| Full packet capture | What was actually said, byte for byte; protocol detail; content when unencrypted | Anything outside its short buffer; encrypted payloads | Storage is expensive, so retention is hours or days — the richest source is usually the first one gone |
| Flow records (NetFlow/IPFIX) | Who talked to whom, when, how much, for how long, over long windows | What was said; anything below the sampling threshold | Sampling. At 1:100, absence of a record is very weak evidence of absence |
| Protocol/session logs (Zeek-style) | Structured per-connection facts — names, certificates, durations, status — over weeks | Content; anything the sensor could not see | Depends entirely on sensor placement, so it inherits every blind spot below |
| Proxy, DNS, firewall logs | Decisions and lookups at a specific chokepoint | Anything that did not traverse that chokepoint | Coverage is assumed to be universal and rarely is |
| Endpoint telemetry | Which process, which user, which file — the "why" the network cannot supply | Anything on a host without an agent | Server and appliance coverage is routinely worse than workstation coverage |
| Authentication and identity logs | Who tried to be whom, and whether it worked | Where they were on the network, or what they did after | Time skew against network sources, which quietly breaks correlation |

The pattern worth carrying: **network sources are strong on *what happened between machines* and weak on *why a machine did it*. Host and identity sources are the reverse.** Most questions that feel unanswerable are questions being asked of the wrong source class.

## Vantage point decides what exists at all

A sensor records what passes it. Everything else is not "missing data" — it was never data.

Four things routinely move the traffic away from where you are looking:

- **Address translation.** Past a NAT boundary, ten hosts become one address. Attribution to a specific host has to come from somewhere else, and you must know which side of the boundary your sensor sits on before you believe any host-level claim.
- **Tunnels and hairpins.** If a branch office routes through headquarters, the edge sensor sees branch traffic wearing the headquarters address. The traffic is visible; the *user* is not, without a second source to correlate against.
- **East-west versus north-south.** An edge sensor sees traffic leaving the organization. It sees nothing of one internal host talking to another, which is where lateral movement and most misconfigurations live.
- **Where encryption terminates.** A sensor before a TLS-terminating proxy and a sensor after it are looking at different things. Knowing which one you have is the difference between "we cannot see the content" and "we can, and nobody told you."

Before trusting any source, answer one question: **what would this sensor have seen if the thing I am looking for had happened?** If the honest answer is "nothing," its silence carries no information.

## Retention runs a clock you do not control

Evidence perishes on different schedules, and the schedules are usually inverted against usefulness: the most detailed source expires first.

This has an ordering consequence that is easy to miss. **Collect against the shortest clock first**, even when a slower source is more convenient — the 30-day logs will still be there this afternoon; the 36-hour capture buffer will not.

And one source is different in kind: **capture can be started.** Everything else answers only about the past. If the activity may be ongoing, beginning collection now creates evidence that does not currently exist, and it is often the highest-value item on the plan even though it answers nothing yet.

## Gaps you did not choose

Some absences are structural rather than accidental, and each one converts "not seen" into a weaker statement than it appears:

- **Sampling** — flow at 1:100 will reliably show a large transfer and may entirely miss a small, slow one.
- **Truncation** — captures configured to store only the first N bytes of each packet keep the headers and discard exactly the content you wanted.
- **Log level** — a device configured to log denies but not permits produces a record where success is invisible.
- **Outages** — a collector down for four hours leaves a hole that looks identical to a quiet period.
- **Coverage by design** — no agent on servers, no sensor between branches, no logging on the segment nobody owns.

An evidence plan that does not name its gaps is not a plan, it is a wish list. Naming them is not pessimism; it is the thing that makes the eventual finding defensible.

## What an evidence plan contains

1. **The question, restated precisely enough to be answerable** — including its time window and scope. "Is this host compromised" is not yet a question. "Did this host send more than a trivial volume to an external destination it has not contacted before, in the last seven days" is.
2. **An inventory of available sources**, each with its coverage window, its placement, and what it cannot show.
3. **Discriminating logic.** For each source: *if explanation X is true, this shows A; if Y is true, it shows B.* A source that looks the same under both explanations is not worth querying first, however easy it is to query.
4. **An order, with reasons** — driven by perishability, discriminating power, and cost, in roughly that priority.
5. **What to start collecting now**, if anything.
6. **What remains unanswerable with the sources available**, and what would be needed to change that.

Point 3 is the one that separates evidence planning from evidence gathering. The instinct is to collect what would confirm the leading explanation. The discipline is to collect what would *separate* the explanations — including the finding that would show you are wrong.

## Worked example

> **Question.** Did the finance file server (FS-FIN-01) send a significant volume of data to an external destination it does not normally contact, at any point in the last seven days?

> **Available sources.** Edge flow records, sampled 1:100, 90-day retention. Edge full packet capture, 36-hour rolling buffer. Zeek-style connection and TLS logs from the edge sensor, 30 days, unsampled. Web proxy logs, 60 days, covering browser traffic only. Internal DNS resolver logs, 14 days. Endpoint telemetry on workstations; **not** on servers.

Working through it:

- **Packet capture is out of range.** It is the richest source available and it cannot answer a seven-day question at all. Recognizing this immediately, rather than after an hour of searching, is most of the skill.
- **Connection logs are the primary source.** They cover the full window, they are unsampled, and they record external destinations per connection. This is where the question is actually answered.
- **Flow records corroborate volume** and extend past 30 days if needed — but at 1:100, their silence is not proof. They can confirm a large transfer; they cannot rule out a small one.
- **DNS resolver logs identify and cross-check**, with two conditions the plan must state: only if the destination was reached by name, and only if the server used the internal resolver.
- **Proxy logs are irrelevant here.** A file server is not browsing. Querying them would produce a clean result that means nothing — a false comfort, which is worse than no result.
- **Endpoint telemetry does not cover this host.** This is the gap that matters most: even with a confirmed transfer, no available source can say which process or account initiated it. That limitation belongs in the finding, not in a footnote.
- **Start capture now**, filtered to this host. If the activity is ongoing it is the only way to obtain content and detail, and every hour of delay is permanent loss.

**Order:** start the capture (perishable, creates evidence) → connection logs (covers the window, discriminates) → DNS logs (14-day clock, identifies) → flow (corroborates volume, no clock pressure).

**Unanswerable as things stand:** the content of anything encrypted; the initiating process or account; anything before the 30-day connection-log boundary except at sampled resolution.

## Your work product

> **Situation.** Users at the Portland branch report that a hosted SaaS application has been intermittently slow for three days. Sometimes it is fine; sometimes pages take fifteen seconds. Other applications seem unaffected. A manager wants to know whether the problem is in your network before the vendor is contacted.

> **Environment.** The Portland branch has no local internet egress — all traffic runs through a VPN tunnel to headquarters and leaves from the HQ edge, sharing its address. Branch router flow export is unsampled, 7-day retention. HQ edge full packet capture, 36-hour buffer. HQ firewall logs record connection-level events, 45 days. Endpoint telemetry is deployed on branch workstations. Traffic to the SaaS provider is TLS and is not intercepted. The provider publishes a status page and offers per-request server-side timing in its admin console. There is no sensor of any kind between the HQ egress and the provider.

Produce an evidence plan of about a page, containing all six elements listed above.

Three things the case is specifically testing — make your handling of each visible:

- The hairpin. Work out what the HQ edge sensor can and cannot attribute, and what a second source would have to supply to make per-user claims possible.
- The blind segment. A meaningful part of the path is observed by nobody you control. Decide what that does to the question as asked.
- The question's shape. "Is the problem in our network?" is a two-sided question, and one of the two sides has better evidence available than the other. Say which, and what that means for how strong your eventual answer can be.

## Reviewing your own work

- For each source you listed: what would it have shown if the problem *is* in your network, and what would it have shown if it is not? If those two answers are the same, why is that source in your plan?
- Did you write down any source's coverage window, or did you assume the sources cover the three days in question? One of them does not.
- What did you plan to start collecting? If the answer is nothing, and the problem is intermittent and ongoing, revisit that.
- Did you order by perishability, or by which system you find easiest to query?
- Name one finding that would make you conclude the problem is *not* in your network. If your plan cannot produce that finding, it is built to confirm rather than to discriminate.
- Did you state what remains unanswerable? A plan that appears to answer everything has hidden a gap rather than closed one.
- Would a colleague reading your plan know what your eventual "we found nothing" would actually mean?

## What this lesson does not do

It does not teach evidence *collection*. Configuring a sensor, choosing a capture filter under load, discovering that your tap sees one direction of a conversation, or finding out that a retention policy is not what the documentation claims — those are lab experiences, and this module does not provide them. It develops the reasoning that decides what to collect and how to weigh what comes back; a lab exercise remains worth building on top of it.

It also does not establish proficiency, scoring, or completion. One evidence plan for one supplied environment is a single sample.
