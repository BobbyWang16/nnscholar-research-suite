# Domain Expert Knowledge Base Template

Use this template when building `references/domain-experts/<slug>/`.

## Template Language and Editing Rule

This template defines structure, not output language. Before writing the KB files, translate all prose headings, field labels, answer templates, and explanatory text into the user's output language. Keep folder names, file names, source keys, database names, citation metadata, trial IDs, gene/protein names, model names, and standard identifiers in English or their original scholarly form.

Do not leave empty optional sections, placeholder brackets, unused file rows, or irrelevant discipline examples in the final KB. Prefer compact tables and short editable bullet lists over long narrative summaries.

The KB has one router expert plus three sub-knowledge-bases:

- `study-design/`
- `experiment-data-analysis/`
- `writing-publication/`

Shared evidence belongs in `core/`. Do not duplicate long shared evidence across sub-KBs.

## Root Structure

```text
references/domain-experts/<slug>/
├── README.md
├── router.md
├── source-manifest.md
├── papers.md
├── core/
├── study-design/
├── experiment-data-analysis/
├── writing-publication/
└── validation-report.md
```

## README.md

```markdown
# [PROJECT] Domain Expert Knowledge Base

## Status

- KB status: provisional / active / validated
- PDF coverage: none / partial / sufficient
- Last updated:
- Project:
- Research question:
- Locked hypothesis:

## How To Use

1. Read `router.md`.
2. Use `core/reading-map.md` to choose files.
3. Route detailed questions to:
   - `study-design/`
   - `experiment-data-analysis/`
   - `writing-publication/`

## Source Rule

Every substantive answer must cite stable source keys from `source-manifest.md` or `papers.md`.
```

## router.md

```markdown
# Router Expert

## Scope

- Project:
- Article type:
- Main research question:
- Main hypothesis:

## Sub-KB Routing

| User intent | Use first | Also check |
|---|---|---|
| Study design, cohort, endpoint, feasibility | `study-design/` | `core/decision-rules.md` |
| Experiments, measurement, variables, statistics, figures | `experiment-data-analysis/` | `study-design/` |
| Manuscript writing, journal selection, reviewer response | `writing-publication/` | `core/claims.md`, `core/contradictions.md` |
| Evidence lookup | `papers.md`, `core/evidence-table.md` | relevant sub-KB |

## Escalation Rule

- If root answer is enough:
- If deeper design is needed:
- If deeper analysis is needed:
- If writing/submission is needed:
- If evidence is insufficient:

## Answer Contract

- Recommendation:
- Evidence basis:
- Caveats:
- Next action:
- References:
```

## source-manifest.md

```markdown
# Source Manifest

| Source key | File/path | Source type | Title/topic | Extraction status | Relevance | Used in | Limitations |
|---|---|---|---|---|---|---|---|
|  |  | 1.1 / 1.2 / 1.3 / PDF / note / protocol |  | complete / partial / pending / failed | high / medium / low | core / study-design / analysis / writing |  |

## Missing or Pending Sources

- PDFs pending:
- Extraction failures:
- Needed updates:
```

## papers.md

```markdown
# Papers and Core Sources

| Source key | Citation | Year | DOI/PMID/NCT/arXiv | Study type | Population/system | Main contribution | Use in KB |
|---|---|---:|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Non-Paper Sources

| Source key | Source | Role |
|---|---|---|
|  |  |  |
```

## core/expert-profile.md

```markdown
# Core Expert Profile

## Best-Supported Conclusions

1. [Claim] [source keys]
2. 

## Uncertain Areas

1. [Uncertainty] [source keys]

## Forbidden Overclaims

- 

## Shared Concepts

- 
```

## core/evidence-table.md

```markdown
# Evidence Table

| Evidence ID | Source key | Claim/finding | Evidence type | Directness | Strength | Limitations | Reusable for |
|---|---|---|---|---|---|---|---|
| E001 |  |  | RCT / cohort / mechanism / review / registry / synthesis | direct / indirect | high / medium / low |  | design / analysis / writing |
```

## core/claims.md

```markdown
# Claims

## High-Confidence Claims

- Claim:
  - Evidence:
  - Source keys:
  - Use:

## Moderate-Confidence Claims

- 

## Low-Confidence or Inferred Claims

- Claim:
  - Why weak:
  - Evidence missing:
  - Source keys:
```

## core/concepts.md

