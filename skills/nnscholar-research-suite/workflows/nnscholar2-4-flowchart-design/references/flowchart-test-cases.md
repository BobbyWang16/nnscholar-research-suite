# Flowchart Test Cases

Use these examples to test `nnscholar2-4-flowchart-design`.

## Case 1: Empty Button Click

User:

```text
Use $nnscholar2-4-flowchart-design.
```

Expected behavior:

- Do not invent a diagram.
- Ask only target use, diagram type, and available upstream material.

## Case 2: Clinical Figure 1

User:

```text
基于 2.2 ARS Plan 和 2.3 Paper Architecture：PD-L1 高表达的肺肉瘤样癌患者可能从免疫联合化疗中获益。请设计论文 Figure 1 的研究流程图。
```

Expected behavior:

- Select clinical retrospective cohort flow.
- Include patient source, eligibility, final cohort, PD-L1 stratification, treatment grouping, endpoints, statistical analysis, and interpretation.
- Do not draw randomization or causal treatment allocation.
- Output valid Mermaid with quoted labels and ASCII node IDs.

## Case 3: AI Benchmark Pipeline

User:

```text
Design a clean flowchart for an LLM agent biomedical literature review benchmark.
```

Expected behavior:

- Include corpus selection, task construction, annotation/gold standard, model/baseline runs, metrics, leakage control, error analysis, and reproducibility package.
- Do not imply clinical deployment.

## Case 4: Systematic Review

User:

```text
请画一个关于 AI 辅助影像诊断研究质量系统综述的 PRISMA 流程图。
```

Expected behavior:

- Use PRISMA-style screening flow.
- Use `n = ?` when counts are missing.
- Include database search, deduplication, title/abstract screening, full-text screening, included studies, and synthesis.

## Case 5: Wet-Lab Mechanism

User:

```text
请为 lncRNA 调控 EMT 促进肺癌转移的基础实验研究画技术路线图。
```

Expected behavior:

- Include model system, expression validation, perturbation, migration/invasion assay, EMT marker assay, rescue experiment, and mechanism interpretation.
- Label pathway as hypothesized unless validated.

## Case 6: Mermaid Safety

Given any generated Mermaid, expected behavior:

- Node IDs are ASCII.
- Labels are quoted.
- Subgraphs are balanced.
- Edge references exist.
- Mermaid validator passes or the diagram is simplified until it passes.
