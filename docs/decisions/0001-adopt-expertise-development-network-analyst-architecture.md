# ADR-0001: Adopt NADF as an expertise-development architecture centered on the network analyst role

- **Status:** accepted
- **Accepted:** 2026-07-12
- **Date:** 2026-07-11
- **Owners:** NADF Design Studio (proposal); NADF Project Director / Orchestrator (review and disposition)
- **Related evidence:**
  - [NADF Architecture Baseline v0.2 — Proposed](../design-studio/2026-07-11-nadf-architecture-baseline-v0.2-proposed.md)
  - [Architecture Baseline v0.2 — Orchestrator Review](../design-studio/2026-07-11-nadf-architecture-baseline-v0.2-orchestrator-review.md)
  - [R001–R003 Reconciliation and Provenance Recovery](../research/2026-07-11-r001-r003-reconciliation-provenance-recovery.md)
  - [Evidence Index](../research/EVIDENCE_INDEX.md)
- **Related research questions:** R001, R002, and R003 as reconciled in the related research and evidence records

## Context

NADF requires a clear primary architectural identity before later architectural decisions can be evaluated consistently.

The current governed Design Studio baseline proposal, NADF Architecture Baseline v0.2, has been accepted with conditions as the current governed Design Studio proposal. It is not accepted framework architecture. That baseline identifies the first consequential decision candidate as whether NADF should be an expertise-development architecture centered on the network analyst role.

Without an explicit identity decision, NADF could drift among several materially different purposes:

- a protocol syllabus;
- a content catalog;
- a tool-training program;
- a procedural checklist;
- a collection of unrelated learning assets;
- or a broad cybersecurity workforce framework covering multiple roles.

These alternatives are not merely different delivery formats. They imply different answers to what NADF is intended to develop, how success will later be judged, which content belongs within scope, and how future architectural choices should be assessed.

### Research-supported direction

The recovered and reconciled R001–R003 evidence materially supports the following broad direction:

- professional capability is more than factual recall or tool operation;
- expertise depends on organized, structured, causal, and revisable knowledge;
- capable performance includes explanation, investigation, evidence use, judgment, communication, and learning from outcomes;
- novices generally benefit from guidance, scaffolding, feedback, and progressively greater independence;
- authentic and practice-rich work is important to the development of transferable capability;
- tool use is valuable when it serves conceptual understanding and professional performance rather than substituting for them.

The evidence is strongest as cognitive, developmental, and instructional direction. It does not, by itself, determine a complete NADF architecture, competency taxonomy, assessment system, or project-specific structural model.

### Design Studio interpretation

The Design Studio interprets the research-supported direction to mean that NADF should be architected around the development of capable network analysts rather than around the delivery of content or operation of particular tools.

This interpretation is an architectural judgment. Research supports expertise development as a legitimate target, but research does not automatically determine that NADF must adopt this identity, define the network analyst as its primary role, or exclude automatic expansion into a general cybersecurity workforce framework.

### Evidence qualification

R002 contributes useful conceptual support concerning analytical work, evidence use, uncertainty, judgment, communication, and learning. However, R002-dependent high-consequence claims remain qualified pending any future authorized citation, source-quality, and claim-to-source remediation.

This ADR does not depend on:

- adoption of the R002 analytical lifecycle;
- any R002-derived sequence as canonical doctrine;
- validated developmental levels;
- validated assessment instruments;
- or any other claim that requires R002 remediation.

The proposed decision rests on the broader convergent direction recovered across R001–R003 and on Design Studio architectural judgment.

### Decision question

Should NADF define its primary architectural identity as an expertise-development architecture for the network analyst role, rather than primarily as:

- a protocol syllabus;
- a content catalog;
- a tool-training program;
- a procedural checklist;
- or a general workforce framework covering all cybersecurity roles?

## Decision drivers

1. **Clarity of purpose**
   Future NADF decisions require a stable answer to what the framework is intended to develop.

2. **Alignment with the recovered evidence**
   The evidence materially supports integrated capability, structured knowledge, reasoning, practice, feedback, and adaptive performance more strongly than a recall-, content-, or tool-centered conception.

3. **Role focus**
   A defined primary role reduces uncontrolled scope growth and permits later competency, assessment, and learning decisions to be evaluated against a coherent target.

4. **Transferability**
   A capability-centered identity is less dependent on a specific protocol list, vendor, product, interface, or fixed procedure.

