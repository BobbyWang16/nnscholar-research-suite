# NNScholar Research Suite

这是 NNScholar 学术研究流程的 Codex 原生单 skill 打包版本。

仓库只暴露一个可安装 skill：

```text
skills/nnscholar-research-suite/
```

16 个具体工作流放在：

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
请为这个假设设计并锁定可执行研究方案。
```

也可以使用当前工作流别名：

```text
/nnscholar4-3-paper-writing 请基于这些材料起草论文
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
| 3.1 | `nnscholar3-1-experiment-validation-plan` |
| 4.1 | `nnscholar4-1-paper-figure` |
| 4.2 | `nnscholar4-2-paper-table` |
| 4.3 | `nnscholar4-3-paper-writing` |
| 5.1 | `nnscholar5-1-journal-conference-recommendation` |
| 5.2 | `nnscholar5-2-submission-finalization` |
| 5.3 | `nnscholar5-3-submission-portal-workflow` |
| 5.4 | `nnscholar5-4-cover-letter` |
| 5.5 | `nnscholar5-5-reviewer-response` |

新版合并了旧拆分阶段：`2.2` 同时负责 ARS 方案、实验流程图、验证路线、可行性审计、pilot 计划、go/no-go 标准和 fallback 方案；`4.1` 负责数据图、示意图、图形摘要和多面板组图；`4.2` 负责论文表格；`4.3` 负责论文起草、修改、润色和审计。

## 专业 Guardrails

套件在 `references/` 下内置了多层约束：

- `companion-skill-bridge.md`：把 NNScholar 阶段映射到医学、影像 AI、证据检索、文件格式、技术论文等 co-installed specialist skills。
- `supervisor-research-guardrails.md`：为 AI/data-science、数据库、系统、ML、NLP、benchmark 等论文加入导师式检查。
- `ai-research-engineering-guardrails.md`：加入实验工程、复现、训练、benchmark、自主循环和发布就绪审计。
- `high-impact-paper-guardrails.md`：加入 Nature/CNS 风格的论文结构、图表、引用、数据代码可用性和审稿回复检查。

NNScholar 始终是阶段编排器。协同 skill 可以细化证据、领域规范、报告标准或文件处理，但不能在不回到上游 workflow 的情况下覆盖已经锁定的 NNScholar protocol。

## Zotero 示例 Atlas

套件包含一个基于用户 Zotero 库整理的版权安全示例 atlas：

```text
skills/nnscholar-research-suite/references/zotero-example-atlas.md
```

它为工作流任务提供结构示例卡，并为 `nnscholar4-1-paper-figure` 提供 12 个图表生成示例。示例会保留 Zotero key、期刊、DOI/URL 和可模仿结构，但不会复制论文原图、caption、表格或长段原文。

为了让图表生成有更具体的版式参考，套件还附带 12 张低分辨率 CC BY 图表示例截图和 manifest：

```text
skills/nnscholar-research-suite/assets/zotero-figure-examples/manifest.json
```

这些截图只作为生成原创图表时的布局参考使用；在 handoff 中应保留来源和许可信息。

## 测试

```bash
python scripts/validate_suite.py
```

测试会检查：

- 仓库只暴露一个根 `SKILL.md`
- 16 个 workflow 都存在并使用 `WORKFLOW.md`
- `manifest.json` 与文件系统一致
- 根路由覆盖所有当前 workflow 别名
- 本地 `references/` 和 `scripts/` 引用都存在
- 旧拆分阶段 workflow 名称不会残留
- 根 skill frontmatter 符合 Codex 推荐的 `name` + `description` 规范
- Zotero atlas 覆盖当前 workflow，并为 `nnscholar4-1-paper-figure` 提供至少 10 个 figure examples
- Zotero 图表示例截图存在，并在 manifest 中记录可复用的 CC BY 许可
