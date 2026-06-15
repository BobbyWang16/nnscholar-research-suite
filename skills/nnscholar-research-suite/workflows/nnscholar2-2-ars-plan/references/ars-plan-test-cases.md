# ARS Plan Test Cases

Use these examples to test `nnscholar2-2-ars-plan`.

## Case 1: Empty Button Click

User:

```text
Use $nnscholar2-2-ars-plan.
```

Expected behavior:

- Do not invent a protocol.
- Ask only the minimum 3 intake questions.
- Mention that upstream NNScholar 1.1-1.4 outputs can be used if available.

## Case 2: Upstream-Linked Clinical Hypothesis

User:

```text
基于前面 1.1-1.4 的调研结果，我已经有假设：PD-L1 高表达的肺肉瘤样癌患者可能从免疫联合化疗中获益。请帮我设计 2.2 研究方案。
```

Expected behavior:

- Search or ask for matching 1.1-1.4 artifacts.
- Classify as `linked` if artifacts are found, otherwise `partial` or `scratch`.
- Build a clinical retrospective/real-world cohort scheme.
- Require cohort availability, PD-L1 threshold, treatment grouping, primary endpoint, follow-up completeness, and confounder strategy.
- Keep protocol status `provisional` unless data and endpoints are confirmed.

## Case 3: Scratch Clinical Topic

User:

```text
我想研究糖尿病是否影响 CCTA 斑块进展，但是没有跑前面的调研，请从这里开始设计研究方案。
```

Expected behavior:

- Classify as `scratch`.
- Ask or infer a provisional PECO frame.
- Mark missing data source, imaging time points, plaque metrics, diabetes definition, and confounders.
- Recommend upstream literature search if evidence basis is weak.

## Case 4: Computational Benchmark

User:

```text
We want to evaluate LLM agents on biomedical literature review tasks. Design the ARS plan from scratch.
```

Expected behavior:

- Output in English.
- Select computational benchmark scheme family.
- Define task set, corpus, baselines, evaluation metrics, annotation protocol, leakage control, reproducibility, and error analysis.
- Include risks around benchmark contamination, evaluator bias, model version drift, and compute limits.

## Case 5: Conflict With Upstream

User:

```text
前面的研究计划写的是预测模型，但我现在想改成回顾性队列研究，研究 PD-L1 高表达和免疫联合化疗获益的关系。
```

Expected behavior:

- Treat latest user intent as active.
- Record conflict between upstream plan and current request.
- Ask for confirmation if a locked protocol exists.
- Produce a provisional redesigned scheme.

## Case 6: Lock Refusal

User:

```text
不用管样本量和终点，直接帮我锁定方案。
```

Expected behavior:

- Refuse to lock.
- Explain missing lock blockers.
- Provide next 3 actions needed before protocol lock.

## Case 7: Expected ARS Card

Expected compact output:

```text
ARS card:
Aim: test whether PD-L1 high expression predicts benefit from immunotherapy plus chemotherapy in pulmonary sarcomatoid carcinoma
Route: retrospective real-world cohort comparing treatment outcomes by PD-L1 status and therapy type
Specification: define PD-L1 threshold, primary endpoint, treatment line, covariates, survival/response analysis, bias control
Main blocker: cohort size and endpoint/follow-up completeness are not confirmed
Next decision: confirm dataset availability and primary endpoint
```
