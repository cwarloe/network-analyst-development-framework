# What Can You Responsibly Say?

## At a glance

- **Part of:** [the narrative track](README.md) · read before [Lesson 08](../lessons/08-judgment-and-handoff.md)
- **Version:** 0.1 — draft
- **Date:** 2026-08-22
- **Time:** about 12 minutes
- **Requires:** nothing. No tooling, capture, or account.
- **Creates the question:** When operational pressure demands a single headline, how does an analyst deliver a proportionate judgment without destroying vital distinctions?

---

By the fifth month of my time at Harrowmere Equipment Group, I had learned how to investigate.

I could trace a connection through an enterprise switch fabric, distinguish an active TCP reset from a silent firewall drop, and evaluate whether periodic traffic represented background software or malicious convergence. I had stopped guessing at what took place inside encrypted tunnels, and I had learned to ask what each physical sensor was capable of seeing before relying on its silence.

What I had not yet learned was how to speak to leadership under pressure.

On a rainy Tuesday morning, that gap became very sharp.

At 08:12 UTC, Network Engineering rolled out an updated routing policy across our primary transit path to improve WAN performance. By 09:30 UTC, our monitoring dashboards lit up with red alerts. The corporate authentication service was recording a massive surge in failed login attempts. Over three thousand user workstations and services were reporting authentication timeouts and access denials.

Nia Alvarez, our Security Operations Manager, had gathered the incident response team into the main conference room.

On the whiteboard, the room was divided into two competing camps:
- Network Engineering insisted that the routing change at 08:12 was completely clean and that someone had launched a brute-force password spraying attack against Harrowmere’s identity directory.
- Application and Identity teams insisted that the network had broken the Kerberos and RADIUS transit paths, demanding an immediate emergency rollback of the entire morning change.

Nia looked around the table, her pen tapping rhythmically against her tablet.

“I have the Chief Information Officer calling me in twenty minutes,” Nia said, her voice measured and quiet. “She wants to know whether Harrowmere is currently under active cyber attack, or whether our own engineering teams broke authentication. I need a clear headline.”

She turned her eyes to Dana Shah.

Dana did not stand up. Instead, she leaned back slightly and looked over at me.

“Ethan analyzed the authentication telemetry and perimeter captures from the 08:12 window,” Dana said evenly. “He has the data.”

My stomach dropped. In earlier months, Dana would have stepped in, framed the technical issue with razor precision, and gently guided the room toward an evidence-based conclusion. Today, she sat with her arms folded, offering no prompts, no leading questions, and no editorial safety net.

I stood up and plugged my laptop into the conference room projector.

“I pulled the last ninety minutes of authentication failure records from our identity logs,” I began, bringing up the summary dataset. “We recorded 3,240 total failed authentication events across the network between 08:15 and 09:15 UTC.”

“Is it an attack?” Leah Moreno asked from the application side of the table.

“Look at the distribution of the failures,” I said, bringing up a split chart.

“Of those 3,240 failures, exactly 3,046 events—or 94% of the total—originated exclusively from workstations traversing the specific transit router where the 08:12 configuration update was applied. In the packet captures on that segment, client authentication requests to the directory servers are receiving no response. The TCP connections to port 88 and port 389 are terminating in `S0` states. The clients are timing out before they ever receive an authentication challenge.”

“So the routing change broke the path,” Owen Kline said, leaning forward.

“The configuration change is the leading operational explanation for that 94%,” I said carefully. “Association in time is strong, but association alone does not establish causation. We have not yet verified the routing table rollback.”

“What about the other 6%?” Nia asked immediately. Her eyes were sharp and focused. “What are the remaining two hundred failures?”

I clicked to the next slide, displaying the residual traffic.

“The remaining 194 failures originated from twenty-four external IP addresses across three different branch offices that do *not* traverse the modified transit path. These failures are not transport timeouts; they are explicit application rejections—`STATUS_LOGON_FAILURE`. They show a single source attempting dozens of different executive account names using a small, fixed dictionary of passwords at twenty-second intervals.”

The room went dead silent.

“Password spraying,” Leah murmured.

“So we *are* under attack,” an operations lead said, reaching for his phone. “We need to isolate the external branch gateways and trigger an enterprise-wide credential reset immediately.”

“Wait,” I intervened. 

It was the first time I had ever interrupted a senior operations lead in a management briefing. The room turned to look at me.

I took a breath, remembering Dana’s instruction: *A proportionate judgment does not exceed the evidence under it, and an action must be sized to its risk and reversibility.*

“We cannot compress these two findings into a single headline,” I said, addressing Nia directly. “If we declare that the entire incident is a password spraying attack, we will leave the broken routing policy in place, and three thousand legitimate employees will remain locked out of their jobs all day. But if we declare that this is merely a benign network misconfiguration, we will ignore an active credential spray targeting executive accounts at the branches.”

