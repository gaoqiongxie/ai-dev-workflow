# AI 协作开发工作流（ai-dev-workflow）

一套在真实业务项目中打磨出来的 **AI 辅助开发工作流 skill 集**，面向 Claude Code、Trae 等支持 Skill 机制的 AI 编程工具。

核心思想：**让 AI 像一名有规矩的工程师一样工作**——需求先落文档再动手、变更可追溯、每日工作留痕可回顾、多 AI 工具共享同一套记忆。

> 本仓库已从原始项目中完全脱敏：不含任何公司系统、内网地址、人名与联系方式。文中所有「需求追踪系统」「企业 IM」均为占位概念，接入时替换为你团队实际使用的工具（Jira / Zentao / 飞书 / Slack…）即可。

## Skill 总览（12 个）

### 一、OpenSpec SDD 工作流（7 个）

Spec-Driven Development：用结构化文档驱动开发，AI 每个阶段有明确的输入、输出和检查单。

| Skill | 作用 | 触发示例 |
|-------|------|----------|
| `openspec-sdd` | 工作流总入口与阶段路由 | 「走 SDD 流程开发 xx 需求」 |
| `openspec-propose` | 阶段 1-2：需求探询 + 结构化提案（中文命名、影响面评估） | 「帮我提个需求」 |
| `openspec-explore` | 阶段 3：技术调研，多方案对比 | 「调研一下 xx 怎么实现」 |
| `openspec-apply-change` | 阶段 4：按提案实施变更 | 「开始开发」 |
| `openspec-audit` | 阶段 4 内嵌：质量审计（含全量审核矩阵基线） | 「审计一下当前变更」 |
| `openspec-archive-change` | 阶段 5：归档变更、沉淀经验 | 「归档这个需求」 |
| `openspec-init-baseline` | 项目初始化：建立 OpenSpec 目录与审计基线 | 「初始化 OpenSpec」 |

### 二、质量与复盘（3 个）

| Skill | 作用 | 触发示例 |
|-------|------|----------|
| `low-rework-dev-gate` | 防返工门禁：提交/合并前的检查清单，把返工挡在事前 | 「过一遍门禁」 |
| `daily-work-review` | 每日工作回顾：从当日对话日志自动生成结构化日报 | 「生成今日回顾」 |

### 三、共享记忆库（3 个）

让多个 AI 工具（Claude / Trae / Kimi…）读写同一份项目记忆，换工具不丢上下文。

| Skill | 作用 | 触发示例 |
|-------|------|----------|
| `init-memory-bank` | 初始化 memory-bank 目录结构与写作规范 | 「初始化记忆库」 |
| `memory-lookup` | 跨项目记忆检索（约束 AI 先查后写） | 「查一下之前怎么做的」 |
| `shared-memory-bank` | 共享记忆库协作宪章与读写规范 | 「记忆库怎么协作」 |

## 最快接入：让 AI 帮你装上这套工作流

把下面这段 prompt **原样**发给你项目里的 AI 编码助手（Claude Code / Trae / Kimi / Cursor 均可），它会把本仓库的 skill 集装配进你的项目：

```text
我要给当前项目接入一套 AI 协作开发工作流 skill 集，仓库地址：
https://github.com/gaoqiongxie/ai-dev-workflow

请先通读该仓库的 README.md，然后帮我完成接入：

1. git clone（或下载）该仓库到临时目录，把 skills/ 下 12 个 skill 目录复制到我当前
   项目的 skill 目录（Claude Code 用 .claude/skills/，Trae 用 .trae/skills/，
   按我实际用的工具选择，不确定先问我）
2. 全局搜索 skill 文件里的占位概念并替换成我们团队的真实工具（先列出替换计划给我看，
   确认后再改）：
   - 「需求追踪系统」→ 我们实际用的 Jira / Zentao / 飞书项目及编号格式
   - 「企业 IM 机器人」→ 我们的通知渠道（没有就删除相关段落）
3. 项目根目录没有规则入口的话，顺手建一个（CLAUDE.md / AGENTS.md），写明：
   新需求必须走 openspec-sdd 流程，禁止跳过提案直接开发
4. 跑一次 openspec-init-baseline 初始化 OpenSpec 目录与审计基线
5. 验证：让我说一句「走 SDD 流程开发 xx 需求」，确认 AI 能正确路由到 openspec-propose

【红线】
- 替换占位概念时只改 skill 文档与模板，不要动我项目里已有的业务代码
- skill 里的阶段编号/检查单结构保持原样，不要"顺手优化"重组
- 接入完成后给我一份变更清单（改了哪些文件、替换了哪些占位词）
```

## 快速接入

1. 把 `skills/` 下需要的目录复制（或软链）到你的工具 skill 目录：
   - Claude Code：`<项目>/.claude/skills/`
   - Trae：`<项目>/.trae/skills/`
2. 按需替换占位概念：
   - 「需求追踪系统」→ 你们的 Jira / Zentao 及编号格式
   - 「企业 IM 机器人」→ 通知渠道（如有）
3. 跑一次 `openspec-init-baseline` 初始化项目基线，即可开始用 `openspec-sdd` 走完整流程。

## 典型一天

```
早上   AI 读记忆库 → 恢复上下文（memory-lookup）
      新需求 → openspec-propose 出提案 → 确认后 apply-change 开发
      中途  → audit 质量审计，门禁拦截返工（low-rework-dev-gate）
晚上  → daily-work-review 生成日报，对话日志自动归档
```

## 设计原则

- **文档先行**：没有提案不开发，没有检查单不合入
- **一事一日志**：对话日志即资产，日报/复盘从日志自动生成
- **记忆共享**：所有 AI 工具读写同一 memory-bank，人离开项目记忆不离开
- **阶段可单用**：每个 skill 独立可用，也可串成完整 SDD 流水线

## 许可与说明

- 代码与文档可自由用于学习与内部使用；如需商用请自行评估
- 本工作流在真实项目中持续演进，欢迎提 Issue 交流使用场景
