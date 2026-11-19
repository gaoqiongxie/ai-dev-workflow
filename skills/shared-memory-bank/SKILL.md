---
name: "shared-memory-bank"
description: "Manages shared memory bank and collaborative dev rules for multiple projects (e.g. backend service A & B). Invoke when user mentions cross-project memory, shared rules, dialogue logs, syncing context between projects, or initializing a new project's memory bank and rules."
---

# 多项目共享记忆库与协同开发

## 适用场景

- 用户提到跨项目（项目 A ↔ 项目 B）共享上下文、规则同步
- 需要写入对话日志到共享记忆库
- 需要读取或更新共享的编码规范、TODO 追踪、项目概况
- 涉及多个项目前后端联调时的上下文同步

> 新项目记忆库初始化统一使用 `init-memory-bank`，本 Skill 只维护已存在的共享记忆库。

---

## 项目清单

| 项目 | 代码路径 | 规则文件 | 记忆库目录 | 说明 |
|------|----------|----------|-----------|------|
| project-a | `<代码根目录>/project-a` | `.trae/rules/project-a-shared-rules.md` | `memory-bank/project-a/` | 后端业务服务 |
| project-b | `<代码根目录>/project-b` | `.trae/rules/project-b-shared-rules.md` | `memory-bank/project-b/` | 后端业务服务 |
| web-frontend | `<代码根目录>/web-frontend` | 沿用通用+project-a（未单独建） | `memory-bank/web-frontend/` | 前端项目 |
| batch-service | `<代码根目录>/batch-service` | 未单独建（依赖根通用规则） | （记忆库未初始化） | 批处理服务 |
| job-service | `<代码根目录>/job-service` | 未单独建（依赖根通用规则） | （记忆库未初始化） | 定时任务服务 |
| order-center | `<代码根目录>/order-center` | 未单独建（依赖根通用规则） | （记忆库未初始化） | 订单中心服务 |

> 新项目初始化后，自动追加到本表格。

---

## 共享记忆库结构

`memory-bank/` 是所有项目的共用工作记忆库根目录（可放在任意工作目录外位置）：

```
memory-bank\
├── project-a\                    ← 项目 A 记忆（40+ 编号文档）
│   ├── 00-memory-bank-rules.md      ← 工作规则（每次对话前必读）
│   ├── 01-project-profile.md        ← 项目概况
│   ├── 02-tech-stack.md             ← 技术栈清单
│   ├── 03-architecture.md           ← 架构设计
│   ├── 04-database.md               ← 数据库速查
│   ├── 05-api-reference.md          ← API 参考
│   ├── 06-dev-commands.md           ← 开发命令
│   ├── 07-coding-standards.md       ← 编码规范索引（指向 `07-coding-standards/` 子目录）
│   ├── 07-coding-standards/         ← 编码规范子文件（命名、异常、日志、API、数据库等）
│   ├── 08-issue-log.md              ← 问题记录
│   ├── 09-todo-tracker.md           ← TODO 追踪
│   ├── 10-snippets.md               ← 常用代码片段
│   ├── 11-database-enums.md         ← 数据库字段与枚举对照
│   ├── 12-ext-database-enums.md    ← 扩展数据库枚举（项目 A 特有）
│   ├── 13-feign-client-guide.md     ← Feign 调用指南
│   ├── 14-i18n-guide.md             ← i18n 指南
│   ├── 15-es-integration.md         ← ES 集成指南
│   ├── 16-job-tasks.md              ← 定时任务清单
│   ├── 17-data-permission.md        ← 数据权限控制
│   ├── 18-account-set-guide.md      ← 账套判断规范
│   ├── 38-overseas-project-proposal.md ← 海外项目方案
│   ├── 40-sql-cookbook.md           ← SQL 查询手册（DBeaver 沉淀）
│   └── 99-dialogue-logs\            ← 对话日志
├── project-b\                    ← 项目 B 记忆（33+ 编号文档）
│   ├── 00-memory-bank-rules.md
│   ├── 01-project-profile.md
│   ├── 02-tech-stack.md
│   ├── 03-architecture.md
│   ├── 04-database.md
│   ├── 05-api-reference.md
│   ├── 06-dev-commands.md
│   ├── 07-coding-standards.md       ← 编码规范索引
│   ├── 07-coding-standards/
│   ├── 08-issue-log.md
│   ├── 09-todo-tracker.md
│   ├── 10-snippets.md
│   ├── 11-database-enums.md
│   ├── 12-feign-client-guide.md     ← Feign 客户端调用指南
│   ├── 13-mq-guide.md               ← MQ 指南
│   ├── 14-job-tasks.md              ← 定时任务清单
│   ├── 15-client-api.md             ← 对外 Client API
│   ├── 33-sql-cookbook.md           ← SQL 查询手册（DBeaver 沉淀）
│   └── 99-dialogue-logs\
├── <新项目名>\                   ← 新项目记忆（按需创建）
│   └── ...
└── shared\                       ← ★ 所有项目共享记忆
    ├── 01-cross-project-map.md   ← 跨项目依赖关系图
    ├── 02-shared-constants.md    ← 共享常量与枚举映射
    ├── 03-api-contracts.md       ← 跨项目 API 契约（Feign 接口）
    ├── 04-db-shared-tables.md    ← 共享数据库表说明
    └── 99-dialogue-logs\         ← 跨项目对话日志
```

