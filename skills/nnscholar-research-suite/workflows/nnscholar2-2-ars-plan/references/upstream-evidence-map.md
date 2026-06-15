# Upstream Evidence Map

Use this file when `nnscholar2-2-ars-plan` needs to coordinate with earlier NNScholar skills.

## Purpose

Convert upstream research artifacts into a scheme-ready evidence map. Do not simply quote earlier outputs. Extract decisions, constraints, and unresolved conflicts.

## Source Extraction

| Source | Extract | Use in 2.2 |
|---|---|---|
| `nnscholar1-1-question-mining` | primary question, secondary questions, research gap, novelty rationale, scope boundary, feasibility notes | Aim, scope, success criteria |
| `nnscholar1-2-literature-searching` | key papers, evidence strength, controversy, common designs, endpoint precedents, sample/model references | Route, method choice, endpoint choice, risk audit |
| `nnscholar1-3-hypothesis-generation` | locked hypothesis, mechanism, testable prediction, falsification rule, competing explanations | Aim, analysis targets, sensitivity checks |
| `nnscholar1-4-domain-expert-knowledge-base` | domain terms, clinical/technical constraints, reviewer objections, safety/ethics risks, known limitations | Specification, risk control, quality gates |
| `nnscholar2-1-research-planning` | target output, timeline, work packages, resources, dependencies, bottlenecks | Scheme scope, feasibility, handoff plan |
| Current user message | latest goal, resource constraints, corrections, preferred output | Active intent and final priority |

## Search Heuristics

If the user does not provide files:

1. Search file names for `nnscholar1-1`, `question-mining`, `nnscholar1-2`, `literature`, `nnscholar1-3`, `hypothesis`, `nnscholar1-4`, `knowledge-base`, `research-plan`.
2. Search content for topic keywords, disease names, model names, dataset names, intervention names, and output dates.
3. Prefer files whose topic and date match the current request.
4. If multiple bundles look plausible, present up to 3 candidates and ask for confirmation.

## Conflict Handling

Record conflicts in a small table:

| Conflict | Upstream says | Current user says | Resolution |
|---|---|---|---|

Rules:

- Latest user intent wins unless it contradicts factual evidence.
- Confirm before discarding a locked hypothesis or changing a primary endpoint.
- Mark the scheme as `provisional` when conflicts affect methods, data, or claims.

## Evidence Strength Labels

Use these labels in the output:

- `confirmed`: directly stated by user or locked upstream artifact.
- `supported`: supported by upstream literature or knowledge base.
- `inferred`: reasonable inference from available material.
- `missing`: required but unavailable.
- `conflicting`: upstream and current intent disagree.

## Minimum Evidence for Locking

Do not lock a protocol unless these are at least `confirmed` or `supported`:

- research question or hypothesis;
- target output;
- data/sample/material/corpus availability;
- primary endpoint or evaluation metric;
- main method or study design;
- core variables or measurable constructs;
- major ethical/privacy/licensing constraints.
