# Literature Search Protocol Template

## Template Language and Editing Rule

This template defines structure, not output language. Before writing the final report, translate all headings, field labels, and explanatory text into the user's output language. Keep filenames, database names, source keys, citation metadata, search strings, and standard identifiers in English or their original scholarly form.

Do not leave empty optional rows, unused database rows, bracket placeholders, or fields that were not applicable. Preserve search transparency by explicitly marking failed or inaccessible sources instead of deleting them silently.

```markdown
# [TOPIC] 文献检索方案

## 基本信息

- 输入问题：
- 输出语言：
- 文件命名规则：英文 ASCII slug
- 检索模式：quick scan / standard search / review search / systematic-ready
- 输出目的：literature review only / research planning
- 引用格式：Vancouver / GB/T 7714 / APA / IEEE / ACM / 用户指定
- 检索日期：
- 时间范围：
- 是否承接 1.1 Question Mining Agent Handoff：是/否

## 研究问题


## 交互式选择记录

- 是否询问用户检索模式：
- 用户选择：
- 是否询问输出目的：
- 用户选择：
- 若未询问，原因：

## 从 1.1 Agent Handoff 抽取的信息

- 首选问题：
- 建议检索概念：
- 必须纳入的研究类型：
- 建议文献表字段：
- 需要重点补充的证据：

## 检索范围

- 时间范围：
- 语言：
- 文献类型：
- 学科/数据库范围：
- 纳入标准：
- 排除标准：

## 检索概念

| 概念组 | 关键词/同义词 | 控制词或数据库标签 |
|---|---|---|
| Population/System |  |  |
| Exposure/Method |  |  |
| Comparator/Context |  |  |
| Outcome/Endpoint |  |  |
| Biomarker/Data type/Mechanism |  |  |
| Trial/Drug/Dataset/Benchmark names |  |  |
| Humanities/Social science terms |  |  |

## 代表性检索式

- 英文检索式：
  1. 
  2. 
  3. 
- 中文检索式（如适用）：
  1. 
  2. 

## 数据库与检索式

| 数据库/来源 | 访问方式/API | 检索式或 endpoint | 日期 | 结果数 | 状态 | 备注 |
|---|---|---|---:|---:|---|---|
| PubMed |  |  |  |  | 成功/失败/未使用 |  |
| ClinicalTrials.gov |  |  |  |  | 成功/失败/未使用 |  |
| FDA/EMA/Guidelines |  |  |  |  | 成功/失败/未使用 |  |
| Google Scholar-style web search |  |  |  |  | 成功/失败/未使用 |  |
| CNKI/Wanfang-style Chinese search |  |  |  |  | 成功/失败/未使用 |  |
| OpenAlex |  |  |  |  | 成功/失败/未使用 |  |
| Semantic Scholar |  |  |  |  | 成功/失败/未使用 |  |
| arXiv |  |  |  |  | 成功/失败/未使用 |  |
| bioRxiv/medRxiv |  |  |  |  | 成功/失败/未使用 |  |
| Crossref |  |  |  |  | 成功/失败/未使用 |  |

## 来源/API 透明度

- 实际调用的数据库/API：
- 使用网页检索的来源：
- 未能调用或失败的来源：
- 替代检索方法：
- 不能声称 comprehensive 的限制：

## 筛选规则

- 第一轮：标题/摘要筛选。
- 第二轮：全文或详细摘要筛选。
- 高优先级文献：
- 排除理由分类：
- 质量分层：
  - A：
  - B：
  - C：
  - Excluded：

## 输出目标

- 核心文献集合：
- 文献凝练表：
- 规范引用清单：
- 文献汇总综述：
- 研究空白：
- 研究设想/研究计划（如适用）：
- 下一步建议：
```