---

## ★ 新项目初始化流程

当用户说"帮我初始化 XXX 项目的记忆库和规则"或类似意图时，执行以下步骤：

### 第一步：收集项目信息

向用户确认以下信息（如果用户未提供）：

| 信息项 | 示例 | 说明 |
|--------|------|------|
| 项目名称 | `demo` | 英文缩写，用于目录命名 |
| 项目中文全称 | 财务共享服务 | 用于规则文件和日志 |
| 代码路径 | `<代码根目录>/demo-service` | 项目根目录 |
| 技术栈 | Spring Boot + Vue 3 | 主要技术栈 |
| 项目说明 | 财务共享服务平台 | 一句话描述 |

### 第二步：创建项目记忆库

使用 Python 脚本中转，在 `memory-bank/<项目名>\` 下创建以下模板文件：

| 文件 | 模板内容 |
|------|---------|
| `00-memory-bank-rules.md` | 工作规则（每次对话前必读的启动规则） |
| `01-project-profile.md` | 项目概况（名称、技术栈、目录结构、核心模块） |
| `02-tech-stack.md` | 技术栈清单（空模板） |
| `03-architecture.md` | 架构设计（空模板） |
| `04-database.md` | 数据库速查（空模板） |
| `05-api-reference.md` | API 参考（空模板） |
| `06-dev-commands.md` | 开发命令（空模板） |
| `07-coding-standards.md` | 编码规范索引（继承通用规范 + 项目特有规范，指向 `07-coding-standards/` 子目录） |
| `07-coding-standards/` | 编码规范子目录（命名、异常、日志、API、数据库等，按需创建子文件） |
| `08-issue-log.md` | 问题记录（空模板） |
| `09-todo-tracker.md` | TODO 追踪（空模板） |
| `10-snippets.md` | 代码片段（空模板） |
| `11-database-enums.md` | 数据库字段与枚举对照（空模板） |
| `12-feign-client-guide.md` | Feign 调用指南（空模板） |
| `13-mq-guide.md` | MQ 使用指南（空模板） |
| `99-dialogue-logs/` | 对话日志目录（创建目录即可） |

**模板内容参考**：

```markdown
# 01-project-profile.md 模板

# <项目中文全称> — 项目概况

## 基本信息

| 项目 | 值 |
|------|-----|
| 项目名称 | <项目中文全称> |
| 英文缩写 | <项目名> |
| 代码路径 | <代码路径> |
| 技术栈 | <技术栈> |
| 初始化日期 | <YYYY-MM-DD> |

## 项目结构

（待补充：扫描项目目录后自动生成）

## 核心模块

（待补充：了解业务后逐步完善）
```

```markdown
# 09-todo-tracker.md 模板

# <项目中文全称> — TODO 追踪

## 进行中

| 编号 | 需求/Bug | 需求编号 | 状态 | 备注 |
|------|---------|---------|------|------|
| - | - | - | - | - |

## 已完成

| 编号 | 需求/Bug | 需求编号 | 完成日期 | 备注 |
|------|---------|---------|---------|------|
| - | - | - | - | - |
```

### 第三步：创建项目规则文件

在项目的 `.trae/rules/` 目录下创建两个文件：

#### 1. `<项目名>-shared-rules.md` — 项目共享规则

```markdown
# <项目中文全称> 项目共享规则

