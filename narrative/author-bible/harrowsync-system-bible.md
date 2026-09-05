# HarrowSync Environment System Bible — v0.1
## Author-only persistent technical/story environment for Book 1

## Status

**Working author canon, technically provisional.**

This defines the recurring Harrowmere business-system environment used for continuity across Book 1. It intentionally fixes logical behavior and ownership before exact IP addresses, vendor products, or packet-level artifacts. Any learner-facing technical detail must be validated against committed captures, logs, and lesson objectives.

## 1. Working name: HarrowSync

**HarrowSync** is Harrowmere's internal umbrella name for the set of services and jobs that keep warehouse/inventory activity synchronized with central business systems.

It is **not one application**. People casually say “HarrowSync is down,” but the workflow spans multiple components, owners, and evidence sources. Ethan initially treats it as one technical object and gradually learns to decompose it.

## 2. Business purpose

HarrowSync supports:
- inventory adjustments;
- receiving/shipping status;
- warehouse reconciliation;
- product/location updates;
- selected finance/accounting reconciliation data;
- scheduled site-to-central synchronization;
- vendor-supported integration components.

If delayed, consequences may include stale inventory state, delayed reconciliation, manual workarounds, finance-reporting delays, or shipment-processing friction. Impact depends on site, time, business cycle, failed component, and catch-up capability.

## 3. Logical components

### Site Sync Client / Agent
Packages local changes, submits updates, retrieves responses/configuration, retries failed work, and participates in scheduled reconciliation.

### Central HarrowSync Service
Internal file/API-facing service that accepts site requests, authenticates/authorizes, queues/validates, and hands data to downstream integration. Supports Episodes 1–3.

### Integration / Transformation Component
Translates or enriches data and passes it to ERP/inventory/finance systems.

### Central Business Systems
ERP / inventory / finance functions whose cycles create daily, first-business-day, month-end, and inventory-count variation.

### Vendor / Cloud Support Service
Legitimate encrypted external dependency for software-update metadata, packages, licensing, support/telemetry, or integration metadata. Supports Episodes 6 and 14.

### Internal Update / Automation Mechanism
Internal package repository + deployment/automation service + service credential + approved manifest/hash + staged rollout groups. Exists before Episode 14.

## 4. Ownership map

**Leah Moreno — application/workflow ownership:** business purpose, schedules, dependencies, job history, vendor relations, approved update behavior, operational consequence.

**Priya Raman — network/infrastructure ownership:** site connectivity, routing, segmentation, firewall/policy context, resolver relationships, failover, sensor-placement implications.

**Cal Rowan — security telemetry/tooling ownership:** network sensors, Zeek/Suricata-style telemetry, Security Onion ingest/search, enrichment, field normalization/derivation, detections, selected endpoint integrations.

**Dana/Owen/Ethan — analytical integration:** observed behavior + system model + domain context + source limitations + competing explanations + decision needs.

**Nia Alvarez — decision ownership:** investigation priority, escalation, interruption/containment, evidence preservation, business coordination.

## 5. High-level flows

Typical legitimate workflow:

**Warehouse/site activity → Site Sync Client → name resolution / routing → Central HarrowSync Service → Integration/Transformation → central inventory/finance systems**

Some workflows include:

**Site or central component → encrypted Vendor/Cloud Support Service**

Software lifecycle includes:

**Approved vendor artifact → internal package repository → automation/deployment service → selected HarrowSync hosts**

These are logical relationships, not guarantees of a single packet path.

## 6. Expected schedules and variation

### Daily incremental activity
Regular but imperfect timing; smaller transfers; multiple sites; retries; site-workload variation.

### First-business-day / month-end reconciliation
Larger volume, longer processing, additional central-system interaction, possibly more external calls.

### Full reconciliation / inventory-count activity
Less frequent, substantially larger or longer, and unsuitable as a universal baseline.

### Software-update windows
Occasional, staged, and governed by approved artifact/version/target-group expectations.

