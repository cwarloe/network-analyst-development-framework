# NADF Active Training Architecture Baseline

## Status & Overview

- **Artifact:** NADF Training Architecture Baseline
- **Status:** Active governing baseline
- **Scope:** Authoritative architecture for Network Analyst Development Framework training, curriculum, and practical exercise development

This is NADF's single active governing training architecture baseline. Existing [research](docs/research/), [ADRs](docs/decisions/), and [Design Studio artifacts](docs/design-studio/) remain available as historical records and supporting context.

## 1. Purpose & Identity

The Network Analyst Development Framework (NADF) is an expertise-development architecture designed for the network analyst role. Its purpose is to build technical understanding, structured mental models, analytical reasoning, evidence use, judgment, communication, and adaptive learning required to perform network analysis in operational environments.

NADF targets integrated performance, developing analysts who can:

- Observe network activity accurately.
- Explain system and communication behavior.
- Connect observations to structural and causal models.
- Investigate ambiguous conditions and evaluate evidence.
- Distinguish observation from interpretation and judgment.
- Manage uncertainty and alternative explanations.
- Communicate defensible assessments.
- Learn from outcomes and revise mental models.

## 2. Core Architectural Principles

1. **Reality and Context Matter:** Technical knowledge connects protocols and tools to real system purposes, behaviors, constraints, and operational context.
2. **Mental Models Must Be Structured and Revisable:** Learners build relational, causal, and testable mental models that support explanation, prediction, and troubleshooting.
3. **Analytical Reasoning Is Cross-Cutting:** Analytical skills are developed across technical subject areas rather than isolated in standalone method lessons.
4. **Expected Behavior Before Anomaly Interpretation:** Learners develop contextual understanding of expected system behavior to properly reason about deviations.
5. **Guidance Precedes Independence:** Novices receive structured support, worked examples, and scaffolding, which progressively reduce as capability develops.
6. **Tools Serve Analyst Performance:** Tools are necessary implementation environments but do not define the framework's architectural identity.
7. **Assessment Measures Integrated Performance:** Assessment gathers evidence of integrated performance through designed evidence of reasoning, explanation, troubleshooting, and task execution.

## 3. Core Architectural Concerns

NADF organizes training and curriculum design around six core concerns:

### 3.1 Concern A — Operational and Domain Reality

Connects protocols, systems, and behaviors to operational purpose, communication intent, expected patterns, and potential failure or adversary modes.

### 3.2 Concern B — Knowledge and Representation

Supports coherent, traceable representations of systems, protocols, causal dependencies, observables, and evidence relationships across training materials.

### 3.3 Concern C — Analyst Cognition & Reasoning

Teaches analysts how to notice relevant signals, build mental models, generate hypotheses, evaluate evidence, and communicate assessments under uncertainty.

### 3.4 Concern D — Development and Learning

Provides framework-level guidance for scaffolding, deliberate practice, feedback, worked examples, and scenario-based learning.

### 3.5 Concern E — Assessment & Evidence of Competence

Gathers observable evidence of integrated performance through troubleshooting tasks, explanations, predictions, and practical exercise outputs.

### 3.6 Concern F — Supporting Artifacts & Exercises

Enables flexible development of modules, PCAP walkthroughs, telemetry labs, scenarios, instructor guides, and capstones without forcing rigid one-to-one coupling.

## 4. Provisional Analytical Functions

NADF structures analytical problem-solving around seven recurring functions:

1. Problem framing
2. Candidate explanation or hypothesis generation
3. Evidence planning
4. Evidence collection and preservation
5. Evidence evaluation and sensemaking
6. Judgment, action, and communication
7. Learning and model revision

These functions operate dynamically and adaptively depending on task complexity and operational conditions.

## 5. Core Principles & Guidelines for Curriculum Authoring

- **Focus on Practical Skill Transfer:** Design modules and exercises that build hands-on troubleshooting and analytical confidence.
- **Scaffold Novice Learning:** Pair initial technical concepts with guided demonstrations before requiring independent execution.
- **Integrate Authentic PCAPs & Telemetry:** Ensure exercises reflect authentic network behaviors, protocol interactions, and operational edge cases.

The Curriculum Studio's current development priority is **C001 – Foundations of Network Analysis**.
