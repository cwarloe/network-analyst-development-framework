# Capability Model v0.1 Validation Slice: DNS Failure and Model Revision

## Purpose

This slice extends validation of the [proposed Network Analyst Capability Model v0.1](2026-07-12-nadf-network-analyst-capability-model-v0.1-proposed.md) into capabilities that the first slice could not observe: feedback use, model revision, transfer, targeted learning, and audience adaptation.

It is a synthetic architecture-validation case, not curriculum, a scored assessment, or a prescribed analytical lifecycle. All names, domains, and addresses are fictional or reserved for documentation.

## Case

Users in one office report intermittent DNS failures after 08:00. Monitoring also highlights long, encoded-looking query labels sent every five minutes to `inventory.agent.example`. Internal resolver `192.0.2.53` records increased retries and `SERVFAIL` responses.

The analyst must determine whether the unusual queries explain the service failure and whether they indicate tunneling or another security concern.

## Round 1 evidence

| ID | Observation | Limitation |
|---|---|---|
| R1-01 | Affected clients send long labels to `inventory.agent.example` every five minutes. | Label appearance and periodicity do not establish tunneling. |
| R1-02 | The query labels differ by host but remain stable for each host. | The encoding purpose is unknown. |
| R1-03 | DNS retries and `SERVFAIL` responses increased after 08:00. | Resolver symptoms do not identify the failing component or direction. |
| R1-04 | Users report intermittent failures across several business applications. | The affected applications use many unrelated domains. |
| R1-05 | No known-malicious domain or address match exists. | Reputation absence does not establish legitimacy. |

## Initial analyst note

> Periodic encoded-looking queries may indicate DNS tunneling and may be causing resolver load or service disruption. Recommend blocking `inventory.agent.example` while investigating affected hosts.

## Feedback on the initial note

A peer reviewer does not accept the recommendation because the note:

- treats visual encoding and periodicity as stronger evidence than they are;
- does not establish whether the query pattern is new;
- does not compare affected and unaffected network segments;
- does not trace request and response behavior across the DNS path;
- does not test whether the queries are related to authorized software; and
- recommends a potentially disruptive block without showing that the domain causes the failures.

The feedback is specific to evidence and reasoning, not stylistic conformity.

## Round 2 evidence

| ID | Observation | Analytical relevance |
|---|---|---|
| R2-01 | Historical logs show the same per-host query labels for at least 30 days without prior service impact. | Weakens the claim that the query pattern itself caused the new failures. |
| R2-02 | The endpoint process is a signed inventory agent deployed across the organization. Its documentation says the label contains a non-secret device identifier. | Provides a plausible authorized purpose without proving all behavior benign. |
| R2-03 | A firewall policy change affecting the office path completed at 07:55. | Creates a timing-aligned alternative explanation. |
| R2-04 | Resolver-side capture shows successful upstream responses around 1,680 bytes for several affected domains. Client-side capture shows queries and retransmissions but no complete UDP response. | Localizes loss to the response path and makes fragmentation behavior relevant. |
| R2-05 | The new firewall policy drops non-initial IP fragments and does not permit DNS TCP fallback for the office segment. | Provides a mechanism capable of producing intermittent failure for larger responses. |
| R2-06 | A comparison office without the policy change resolves the same domains successfully and continues the same inventory-agent queries. | Separates the unusual query pattern from the failure condition. |
| R2-07 | A temporary policy rollback restores successful resolution immediately. Inventory-agent queries continue unchanged. | Strongly supports the path-policy explanation and weakens the tunneling-causation claim. |

## Revised analyst work product

### Revised assessment

The intermittent DNS failures were caused by the 07:55 firewall policy change blocking fragmented UDP responses and DNS TCP fallback for the affected office segment, with **high confidence**.

The periodic `inventory.agent.example` queries are consistent with an authorized inventory agent and are not supported as the cause of the service failure. Their appearance justified inspection, but the initial tunneling hypothesis over-weighted label form and timing while neglecting historical prevalence, path behavior, and comparison segments.

This assessment does not prove that every future query to the domain is benign; it establishes that the observed query pattern did not cause this incident and that current evidence does not support a tunneling finding.

### Model revision

| Element | Initial model | Revised model |
|---|---|---|
| Suspected cause | Encoded periodic queries causing tunneling or resolver load | Response-path failure introduced by the firewall policy |
| Key missing context | Query history, authorized application purpose, segment comparison | Now established through R2-01, R2-02, and R2-06 |
| Mechanism | Unspecified DNS abuse | Large UDP responses fragmented; fragments dropped; TCP fallback unavailable |
| Discriminating test | Block the suspicious-looking domain | Compare paths and temporarily restore prior policy behavior |
| Result | Not tested and potentially disruptive | Rollback restored resolution while the query pattern continued |