5. **Integrated performance**
   Network analysis requires combinations of technical understanding, observation, explanation, investigation, evidence use, judgment, communication, and learning.

6. **Team context without automatic scope expansion**
   Network analysts operate with adjacent roles, but recognizing those interfaces does not require NADF to become a complete workforce framework for every cybersecurity role.

7. **Architectural sequencing**
   Identity and primary scope should be decided before later choices concerning competencies, knowledge representations, assessment, tooling, or curriculum.

8. **Governance traceability**
   A durable identity decision provides a reviewable basis for accepting, rejecting, or constraining later proposals.

9. **Avoidance of content and tool drift**
   Without a clear identity, the framework may become an accumulation of topics, tools, exercises, or artifacts without a coherent developmental purpose.

10. **Reversibility and scope control**
    The decision should be explicit enough to guide future work while avoiding premature decisions about unresolved structural and implementation concerns.

## Options considered

### Option 1 — Expertise-development architecture centered on the network analyst role

NADF would define its primary identity as an architecture for developing network analysts who can integrate technical understanding, structured and revisable mental models, observation, explanation, investigation, evidence use, judgment, communication, and adaptive learning.

Adjacent cybersecurity roles would be treated as interfaces, collaborators, dependencies, or consumers and producers of information where relevant. They would not automatically become additional primary development targets.

#### Benefits

- Provides a coherent purpose for later architectural decisions.
- Aligns with the strongest recovered research direction.
- Supports capability beyond recall, content completion, and tool operation.
- Preserves transferability across technologies and products.
- Creates a focused basis for later competency and assessment work.
- Recognizes team operation without requiring immediate multi-role expansion.
- Allows protocols, tools, procedures, content, scenarios, and artifacts to serve the developmental purpose rather than define it.

#### Risks

- `Expertise development` may remain too abstract unless later decisions define competencies and evidence of performance.
- A role-centered identity can become overly narrow if adjacent-role interfaces are poorly defined.
- Stakeholders may interpret the identity as rejecting foundational content or procedural training, even though both may remain necessary.
- The framework may overclaim expertise if later assessment and validation are inadequate.
- The term `network analyst` still requires later boundary clarification.

#### Downstream effects

- Later proposals should explain how they contribute to development of network-analyst capability.
- Protocols, tools, procedures, and content become means within the architecture rather than the architecture's primary identity.
- Competency, progression, assessment, knowledge-representation, tooling, and curriculum decisions remain necessary.
- Adjacent roles require explicit interface treatment where their work materially affects the network analyst.
- Framework claims must remain bounded by the evidence and validation actually available.

#### Consistency with recovered evidence

**High directional consistency.**

The recovered evidence supports expertise beyond recall and tool operation, structured and revisable mental models, guided development, authentic practice, evidence use, judgment, communication, and model revision.

The evidence does not independently prove that this is the only valid NADF identity. Selecting it remains a Design Studio architectural judgment.

#### Reversibility

**Moderate.**

The identity can be superseded by a later ADR, but it will influence many downstream decisions. Reversal becomes more costly after competency, assessment, curriculum, and artifact systems are built around it.

---

### Option 2 — Content- or syllabus-centered framework

NADF would define itself primarily through an organized body of content, such as network concepts, protocols, systems, technologies, threats, and analysis topics.

#### Benefits

- Easy to understand and communicate.
- Straightforward to organize into courses, modules, or topic sequences.
- Coverage can be audited against a defined content list.
- Foundational knowledge can be planned systematically.
- Familiar to instructors, learners, and program managers.

#### Risks

- Topic coverage can be mistaken for capability.
- Encourages accumulation of content without a coherent performance model.
- May reinforce isolated facts instead of structured and causal understanding.
- Can become obsolete as technologies, protocols, and operational priorities change.
- Provides a weak basis for evaluating reasoning, judgment, transfer, and adaptation.
- May treat completion of content as evidence of competence.

#### Downstream effects

- Architecture would likely be organized around domains, topics, or protocol families.
- Assessment could drift toward recall and content sampling.
- Labs and tools could become appendices to syllabus coverage rather than integrated performance environments.
- Role boundaries may remain implicit.
- Later competency and assessment work would need to compensate for the content-centered identity.

#### Consistency with recovered evidence

**Partial consistency.**

