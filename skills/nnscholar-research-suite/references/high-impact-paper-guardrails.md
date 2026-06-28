# NNScholar High-Impact Paper Guardrails

Use this reference when the target is Nature/CNS, Nature-family, Cell/Science-family, or any high-impact multidisciplinary venue. These rules are native NNScholar rules distilled from external Nature-style skill patterns; do not call an external nature skill unless the user explicitly asks.

## Paper-Type Taxonomy

Classify the manuscript before planning, writing, polishing, or reviewing:

| Type | Central reader question | NNScholar consequence |
|---|---|---|
| `research` | What was found and why does it matter? | Build a finding-to-meaning evidence ladder. |
| `methods` | Does the method work, improve on alternatives, and reproduce? | Emphasize validation, comparison, reproducibility, and failure modes. |
| `hypothesis` | Is the proposed mechanism or causal explanation supported? | Separate direct evidence from speculation and require alternative explanations. |
| `algorithmic` | Does the model/system perform under fair comparison? | Require baselines, splits, seeds/variance, ablations, and error analysis. |
| `review` | What is known, contested, and open? | Organize by argument, not paper-by-paper summary. |

## Terminology Ledger

Before drafting, polishing, making captions, or building submission packages, create or update a compact terminology ledger:

```text
Canonical term:
First-use definition:
Variants seen:
Decision:
Affected sections/figures/tables:
```

Lock one name for each method, model, dataset, cohort, metric, gene/protein, material, assay, or concept. Do not introduce synonyms for variety. If a term is missing or ambiguous, add an author query instead of coining a new term.

## Article Architecture

High-impact papers need a visible argument chain:

```text
field-scale need -> unresolved bottleneck -> proposed move -> decisive evidence -> broader implication -> boundary
```

If any link is missing, mark the architecture provisional. Do not compensate with stronger prose.

For Results, use an evidence ladder:

1. system, workflow, cohort, material, or design overview;
2. validation that the platform/assay/model is credible;
3. primary discovery or performance result;
4. fair comparison with baseline or prior practice;
5. mechanism, interpretation, error analysis, or subgroup/robustness;
6. scale-up, application, generalization, or stress test.

## Abstract, Introduction, and Discussion Checks

- Abstract: state problem, gap, contribution, strongest supported result, and bounded implication. Prefer concrete numbers or comparisons when available.
- Introduction: avoid citation lists; narrow from field stake to bottleneck to exact gap to the present response.
- Discussion: widen from central finding to meaning, relation to prior work, limitations, and future work. Do not restate every figure.
- Title: make it specific and searchable. Avoid unsupported `first`, `novel`, `powerful`, `best`, or vague prestige words.

## Figure Contract

Before plotting or assembling a figure, lock:

```text
Core conclusion:
Figure archetype:
Target journal/output:
Final size:
Panel map:
Evidence hierarchy:
Statistics needed:
Source data needed:
Image-integrity notes:
Reviewer risk:
```

Each panel must answer a unique scientific question. If removing a panel would not weaken the argument, remove or merge it. Separate hero evidence from validation, controls, robustness, and limitations.

Use these archetypes:

- `quantitative grid`: numerical comparisons and metrics.
- `schematic-led composite`: workflow, mechanism, method, model architecture.
- `image plate + quant`: microscopy, imaging, histology, segmentation, blots/gels.
- `asymmetric mixed-modality`: schematic, raster images, heatmaps, and quantitative plots.

## Figure and Table Legend Rules

- Use caption titles as concise noun phrases: `Fig. N | ...` or `Table N | ...`.
- Make legends self-contained: include panel mapping, color/shape meanings, `n`, error type, test/correction, units, and key identifiers when relevant.
- Use present tense for visual facts and past tense for what was experimentally done.
- A legend may include one claim-closing sentence only when the panel directly supports it.
- For adapted or reused panels, require permission/source attribution. Do not recreate copyrighted figures.

## Display and Export Checks

- Prefer vector output for line art: SVG/PDF with editable text.
- Keep in-figure fonts consistent and readable at final size.
- Avoid rainbow maps and color-only encoding; preserve grayscale/colorblind readability.
- For image panels, record crop, contrast, pseudo-color, scale calibration, stitching, reuse, raw-file path, and quantification link.
- For model figures, record train/validation/test split, seeds/folds, metric definition, CI/variance, and baseline definition.

## Data, Code, and FAIR Availability

For original research, finalization must inventory every dataset supporting central conclusions:

| Dataset family | Access route | Identifier/status | Supports | Risk |
|---|---|---|---|---|

Access routes:

- public repository with DOI/accession;
- controlled repository with access procedure;
- supplementary/source data;
- reused public data with source/version/date accessed;
- third-party restricted data with owner/request route;
- request-based access with specific reason and responsible institution;
- not applicable only when no datasets were generated or analysed.

Block final approval if central data have no durable access route, sensitive-data restrictions lack a procedure, repository records lack README/metadata/licence, or manuscript statements do not match files.

## Citation and Source Discipline

- Cite the source actually read and verified.
- Use primary sources for their own data, methods, claims, and conclusions.
- Segment long passages into citable claims before searching.
- Verify DOI/PMID/arXiv/URL or official pages for formal citation work.
- Deduplicate by DOI first; if DOI is missing, compare title plus first author.
- Use source tiers: structured APIs and official sources first, limited APIs second, unstable scraped/manual sources only with a warning.

## Reviewer-Style Pre-Submission Audit

Before high-impact submission, simulate three reviewer emphases without inventing reviewer identities:

1. technical soundness and missing controls;
2. originality and scientific significance;
3. interdisciplinary readership and nonspecialist readability.

Always produce:

```text
Shared manuscript claim summary:
Visible evidence base:
Missing materials affecting confidence:
Consensus strengths:
Consensus technical risks:
Broad-interest / significance readout:
Unsupported or not-assessable claims:
```

Do not state an editorial decision or guarantee venue fit.

## Reviewer Response Discipline

For revisions, classify every editor/reviewer item:

| Severity | Meaning |
|---|---|
| `minor` | wording, formatting, citation, small detail |
| `major` | evidence, method, statistics, validation, interpretation |
| `blocking` | ethics, compliance, data integrity, central unsupported claim |
| `unclear` | cannot judge without author facts |

Use action labels:

`ACCEPT_TEXT`, `ACCEPT_ANALYSIS`, `ACCEPT_EXPERIMENT`, `ACCEPT_FIGURE`, `CLARIFY_EXISTING`, `ADD_CITATION`, `SOFTEN_CLAIM`, `PARTIAL`, `DISAGREE`, `OUT_OF_SCOPE`, `AUTHOR_INPUT_NEEDED`, `BLOCKING`.

Every response needs a comment ID, action, manuscript location or placeholder, evidence/source, readiness state, and unresolved risk. Never invent experiments, line numbers, figure panels, citations, p values, accessions, or manuscript changes.

## Cover Letter Triage

For high-impact journals, avoid generic praise. State:

1. what the finding is;
2. what makes it new;
3. why it matters beyond one narrow specialty;
4. what the evidence boundary is.

Do not invent exclusivity, prior communication, ethics approval, data availability, funding, or conflicts.