## 7. DNS behavior

Site clients use Harrowmere resolver infrastructure. Caching, TTLs, CNAME/vendor indirection, and vantage produce legitimate variation.

Author rule:

> “Name resolution occurred” and “I observed a DNS query from this host in this capture” are different statements.

Any unusual DNS behavior used in Episode 10 must be technically validated before canonizing exact query structure.

### Episode 10 causal sequence

Selected author design; exact artifacts are not yet built. This replaces the earlier unspecified tunneling and hour-long detour candidates in the Snowflake and beat matrix.

- **Initial view:** one site's sync failures coincide with conspicuous inventory-agent DNS bursts and a recent policy change. The baseline identifies the agent but does not establish its present request load. Effective path policy and paired captures have not yet arrived.
- **Ethan's hypothesis:** a malfunctioning inventory agent is creating client-side lookup contention. He overweights the conspicuous bursts; odd names alone do not establish maliciousness. Path policy remains an explicit alternative.
- **Discriminator:** if the agent causes local contention, stopping it and allowing pending lookups to drain should restore resolution on that client. A path-policy fault should persist and vary with response size or path. This test does not rule out load from other clients on a shared resolver.
- **Bounded action:** Leah confirms this background inventory task can pause on a test client without stopping essential sync. Nia authorizes a short test with a stop time; Priya prepares a safe policy comparison in parallel. Dana checks the prediction rather than supplying the answer. No domain-wide block or intentionally delayed decisive evidence.
- **Cost and failed prediction:** the queries stop, pending work drains, but resolution still fails. Staff time has been spent on a detour while that client's business workflow remains degraded. Ethan records the failed prediction and changes branches at the deadline.
- **Correction:** paired resolver/client evidence shows large responses failing to arrive intact; effective policy drops non-initial fragments and does not permit DNS TCP fallback. A controlled correction restores resolution, including after the agent resumes. Owner records and history support the agent's legitimate purpose separately from this causal finding.
- **Responsibility:** Ethan owns his overconfident ranking; Nia owns the permitted operational risk. Experienced colleagues allowed a bounded discriminating test, not an unsupported security verdict. Ethan recognizes the failed prediction before Dana explains it.

The existing fragmentation capture has two surviving fragments of an outbound query. It cannot substitute for paired failed-response observations or measured rollback results. Until those artifacts exist, this is a causal design for engineering, not claimed captured evidence. Reveal later facts by their actual collection times.

## 8. Network-path model

- Multiple sites do not have identical topology.
- At least one relevant redundant/failover path exists.
- Controls sit at different boundaries.
- Policy changes can affect sites/paths differently.
- Sensor visibility can change during failover.

Exact subnets/routers remain unresolved until exercises require them.

## 9. Historical network exception

A legitimate exception survived earlier standardization. It was once justified, is imperfectly documented, and can alter path/policy behavior. Purpose: show that current behavior partly reflects accumulated prior decisions, not create a “hidden config gotcha.”

## 10. Application historical exception

A legacy/fallback integration believed retired remains executable. It is rarely invoked and can wake under a specific failure condition. This is part of Leah's prehistory; it need not become a Book 1 incident.

## 11. Authentication / service identity

Legitimate automation uses service identities. Some historical operational requirements may have produced broader access than ideal. Credential use is not perfectly visible across every evidence source.

Episode 14 may involve misuse of a valid automation/deployment credential; technically provisional.

## 12. Update lifecycle

1. vendor/owner approves release;
2. artifact is retrieved/staged;
3. Harrowmere verifies approved artifact/manifest;
4. internal repository stores version;
5. automation deploys to selected group;
6. hosts install/update;
7. expected post-update behavior occurs;
8. rollout expands after validation.

**Selected Episode 14 trust boundary:** approval verifies the staged vendor artifact, but deployment later reads a mutable repository path without comparing the deployed bytes with the approved manifest again. Replacement after staging verification can therefore enter the rollout. Later audit evidence must establish both the ordering and this control gap; the initial change ticket does not establish either.

