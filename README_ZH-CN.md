# NNScholar Research Suite

这是 NNScholar 学术研究流程的 Codex 原生单 skill 打包版本。

仓库只暴露一个可安装 skill：

```text
skills/nnscholar-research-suite/
```

20 个具体工作流都放在：

```text
skills/nnscholar-research-suite/workflows/
```

内部入口文件统一叫 `WORKFLOW.md`，而不是 `SKILL.md`。这样 Codex 只会注册
`$nnscholar-research-suite` 一个 skill，但桌面软件仍然可以展示 20 个按钮，并通过
`Workflow: <id>` 路由到对应模块。

## 安装

```bash
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo BobbyWang16/nnscholar-research-suite \
  --ref main \
  --path skills/nnscholar-research-suite \
  --method git
```

Windows 可以用 Codex 自带 Python：

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

## 测试

```bash
python scripts/validate_suite.py
```

测试会检查单入口结构、20 个 workflow、manifest、路由别名、本地引用文件和旧命名残留。
