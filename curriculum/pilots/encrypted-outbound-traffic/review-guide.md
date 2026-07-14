# Review and Self-Review Guide

This guide supports useful feedback. It is not a scoring rubric, answer key that rewards matching language, or basis for a mastery claim.

## Review the initial work on the evidence available then

Do not penalize the learner for lacking `F-01` through `F-05`. A well-supported initial assessment will often judge authorized update or telemetry activity more likely than compromise, with bounded confidence, because timing, process lineage, peer behavior, names, certificate metadata, and shared hash align.

Other initial conclusions can be defensible if they accurately weight the packet, preserve alternatives, and recommend proportionate action. Immediate certainty in either direction is not supported.

Look for:

- the operational decision and cost of disruption are explicit;
- observations remain distinguishable from interpretations;
- both expected software activity and shared compromise or deployment failure remain plausible;
- certificate validity, signatures, reputation absence, and peer prevalence are not treated as proof;
- vendor release metadata and binary/runtime parity are prioritized because they can change the decision;
- the assessment is no stronger than the available evidence;
- monitoring and targeted validation are considered before broad disruption, with conditions that would trigger escalation;
- the handoff gives adjacent roles the timeline, scope, destination, process, peer pattern, and open questions.

## Review the revision

The follow-up evidence should materially change the model. Useful revision will usually move toward suspected compromise of the deployment package and coordinated containment or risk reduction across the affected cohort.

Look for:

- `F-01` and `F-02` directly contradict the expected-vendor explanation;
- `F-03` and `F-04` provide a distribution path and suspicious host mechanism;
- peer similarity is reinterpreted as evidence of shared exposure rather than reassurance;
- the learner explains the change instead of silently replacing the conclusion;
- action accounts for all 37 affected systems, preserves evidence, validates offline scope, and protects or investigates the automation path;
- uncertainty remains about initial access, complete behavior, impact, and offline systems;
- the handoff respects role boundaries while making coordinated response possible.

Ask the learner:

- Which initial inference was reasonable but provisional?
- Which new observation had the greatest decision value?
- What would have made the initial action too disruptive or too passive?
- What should monitoring or collection preserve for the response teams?

## Review the transfer response

A coherent transfer response identifies the firewall policy as the cause of the DNS failures: large responses are fragmented, the path drops required fragments, and TCP fallback is unavailable. History, the unaffected comparison office, and successful rollback weaken the tunneling explanation while the inventory queries continue.

The important evidence is not agreement with that sentence. Look for application of the underlying practices:

- separate an unusual observation from a causal claim;
- use time, history, comparison, mechanism, and outcome together;
- seek evidence that distinguishes explanations;
- revise a model when its prediction fails;
- recommend a bounded network-policy correction and verification rather than an unrelated domain block;
- avoid turning a targeted learning need into a generic requirement to study all DNS topics.

## Final reflection

The learner should be able to name at least one practice worth carrying into future work, such as:

- ask what decision the evidence must support;
- preserve the difference between observation and interpretation;
- compare explanations before escalating collection or disruption;
- treat common behavior as context, not automatic legitimacy;
- state what evidence would change the judgment;
- revise visibly when new evidence changes the model.

One performance experience does not establish proficiency, consistency, independence, or transfer across real work. It provides a useful work product and feedback opportunity.

## Design references

This pilot implements the existing [Network Analyst Capability Model v0.1](../../../docs/design-studio/2026-07-12-nadf-network-analyst-capability-model-v0.1-proposed.md) and [Assessment Evidence Model v0.1](../../../docs/design-studio/2026-07-13-nadf-assessment-evidence-model-v0.1-proposed.md). Its source cases remain available as the [encrypted-traffic validation slice](../../../docs/design-studio/2026-07-13-encrypted-outbound-traffic-capability-validation-slice.md) and [DNS model-revision validation slice](../../../docs/design-studio/2026-07-13-dns-failure-model-revision-capability-validation-slice.md).
