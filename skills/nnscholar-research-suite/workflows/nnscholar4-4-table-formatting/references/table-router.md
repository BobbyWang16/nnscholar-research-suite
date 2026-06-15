# Table Router

Use this file to choose the manuscript table type and formatting expectations.

## Universal Questions

1. What is the table's role: describe sample, report primary results, compare methods, summarize literature, define variables, or support robustness?
2. Are rows observations, groups, variables, models, datasets, materials, papers, sources, or conditions?
3. Are columns groups, metrics, model specifications, time points, outcomes, or annotations?
4. What must appear in table notes: abbreviations, tests, models, missing data, units, scale ranges, or data source?

## Common Table Types

| Table type | Typical rows | Typical columns | Required notes |
|---|---|---|---|
| Baseline characteristics | Variables | Total and groups | n, summary format, tests, missingness, abbreviations |
| Primary results | Outcomes/endpoints | Groups/time/model | effect size, CI, p value, adjustment, time window |
| Regression/model | Predictors/specifications | Models or coefficients | SE/CI, fixed effects, clustering, covariates |
| AI benchmark | Methods | Datasets/metrics | metric direction, split, seeds/folds, baseline |
| Ablation | Components/settings | Metrics | full model, delta, repeated runs |
| Materials property | Samples/materials | Composition/properties/performance | units, test condition, batch/repetition |
| Biomedical assay | Treatment/condition | Readouts/time/dose | n, normalization, control, test |
| Literature comparison | Papers/studies | Design/method/results | search scope, inclusion logic |
| Variable definition | Variables | Definition/type/source | coding, units, missingness |
| Corpus/source table | Sources/corpora | period/genre/counts/coding | selection rule, normalization |

## Style Defaults

- Use three-line table for Chinese academic writing and many biomedical/social-science drafts.
- Put table title above the table.
- Put notes below the table.
- Define abbreviations in notes, not in long column headers.
- Prefer concise headers and explanatory notes.
- Use consistent decimals; avoid false precision.
- Keep p values as exact values where possible, with thresholds only when appropriate.