> 本文件是项目规则的单一事实来源，供 Trae IDE 和 Kimi CLI 共同引用。

---

## 项目清单

| 项目 | 代码路径 | 说明 |
|------|----------|------|
| <项目中文全称> | <代码路径> | <项目说明> |

---

## 技术栈

<技术栈>

---

## 项目结构

（扫描项目目录后补充）

---

## 编码规范

- 遵循项目现有代码风格
- 新增方法必须有 Javadoc
- 复杂逻辑加行注释
- ServiceImpl 禁止直接注入外部 Feign Client，统一走 proxy 层
- 金额用 BigDecimal，日期用 LocalDateTime
- MQ 消费遵循项目现有模式

---

## 工作流程

1. **查规范再动手**：编码前先看同模块已有文件的写法，遵循现有代码风格
2. **最小修改**：只做必要改动，不改无关文件和测试逻辑
3. **Git 规范**：提交信息格式 `feat:<issue-key> <需求名称> <具体改动>`（issue-key 为需求追踪系统中的需求编号，如 story#xxx）
4. **Fallback 说明**：如果用户没有指定需求编号，主动询问确认后再写代码

### 快捷指令

| 用户说法 | 执行操作 | 说明 |
|---------|---------|------|
| "更新下代码" | `git pull` | 直接执行，无需确认 |
| "提交代码" | `git add` + `git commit` | 需确认提交信息 |
| "推送代码" | `git push` | 需确认 |

---

## 禁止行为

- 禁止执行 `git reset --hard`、`git rebase` 等改写历史的操作
- 禁止修改无关文件和测试逻辑
- 禁止使用 `System.out.println()`，统一用 `@Slf4j` 的 `log`
- 禁止在 `memory-bank` 及其子目录存放非 `.md` 文件
```

#### 2. `ai-java-assistant.md` — 助手配置

```markdown
# AI 助手 — IDE 专属配置（<项目中文全称>）

> 项目共享规则已提取到 `<项目名>-shared-rules.md`，本文件只保留 IDE 环境专属指令。
> IDE 会自动加载 `.trae/rules/` 下所有 `.md` 文件，无需手动读取。

---

# Role
你是本项目的专属 Java 后端开发助手。你熟悉 <技术栈>、<项目中文全称> 业务。

# IDE 环境说明

- IDE **自动加载** `.trae/rules/` 目录下所有规则文件，项目共享规则已在 `<项目名>-shared-rules.md` 中自动生效，无需手动读取。
- Memory Bank 路径：`memory-bank/<项目名>/`（与命令行 AI 工具共享上下文）
- 如需查阅更详细的编码参考，可按需读取 memory-bank 中的对应文件：
  - `memory-bank/<项目名>/07-coding-standards.md`（索引文件，指向 `07-coding-standards/` 子目录）、`10-snippets.md`、`12-feign-client-guide.md`、`13-mq-guide.md`

# IDE 专属工作流

1. **自动生效**：共享规则已通过 IDE 自动加载，无需额外操作
2. **查规范再动手**：编码前先看同模块已有文件的写法，遵循现有代码风格
3. **边做边备份**：产生有价值信息时，按 `<项目名>-shared-rules.md` 中的规则写入对话日志
4. **按需读取上下文**：涉及新需求/Bug 时，读取 `memory-bank/<项目名>/09-todo-tracker.md` 和 `01-project-profile.md`
5. **前后端联调**：涉及接口变更时，同步确认前端 API 调用是否需要调整
```

### 第四步：更新 Skill 项目清单

将新项目追加到本 Skill 的「项目清单」表格中。

### 第五步：更新共享记忆库

在 `memory-bank/shared/01-cross-project-map.md` 中追加新项目的依赖关系信息。

### 第六步：同步 Skill 到新项目

将本 Skill（`.trae/skills/shared-memory-bank/`）同步到新项目的 `.trae/skills/shared-memory-bank/`，所有项目共享同一套 Skill。

---

## 写入对话日志流程

由于 IDE 的 `Write` 工具可能无法直接写入记忆库根目录（如工作目录外位置），使用 Python 脚本中转。**优先复用现成模板脚本，避免每次手写**：

```text
scripts/write_memory_template.py   ← 标准写入脚本模板（复制后改路径/内容即可）
```

**标准写流程（两步，代替 4 步手写）**：

1. `Write` 工具创建临时内容文件 `ai-temp/mem_content.md`（写入真实 Markdown 内容）
2. 执行：`python scripts/write_memory_template.py --target="memory-bank/<项目>/99-dialogue-logs/YYYY-MM-DD_<主题>.md" --content-file="ai-temp/mem_content.md"`
3. `DeleteFile` 删除临时内容文件与临时脚本（模板脚本常驻 skill 目录，不删）

**脚本说明**：支持 `--target=`（目标绝对路径，缺省提示用默认路径）与 `--content-file=`（内容文件，缺省为占位模板）；自动创建目标目录、UTF-8 写入、打印字节数供校验。也可参考脚本内注释把路径/内容写死为单文件临时脚本执行。

**日志文件命名规范**：`YYYY-MM-DD_<主题>.md`

**批量创建文件**（用于初始化记忆库，创建完整标准结构）用下方脚本：
```python
import os

