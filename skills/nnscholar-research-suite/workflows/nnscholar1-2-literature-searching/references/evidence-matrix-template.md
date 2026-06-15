# Literature Table Template

## Template Language and Editing Rule

This template defines structure, not output language. Before writing the final report, translate all headings, field labels, and explanatory text into the user's output language. Keep filenames, database names, source keys, citation metadata, search strings, and standard identifiers in English or their original scholarly form.

Use only the discipline-specific extension tables that fit the user's topic. Remove irrelevant tables from the final report to keep the document readable and easy to revise.

```markdown
## 检索与筛选摘要

| 阶段 | 数量 | 说明 |
|---|---:|---|
| 初始检索 |  |  |
| 去重后 |  |  |
| 标题/摘要筛选后 |  |  |
| 全文/深度筛选后 |  |  |
| 核心文献 |  |  |

## 数据库结果与失败记录

| 数据库/来源 | 检索式数量 | 初始结果数 | 纳入候选数 | 状态 | 失败或限制说明 |
|---|---:|---:|---:|---|---|
| PubMed |  |  |  |  |  |
| ClinicalTrials.gov |  |  |  |  |  |
| OpenAlex/Semantic Scholar |  |  |  |  |  |
| 其他 |  |  |  |  |  |

## 排除理由统计

| 排除理由 | 数量 | 示例 |
|---|---:|---|
| 错疾病/错人群/错模型/错任务 |  |  |
| 低相关 |  |  |
| 重复记录 |  |  |
| 评论/新闻/社论且无原始证据 |  |  |
| 样本过小且无验证 |  |  |
| 元数据不可核验 |  |  |

## 核心文献凝练表

| Paper ID | 规范引用 | 年份 | DOI/PMID/NCT/arXiv | 数据库/出处 | 类型 | 质量等级 | 研究对象/数据来源 | 方法/干预/理论 | 主要结果 | 关键结论 | 局限 | 与本主题的关系 | 可复用点 |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| P001 |  |  |  |  |  | A/B/C |  |  |  |  |  |  |  |

## 临床研究扩展字段

| Paper ID | PICO/PECO | 分期/疾病定义 | 样本量 | 治疗线数 | 随访 | 主要终点 | 关键次要终点 | 安全性 | 偏倚风险 | 指南/监管相关性 | 对研究设计的启发 |
|---|---|---|---:|---|---|---|---|---|---|---|---|

## 基础医学扩展字段

| Paper ID | 模型 | 样本来源 | 扰动 | readout | 机制链条 | rescue/验证 | 可复用方法 | 转化风险 |
|---|---|---|---|---|---|---|---|---|

## AI/数据科学扩展字段

| Paper ID | 数据集 | 任务 | baseline | 指标 | 消融 | 错误模式 | 代码/数据可用性 | 复现风险 | benchmark 竞争关系 |
|---|---|---|---|---|---|---|---|---|---|

## 人文社科扩展字段

| Paper ID | 理论框架 | 资料/语料/档案来源 | 时间/地区 | 方法 | 核心观点 | 所处争论 | 可借鉴之处 |
|---|---|---|---|---|---|---|---|

## 文献汇总综述

- 主题 1：
- 主题 2：
- 主题 3：
- 主要共识：
- 主要分歧：
- 证据不足：

## 研究空白与研究计划（仅在 research planning 输出目的下使用）

- 可研究空白：
- 研究设想：
- 研究对象/数据：
- 方法路线：
- 预期结果：
- 风险与替代方案：

## 文献综述任务结论（仅在 literature review only 输出目的下使用）

- 综述主线：
- 推荐章节结构：
- 需要补充的文献类型：
- 引用格式注意事项：
```
