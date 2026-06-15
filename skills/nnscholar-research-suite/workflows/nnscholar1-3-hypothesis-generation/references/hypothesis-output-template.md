# Hypothesis Output Template

## Template Language and Editing Rule

This template defines structure, not output language. Before writing the final report, translate all headings, field labels, and explanatory text into the user's output language. Keep filenames, source keys, citation metadata, hypothesis IDs, variable names, endpoint names, and standard identifiers in English or their original scholarly form when that is clearer.

Do not leave empty rounds, unused hypothesis rows, bracket placeholders, or bilingual duplicate sections in the final report. If a hypothesis is provisional, mark it explicitly and explain the missing evidence.

```markdown
# [TOPIC] 研究假说生成与校正报告

## 基本信息

- 输入主题/研究问题：
- 输出语言：
- 文章类型：
- 学科领域：
- 研究目标：
- 数据/样本/模型：
- 检索或证据来源：
- 文件命名规则：英文 ASCII slug
- 生成日期：

## 本地证据定位

| 来源类型 | 文件/路径 | 匹配理由 | 使用状态 | 备注 |
|---|---|---|---|---|
| 1.2 Literature Searching |  |  | 使用/未使用/缺失 |  |
| 1.1 Question Mining |  |  | 使用/未使用/缺失 |  |
| Local project files |  |  | 使用/未使用/缺失 |  |

## 上游一致性检查

| 检查项 | 结果 | 问题 | 修正 |
|---|---|---|---|
| 是否对应 1.1 研究空白 |  |  |  |
| 是否基于 1.2 核心文献 |  |  |  |
| 是否避开不建议方向 |  |  |  |
| 是否能转入研究设计 |  |  |  |
| 是否证据不足需标记 provisional |  |  |  |

## 多轮对话记录

| 轮次 | 目标 | 用户选择/反馈 | 修改结果 |
|---|---|---|---|
| Round 0 Evidence + Intake | 定位本地证据并确认文章类型 |  |  |
| Round 1 Mapping | 证据到假说框架 |  |  |
| Round 2 Candidates | 候选假说生成 |  |  |
| Round 3 Challenge | 反方挑战与修正 |  |  |
| Round 4 Quality Gate | 质量评分 |  |  |
| Round 5 Lock | 最终锁定 |  |  |

## 工作假说卡片

- Current claim：
- Study object：
- Mechanism/path：
- Primary measurable endpoint：
- Main uncertainty：
- Next decision needed：

## 证据到假说映射

- 研究问题：
- 关键证据：
- 已知研究空白：
- 关键矛盾或争议：
- 可能机制链：
- 可用数据/材料：
- 约束条件：

```text
Research gap -> Evidence anchors -> Missing mechanism/decision -> Testable hypothesis -> Required design
```

## 候选假说

| ID | 假说陈述 | 类型 | 证据依据 | 核心假设 | 预测观察 | 需要的数据/实验 | 可行性 | 主要风险 |
|---|---|---|---|---|---|---|---|---|
| H1 |  |  |  |  |  |  |  |  |
| H2 |  |  |  |  |  |  |  |  |
| H3 |  |  |  |  |  |  |  |  |

## 反方挑战与修正

| 假说 | 主要挑战 | 替代解释 | 修正建议 | 是否保留 |
|---|---|---|---|---|
| H1 |  |  |  |  |
| H2 |  |  |  |  |
| H3 |  |  |  |  |

## 最终锁定假说

### 主假说

**Hypothesis**：

**中文表述**：

**英文表述**：

**假说类型**：

**研究对象/系统**：

**暴露/干预/扰动/方法**：

**对照/比较**：

**主要终点/读数**：

**预测结果**：

**能够推翻该假说的结果**：

### 次要假说

1. 
2. 
3. 

### 零假说/替代假说

- 零假说：
- 替代解释 1：
- 替代解释 2：

## 变量、终点与读数

| 类别 | 名称 | 定义 | 测量方法 | 时间点 | 备注 |
|---|---|---|---|---|---|
| Population/System |  |  |  |  |  |
| Exposure/Intervention |  |  |  |  |  |
| Comparator |  |  |  |  |  |
| Primary endpoint/readout |  |  |  |  |  |
| Secondary endpoint/readout |  |  |  |  |  |
| Safety/negative readout |  |  |  |  |  |
| Confounder/covariate |  |  |  |  |  |

## 质量门控评分

| 假说 | 证据扎根 | 可证伪性 | 具体性 | 机制清晰度 | 可测量性 | 可行性 | 新颖性 | 设计就绪度 | 总体建议 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| H1 |  |  |  |  |  |  |  |  |  |
| H2 |  |  |  |  |  |  |  |  |  |
| H3 |  |  |  |  |  |  |  |  |  |

## 研究设计 Handoff

- 锁定主假说：
- 建议研究设计类型：
- 最小可行数据/样本：
- 必须控制的混杂/偏倚：
- 必须验证的机制或中介路径：
- 推荐主要终点：
- 推荐次要终点：
- 推荐统计/分析方法：
- 样本量或功效分析提示：
- 伦理/安全/可行性注意事项：
- 不建议进入设计的假说：

## Article Structure Handoff

- 标题方向：
- Introduction 逻辑：
- Methods 模块：
- Results 图表顺序：
- Discussion 主张：
- Limitations：
- Next step：

## 参考证据

1. 
2. 
3. 
```
