# Lesson 08 — Judgment and Handoff

## At a glance

- **Part of:** [the course plan](../COURSE.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-18
- **Capability targets:** JU-1, JU-2, JU-3, JU-4, CT-1, CT-2, CT-3, CT-4
- **Evidence families:** EF-6, EF-7
- **Time:** about 2 hours
- **Requires:** nothing. The analysis is supplied. No capture data or tooling.
- **Assumes:** lessons 01 through 07. This lesson adds no new technical subject matter; it is where the reasoning becomes something another person can use.

## Why this lesson exists

An analysis nobody can act on is not finished. It is a private opinion with citations.

By this point you can frame a question, gather evidence, weigh explanations, and notice when you are wrong. What remains is the part that most often fails in real teams: converting that into a judgment sized correctly to the evidence, an action sized correctly to the risk, and a handoff that lets someone else act without redoing your work or mistaking your uncertainty for fact.

The failure here is rarely ignorance. It is overclaiming under pressure, because a confident answer feels more useful than an honest one.

## Proportionate judgment

A judgment is proportionate when its strength does not exceed the evidence under it, and when a reader can see the connection.

Two failures, equally bad:

- **Overclaiming.** "This is a compromised host." Someone re-images a machine, a team loses a day, and if you were wrong the real cause is still running.
- **Underclaiming.** "There is insufficient evidence to determine anything." Often technically true and operationally useless. You almost always know *something* — which explanation is currently leading, and what would settle it. Refusing to say so is not caution, it is passing the decision to someone with less context than you.

Between them: *"Most likely X, because of A and B. Y remains possible and is not ruled out because we lack C. If C shows D, that changes the answer."* That sentence is the deliverable of this lesson.

## Confidence with a basis

Confidence language is worthless without a stated reason for it. "High confidence" alone tells the reader how you feel.

Say what the confidence rests on, in the same breath:

> Moderate confidence. Three independent sources agree, but all three depend on the same logging pipeline, and if that pipeline is wrong they are all wrong together.

Two habits worth carrying:

- **Name the dependency.** Independent-looking evidence that shares a single source is one piece of evidence wearing three hats.
- **State the breaker.** What single finding would most reduce your confidence? If nothing would, you are not holding a judgment, you are holding a belief.

## Action sized to risk and reversibility

The recommendation is a separate decision from the judgment, and it is not simply the judgment restated. Weigh:

- **Consequence of being wrong in each direction.** Blocking a legitimate business service and missing an active intrusion are both errors, with very different shapes.
- **Reversibility.** Isolating a host is reversible in an hour. Reimaging destroys the evidence you would need to check yourself.
- **Cost of waiting.** Sometimes an hour of collection is cheap and the risk of waiting is low. Say so — "wait and collect C" is a real recommendation, not an absence of one.
- **A stopping point.** JU-4 includes knowing when to stop. Investigation without a stopping condition expands until someone gets bored, which is not a decision.

## The two-audience problem

The same analysis goes to people who need different things, and the evidence underneath must not change between them.

**A peer or responder** needs enough to act and to check you: what you saw, what you concluded, what you are unsure about, what you already ruled out, and what you did not look at. Detail is respect for their time, not a burden on it.

**A manager or system owner** needs the decision, its consequence, and the uncertainty that matters to *their* choice. Compression is the skill. Deleting the uncertainty is not compression — it is a different claim.

The line: adapt framing, depth, and vocabulary freely. Never adapt the strength of the claim to the audience's appetite for it. If leadership hears "confirmed" and your peer hears "probable," you have told two different stories, and one of them is false.

## Anatomy of a handoff

A handoff another role can use contains:

1. **What is being handed over, and what you are asking for.** "Please determine X" beats "FYI."
2. **The current best explanation, with its confidence and basis.**
3. **What you ruled out, and how.** This is the part most often omitted and most often re-done at cost.
4. **What you did not examine.** Silence reads as "checked and clear."
5. **Live uncertainties**, especially any that change what the receiver should do.
6. **Time and scope boundaries.** What window, which hosts, which data sources — and what is outside them.

## When it stops being your job

CT-4. Network analysis borders incident response, threat hunting, detection engineering, intelligence, and system ownership, and the boundary is not clean. You will routinely be the first person to see something that belongs to someone else.

The professional move is neither to grab it nor to drop it: state what you found, name the role that owns the next step, and say what you can still contribute. "This looks like a credential problem — the identity team owns it, and I can supply the source addresses and timing whenever they want them" hands off cleanly without abandoning it.

## Worked contrast

One analysis, two write-ups. Same evidence.

> **Overclaimed:** "HOST-22 is compromised and was used to attack the authentication service. Recommend immediate reimage and a password reset for all affected users."

> **Proportionate:** "A configuration change at 08:12 explains most of the authentication failures. A residue of about 40 failures does not fit that pattern and is consistent with password spraying, though it is also consistent with a stale service account retrying. Moderate confidence in the configuration cause; low confidence on the residue. Recommend rolling back the change now — it is reversible and low-cost — and asking the identity team to review the 40 residual attempts before anyone resets credentials."

The second is longer, more useful, and easier to be wrong in safely. It also tells the reader exactly which future finding would change it.

## The case

You are handed a completed analysis. Your job is the judgment and the communication, not the investigation.

> **Situation.** Intermittent authentication failures across the Denver office began at approximately 08:15 and continued through 11:00. A helpdesk backlog is growing. The identity team, the network team, and a manager are all in the same chat asking for an answer.

| ID | Finding from the completed analysis |
|---|---|
| D-01 | A load balancer configuration change affecting the Denver authentication path was applied at 08:12. |
| D-02 | 94% of failures originate from clients whose sessions traversed the changed path. |
| D-03 | The remaining 6% — about 40 attempts — came from outside the office address range, against 12 distinct accounts, none of which succeeded. |
| D-04 | The 40 attempts occurred in two bursts, at 08:40 and 10:05, and used a single source address not seen in the prior 30 days of available records. |
| D-05 | Two of the 12 targeted accounts belong to users who left the company more than a year ago and remain enabled. |
| D-06 | Endpoint telemetry for the Denver office was unavailable during the window because of an unrelated collector outage. |
| D-07 | A rollback of the 08:12 change has been prepared and can be applied in about ten minutes. |

## Your work product

Produce two documents from this one analysis. Together they should take about a page and a half.

**1. A handoff to the identity team.** They own the accounts and the credential decision. Give them what they need to act and to check you, including what you did not examine.

**2. A summary for the manager who has to decide what happens in the next hour.** Same evidence, same claim strength, compressed to what bears on their decision.

Across both, make these visible:

- Your judgment on the 94%, and your separate judgment on the 6%. They do not have the same confidence and must not be merged into one verdict.
- The basis of each confidence level, and what would change it.
- A recommended action for the next hour, with its reversibility and cost stated.
- A stopping point: what would make this finished, or make it someone else's.
- The role boundary: what is yours, what is not, and what you can still supply.
- The consequence of D-06 — a gap you did not choose and cannot close, which a reader must not mistake for "nothing was there."

## Reviewing your own work

- Read your strongest sentence. Point to the finding directly beneath it. If you cannot, weaken the sentence.
- Do your two documents make claims of the same strength? Put them side by side and compare only the claim sentences.
- Did D-05 change your recommendation, or only your tone? Two enabled accounts for departed users is a real finding — but it is a finding about account hygiene, not evidence that this attempt succeeded. Did you keep those separate?
- Would the identity team have to re-derive anything you already know?
- Did you state what you did *not* look at, or did you leave silence to imply coverage?
- Is your recommended action reversible? If not, is that justified by the evidence, and did you say so?
- If the 40 attempts turn out to be a misconfigured legacy service retrying with old credentials, does your write-up survive? If it embarrasses you, it was overclaimed.

## What this lesson does not do

It does not define proficiency, scoring, or completion. It does not establish that your communication is effective — that requires a real reader, which is what lesson 09 and the [run records](run-records.md) exist to gather. Two documents from one supplied analysis is a single sample.