The evidence supports the importance of technical and conceptual knowledge, but it does not support treating content coverage as sufficient for expertise. A content architecture could contribute to NADF, but the recovered evidence does not support making it the primary identity.

#### Reversibility

**Moderate to low after implementation.**

Topic structures are easy to create but can become deeply embedded in courses, indexes, assessment plans, and staffing assumptions.

---

### Option 3 — Tool- and procedure-centered training framework

NADF would define itself primarily through proficiency with selected analysis tools, interfaces, workflows, procedures, and checklists.

#### Benefits

- Produces immediately recognizable operational tasks.
- Can support rapid onboarding to a specific environment.
- Performance can often be observed directly.
- Procedures can improve consistency for routine or regulated work.
- Tool proficiency is necessary for practical network analysis.

#### Risks

- Skills may not transfer across products, environments, or novel conditions.
- Tool operation may be mistaken for understanding or judgment.
- Checklists can become brittle when the situation differs from the expected case.
- Vendor or platform changes can rapidly obsolete the framework.
- Learners may follow procedures without understanding why observations matter.
- Encourages the architecture to mirror current interfaces rather than stable analyst capabilities.

#### Downstream effects

- Tool selection and telemetry assumptions would become foundational architecture prematurely.
- Curriculum and assessments would likely focus on procedural execution.
- Portability would decrease.
- Conceptual understanding, uncertainty, and judgment could become secondary.
- The framework might require frequent restructuring as tools change.

#### Consistency with recovered evidence

**Low as a primary identity; compatible only as a subordinate implementation approach.**

The evidence supports guided tool use, procedural scaffolds, and authentic practice. It does not support defining expertise primarily as tool operation or checklist completion.

#### Reversibility

**Low to moderate.**

Individual tool modules can be replaced, but organizational dependence on product-specific workflows, labs, and assessments can create substantial migration cost.

---

### Option 4 — Broad cybersecurity workforce framework spanning multiple roles

NADF would define itself as a common development architecture for a broad set of cybersecurity roles, potentially including network analysts, threat hunters, incident responders, detection engineers, intelligence analysts, forensic analysts, security engineers, and others.

#### Benefits

- Could create shared concepts and language across a team.
- May reduce duplication among role-development efforts.
- Reflects the interdependent nature of cyber defense.
- Could support cross-training and team coordination.
- May eventually enable a wider family of role-specific pathways.

#### Risks

- Expands scope before the network analyst role is adequately defined.
- Risks producing abstractions too broad to guide meaningful development.
- Increases evidence, architecture, governance, and assessment requirements substantially.
- Blurs ownership of role-specific competencies and artifacts.
- May delay usable progress by attempting to solve the entire workforce architecture at once.
- Could transform NADF into a different project without an explicit scope decision.

#### Downstream effects

- Requires role taxonomies, shared and role-specific competencies, cross-role interfaces, and governance for multiple pathways.
- Increases the complexity of assessment and progression.
- May force early decisions about team cognition, shared knowledge, and organizational structures.
- Expands research and validation needs.
- Changes the meaning of existing network-analyst-focused work.

#### Consistency with recovered evidence

**Undetermined to partial.**

The evidence recognizes team and adjacent-role context, but R001–R003 do not establish a complete multi-role cybersecurity workforce architecture. The current recovered evidence is insufficient to justify automatic expansion of NADF's primary scope.

#### Reversibility

**Low after adoption.**

Multi-role scope would create significant structural, governance, and stakeholder commitments. Returning to a focused network-analyst architecture would be costly and politically difficult.

---

### Option 5 — Defer architectural identity and continue as an uncommitted collection of concerns

NADF would retain its current concerns and artifact categories without selecting a primary identity or development target.

#### Benefits

- Preserves maximum short-term flexibility.
- Avoids premature commitment.
- Allows additional research and experimentation before selecting an identity.
- Minimizes immediate governance work.

#### Risks

- Leaves no stable basis for later decisions.
- Encourages contradictory assumptions across studios and artifacts.
- Allows content, tools, procedures, research interests, and project ideas to compete without a governing purpose.
- Makes scope growth difficult to detect or control.
- Increases the likelihood of rework.
- Prevents clear evaluation of whether future work belongs in NADF.
- Can turn caution into indefinite architectural ambiguity.

#### Downstream effects