**Signature scope:** the altered package contains a validly signed updater binary different from the approved release, plus an unsigned module it loads. The executable's signature does not approve the entire package, its version, or its runtime dependencies. This is selected fictional case behavior, not a demonstrated vendor implementation. Do not imply that arbitrary modification preserves a binary's original valid signature; validate the selected implementation before treating endpoint mechanics as executed evidence.

The capstone should subvert a trusted process rather than rely on an obviously malicious random download.

## 13. Episode 14 provisional failure mechanism

A valid deployment credential is used to replace or alter a package inside the trusted internal update chain.

- updated hosts receive the same altered artifact;
- hosts show similar new outbound behavior;
- similarity initially supports the benign “shared approved update” explanation;
- vendor/domain/artifact verification later breaks that explanation;
- the same peer similarity becomes evidence of shared exposure.

**Execution and investigation owners:** Leah coordinates application impact and vendor confirmation. The enterprise deployment administrator owns the repository/job and pauses distribution; the identity team owns credential restriction or rotation; endpoint responders collect host evidence and investigate modules/persistence. Priya implements approved network controls, Cal supplies telemetry lineage and correlations, Ethan integrates findings, and Nia authorizes coordinated action. These adjacent teams need no new named protagonists. Cal does not silently become the endpoint investigator, deployment administrator, or credential owner.

## 14. Evidence sources and limits

### Network sensor / Zeek-style telemetry
Good for connection metadata, DNS, TLS metadata where visible, timing, volume, network relationships. Cannot establish process identity, business purpose, user intent, encrypted content, or end-to-end business success.

### Suricata/detection layer
Good for signatures/rules and selected anomalies. Alert presence does not equal maliciousness; alert absence does not equal benignness.

### Security Onion search/index
Good for multi-source search, stored fields, dashboards, analyst workflow. Some fields may be normalized or derived rather than directly present in raw evidence.

### Firewall/network logs
Good for policy allow/deny and selected session context. Cannot establish application success or full path/payload.

### Endpoint telemetry
Where present, useful for process-to-network relations, hashes, modules, persistence, and local files. Coverage is substantial but not universal.

### Application/job logs
Useful for job identity, schedule, local component outcome, and workflow context. “Job succeeded” is only success relative to that component's responsibility.

### Change/deployment records
Useful for intended change, approval, target group, timing, package/version expectation. Intended execution is not proof of actual execution.

### Human testimony
Leah, Priya, Owen, Cal and others provide high-value evidence with bounded scope, not ground truth.

## 15. Vantage model

### Site-side
May see client DNS, outbound initiation, local retries; may not see central application completion or other-site peers.

### Central network/security
May see site-to-central sessions, central-to-vendor traffic, cross-site comparisons; may miss process identity and some failover traffic.

### Application
May see jobs/transactions/local app results; may miss network drops or exact packet behavior.

### Endpoint
May see process → connection and artifact behavior; may not see full network path or remote business outcome.

## 16. Known observability gap

During a particular alternate/failover path, not all traffic traverses the same network-sensor vantage. Security Onion remains useful; absence at that vantage is not sufficient to establish absence of traffic during that condition.

## 17. Retention

Different evidence families have different useful windows:
- high-fidelity packet capture: short;
- session/protocol metadata: longer;
- application logs: component-dependent;
- endpoint telemetry: longer but coverage-dependent;
- change records: durable;
- vendor detail: outside Harrowmere control.

Exact durations remain unresolved.

## 18. What “normal HarrowSync” means

There is no single normal. Expected behavior depends on:
- site;
- job type;
- business date;
- software version;
- workflow stage;
- destination class;
- update state;
- path;
- daily/reconciliation/retry/update role.

## 19. Stable relationships worth baselining