base_dir = os.path.join('memory-bank', '<项目名>')
dirs = ['07-coding-standards', '99-dialogue-logs']
files = {
    '00-memory-bank-rules.md': '# <项目中文全称> — 工作规则\n\n> 每次新对话启动时，Kimi CLI / Trae 自动读取此文件恢复上下文。\n\n## 启动必读\n\n1. 读取本文件恢复上下文\n2. 如任务涉及新需求/Bug，同步读取 `09-todo-tracker.md` 和 `01-project-profile.md`\n3. 写代码时参考 `07-coding-standards/` 目录下对应子文件和 `10-snippets.md`\n\n## 项目基础信息\n\n| 属性 | 内容 |\n|------|------|\n| **项目名称** | <项目中文全称> |\n| **代码路径** | <代码路径> |\n| **Memory Bank 路径** | `memory-bank/<项目名>` |',
    '01-project-profile.md': '# <项目中文全称> — 项目概况\n\n## 基本信息\n\n| 项目 | 值 |\n|------|-----|\n| 项目名称 | <项目中文全称> |\n| 英文缩写 | <项目名> |\n| 代码路径 | <代码路径> |\n| 技术栈 | <技术栈> |\n| 初始化日期 | <YYYY-MM-DD> |\n\n## 项目结构\n\n（待补充：扫描项目目录后自动生成）\n\n## 核心模块\n\n（待补充：了解业务后逐步完善）',
    '02-tech-stack.md': '# <项目中文全称> — 技术栈\n\n（待补充）',
    '03-architecture.md': '# <项目中文全称> — 架构设计\n\n（待补充）',
    '04-database.md': '# <项目中文全称> — 数据库速查\n\n（待补充）',
    '05-api-reference.md': '# <项目中文全称> — API 参考\n\n（待补充）',
    '06-dev-commands.md': '# <项目中文全称> — 开发命令\n\n（待补充：常用 Maven 命令、启动命令、调试命令等）',
    '07-coding-standards.md': '# 📐 <项目中文全称> 编码规范\n\n> 本规范按主题拆分为多个子文件，便于精准加载和维护。\n> **注意：以下规则仅对新开发代码生效，历史代码保持不动。**\n\n## 目录\n\n- [命名规范](07-coding-standards/02-naming.md)\n- [代码风格与注释](07-coding-standards/03-coding-style.md)\n- [异常处理](07-coding-standards/04-exception.md)\n- [日志规范](07-coding-standards/05-logging.md)\n- [Maven 规范](07-coding-standards/06-maven.md)\n- [API 设计规范](07-coding-standards/07-api-design.md)\n- [数据库规范](07-coding-standards/08-database.md)\n- [安全规范](07-coding-standards/09-security.md)\n- [代码审查清单](07-coding-standards/10-checklist.md)',
    '08-issue-log.md': '# <项目中文全称> — 问题记录\n\n## 已解决问题\n\n| 日期 | 问题描述 | 解决方案 | 记录人 |\n|------|---------|---------|--------|\n| - | - | - | - |',
    '09-todo-tracker.md': '# <项目中文全称> — TODO 追踪\n\n## 进行中\n\n| 编号 | 需求/Bug | 需求编号 | 状态 | 备注 |\n|------|---------|---------|------|------|\n| - | - | - | - | - |\n\n## 已完成\n\n| 编号 | 需求/Bug | 需求编号 | 完成日期 | 备注 |\n|------|---------|---------|---------|------|\n| - | - | - | - | - |',
    '10-snippets.md': '# <项目中文全称> — 代码片段\n\n（待补充：常用代码模板、工具类示例等）',
    '11-database-enums.md': '# <项目中文全称> — 数据库字段与枚举对照\n\n（待补充）',
    '12-feign-client-guide.md': '# <项目中文全称> — Feign 调用指南\n\n（待补充）',
    '13-mq-guide.md': '# <项目中文全称> — MQ 使用指南\n\n（待补充）',
}