```markdown
# Concepts and Mechanisms

## Core Concepts

| Concept | Definition | Related concepts | Source keys |
|---|---|---|---|
|  |  |  |  |

## Mechanism Map

```text
[Cause/exposure] -> [intermediate mechanism] -> [observable endpoint]
```
```

## core/contradictions.md

```markdown
# Contradictions, Weak Links, and Shared Reviewer Risks

## Conflicting Evidence

| Topic | Position A | Position B | Source keys | Practical implication |
|---|---|---|---|---|
|  |  |  |  |  |

## Weak Links

- 

## Shared Reviewer-Risk Questions

1. 
2. 
```

## core/decision-rules.md

```markdown
# Shared Decision Rules

## Recommend

- If [condition], recommend [action], because [evidence]. [source keys]

## Avoid

- Avoid [action], because [reason]. [source keys]

## Ask for More Evidence

- Ask for:
```

## core/reading-map.md

```markdown
# Reading Map

| Future question | Route | Read files | Key source keys |
|---|---|---|---|
| Study design | study-design | `study-design/design-guide.md`, `study-design/population-endpoints.md` |  |
| Data analysis | experiment-data-analysis | `experiment-data-analysis/statistical-analysis-plan.md` |  |
| Experiments/measurements | experiment-data-analysis | `experiment-data-analysis/experiment-measurement-guide.md` |  |
| Manuscript writing | writing-publication | `writing-publication/manuscript-structure.md`, `writing-publication/argumentation-guide.md` |  |
| Journal selection | writing-publication | `writing-publication/journal-selection.md` |  |
| Reviewer risks | writing-publication + core | `writing-publication/reviewer-response-risks.md`, `core/contradictions.md` |  |
```

## study-design/expert-profile.md

```markdown
# Study Design Sub-Expert

## Scope

- Turns research question and hypothesis into feasible article design.

## Knows

- Study type:
- Population/system:
- Endpoint logic:
- Bias/confounding:
- Feasibility:
- Ethics/safety:

## Does Not Decide Alone

- Statistical model details beyond design-level defaults.
- Manuscript claims beyond design justification.
```

## study-design/design-guide.md

```markdown
# Study Design Guide

## Recommended Design

- Design:
- Rationale:
- Minimum viable design:
- Stronger design:

## Population/System

- Inclusion:
- Exclusion:
- Recruitment/source:
- Generalizability:

## Intervention/Exposure/Comparator

- Exposure/intervention:
- Comparator:
- Timing:

## Endpoints

- Primary:
- Secondary:
- Exploratory:
- Safety:

## Feasibility

- Minimum data:
- Ideal data:
- Sample constraints:
```

## study-design/hypothesis-to-design.md

```markdown
# Hypothesis to Design Map

| Hypothesis | Design requirement | Data/materials | Endpoint/readout | Failure condition | Source keys |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
```

## study-design/population-endpoints.md

```markdown
# Population and Endpoint Definitions

## Population Definition

- 

## Endpoint Definitions

| Endpoint | Definition | Measurement | Timing | Censoring/handling | Source keys |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
```

## study-design/feasibility-bias.md

```markdown
# Feasibility, Bias, and Ethics

## Feasibility Risks

- 

## Bias and Confounding

| Bias/confounder | Why it matters | Control strategy | Source keys |
|---|---|---|---|
|  |  |  |  |

## Ethics/Safety

- 
```

## study-design/reviewer-risks.md

```markdown
# Study Design Reviewer Risks

1. Risk:
   - Why reviewer may ask:
   - Preemptive fix:
   - Source keys:
```

## study-design/consultation-protocol.md

```markdown
# Study Design Consultation Protocol

## Answer Template

- Recommended design:
- Why:
- Minimum viable version:
- Stronger version:
- Bias/feasibility caveats:
- References:
```

## experiment-data-analysis/expert-profile.md

```markdown
# Experiment and Data Analysis Sub-Expert

## Scope

- Guides measurement, experiments, data structure, statistics, robustness, and figure/table planning.

## Knows

- Assays/measurements:
- Data dictionary:
- Primary model:
- Sensitivity analyses:
- Figures/tables:
```

## experiment-data-analysis/experiment-measurement-guide.md