- Competency, assessment, knowledge, tooling, artifact, and curriculum work would lack a common target.
- Different contributors could implement incompatible interpretations.
- Repository growth could outpace architectural coherence.
- Later identity decisions would require reconciling more accumulated work.

#### Consistency with recovered evidence

**Inconsistent with the maturity of the current evidence and synthesis.**

The evidence does not determine every architectural choice, but it provides enough directional support for a responsible identity decision. The current Design Studio baseline and Orchestrator review have already isolated this as the first ADR-ready decision.

#### Reversibility

**Superficially high, practically decreasing over time.**

Deferral preserves formal optionality, but ungoverned work creates implicit decisions and sunk costs that become harder to reverse.

## Decision

**Proposed decision: Adopt Option 1.**

If accepted, NADF's primary architectural identity will be:

> **An expertise-development architecture centered on the network analyst role.**

NADF will primarily develop the integrated capability required to perform network analysis in uncertain operational environments.

The broad target outcome includes development of the network analyst's ability to combine:

- technical and conceptual understanding;
- structured, relational, causal, and revisable mental models;
- accurate observation;
- explanation of system and communication behavior;
- investigation of ambiguous conditions;
- appropriate collection, selection, and evaluation of evidence;
- distinction among observation, interpretation, finding, judgment, and recommendation where relevant;
- management and communication of uncertainty and alternative explanations;
- defensible judgment;
- clear communication;
- reflection, feedback use, and adaptive learning.

This list defines broad integrated performance. It is not a competency taxonomy, developmental model, analytical lifecycle, assessment rubric, or curriculum sequence.

NADF will not define its primary identity as:

- a protocol syllabus;
- a content catalog;
- a tool-training program;
- a procedural checklist;
- or a general cybersecurity workforce framework spanning all roles.

Protocols, content, tools, and procedures may be necessary and valuable components of NADF. They will serve the development of network-analyst expertise rather than replace that purpose.

The network analyst will be the primary development target.

Adjacent roles will be treated as interfaces where relevant. NADF may describe:

- information the network analyst receives from adjacent roles;
- information the network analyst provides to adjacent roles;
- shared operational contexts;
- coordination dependencies;
- handoffs;
- and boundaries of responsibility.

Recognizing an adjacent-role interface does not automatically place that role within NADF's primary development scope.

Expansion of NADF to make another role a primary development target will require explicit future governance and must not occur by implication.

### Explicit non-decisions

This ADR does **not** decide:

- the architecture root;
- the knowledge-representation architecture;
- a canonical analytical lifecycle;
- the competency taxonomy;
- developmental levels;
- assessment architecture;
- TOM or COM purpose, structure, authority, or coupling;
- model-driven generation;
- minimum tooling or telemetry;
- curriculum organization or sequencing;
- the exact boundary of every adjacent role;
- the relationship among the historical architecture views;
- or promotion of the Architecture Baseline into accepted framework architecture.

These matters remain governed by the current Architecture Baseline v0.2 conditions and require separate synthesis and, where consequential, separate decisions.

## Consequences

### Positive consequences

1. **NADF gains a stable architectural identity.**
   Later proposals can be evaluated according to whether they contribute to development of network-analyst expertise.

2. **Role scope becomes explicit.**
   The network analyst is the primary development target, reducing uncontrolled expansion into all cybersecurity roles.

3. **Content, tools, and procedures receive a subordinate but legitimate place.**
   They remain important means of development without defining the framework's identity.

4. **Transferability becomes an architectural concern.**
   NADF should favor capabilities that remain useful across changing tools, technologies, and situations.

5. **Integrated performance becomes the broad outcome.**
   Future competency and assessment work must account for more than recall or procedural execution.

6. **Team context is preserved.**
   Adjacent roles can be represented through interfaces without requiring immediate multi-role architecture.

7. **Later decisions receive a governing lens.**
   Competency, assessment, knowledge, tooling, TOM/COM, generation, and curriculum proposals must remain consistent with this identity if the ADR is accepted.

### Negative consequences and risks

1. **The identity remains broad.**
   Additional decisions will be required before the framework can specify competencies, progression, assessment, or implementation.

2. **Expertise claims create a burden of proof.**
   NADF must avoid claiming that it develops or validates expertise beyond the evidence its future assessments and validation can support.

3. **Role boundaries remain incomplete.**
   Treating adjacent roles as interfaces does not itself define where the network analyst role begins and ends.

