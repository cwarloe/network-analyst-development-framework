# Capability Model v0.1 Validation Slice: Encrypted Outbound Traffic

## Purpose

This slice tests whether the [proposed Network Analyst Capability Model v0.1](2026-07-12-nadf-network-analyst-capability-model-v0.1-proposed.md) can describe and expose evidence of useful analyst performance in one realistic case.

It contains a synthetic evidence packet, a representative analyst work product, capability mapping, and a minimal evidence review. It is architecture validation—not a curriculum lab, answer key, scored assessment, or claim that the model is complete.

All organizations, systems, domains, addresses, and software names are fictional. Reserved `.example` domains and TEST-NET addressing are used intentionally.

## Synthetic case

At 09:20 local time, monitoring identifies sustained encrypted outbound traffic from workstation `WS-447` to `203.0.113.42:443`. The connection pattern begins shortly after a scheduled update to a fictional synchronization client named AcmeSync.

The immediate question is:

> Is the traffic reasonably explained by the authorized software update, or does available evidence justify containment or escalation as potentially unwanted or adversary-controlled activity?

### Available evidence

| ID | Source | Observation | Known limitation |
|---|---|---|---|
| E-01 | Change record | AcmeSync 4.8.2 deployment began at 09:00 for 40 workstations. | The record does not describe post-update telemetry destinations. |
| E-02 | DNS log | `WS-447` resolved `telemetry.acmesync.example` to `203.0.113.42` at 09:14:52. | The domain and address are fictional; DNS resolution alone does not establish legitimacy. |
| E-03 | Network flow | `WS-447` began TLS connections to `203.0.113.42:443` at 09:15:03, transferred 18.4 MB outbound and 1.8 MB inbound over 42 minutes, and reconnected approximately every 60 seconds. | Flow data does not expose encrypted content. |
| E-04 | TLS metadata | The observed server name and certificate subject reference `telemetry.acmesync.example`; the certificate chain validates in the collection environment. | A valid certificate does not prove that the process or service is trustworthy. |
| E-05 | Endpoint process record | Signed `AcmeSync.exe` launched signed `AcmeSyncUpdater.exe` at 09:14:39. The updater initiated the connections. | Loaded modules, runtime behavior, and binary provenance have not been independently reviewed. |
| E-06 | Peer comparison | 37 of 40 targeted workstations contacted the same destination after updating. Transfer volume ranged from 14 MB to 21 MB during the first hour. | Three targeted systems were offline; peer similarity can also reflect broad compromise or a compromised update channel. |
| E-07 | Proxy categorization | The destination is newly observed and uncategorized. No policy block or known-malicious match exists. | Lack of a reputation match is not evidence of safety. |
| E-08 | User report | The user did not manually start AcmeSync and observed no visible prompt. | Background update activity may be expected; user awareness is not determinative. |
| E-09 | Software inventory | `WS-447` reports AcmeSync 4.8.2 installed successfully. The updater hash matches the hash reported by the 36 online peer systems. | The expected vendor hash and release documentation are not yet available. |

## Representative analyst work product

### Assessment

The outbound TLS traffic is **more likely than not associated with the authorized AcmeSync 4.8.2 update**, with **moderate confidence**.

The timing, process attribution, DNS name, certificate metadata, peer prevalence, transfer-volume range, and matching updater hash form a coherent benign explanation. The available evidence does not establish malicious activity or justify immediate isolation of `WS-447`.

Confidence remains moderate rather than high because the evidence packet does not independently establish that the destination, signer, and updater hash belong to the expected vendor release. Encrypted payload content, loaded-module behavior, and vendor release documentation are unavailable.

### Observations separated from interpretation

- The deployment began before the new traffic appeared.
- The updater process initiated the observed connections.
- Most updated peers contacted the same destination with similar transfer volumes.
- DNS and TLS metadata use a name consistent with the fictional product.
- The destination is newly observed and uncategorized.
- The encrypted content and expected vendor release metadata are not available.

These observations support—but do not prove—the interpretation that the traffic is legitimate update or telemetry behavior.

### Plausible explanations

| Explanation | Supporting evidence | Evidence against or unresolved |
|---|---|---|
| Authorized update or first-run telemetry | E-01 through E-06 and E-09 align in time, process, destination, and peer behavior. | Vendor ownership, expected hash, and documented transfer behavior remain unverified. |
| Authorized software behaving unexpectedly or misconfigured | The volume is substantial and the destination is newly observed. | Peer volumes are similar, reducing the likelihood of a host-specific fault. |
| Compromised or malicious update channel | Broad peer consistency and signed processes could occur in a supply-chain compromise. | No contradictory process, destination, certificate, reputation, or peer evidence currently supports this explanation. |
| Malicious process masquerading as or injected into AcmeSync | Encrypted traffic and incomplete runtime visibility leave this possible. | Process lineage, signatures, and peer hash consistency make simple masquerading less likely. |

