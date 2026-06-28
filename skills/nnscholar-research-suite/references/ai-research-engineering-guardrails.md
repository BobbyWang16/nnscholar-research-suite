# AI Research Engineering Guardrails

Use this internal NNScholar reference for AI/data-science, ML, LLM, agent,
RAG, multimodal, systems, benchmark/evaluation, or model-training projects.
It distills reusable workflow patterns from the AI-Research-SKILLs library into
NNScholar's own research lifecycle.

Keep the active NNScholar workflow as the stage authority. These guardrails add
engineering rigor, experiment provenance, benchmark reproducibility, and
paper-writing safeguards.

## Trigger Map

| Request signal | Apply guardrail |
|---|---|
| iterative AI experiment, model improvement, benchmark optimization | Two-Loop Research Cycle |
| running or planning ML/LLM experiments | Experiment Protocol and Trajectory Gate |
| model training, fine-tuning, post-training, RAG, inference, interpretability | Skill Routing and Environment Gate |
| LLM/code model benchmarking, benchmark table, leaderboard claim | Evaluation Harness Gate |
| paper from repo/results/logs | Repo-to-Paper Evidence Gate |
| citation, bibliography, related work, venue template | Citation and Venue Gate |
| long-running project or multi-session research | ARA Provenance Gate |
| final research package, release, or paper claim audit | Rigor Review Gate |

## Two-Loop Research Cycle

Use in 2.1, 2.2, 4.3, and long-running AI projects.

1. Bootstrap once:
   - scope the research question;
   - search literature and save source notes;
   - form testable hypotheses;
   - define baseline, proxy metric, and success/falsification criteria.
2. Inner loop:
   - pick one hypothesis;
   - write a protocol before running;
   - run the smallest credible experiment;
   - sanity-check training/evaluation;
   - record metrics, logs, configs, code version, and outcome;
   - label the result as confirmatory if it matches a locked protocol, otherwise
     exploratory.
3. Outer loop:
   - synthesize 5-10 experiments or any surprising result;
   - update the project narrative;
   - decide to deepen, broaden, pivot, or conclude;
   - return to literature or ideation when stuck.
4. Conclude only when `findings.md` or the NNScholar equivalent can support a
   paper abstract: problem, method, evidence, and contribution are clear.

## Experiment Protocol and Trajectory Gate

Use in 2.2 before protocol lock and in 4.3 before drafting Results.

Every AI experiment should record:

- hypothesis ID and statement;
- prediction and falsification condition;
- dataset/task/split;
- model/checkpoint/tokenizer;
- baseline and comparator;
- metric, direction, and statistical uncertainty plan;
- seed, hardware, precision, software versions, and config file;
- training/evaluation command;
- expected run time and compute budget;
- artifact paths for logs, checkpoints, predictions, and result JSON/CSV.

For training or fine-tuning, require:

- data inspection before training;
- trivial end-to-end run;
- overfit-one-batch check when debugging;
- baseline reproduction before claiming improvement;
- NaN/Inf/loss-spike checks;
- gradient norm or comparable health metric when available;
- run table with commit/config, metric, delta, wall time, and keep/discard status.

Do not accept a leaderboard or benchmark claim from a single unlogged run.

## Skill Routing and Environment Gate

Use in 2.2 when selecting an AI engineering route. Route details can be supplied
by co-installed specialist skills, but NNScholar must preserve the design
contract.

| Activity | Required NNScholar questions |
|---|---|
| data preparation | What raw data, filters, deduplication, leakage checks, and licenses apply? |
| fine-tuning/post-training | Which base model, method, data format, reward/preference signal, and eval gate? |
| distributed training | What parallelism, checkpointing, failure recovery, and cost limit? |
| inference/serving | What latency, throughput, memory, batching, and quantization constraints? |
| RAG/agents | What corpus, retrieval eval, tool safety, failure modes, and trace logs? |
| interpretability | What intervention, activation/feature evidence, and causal claim boundary? |
| MLOps/observability | Where are configs, metrics, artifacts, dashboards, and model versions recorded? |

If the exact framework is unknown, produce a provisional route and list the
specialist skill to consult, but do not invent commands or benchmark numbers.

## Evaluation Harness Gate

Use for LLM, code model, multimodal, RAG, agent, or benchmark papers.

