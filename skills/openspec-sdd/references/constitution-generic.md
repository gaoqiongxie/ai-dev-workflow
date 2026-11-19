# 项目宪法 (Constitution) — 通用模板

> 本文件是项目的顶层设计约束，所有变更必须遵循。
> 与项目共享规则（`.trae/rules/*-shared-rules.md`）的区别：共享规则是操作手册，constitution.md 是设计原则。

---

## 1. 项目定位

[一句话描述项目定位和业务范围]

## 2. 技术栈约束（不可违背）

| 层级 | 技术选型 | 备注 |
|------|---------|------|
| 框架 | [Spring Boot / Django / React / Vue 等] | [禁止引入的技术] |
| ORM/数据访问 | [MyBatis-Plus / JPA / Prisma 等] | [约束说明] |
| 消息队列 | [RocketMQ / Kafka / RabbitMQ 等] | [消费模式约束] |
| 缓存 | [Redis / Caffeine / Memcached 等] | [使用规范] |
| 数据库 | [MySQL / PostgreSQL / TiDB 等] | [特殊约束] |

## 3. 架构约束（不可违背）

### 3.1 分层规范
- Controller / API 层只做参数校验和结果封装，禁止写业务逻辑
- Service 层负责事务编排，复杂逻辑委托给 Component / Strategy / Factory
- DAO / Repository 层只负责数据访问，禁止跨库 join

### 3.2 外部服务调用规范
- 外部 Client 禁止直接注入 ServiceImpl
- 正确路径：ServiceImpl -> Proxy / Adapter -> Client
- 统一包路径：[项目约定的 proxy 包路径]

### 3.3 差异化逻辑隔离
- 字段校验差异 -> StrategyFactory + ValidationService
- 算法差异 -> CalculateFactory + AbstractTemplate
- 枚举值差异 -> 前缀匹配 + 默认回退
- **禁止在 Service 中写 if-else 判断业务标识来做逻辑分支**

### 3.4 定时任务规范
- 分页查询必须指定页大小
- 批量更新必须走临时表过渡或分批提交
- 必须有开关控制（可随时停止）

## 4. 编码规范（不可违背）

- 新增公共方法必须有文档注释（参数、返回值、异常说明）
- 金额用高精度类型（BigDecimal / Decimal），禁止用 float/double
- 日期传输用标准格式（Long 时间戳 / ISO 字符串），内部计算用类型安全的日期类型
- 日志统一用框架日志，禁止直接输出到控制台
- 异常禁止吞掉，必须记录日志或抛出自定义异常

## 5. 数据规范（不可违背）

- 敏感字段必须脱敏处理
- 删除逻辑统一用软删标记，禁止物理删除
- 多语言字段统一走注册体系
- 客户/用户名称统一走脱敏规则

## 6. 测试规范（不可违背）

- 新增接口必须补充单元测试（Service 层）
- 涉及资金/结算的改动必须跑通集成测试
- 定时任务必须验证分页逻辑
- 差异化逻辑必须覆盖至少 2 个场景的边界 case

## 7. 文档规范（不可违背）

- 架构变更必须同步更新项目文档
- 新增接口必须同步更新 API 文档
- 新增表/字段必须同步更新数据库文档
- 对话结束后必须归档到对话日志目录
- **所有备份必须在单次对话过程中完成**

## 8. Git 规范

- 提交信息格式：[类型]:[标识] <描述>
- 禁止执行改写历史的操作（reset --hard、rebase 等）
- 禁止提交未完成的变更（WIP 代码）
