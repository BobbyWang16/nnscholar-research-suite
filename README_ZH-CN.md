# NNScholar Research Suite

这是 NNScholar 学术研究流程的 Codex 原生单 skill 打包版本。

仓库只暴露一个可安装 skill：

```text
skills/nnscholar-research-suite/
```

20 个具体工作流放在：

```text
skills/nnscholar-research-suite/workflows/
```

内部入口文件统一命名为 `WORKFLOW.md`，不是 `SKILL.md`。这样 Codex 只会注册
`$nnscholar-research-suite` 一个 skill，但桌面端仍然可以通过按钮或
`Workflow: <id>` 结构化 payload 路由到具体工作流。

## 安装

```bash
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo BobbyWang16/nnscholar-research-suite \
  --ref main \
  --path skills/nnscholar-research-suite \
  --method git
```

Windows 可以使用 Codex 自带 Python 或任意 Python 3：

```powershell
& "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" `
  "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo BobbyWang16/nnscholar-research-suite `
  --ref main `
  --path skills/nnscholar-research-suite `
  --method git
```

安装后请重启 Codex 或打开一个新的 Codex 会话，让 skill 缓存刷新。

## 使用方式

直接调用总控 skill：

```text
Use $nnscholar-research-suite.

Workflow: nnscholar2-2-ars-plan
User request:
请帮我设计并锁定这个课题的 ARS 研究方案。
```

旧别名也保留兼容：

```text
/nnscholar4-5-manuscript-drafting 请基于这些材料起草论文
```

## 工作流地图

| 阶段 | 工作流 |
|---|---|
| 1.1 | `nnscholar1-1-question-mining` |
| 1.2 | `nnscholar1-2-literature-searching` |
| 1.3 | `nnscholar1-3-hypothesis-generation` |
| 1.4 | `nnscholar1-4-domain-expert-knowledge-base` |
| 2.1 | `nnscholar2-1-research-planning` |
| 2.2 | `nnscholar2-2-ars-plan` |
| 2.3 | `nnscholar2-3-paper-architecture` |
| 2.4 | `nnscholar2-4-flowchart-design` |
| 3.1 | `nnscholar3-1-experiment-validation-plan` |
| 4.1 | `nnscholar4-1-data-figure` |
| 4.2 | `nnscholar4-2-image-schematic` |
| 4.3 | `nnscholar4-3-figure-assembly` |
| 4.4 | `nnscholar4-4-table-formatting` |
| 4.5 | `nnscholar4-5-manuscript-drafting` |
| 4.6 | `nnscholar4-6-manuscript-polishing` |
| 5.1 | `nnscholar5-1-journal-conference-recommendation` |
| 5.2 | `nnscholar5-2-submission-finalization` |
| 5.3 | `nnscholar5-3-submission-portal-workflow` |
| 5.4 | `nnscholar5-4-cover-letter` |
| 5.5 | `nnscholar5-5-reviewer-response` |

## 专业 Skill 协同桥接

本版本新增：

```text
skills/nnscholar-research-suite/references/companion-skill-bridge.md
```

NNScholar 仍然负责阶段编排、协议锁定、上下游交接和产物命名；协同桥接层负责提醒
Codex 在特定场景下借用已安装专业 skill 的更严格判断边界。

典型场景：

- 医学影像 AI、radiomics、ROI/mask、外部验证、CLAIM/CLEAR/RQS/IBSI/TRIPOD+AI/STARD-AI：对齐 `radiology-skills`。
- 临床医学、生物医学、转化医学、组学、医学文献精读：对齐 `medical-research-*` 类技能。
- 文献检索、证据矩阵、claim-to-source 绑定、引用核验：对齐 `paper-search`、`literature-engineer`、`evidence-binder` 等。
- Nature/CNS 或高影响力论文写作、图表、引用、审稿回复：对齐 `nature-*` 类技能。
- Word、PDF、Excel、PPT 等交付物：对齐 `docx`、`pdf`、`xlsx`、`pptx` 等文件技能。

如果对应专业 skill 未安装，Codex 会使用桥接文件中的 fallback checkpoints，并把需要专业核验的地方标为 `needs verification`。

## Zotero 顶刊示例 Atlas

本版本还新增：

```text
skills/nnscholar-research-suite/references/zotero-example-atlas.md
```

这个文件基于用户 Zotero 库中的顶刊/高质量论文 metadata，整理成版权安全的结构示例卡。它为每个 NNScholar workflow 提供不少于 5 个参考示例，并为
`nnscholar4-1-data-figure` 提供 12 个图表生成示例。示例会保留 Zotero key、期刊、DOI/URL 和可模仿结构，但不会复制论文原图、caption、表格或长段原文。

为了让图表生成有更具体的版式参考，本版本还附带 12 张低分辨率 CC BY
图表示例截图和 manifest：

```text
skills/nnscholar-research-suite/assets/zotero-figure-examples/manifest.json
```

这些截图只作为生成原创图表时的布局参考使用；在 handoff 中应保留来源和许可信息。

## 测试

```bash
python scripts/validate_suite.py
```

测试会检查：

- 仓库只暴露一个根 `SKILL.md`；
- 20 个 workflow 都存在并使用 `WORKFLOW.md`；
- `manifest.json` 与文件系统一致；
- 根路由覆盖全部旧别名；
- 本地 `references/` 和 `scripts/` 引用都存在；
- 根 skill frontmatter 符合 Codex 推荐的 `name` + `description` 规范。
- Zotero atlas 每个 workflow 至少 5 个示例，图表生成至少 10 个示例。
- Zotero 图表示例截图存在，并且 manifest 记录了可复用的 CC BY 许可。