“So what is your assessment, Ethan?” Nia asked. “Give me the claim, the confidence, and the [[confidence_breaker|breaker]].”

I brought up the two-paragraph brief I had prepared:

> **Proportionate Assessment:**
> 1. *Primary Incident (94% of volume):* We have **moderate confidence** that the 08:12 routing update introduced a transit drop or MTU defect affecting authentication traffic on the primary WAN segment. The confidence basis is the strict temporal and topological alignment of 3,046 transport timeouts (`S0` states). The breaker: If a controlled rollback of the 08:12 change does not immediately restore successful authentication handshakes on that path within ten minutes, the network change is disproven as the sole cause.
> 2. *Secondary Security Residue (6% of volume):* We have **high confidence** that the 194 failed attempts across branch gateways represent an external credential spray against executive accounts. The basis is the explicit `STATUS_LOGON_FAILURE` codes, sequential account targeting, and temporal independence from the WAN path change. There is zero evidence that any of these attempts succeeded.

Nia read the slide carefully.

“And what is the [[proportionate_action|proportionate action]]?” Nia asked. “What do we tell the CIO, and what do we do on the network right now?”

“First, execute a controlled rollback of the 08:12 routing change on the WAN transit router,” I recommended. “Rollback is [[action_reversibility|highly reversible]] and carries minimal risk. If failure rates drop back to baseline on that path, the operational outage is resolved.”

“Second, do not issue an enterprise-wide password reset. That would disrupt thousands of users who are already dealing with connection timeouts. Instead, hand the 194 residual authentication events to the Identity and Incident Response team to temporarily lock and review the specific targeted executive accounts, while applying a dynamic block at the branch firewalls against the twenty-four originating external IPs.”

“Third, what did we *not* examine?” Nia asked, pressing me. “What is outside this analysis?”

“We did not inspect host endpoint logs on the branch workstations,” I stated clearly. “We do not know whether any internal credentials were leaked prior to this window. That investigation belongs to the Incident Response team.”

Nia sat back in her chair. The tension that had filled the room began to disperse into actionable clarity.

She picked up her phone to dial the CIO.

“Okay,” Nia said. “We execute the rollback on the WAN router now. Identity team, take Ethan’s IP list and review the branch executive accounts. Owen, monitor the transit path failure rates for the next fifteen minutes. Ethan, prepare the `[[two_audience_handoff|technical notes for Owen and your summary slide for my inbox]]`.”

The room broke into purposeful motion. Engineers headed for their keyboards, and managers began coordinating the rollback.

I unplugged my laptop, feeling the adrenaline slowly recede. I turned around to look at Dana.

She had stayed in her seat throughout the entire presentation. She hadn't corrected a single sentence. She hadn't added a clarifying footnote. She hadn't signaled approval or disapproval.

“How was the framing?” I asked quietly as we walked out into the hallway.

Dana looked at me with a slight, satisfied smile.

“You didn’t let them force a false choice,” Dana said. “A novice wants to be the person with the dramatic answer. An analyst is the person who protects the distinction between what is known, what is probable, and what is still unresolved under pressure.”

She tapped the printout in my hand.

“When you write your handoff in Lesson 08,” Dana added, “remember what just happened in that room. The people who read your reports will often want a single headline. If you give it to them at the cost of truth, you aren’t serving leadership. You’re just hiding the work.”

I walked back to my desk and opened the ticket queue. 

On the monitoring dashboard, the WAN router rollback was applied. Within three minutes, the 3,000 connection timeouts dropped to zero. Across the room, the identity team was quietly blocking the branch IP addresses.

The incident was not over, but the work was moving in the right direction—guided not by noise or panic, but by a judgment sized honestly to the evidence.

---

### Vocabulary & Concepts

| Term | Desk Translation |
|---|---|
| [Proportionate Action](#term-proportionate_action) | A recommended operational or defensive response whose severity, impact, and disruption are balanced against the strength of the supporting evidence and the reversibility of the decision. |
| [Confidence Breaker](#term-confidence_breaker) | A specifically named future finding or test result that, if observed, would immediately falsify or dramatically reduce confidence in the currently leading hypothesis. |
| [Action Reversibility](#term-action_reversibility) | The ease and speed with which an operational or security decision (such as rolling back a route versus wiping an endpoint) can be undone without causing permanent data loss or operational damage. |
| [Two-Audience Handoff](#term-two_audience_handoff) | An analytical communication discipline that presents identical claim strengths and evidence baselines to both technical peers and executive managers while appropriately tailoring technical depth and operational consequences to each group. |

---

**What happens next.** [Lesson 08 — Judgment and Handoff](../lessons/08-judgment-and-handoff.md) puts this communication discipline into practice, walking through the 94/6 authentication incident, the construction of confidence breakers, and the authoring of defensible peer handoffs and manager summaries.
