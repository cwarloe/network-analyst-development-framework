# Research Protocol

## Purpose

This protocol makes framework claims traceable and reviewable. It is intended for applied engineering research, not as a substitute for a formal systematic review where one is required.

## Workflow

### 1. Frame the question

Use `templates/research-question.md`. Define scope, decision relevance, inclusion and exclusion criteria, and what would change the current view.

### 2. Search reproducibly

Record databases, repositories, search terms, filters, and search dates. Preserve stable identifiers such as DOI, RFC number, standard number, or release version.

### 3. Assess sources

Evaluate authority, methodology, recency, directness, reproducibility, and conflicts of interest. A high-quality source can still be indirect or inapplicable; record both quality and relevance.

### 4. Extract evidence

Create an evidence record using `templates/evidence-record.md` and add it to `EVIDENCE_INDEX.md`. Paraphrase by default. Clearly mark short quotations and page or section locations.

### 5. Synthesize

Group evidence by claim, include conflicting findings, state confidence, and identify gaps. Do not count sources as votes; weight them by quality and applicability.

### 6. Decide and maintain

Link syntheses to ADRs and framework documents. Revisit claims when sources are superseded, retracted, or invalidated by implementation evidence.

## Confidence scale

- **High:** consistent, directly applicable evidence from multiple strong sources or reproducible primary evidence.
- **Moderate:** credible evidence with meaningful limitations, indirectness, or some disagreement.
- **Low:** sparse, indirect, preliminary, or substantially conflicting evidence.
- **Unknown:** insufficient assessment.

Confidence describes the evidence for a claim, not certainty that a proposed design will succeed.
