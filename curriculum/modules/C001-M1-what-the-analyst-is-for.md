# C001-M1 — What the Analyst Is For

## Module control

- **Course:** [C001 — Foundations of Network Analysis](../courses/C001-foundations-of-network-analysis.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-18
- **Capability targets:** OE-2, IR-1
- **Evidence families:** EF-1, EF-2
- **Time:** about 90 minutes
- **Requires:** nothing. No capture data, tooling, or account.

## Why this module exists

Most people arriving at network analysis expect the job to be recognizing bad traffic. It is not. Recognition is something a detection engine already does faster than you, and it is the part of the work most likely to be wrong in a way nobody notices.

The job is to make a decision safe to take. Someone — a responder, a system owner, a manager — is going to act, or decide not to act, and they need to know what is actually known, what is being guessed, and what would change the answer. Producing that is analysis. Everything else in this course is in service of it.

This module builds one habit, which sounds trivial and is not: keeping observation, interpretation, and judgment apart in your own head and on the page.

## Three things that get mixed together

**An observation** is what the data shows. `HOST-14 sent 4.2 GB to 203.0.113.40 between 02:00 and 04:00.` It can be checked. Someone with the same data gets the same observation.

**An interpretation** is what an observation might mean. `That volume at that hour is unusual for a workstation.` It depends on context, and someone with different context may reasonably read it differently.

**A judgment** is what you have concluded, with a stated strength. `This is more likely a backup misconfiguration than exfiltration, with moderate confidence.` It commits you, and it should never be stronger than the evidence under it.

A **recommendation** follows from the judgment and should be sized to it — but that belongs to M8.

Each collapse has its own failure mode:

- Observation stated as judgment: *"HOST-14 is exfiltrating data."* The reader cannot tell what was seen and cannot check you.
- Interpretation stated as observation: *"We observed anomalous traffic."* "Anomalous" is a conclusion wearing an observation's clothes. Anomalous compared to what?
- Judgment with no visible observations: *"I assess with high confidence that this is benign."* Nobody can disagree usefully, which means nobody can help you.

The most common one in real work is the second, and it usually arrives pre-installed in the alert you were handed.

## Worked example — Case A

Read this one with me. Do not write anything yet.

> **Alert:** `Possible data exfiltration — HOST-14`

Supplied observations:

| ID | Observation |
|---|---|
| A-01 | HOST-14 sent 4.2 GB to 203.0.113.40 between 02:00 and 04:00. |
| A-02 | The destination address is not in any internal asset record. |
| A-03 | HOST-14 belongs to a member of the finance team. |
| A-04 | The transfer used TCP/443. |
| A-05 | No prior connection from HOST-14 to this address appears in the 30 days of available records. |

Here is the separation.

**What was observed:** all five rows. Note that A-05 is weaker than it looks — it says the connection does not appear in *available* records, not that it never happened. The limitation is part of the observation.

**What is interpretation:** that 4.2 GB is "large" (large for a workstation, unremarkable for a backup job); that 02:00–04:00 is "off hours" (for the user, not for automated tasks); that an unrecognized destination is suspicious (asset records are usually incomplete); that TCP/443 means "hiding" (TCP/443 is where nearly everything legitimate lives).

**What was smuggled in:** the word *exfiltration*, in the alert title, before any analysis happened. It names a cause. Nothing in A-01 through A-05 establishes one. The alert has handed you a conclusion and asked you to confirm it — and confirming what you were handed is the single most common way network analysis goes wrong.

**What the actual question is:** not "is this exfiltration?" but *"is this transfer explained by authorized activity, and if we cannot tell yet, what would tell us?"* That is IR-1: framing an actionable question from an ambiguous condition. The reframed question is answerable. The original one is a yes/no invitation to guess.

**What is not yet known:** what process on HOST-14 opened the connection; whether the finance team uses a cloud service at that address; whether other hosts did the same thing; what the 30-day limit is hiding.

Notice that no judgment appeared anywhere above. On this evidence, none is available yet — and saying so is a complete and professional answer.

## Guided practice — Case B

Now you work, with prompts.

> **Ticket:** `Users in the Portland office report the intranet is slow. Network team says the network is fine.`

| ID | Observation |
|---|---|
| B-01 | Six users in Portland reported slowness between 09:00 and 11:00. |
| B-02 | Link utilization on the Portland uplink peaked at 34%. |
| B-03 | The intranet application server's CPU averaged 88% during the same window. |
| B-04 | Users in two other offices reported nothing. |
| B-05 | A Portland user says "it started after the update yesterday." |

Work through these:

1. Which rows are observations, and which contain an interpretation already? (Look hard at B-01 and B-05.)
2. "The network is fine" — is that an observation, an interpretation, or a judgment? What is it based on, and what does "the network" mean in that sentence?
3. B-05 is second-hand and vague. Does that make it useless? What is it good for?
4. Write the analytical question you would actually pursue. It should be answerable, and it should not contain the word "slow."
5. Name the two pieces of evidence most likely to change your answer, and say why those two.

There is no answer key. The check is in the next section.

## Your work product — Case C

Do this one unaided.

> **Handed to you:** `A server in the DMZ made 340 outbound DNS queries to a single domain in one hour. Flagged as possible DNS tunneling.`

| ID | Observation |
|---|---|
| C-01 | 340 queries from SRV-DMZ-02 to subdomains of `updates.example-vendor.net` between 13:00 and 14:00. |
| C-02 | Each query name is 28–34 characters and appears randomized. |
| C-03 | The same pattern appears in each of the previous 14 days at similar volume. |
| C-04 | SRV-DMZ-02 runs a vendor-supplied appliance. Its documentation is not available to you. |
| C-05 | No user is logged into SRV-DMZ-02. |

Produce, on one page or less:

- **The observations,** restated in your own words, each with its limitation if it has one.
- **The interpretations,** labeled as such, kept separate from the observations.
- **The question you would pursue,** phrased so that evidence could answer it.
- **Your position,** which may legitimately be that no judgment is available yet — if so, say what is missing.
- **The next two pieces of evidence** you would want, and why those two before others.

Do not write more than a page. Length is not the deliverable.

## Reviewing your own work

Not a score. Questions:

- Can a reader tell, from the page alone, which sentences could be checked against data and which are yours?
- Did the phrase "DNS tunneling" survive into your analysis as an assumption, the way "exfiltration" did in Case A?
- What did you do with C-03? Fourteen days of identical behavior is the most informative row in the table. Did it make the activity more suspicious, less, or neither — and can you say why?
- Is your position stronger than your observations support? Read your strongest sentence and find the evidence directly under it.
- If a responder acted only on your page, what would they do? Is that proportionate?

If C-03 pushed you toward "this has been happening for two weeks undetected," notice what happened: the same fact can support a benign reading (an established, documented vendor behavior) and an alarming one (a persistent channel), and choosing between them needs evidence you do not have. Recognizing that is the module.

## What this module does not do

It does not teach protocol mechanics, tooling, or how to read a capture — those start in M2. It does not establish that you can perform this reliably; one work product shows one performance. No score, level, or completion threshold is defined.
