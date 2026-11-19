# Kimi SDD 工作流 Prompt 模板

> 使用方法：每次开新需求时，将本模板复制到对话开头，替换 [story编号] 和 [需求描述]。

---

## 阶段 1：规范生成（不写代码）

```
我需要实现【story#[编号]：[需求描述]】。

请严格执行以下步骤，**不要直接写代码**：

1. 读取项目宪法：memory-bank/<项目>/openspec/constitution.md
2. 读取记忆库上下文：memory-bank/<项目>/01-project-profile.md 和 09-todo-tracker.md
3. 检查是否已有同主题变更目录：memory-bank/<项目>/openspec/changes/
4. 创建变更目录：memory-bank/<项目>/openspec/changes/[YYYY-MM-DD-需求编号-简短描述]\
5. 生成规划文档（按 templates\ 格式）：
   - proposal.md — 意图和范围
   - design.md — 技术方案
   - specs.md — 验收标准
6. 生成 tasks.md — 任务清单（只列任务，不执行）

完成以上步骤后，请向我汇报生成的规划文档内容，等待我审查确认。
```

---

## 阶段 2：审查确认（人决策）

```
我已审查 proposal/design/specs，确认以下调整：
- [调整点 1]
- [调整点 2]

请按以上调整修改规划文档，然后进入实施阶段。
```

---

## 阶段 3：按规范实施（写代码）

```
请按 tasks.md 逐项实现，每完成一项在 tasks.md 中标记 [x]。

执行约束：
1. 每次修改文件前，先读取该文件确认上下文
2. 遵循 constitution.md 中的架构约束和编码规范
3. 涉及账套差异时，优先使用 Strategy/Factory 模式，禁止 if-else 判断 accountSetCode
4. 修改完成后，在代码中添加必要的 Javadoc 和行注释
5. 如果某个任务需要超出 specs.md 范围的改动，先暂停并向我确认
```

---

## 阶段 4：验证（对照规范检查）

```
请验证当前实现是否符合 specs.md 中的验收标准。

逐条检查：
- [ ] 功能正确性：是否满足 proposal.md 中的 Intent
- [ ] 范围控制：是否触及 Out of Scope 的内容
- [ ] 架构合规：是否违反 constitution.md 的约束
- [ ] 边界 case：是否处理了 specs.md 中的异常场景
- [ ] 文档同步：项目共享规则 / API 文档 / 数据库文档是否需要更新

输出验证报告，标记通过的项和未通过的项（附原因）。
```

---

## 阶段 5：归档（结束对话前必须执行）

```
请执行归档操作：

1. 确认 tasks.md 全部标记 [x]
2. 将本次变更总结写入 memory-bank：
   memory-bank/<项目>/99-dialogue-logs/YYYY-MM-DD_[主题].md
3. 如有架构变更，同步更新 memory-bank/<项目>/01-project-profile.md
4. 更新 memory-bank/<项目>/09-todo-tracker.md
5. 如有代码变更，按 Git 规范提交

归档完成后，输出归档清单。
```

---

## 快捷指令（单次操作）

| 场景 | 使用的 Prompt |
|------|--------------|
| 需求明确，直接开干 | 阶段 1 -> 阶段 3 -> 阶段 4 -> 阶段 5 |
| 需求模糊，先调研 | 阶段 1（仅 proposal）-> 人工确认 -> 继续 |
| 已有规范，继续实现 | 阶段 3（读取现有 tasks.md，从断点继续） |
| 仅修复 Bug | 跳过阶段 1，直接阶段 3（tasks 只有 1~2 项） |
| 纯文档梳理 | 阶段 1 -> 阶段 2 -> 阶段 5（无代码） |