1. Define the benchmark suite before model selection:
   - LLM: MMLU, GSM8K, HellaSwag, TruthfulQA, ARC, HumanEval, or task-specific.
   - Code: HumanEval, MBPP, HumanEval+, MBPP+, MultiPL-E, SWE-bench or related.
   - RAG/agent: retrieval recall, answer correctness, tool success, latency, and
     failure taxonomy.
2. Record for every benchmark:
   - task version;
   - prompt/template;
   - few-shot count;
   - decoding parameters;
   - code-execution or judge setting;
   - number of samples;
   - metric definition;
   - stderr/CI or run-to-run variance;
   - contamination or leakage precautions.
3. For pass@k or sampled decoding, require `n_samples`, temperature, and random
   seed policy.
4. For claimed improvements, require a matched baseline under the same harness
   and settings.
5. Save raw predictions or sample logs when the benchmark permits it.

If evaluation settings differ from a cited paper or leaderboard, label the
comparison as non-identical.

## Repo-to-Paper Evidence Gate

Use in 4.3 when drafting from a codebase, result folder, or experiment repo.

Before writing, inventory:

- README, docs, notes, and prior drafts;
- configs and environment files;
- experiments/results/logs/checkpoints;
- scripts that generated each figure/table;
- existing BibTeX or citation mentions;
- issues, TODOs, known failures, and discarded experiments.

Draft only claims grounded in located artifacts. Use placeholders such as
`[RESULT CHECK]`, `[CITATION NEEDED]`, or `[AUTHOR CHECK]` when the repo lacks
evidence. Do not convert planned or expected results into observed results.

## Citation and Venue Gate

Use in 1.2, 2.3, 4.3, 5.1, and 5.2.

1. Never create BibTeX or formal citations from memory.
2. Verify citations through stable sources: DOI/CrossRef, arXiv, Semantic
   Scholar, DBLP, PubMed, official venue pages, or publisher pages.
3. If a citation cannot be verified, mark it explicitly as a placeholder.
4. For AI/ML conference submissions, check current official venue rules before
   final claims about:
   - page limit;
   - anonymity/double-blind policy;
   - checklist;
   - limitations/ethics/broader impact/LLM disclosure;
   - appendix and supplementary rules;
   - code/data availability or artifact checklist.
5. For LaTeX templates, copy the entire template directory, compile before
   editing, and do not modify style files unless the venue permits it.

## ARA Provenance Gate

Use when the user wants a reusable, auditable research artifact or when an AI
project spans multiple sessions.

Maintain a lightweight research artifact with:

- problem, gaps, assumptions, and key concepts;
- falsifiable claims with proof pointers;
- experiment plans and evidence files;
- solution architecture, algorithms, constraints, and heuristics;
- related-work dependency graph;
- exploration tree with decisions, experiments, dead ends, and pivots;
- session records with provenance tags.

Use provenance tags:

- `user`: explicitly stated or confirmed by the user;
- `ai-suggested`: inferred or suggested by the agent;
- `ai-executed`: action performed by the agent;
- `user-revised`: user corrected an AI suggestion.

Do not upgrade `ai-suggested` to `user` without explicit confirmation.

## Rigor Review Gate

Use in 4.3, 5.2, and before a paper/release claims readiness.

Score or audit six dimensions:

1. Evidence relevance: does evidence substantively support each claim?
2. Falsifiability: are failure criteria actionable and non-trivial?
3. Scope calibration: do claims match the evidence boundary?
4. Argument coherence: do problem, insight, solution, claims, and evidence align?
5. Exploration integrity: are failed paths, alternatives, and pivots honestly
   documented?
6. Methodological rigor: are baselines, ablations, variance, metrics, and
   reproducibility details adequate?

Severity:

- CRITICAL: claim cannot stand or key evidence is missing.
- MAJOR: claim is weakened or method is incomplete.
- MINOR: fixable reporting or polish issue.
- SUGGESTION: improvement opportunity.

## NNScholar Handoff Addendum

When these guardrails affect output, add:

```text
AI research engineering guardrails used:
Two-loop status:
Protocol/evaluation artifacts required:
Benchmark settings locked:
Provenance or ARA records needed:
Rigor review blockers:
Items needing author verification:
```