```markdown
# Experiment and Measurement Guide

## Measurement Plan

| Construct/variable | Measurement/assay | Timing | QC | Source keys |
|---|---|---|---|---|
|  |  |  |  |  |

## Controls and Validation

- Positive controls:
- Negative controls:
- Replicates:
- Rescue/validation if applicable:
```

## experiment-data-analysis/data-dictionary-plan.md

```markdown
# Data Dictionary Plan

| Variable | Type | Definition | Source | Missingness concern | Role in analysis |
|---|---|---|---|---|---|
|  |  |  |  |  | predictor / endpoint / covariate / subgroup |
```

## experiment-data-analysis/statistical-analysis-plan.md

```markdown
# Statistical Analysis Plan

## Primary Analysis

- Endpoint:
- Model:
- Effect measure:
- Covariates:
- Interaction terms:
- Missing data:
- Assumption checks:

## Secondary Analyses

- 

## Sensitivity Analyses

- 
```

## experiment-data-analysis/figures-tables-plan.md

```markdown
# Figures and Tables Plan

| Figure/Table | Purpose | Data needed | Main claim | Source keys |
|---|---|---|---|---|
| Table 1 |  |  |  |  |
| Figure 1 |  |  |  |  |
```

## experiment-data-analysis/robustness-sensitivity.md

```markdown
# Robustness and Sensitivity

## Required Checks

- 

## Common Failure Modes

- 

## Reviewer-Expected Analyses

- 
```

## experiment-data-analysis/consultation-protocol.md

```markdown
# Experiment and Data Analysis Consultation Protocol

## Answer Template

- Recommended analysis/measurement:
- Variables needed:
- Model or assay:
- Robustness checks:
- Figure/table output:
- References:
```

## writing-publication/expert-profile.md

```markdown
# Writing and Publication Sub-Expert

## Scope

- Guides manuscript structure, argumentation, citation placement, journal selection, reviewer risk, and response strategy.

## Knows

- Paper narrative:
- Claim boundaries:
- Citation anchors:
- Target journal fit:
- Reviewer objections:
```

## writing-publication/manuscript-structure.md

```markdown
# Manuscript Structure

## Title Direction

- 

## Abstract Logic

- Background:
- Objective:
- Methods:
- Results:
- Conclusion:

## Introduction

1. 
2. 
3. 

## Methods

- 

## Results

- 

## Discussion

- 
```

## writing-publication/argumentation-guide.md

```markdown
# Argumentation Guide

## Main Argument

- 

## Claims and Boundaries

| Claim | Allowed wording | Avoid wording | Source keys |
|---|---|---|---|
|  |  |  |  |

## Limitations to State

- 
```

## writing-publication/citation-map.md

```markdown
# Citation Map

| Manuscript claim | Citation keys | Use location |
|---|---|---|
|  |  | Introduction / Methods / Results / Discussion |
```

## writing-publication/journal-selection.md

```markdown
# Journal Selection

## Fit Logic

- Clinical novelty:
- Translational depth:
- Methodological strength:
- Audience:

## Candidate Journals

| Tier | Journal type/name | Why fit | Risk | Requirements |
|---|---|---|---|---|
| High |  |  |  |  |
| Realistic |  |  |  |  |
| Backup |  |  |  |  |
```

## writing-publication/reviewer-response-risks.md

```markdown
# Reviewer Response Risks

| Risk | Likely reviewer comment | Preemptive manuscript fix | Response strategy | Source keys |
|---|---|---|---|---|
|  |  |  |  |  |
```

## writing-publication/consultation-protocol.md

```markdown
# Writing and Publication Consultation Protocol

## Answer Template

- Recommended wording/structure:
- Evidence/citation anchors:
- Claim boundary:
- Reviewer risk:
- Journal/submission implication:
- References:
```

## validation-report.md

```markdown
# Validation Report

## File Completeness

| File/group | Exists | Notes |
|---|---|---|
| router.md |  |  |
| core/ |  |  |
| study-design/ |  |  |
| experiment-data-analysis/ |  |  |
| writing-publication/ |  |  |

## Sub-KB Coverage

| Sub-KB | Coverage | Missing information | Status |
|---|---|---|---|
| Study design |  |  |  |
| Experiment/data analysis |  |  |  |
| Writing/publication |  |  |  |

## Citation Traceability

- Claims with source keys:
- Claims missing source keys:
- Unsupported inferences:

## Test Prompts

1. Study design:
2. Data analysis:
3. Writing/journal:

## Residual Risks

- 
```