More useful than simplistic thresholds:
- site role → service family;
- job class → time window;
- update group → approved package/version;
- service → owner;
- workflow → downstream component;
- approved update → known vendor/internal distribution relation.

## 20. Legitimate variation

Transfer size, duration, DNS visibility, number of sessions, retries, exact start time, site volume, TLS metadata visibility, route/vantage under failover.

Variation itself is not suspicious.

## 21. Relationships that should be unusual

- approved process → unapproved destination;
- approved update → wrong artifact hash;
- expected job → unexpected peer/time population;
- expected vendor relation → domain not vendor-controlled;
- known workflow → unexpected/unsigned module;
- shared update → behavior only on altered-package recipients.

## 22. Book 1 artifact catalog

E1 ticket/internal-service evidence  
E2 success vs application refusal  
E3 prediction capture  
E4 DNS/caching comparison  
E5 failure-state comparisons  
E6 TLS/encrypted workflow evidence  
E7 contextual baseline  
E8 same-event multi-vantage evidence  
E9 source/retention-cost table  
E10 DNS + fragmentation/policy staged evidence  
E11 explanation/discriminator case  
E12 benign vs concerning relational patterns  
E14 authorized-update evidence + staged breakers

Episode 13 is intentionally an adjacent transfer case.

## 23. Ethan's growing HarrowSync model

E1–2: “a service”  
E3: repeatable exchange  
E4: resolver/network-dependent service  
E5: workflow with multiple failure boundaries  
E6: system with encrypted external dependencies  
E7: population varying by role/site/time  
E8: differently observed system  
E9: evidence is perishable/costly  
E10: familiar odd behavior can coexist with unrelated failure  
E11: multiple plausible explanations  
E12: source of benign analogues and concerning relational contrasts  
E14: familiar enough that subtle relationship violations matter

## 24. Disclosure rule

Never dump the architecture. Reveal only what the scene requires. The author bible exists so the reader does not have to receive it.

## 25. Technical governance

1. Exact technical claims require committed learner artifacts.
2. Narrative does not invent packet evidence after technical validation merely for drama.
3. Engineering can reject technically impossible/misleading narrative handoffs.
4. Narrative can reject exercises that cannot support the story claim truthfully.
5. Reuse existing captures where possible.
6. Preserve answer-key control.
7. Move advanced mechanisms outside Book 1 when needed.
8. Reader-visible system detail must serve reasoning.
9. HarrowSync should feel like a plausible enterprise integration environment.
10. No evidence source becomes the canonical truth source.

## 26. Thematic function

HarrowSync exists simultaneously as:
- Leah's workflow;
- Priya's topology;
- Cal's telemetry pipeline;
- Owen's pattern history;
- Dana's causal models;
- Nia's operational consequence;
- Ethan's gradually improving mental model.

The analyst's job is not to select which representation is “the real one,” but to construct a judgment that respects how each contacts reality.

## 27. Unresolved technical questions

1. Exact central service protocol(s).
2. Whether file/API service is one component or two.
3. Resolver topology.
4. Site network shapes.
5. Current Security Onion fields/data types.
6. Exact TLS artifacts in E6.
7. E7 baseline schema.
8. E10 DNS/fragmentation mechanics.
9. E14 endpoint evidence.
10. Update-package/automation implementation.
11. Retention durations.
12. Whether “HarrowSync” is reader-visible or mostly internal shorthand.

Resolved at story-design level: Episode 10's bounded test and consequence, and Episode 14's staging-to-deployment verification gap and response ownership. Their exact multi-vantage and endpoint artifacts remain to be built and validated. AcmeSync in the standalone capstone is the fictional case's existing label; adapting it to HarrowSync must preserve the evidence sequence and keep vendor/product identity distinct from Harrowmere's umbrella system name.

## 28. Readiness

The environment is stable enough at author-architecture level for scene cards. Scene cards may use logical components, owners, schedules, evidence classes, and known observability limits, but should not invent exact technical artifacts marked unresolved.