### Technical communication for network engineering

The office firewall policy deployed at 07:55 drops non-initial fragments and omits TCP/53 fallback. Resolver-side captures show complete upstream responses near 1,680 bytes; affected clients receive no complete UDP response and retry until failure. The comparison office is unaffected. Temporary rollback restored resolution.

Recommended correction: permit the environment's approved DNS response behavior, including required fragment handling and TCP fallback, then verify with affected large responses before closing the change. Preserve policy intent and security controls rather than broadly allowing unrelated traffic.

### Service-owner communication

The DNS disruption was traced to a network-policy change, not to the inventory agent. Service was restored through a temporary rollback while the policy is corrected and tested. No current evidence supports a DNS-tunneling finding. The inventory query pattern will remain visible in normal monitoring, so its presence alone should not be treated as a recurrence of this incident.

### Transfer check

The revised model predicts that a segment without the policy change should successfully resolve the same large responses even while producing the same inventory-agent queries. R2-06 confirms that prediction. This demonstrates transfer of the response-path explanation beyond the initially affected clients.

### Targeted learning need

The analyst identifies a specific gap exposed by the initial error: interpreting DNS response size, EDNS behavior, fragmentation, and TCP fallback across monitored paths. The appropriate response is targeted review and practice on that mechanism—not a generic requirement to study all DNS topics again.

## Capability mapping

| Capability area | Demonstrated evidence |
|---|---|
| Observation and evidence | Separates query appearance from causal evidence; uses history, path captures, comparisons, and rollback results. |
| Investigation and reasoning | Reframes the question, tests alternatives, identifies a causal mechanism, and uses a discriminating low-duration rollback. |
| Judgment and uncertainty | Corrects the original overclaim, bounds the revised conclusion, and avoids declaring all future inventory queries benign. |
| Communication and interfaces | Produces distinct technical and service-owner messages while preserving the same evidence and conclusion. |
| LR-1 — Compare expected and observed outcomes | Compares the initial tunneling expectation with continued queries after service restoration. |
| LR-2 — Revise models after feedback or evidence | Explicitly replaces the initial causal model and explains why. |
| LR-3 — Transfer concepts to a changed situation | Predicts and confirms behavior in an unaffected comparison segment. |
| LR-4 — Identify limits and seek targeted learning | Identifies a bounded knowledge gap in DNS transport behavior. |

## Minimum evidence of useful model revision

| Evidence | Useful performance | Failure signal |
|---|---|---|
| Response to feedback | Tests the criticized assumptions and missing comparisons. | Defends the original conclusion without new evidence or changes wording only. |
| Revision trace | Shows what changed, which evidence caused the change, and what remains bounded. | Replaces one conclusion with another without exposing the reasoning change. |
| Outcome use | Uses rollback and continued query behavior to test the causal model. | Treats service restoration as proof without checking competing conditions. |
| Transfer | Makes and checks a prediction in a related segment. | Repeats the same steps without applying the underlying concept. |
| Audience adaptation | Changes detail and action framing while keeping evidence and conclusion consistent. | Changes certainty or factual claims to suit the audience. |
| Learning need | Identifies a specific capability gap connected to performance. | Produces a broad topic list unrelated to the observed error. |

## Validation findings

### What this slice adds

- LR-1 through LR-4 are observable when the task includes feedback, new evidence, an outcome, and a transfer check.
- CT-2 is observable through two products for different consumers without requiring a formal communication taxonomy.
- Model revision can be evaluated through changed reasoning and predictions rather than through agreement with a preferred procedure.
- The capability model supports correction of a security-biased initial interpretation without discouraging legitimate adversary hypotheses.

### Model change decision

**No Capability Model v0.1 statement requires revision from this slice.**

The existing learning/model-revision and communication statements were specific enough to distinguish useful performance from superficial correction. Adding a dedicated capability for cognitive bias, DNS mechanisms, comparison analysis, or rollback testing would overfit the model to this case.

## Result

Across the first two slices, all six domains have produced observable evidence. The remaining uncertainty is no longer whether the model can describe integrated performance; it is whether the statements remain useful across a broader range of network-analysis work and consumers.

The next valuable step is not another scenario document by default. Use the model in the next real design or assessment task, and capture a new validation slice only if that work reveals a material model issue.