for d in dirs:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

for name, content in files.items():
    filepath = os.path.join(base_dir, name)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {filepath}')

print('Done!')
```

---

## 跨项目协同开发规则

### 1. API 契约同步
- 项目间通过 Feign 接口通信，接口变更必须同步更新：
  - model 模块中的 DTO/Req/Resp
  - 前端对应的 API 调用
- 变更记录写入 `shared/03-api-contracts.md`

### 2. 共享常量与枚举
- 跨项目使用的枚举（账套编码、业务线编码等）记录在 `shared/02-shared-constants.md`
- 新增共享枚举时，所有相关项目的规则文件都需同步更新

### 3. 数据库共享表
- 多项目共用的数据库表记录在 `shared/04-db-shared-tables.md`
- 修改共享表结构时，需评估对所有相关项目的影响

### 4. 编码规范对齐
- 所有项目遵循相同的编码规范核心原则：
  - ServiceImpl 禁止直接注入外部 Feign Client，统一走 proxy 层
  - 金额用 BigDecimal，日期用 LocalDateTime
  - 禁止 `System.out.println()`，统一用 `@Slf4j` 的 `log`
  - 新增方法必须有 Javadoc
  - Git 提交格式：`feat:<issue-key> <需求名称> <具体改动>`（issue-key 为需求追踪系统中的需求编号，如 story#xxx）

### 5. 快捷指令（所有项目通用）

| 用户说法 | 执行操作 | 说明 |
|---------|---------|------|
| "更新下代码" | `git pull` | 直接执行，无需确认 |
| "提交代码" | `git add` + `git commit` | 需确认提交信息 |
| "推送代码" | `git push` | 需确认 |

---

## 初始化共享记忆库

当用户首次提到跨项目协同时，检查 `memory-bank/shared/` 目录是否存在，若不存在则创建以下文件：

1. `01-cross-project-map.md` — 跨项目依赖关系图
2. `02-shared-constants.md` — 共享常量与枚举映射
3. `03-api-contracts.md` — 跨项目 API 契约
4. `04-db-shared-tables.md` — 共享数据库表说明

---

## 定时任务配置

### 推荐调度
- **Cron 表达式**：`0 16 * * THU`
- **时区**：Asia/Shanghai
- **调度频率**：每周四 16:00

### 调度消息模板
当通过 Trae 调度任务自动触发本 Skill 时，使用以下自包含消息：

```text
同步并完善 project-a、project-b 共享记忆库。代码源分别为 `<代码根目录>/project-a` 和 `<代码根目录>/project-b`，记忆库根目录为 `memory-bank/`。
```

### 注意事项
- 定时任务消息必须自包含，独立会话中不得依赖原对话上下文。
- 执行时遵循 `.trae/rules/common-shared-rules.md`、各项目自己的 `<项目名>-shared-rules.md` 以及两个记忆库各自的 `00-memory-bank-rules.md`。
- 不修改任何业务代码，不执行 git commit/push，不连接或修改数据库、配置中心、MQ、ES、Redis。
- 不得在记忆库或日志中保存密码、Token、Webhook、手机号密文、真实业务数据或个人账号。

---

## 注意事项

- 所有备份必须在单次对话过程中完成
- 对话日志只放 `.md` 文件，禁止存放非 `.md` 文件到 `memory-bank` 目录
- 写入完成后务必删除临时 `.py` 脚本
- 跨项目变更时，主动提醒用户确认另一个项目是否需要同步调整
- 新项目初始化完成后，需将本 Skill 同步复制到新项目的 `.trae/skills/` 目录