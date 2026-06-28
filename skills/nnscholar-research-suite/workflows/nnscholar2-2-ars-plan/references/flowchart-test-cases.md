# 2.2 Flowchart Test Cases

Use these examples to confirm that `nnscholar2-2-ars-plan` handles
experimental flowcharts as a native part of the ARS protocol.

## Case 1: Empty Protocol Request

User:

```text
Use $nnscholar2-2-ars-plan.
```

Expected behavior:

- Ask only for the research topic/question, available data/materials, and target experimental output.
- Create an ARS protocol with a route and executable flowchart only after the minimum context is clear.

## Case 2: Clinical Study Flow

User:

```text
Based on a 2.2 ARS plan, draw the experimental flowchart for a PD-L1 high-expression lung cancer immunotherapy study and explain how each step is performed.
```

Expected behavior:

- Produce an executable experimental/study flowchart.
- Include patient source, eligibility, cohort grouping, endpoints, statistical analysis, bias control, and expected result pattern.
- Do not draw randomization unless randomization is explicitly part of the design.

## Case 3: AI Benchmark Pipeline

User:

```text
Design a clean flowchart for an LLM agent biomedical literature review benchmark.
```

Expected behavior:

- Include corpus selection, task construction, annotation/gold standard, model/baseline runs, metrics, leakage control, error analysis, and reproducibility package.
- Include expected benchmark result patterns without inventing observed numbers.

## Case 4: Wet-Lab Mechanism Experiment

User:

```text
Create a technical route diagram for a basic experiment testing whether an lncRNA regulates EMT and promotes lung cancer metastasis.
```

Expected behavior:

- Include model system, expression validation, perturbation, migration/invasion assay, EMT marker assay, rescue experiment, expected results, and falsification criteria.
- Label pathway interpretation as hypothesized unless validated.

## Case 5: Mermaid Safety

Given any generated Mermaid, expected behavior:

- Node IDs are ASCII.
- Labels are quoted.
- Subgraphs are balanced.
- Edge references exist.
- Mermaid validator passes or the diagram is simplified until it passes.