4. **Potential misunderstanding must be managed.**
   Stakeholders may incorrectly infer that protocols, foundational content, tools, procedures, or checklists are excluded. They are not excluded; they are not the primary architectural identity.

5. **Future proposals may require rejection or revision.**
   Content, tooling, or artifact initiatives that cannot explain their relationship to network-analyst development may fall outside scope.

6. **Reversal cost will grow.**
   As later decisions and implementations align to this identity, replacing it will require a superseding ADR and significant reconciliation.

### Unresolved consequences

The following remain unresolved after this decision:

- the exact definition and boundaries of the network analyst role;
- the authoritative competency model;
- how adjacent-role interfaces will be represented;
- how integrated performance will be assessed;
- what constitutes sufficient evidence of development or mastery;
- whether NADF will use explicit developmental levels;
- which knowledge representations are required;
- whether a common analytical model is needed;
- the minimum implementation environment;
- the relationship of TOM and COM to the network analyst role;
- the architectural relationship among modules, labs, assessments, and reusable assets;
- and the criteria for future framework promotion.

The decision establishes identity and primary target only. It does not resolve these consequences by implication.

### Evidence qualification consequence

R002 may continue to inform later work, but this decision must not be cited as unqualified acceptance of:

- the R002 analytical lifecycle;
- R002-derived doctrinal claims;
- R002-based assessment structures;
- or any R002-dependent high-consequence conclusion awaiting remediation.

The architectural identity adopted here remains supportable without treating those claims as settled.

## Validation plan

Because this ADR concerns architectural identity rather than a specific implementation, validation will occur through governance traceability and coherence review.

While the ADR remains proposed:

1. The Project Director / Orchestrator should verify that the decision text:
   - decides only identity, primary role, broad outcome, and adjacent-role treatment;
   - preserves the R002 qualification;
   - does not imply approval of the Architecture Baseline as framework architecture;
   - and does not absorb any excluded Architecture Baseline decision.

If the ADR is accepted:

2. Future consequential architectural proposals should identify how they:
   - support development of network-analyst expertise;
   - remain within the network-analyst primary scope or explicitly identify an adjacent-role interface;
   - and avoid substituting content completion, tool operation, or procedural compliance for the framework's broad performance target.

3. Periodic architecture review should examine whether the accepted identity:
   - provides useful decision guidance;
   - prevents scope drift;
   - remains coherent with accepted evidence;
   - and permits necessary technical, procedural, and tool-specific learning without allowing those elements to become the architecture's primary purpose.

4. Any future claim that NADF develops or validates expertise should be reviewed against the actual competency, assessment, and validation architecture then in force.

5. Acceptance of this ADR should be traceable from later accepted architectural records and framework documentation without treating the related research as more conclusive than its recorded qualifications permit.

This validation plan does not authorize curriculum, framework, or Engineering changes.

## Revisit triggers

Revisit this decision if any of the following occurs:

1. A future governed proposal would make another cybersecurity role a primary NADF development target.
2. Competency and role-boundary work demonstrates that `network analyst` is too ambiguous, too narrow, or structurally inseparable from a broader role family.
3. Adjacent-role dependencies cannot be represented responsibly as interfaces without expanding the primary architecture.
4. Strong evidence materially challenges the value of an expertise-development identity for NADF.
5. Future assessment and validation work shows that NADF cannot support defensible claims about integrated analyst development.
6. The framework repeatedly functions in practice as a content catalog, tool-training program, or procedure system despite this decision.
7. A proposed architecture root, knowledge architecture, or multi-role model would materially conflict with this identity.
8. The Project Director / Orchestrator authorizes a broader workforce-architecture decision.
9. A later ADR supersedes or deprecates this decision.

Completion of R002 evidence remediation alone does not require revisiting this ADR unless the remediated evidence materially changes the broad identity question.

## Scope confirmation

This ADR contains one proposed architectural decision only:

> Adopt NADF as an expertise-development architecture centered on the network analyst role.

No other Architecture Baseline decision is included.

In particular, this ADR does not decide the architecture root, knowledge representations, analytical lifecycle, competency taxonomy, developmental levels, assessment architecture, TOM, COM, model-driven generation, tooling or telemetry minimums, curriculum sequencing, or any other unresolved Architecture Baseline choice.
