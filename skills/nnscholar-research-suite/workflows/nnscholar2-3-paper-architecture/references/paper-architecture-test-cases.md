# Paper Architecture Test Cases

Use these examples to test `nnscholar2-3-paper-architecture`.

## Case 1: Empty Button Click

User:

```text
Use $nnscholar2-3-paper-architecture.
```

Expected behavior:

- Do not invent a paper structure.
- Ask only the 3 intake questions: article type/output, question/discipline, and available protocol/material.

## Case 2: Clinical Protocol-Linked Paper

User:

```text
基于 2.2 ARS Plan：PD-L1 高表达的肺肉瘤样癌患者可能从免疫联合化疗中获益。请设计论文架构。
```

Expected behavior:

- Select clinical original article / retrospective cohort architecture.
- Use cautious association language.
- Include Introduction gap around pulmonary sarcomatoid carcinoma, immunotherapy, PD-L1, and real-world evidence.
- Include Table 1, cohort flow, survival/response figure, adjusted model table, subgroup/sensitivity supplement.
- Do not change endpoints or analysis beyond 2.2 protocol.

## Case 3: Computational Benchmark

User:

```text
We have an ARS plan for evaluating LLM agents on biomedical literature review tasks. Build the paper architecture.
```

Expected behavior:

- Select computational/AI benchmark architecture.
- Include dataset/task statistics, benchmark pipeline, baseline comparison, ablation/robustness, error analysis, reproducibility appendix.
- Include claim boundaries around dataset scope, benchmark leakage, model version drift, and evaluator reliability.

## Case 4: Wet-Lab Mechanism Study

User:

```text
我们有一个基础实验方案：某 lncRNA 可能通过调控 EMT 促进肺癌转移。请设计论文架构。
```

Expected behavior:

- Select basic/translational wet-lab architecture.
- Figure order should move from expression/phenotype validation to perturbation, rescue, and mechanism.
- Avoid clinical efficacy claims unless clinical validation exists.

## Case 5: Qualitative / Social Science

User:

```text
I interviewed 35 medical students about AI-assisted learning. Help me build a manuscript architecture.
```

Expected behavior:

- Select qualitative or mixed-methods architecture.
- Include participant/context table, coding/themes table, conceptual model, reflexivity/ethics.
- Avoid overgeneralization beyond sample and setting.

## Case 6: Systematic Review

User:

```text
请基于系统综述方案，设计一篇关于 AI 辅助影像诊断研究质量的论文架构。
```

Expected behavior:

- Select systematic/scoping review architecture.
- Include PRISMA flow, included study characteristics, evidence map/quality assessment, synthesis structure.
- Claim boundaries must track evidence certainty and heterogeneity.

## Case 7: Protocol Missing

User:

```text
我只有一个想法：糖尿病可能影响 CCTA 斑块进展。请直接设计完整 Results 和图表。
```

Expected behavior:

- Classify as `scratch`.
- Produce provisional architecture only.
- Refuse to invent Results details.
- Return to `nnscholar2-2-ars-plan` for protocol/data lock before full Methods/Results architecture.