### Evidence that would most improve the judgment

1. Confirm the expected updater hash, signer, telemetry domain, and first-run transfer behavior from an authoritative software source.
2. Compare loaded modules and effective binary path on `WS-447` with a known-good updated peer.
3. Confirm whether the destination address is part of the expected vendor service infrastructure.
4. Review endpoint behavior for unexpected child processes, persistence, credential access, or unrelated network activity.

Payload decryption is not the first recommendation because existing metadata and endpoint comparisons can test the leading explanations at lower cost and with less operational impact.

### Recommended action and boundary

- Do not isolate `WS-447` on the current evidence alone.
- Maintain monitoring while the software owner or endpoint team validates release metadata and runtime parity with a known-good peer.
- Escalate for containment if validation fails, process behavior diverges, or additional suspicious activity appears.
- Route vendor-release validation and deep endpoint runtime inspection to the appropriate software-owner or endpoint-response interface; the network analyst should provide the observed timeline, destination, peer comparison, and open questions.

## Capability mapping

| Domain | Capabilities demonstrated | Evidence in the work product |
|---|---|---|
| Operational context and system understanding | OC-1, OC-2, OC-3, OC-4 | Connects the deployment, application behavior, peers, destination, and expected update context. |
| Observation and evidence | OE-1, OE-2, OE-3, OE-4, OE-5 | Separates observations from interpretation, evaluates collection limits, and prioritizes discriminating evidence. |
| Investigation and analytical reasoning | IR-1, IR-2, IR-3, IR-4, IR-5 | Frames the decision, compares four explanations, derives evidence needs, and integrates network and endpoint sources. |
| Judgment and uncertainty | JU-1, JU-2, JU-3, JU-4 | Gives a bounded assessment, states confidence and gaps, and recommends a proportionate action. |
| Communication and team interfaces | CT-1, CT-3, CT-4 | Presents a traceable assessment and defines the software-owner and endpoint-response handoff. |
| Learning and model revision | Not directly demonstrated | The evidence packet has no later outcome, feedback, or repeated performance from which to observe LR capabilities. |

CT-2, audience adaptation, is also not directly demonstrated because the slice contains one work product for one general technical audience.

## Minimum observable evidence for this task

This is the smallest evidence set needed to judge meaningful performance in this case. It is not a scored rubric.

| Evidence | What useful performance looks like | Common failure signal |
|---|---|---|
| Situation framing | States the actual decision and relevant operational context. | Treats “encrypted outbound traffic” as automatically malicious or investigates without a decision question. |
| Observation record | Preserves accurate facts and source limitations. | Mixes interpretation into observations or ignores telemetry limits. |
| Alternative analysis | Compares more than one plausible explanation using discriminating evidence. | Commits immediately to a benign or malicious story. |
| Evidence prioritization | Requests evidence that could change the judgment at proportionate cost. | Produces an unprioritized collection wishlist or defaults to the most invasive option. |
| Assessment | Makes a claim no stronger than the evidence and states material uncertainty. | Uses unsupported certainty, vague hedging, or reputation absence as proof. |
| Action and handoff | Recommends a proportionate next step and gives adjacent roles usable context. | Confuses network-analysis scope with endpoint ownership or recommends containment without a stated basis. |

## Validation findings

### What worked

- The six domains described the work without forcing a rigid analytical sequence.
- The capability statements distinguished evidence handling, reasoning, judgment, and communication rather than collapsing them into generic “analysis.”
- Tool neutrality held: the work product depends on evidence characteristics, not a named product interface.
- The adjacent-role capabilities made the boundary between network analysis, software ownership, and endpoint response explicit.
- The model supported a non-security operational explanation without losing adversary-aware reasoning.

### What was not demonstrated

- Learning and model revision require an outcome, feedback, or repeated task and cannot be inferred from a single initial assessment.
- Audience adaptation requires at least two communication contexts.
- Proficiency, consistency, independence, speed, and transfer cannot be judged from one work product.

These are sampling limits, not defects in the model.

### Model change decision

**No Capability Model v0.1 statement requires revision from this slice.**

The exercise did not reveal a missing capability or harmful overlap. Adding new statements for baselining, temporal analysis, peer comparison, or prioritization would create premature task-level detail; those behaviors already fit within OC-3, OE-3 through OE-5, IR-3 through IR-5, and JU-4.

## Next useful validation

Use a case with a known outcome and feedback so the Learning and Model Revision domain can be observed. The intermittent DNS failure scenario is a good candidate because it can include an initial incorrect explanation, new evidence, model revision, service restoration, and a handoff boundary.

Do not add proficiency levels or scoring until multiple slices show that the capability statements are stable and that stronger formalization would serve a real consumer.
