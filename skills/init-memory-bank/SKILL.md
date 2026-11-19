---
name: "init-memory-bank"
description: 'Initialize a standard memory-bank for Java backend projects. Invoke when user says init memory bank / create project memory bank / initialize memory bank / 生成项目记忆库 / 初始化记忆库, or any request to set up a new project memory-bank under memory-bank/<项目名>/.'
---

# init-memory-bank — 项目记忆库初始化

## 适用场景

- 新项目需要建立标准记忆库
- 现有项目记忆库缺失或需要重建
- 复制已有项目记忆库结构到新项目

---

## 标准记忆库结构

```
memory-bank/<项目名>\
├── 00-memory-bank-rules.md      ← 工作规则（每次对话前必读）
├── 01-project-profile.md        ← 项目概况
├── 02-tech-stack.md             ← 技术栈清单
├── 03-architecture.md           ← 架构设计
├── 04-database.md               ← 数据库速查
├── 05-api-reference.md          ← API 参考
├── 06-dev-commands.md           ← 开发命令
├── 07-coding-standards.md       ← 编码规范索引
├── 07-coding-standards/         ← 编码规范子目录
│   ├── 01-git-commit.md         ← Git 提交规范（可选）
│   ├── 02-naming.md             ← 命名规范
│   ├── 03-coding-style.md       ← 代码风格与注释
│   ├── 04-exception.md          ← 异常处理
│   ├── 05-logging.md            ← 日志规范
│   ├── 06-maven.md              ← Maven 规范
│   ├── 07-api-design.md         ← API 设计规范
│   ├── 08-database.md           ← 数据库规范
│   ├── 09-security.md           ← 安全规范
│   ├── 10-checklist.md          ← 代码审查清单
│   └── 11-project-specific.md   ← 项目特有规范（可选）
├── 08-issue-log.md              ← 问题记录
├── 09-todo-tracker.md           ← TODO 追踪
├── 10-snippets.md               ← 常用代码片段
├── 11-database-enums.md         ← 数据库字段与枚举对照
├── 12-feign-client-guide.md     ← Feign 调用指南
├── 13-mq-guide.md               ← MQ 使用指南
├── 99-dialogue-logs/            ← 对话日志目录
```

> 项目特有文件（如 `14-i18n-guide.md`、`15-es-integration.md` 等）按需后续补充。

---

## 初始化流程

### 第一步：收集项目信息

向用户确认（如未提供）：

| 信息项 | 示例 | 说明 |
|--------|------|------|
| 项目名称 | `demo` | 英文缩写，用于目录命名 |
| 项目中文全称 | 财务共享服务 | 用于规则文件和日志 |
| 代码路径 | `<代码根目录>/demo-service` | 项目根目录 |
| 技术栈 | Spring Boot + Vue 3 | 主要技术栈 |
| 项目说明 | 财务共享服务平台 | 一句话描述 |
| 参考项目 | `project-a` / `project-b` | 复制哪个现有项目的结构（如有） |

### 第二步：创建目录和文件

使用 Python 脚本在 `memory-bank/<项目名>/` 下创建完整结构。

**脚本模板**：

```python
import os

base_dir = os.path.join('memory-bank', '<项目名>')
sub_dirs = ['07-coding-standards', '99-dialogue-logs']

files = {
    '00-memory-bank-rules.md': '''# <项目中文全称> — 工作规则

> 每次新对话启动时，Kimi CLI / Trae 自动读取此文件恢复上下文。

## 启动必读

1. 读取本文件恢复上下文
2. 如任务涉及新需求/Bug，同步读取 `09-todo-tracker.md` 和 `01-project-profile.md`
3. 写代码时参考 `07-coding-standards/` 目录下对应子文件和 `10-snippets.md`

## 项目基础信息

| 属性 | 内容 |
|------|------|
| **项目名称** | <项目中文全称> |
| **代码路径** | <代码路径> |
| **Memory Bank 路径** | `memory-bank/<项目名>` |
| **技术栈** | <技术栈> |
''',
    '01-project-profile.md': '''# <项目中文全称> — 项目概况

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
''',
    '02-tech-stack.md': '# <项目中文全称> — 技术栈\n\n（待补充）',
    '03-architecture.md': '# <项目中文全称> — 架构设计\n\n（待补充）',
    '04-database.md': '# <项目中文全称> — 数据库速查\n\n（待补充）',
    '05-api-reference.md': '# <项目中文全称> — API 参考\n\n（待补充）',
    '06-dev-commands.md': '# <项目中文全称> — 开发命令\n\n## 常用命令\n\n```bash\n# 本地启动\n\n# 打包\n\n# 运行测试\n```',
    '07-coding-standards.md': '''# 📐 <项目中文全称> 编码规范

> 本规范按主题拆分为多个子文件，便于精准加载和维护。
> **注意：以下规则仅对新开发代码生效，历史代码保持不动。**

## 目录

- [命名规范](07-coding-standards/02-naming.md)
- [代码风格与注释](07-coding-standards/03-coding-style.md)
- [异常处理](07-coding-standards/04-exception.md)
- [日志规范](07-coding-standards/05-logging.md)
- [Maven 规范](07-coding-standards/06-maven.md)
- [API 设计规范](07-coding-standards/07-api-design.md)
- [数据库规范](07-coding-standards/08-database.md)
- [安全规范](07-coding-standards/09-security.md)
- [代码审查清单](07-coding-standards/10-checklist.md)
''',
    '08-issue-log.md': '''# <项目中文全称> — 问题记录

## 已解决问题

| 日期 | 问题描述 | 解决方案 | 记录人 |
|------|---------|---------|--------|
| - | - | - | - |

## 待解决

| 日期 | 问题描述 | 优先级 | 记录人 |
|------|---------|--------|--------|
| - | - | - | - |
''',
    '09-todo-tracker.md': '''# <项目中文全称> — TODO 追踪

## 进行中

| 编号 | 需求/Bug | 需求编号 | 状态 | 备注 |
|------|---------|---------|------|------|
| - | - | - | - | - |

## 已完成

| 编号 | 需求/Bug | 需求编号 | 完成日期 | 备注 |
|------|---------|---------|---------|------|
| - | - | - | - | - |
''',
    '10-snippets.md': '# <项目中文全称> — 代码片段\n\n（待补充：常用代码模板、工具类示例等）',
    '11-database-enums.md': '# <项目中文全称> — 数据库字段与枚举对照\n\n（待补充）',
    '12-feign-client-guide.md': '# <项目中文全称> — Feign 调用指南\n\n（待补充）',
    '13-mq-guide.md': '# <项目中文全称> — MQ 使用指南\n\n（待补充）',
}

# 07-coding-standards 子文件
coding_standards_dir = os.path.join(base_dir, '07-coding-standards')
coding_files = {
    '02-naming.md': '''## 命名规范

### 包结构

```
com.example.<项目名>
├── controller
├── service
│   └── impl
├── mapper
├── entity
├── dto
├── vo
├── query
├── config
├── utils
├── enums
└── constant
```

### 类命名

| 类型 | 规范 | 示例 |
|------|------|------|
| 实体类 | 名词，驼峰 | `User` |
| DTO | 名词 + Dto | `UserDto` |
| VO | 名词 + Vo | `UserVo` |
| Service | 名词 + Service | `UserService` |
| Mapper | 名词 + Mapper | `UserMapper` |
| Controller | 名词 + Controller | `UserController` |
| 常量类 | 名词 + Constants | `CacheConstants` |
| 枚举 | 名词 + Enum | `UserStatusEnum` |

### 方法命名

| 操作 | 前缀 | 示例 |
|------|------|------|
| 获取单个 | `get` | `getById()` |
| 获取列表 | `list` | `listAll()` |
| 分页查询 | `page` | `pageList()` |
| 新增 | `save` / `add` | `save()` |
| 修改 | `update` / `modify` | `updateById()` |
| 删除 | `remove` / `delete` | `removeById()` |
| 校验 | `check` / `validate` | `checkUnique()` |

### 变量命名

- 常量：全大写 + 下划线（`MAX_RETRY_COUNT`）
- 成员变量：驼峰（`userName`）
- 布尔变量：避免 `is` 开头（`deleted` 而不是 `isDeleted`）
- 集合变量：复数或 `list`/`map` 后缀（`users`、`userNameMap`）
''',
    '03-coding-style.md': '''## 代码格式

### 缩进与空格
- 使用 4 个空格缩进（不使用 Tab）
- 大括号使用 K&R 风格（左括号不换行）

### 空行规范
- 包声明、导入、类声明之间空一行
- 成员变量之间根据逻辑分组，组间空行
- 方法之间空一行

## 注释规范

### 类注释
```java
/**
 * 用户管理服务
 *
 * @author <作者>
 * @since <日期>
 */
```

### 方法注释
```java
/**
 * 根据ID获取用户详情
 *
 * @param id 用户ID
 * @return 用户实体
 */
```

## 代码风格原则（SDD-Global 对齐）

### 事务规范
- 事务注解**只在 Service 层**使用
- 必须指定 `rollbackFor = Exception.class`

### 禁止项
| 禁止项 | 说明 | 正确做法 |
|--------|------|---------|
| 手动创建线程 | `new Thread()` 消耗资源且不可控 | 统一使用线程池 |
| `System.out.println` | 无法分级、无法统一收集 | 使用 SLF4J 日志框架 |
| `@Deprecated` 类/方法 | 可能在未来版本移除 | 使用替代方案或升级依赖 |
| 裸 `RuntimeException` | 丢失业务语义 | 使用 `ServiceException` |
| 流水账代码 | 重复逻辑不抽取 | 提取为独立方法/工具类 |
| 魔法值 | 代码中出现裸字符串/数字 | 统一使用枚举或常量类 |

> **注意：以上规则仅对新开发代码生效，历史代码保持不动。**
''',
    '04-exception.md': '''## 异常处理

### 统一异常处理
```java
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {

    @ExceptionHandler(ServiceException.class)
    public Result<Void> handleServiceException(ServiceException e) {
        log.warn("业务异常: {}", e.getMessage());
        return Result.fail(e.getCode(), e.getMessage());
    }

    @ExceptionHandler(Exception.class)
    public Result<Void> handleException(Exception e) {
        log.error("系统异常", e);
        return Result.fail(500, "系统繁忙，请稍后重试");
    }
}
```

### 业务异常使用
```java
if (user == null) {
    throw new ServiceException("用户不存在");
}
```

## 异常处理补充规范（SDD-Global 对齐）

### 禁止项
| 禁止项 | 说明 | 正确做法 |
|--------|------|---------|
| `printStackTrace()` | 直接打印到标准错误流 | 使用日志框架 `log.error("...", e)` |
| 空 `catch` 块 | 吞掉异常不处理 | 至少记录日志或抛出自定义异常 |
| 裸 `RuntimeException` | 无业务语义 | 使用 `ServiceException` |

> **注意：以上规则仅对新开发代码生效，历史代码保持不动。**
''',
    '05-logging.md': '''## 日志规范

### 日志级别使用
```java
// ERROR: 系统错误，需要立即处理
catch (Exception e) {
    log.error("保存失败, id={}", id, e);
}

// WARN: 警告，业务异常或潜在问题
if (count > 10000) {
    log.warn("数量超过阈值, count={}", count);
}

// INFO: 重要业务信息
log.info("创建成功, id={}", id);

// DEBUG: 调试信息，只在开发环境打印
log.debug("查询参数: {}", query);
```

### 日志格式
- 推荐：使用占位符 `log.info("id={}", id)`
- 不推荐：字符串拼接 `log.info("id=" + id)`

## 日志规范补充（SDD-Global 对齐）

### 强制要求
- **入参、出参、异常必须打印日志**
- 禁止日志级别混乱（如错误场景用 `info`、正常流程用 `error`）
- 不打印敏感数据（密码、身份证、手机号）

> **注意：以上规则仅对新开发代码生效，历史代码保持不动。**
''',
    '06-maven.md': '''## Maven 规范

### 依赖管理
- **所有依赖版本统一在父 POM `<properties>` 标签中定义**
- 子模块 `<dependency>` 中**不指定版本号**
- 禁止使用 `<scope>system</scope>` 和 `<systemPath>`

### 示例
```xml
<!-- 父 POM -->
<properties>
    <mybatis-plus.version>3.5.9</mybatis-plus.version>
</properties>

<!-- 子模块 -->
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
</dependency>
```
''',
    '07-api-design.md': '''## API 设计规范

### 接口路径前缀规范

| 接口类型 | 前缀 | 示例 |
|---------|------|------|
| 前端接口 | `/api/` | `/api/<项目名>/user/list` |
| 内部 Feign 接口 | `/feign/` | `/feign/user/getById` |
| 第三方 OpenAPI | `/open-api/` | `/open-api/user/sync` |
| 定时任务 | `/job/` | `/job/user/refresh` |

### 接口命名规范
- URL 统一使用**小写**
- 双斜杠间尽可能使用**单个有意义的单词**
- 多个单词使用**中划线 `-`** 拼接

### 统一返回
```java
@Data
public class Result<T> {
    private Integer code;
    private String msg;
    private T data;
    private Long timestamp;

    public static <T> Result<T> success(T data) {
        Result<T> result = new Result<>();
        result.setCode(200);
        result.setMsg("success");
        result.setData(data);
        result.setTimestamp(System.currentTimeMillis());
        return result;
    }

    public static <T> Result<T> fail(Integer code, String msg) {
        Result<T> result = new Result<>();
        result.setCode(code);
        result.setMsg(msg);
        result.setTimestamp(System.currentTimeMillis());
        return result;
    }
}
```

> **注意：`code: 200` 表示成功，字段名为 `msg`。**
''',
    '08-database.md': '''## 数据库规范

### SQL 编写
- 禁止 `SELECT *`，显式列出字段
- `IN` 查询参数不超过 1000 个
- 批量插入使用 `foreach`
- 分页查询必须带排序或索引字段

### 索引使用
- 单表索引不超过 7 个
- VARCHAR 超过 255 不能建索引（可用前缀索引）
- 外连接统一用 `LEFT JOIN`

### 禁止项
| 操作 | 禁止原因 | 正确做法 |
|------|---------|---------|
| `ALTER TABLE ... AFTER/FIRST` | 大表重建风险 | 直接 `ADD COLUMN` |
| `UPDATE/DELETE ... LIMIT` 无 `ORDER BY PK` | 非确定性更新 | 加 `ORDER BY id` |
| 关联子查询 | 性能差 | 拆为 JOIN 或代码处理 |
| procedure/function/trigger/views/event/外键 | 消耗数据库资源 | 程序端实现 |

### 禁止物理删除
- **禁止直接操作物理删除数据库记录**，统一使用逻辑删除
- 逻辑删除字段统一为 `delete_flag`（0-正常，1-已删除）

> **注意：以上规则仅对新开发代码生效，历史代码保持不动。**
''',
    '09-security.md': '''## 安全规范

### 1. 防止 SQL 注入
- 使用 MyBatis 参数绑定 `#{param}`
- 避免使用 `${param}` 拼接 SQL

### 2. 防止 XSS
- 输入参数进行转义
- 输出内容进行过滤

### 3. 敏感信息
```java
// 日志中脱敏处理
log.info("手机号: {}", DesensitizeUtils.maskPhone(phone));
// 输出: 手机号: 138****8888
```

### 4. 接口鉴权
```java
@PreAuthorize("hasAuthority('<模块>:<资源>:<操作>')")
@GetMapping("/{id}")
public Result<UserVo> getById(@PathVariable Long id) {
    // ...
}
```
''',
    '10-checklist.md': '''## 代码审查清单

- [ ] 命名是否符合规范
- [ ] 是否包含必要的注释
- [ ] 是否有空指针风险
- [ ] 是否有资源未关闭（流、连接等）
- [ ] SQL 是否有注入风险
- [ ] 日志是否使用占位符
- [ ] 异常是否被正确处理
- [ ] 魔法值是否提取为常量
- [ ] 重复代码是否抽取方法
- [ ] 单元测试是否通过
- [ ] 接口是否使用正确的 `/api/` 前缀
- [ ] 方法行数是否超过 80 行（建议抽子方法）
- [ ] 单行代码是否超过 120 字符
- [ ] 查询是否避免 `SELECT *` 和 `IN` 超过 1000
''',
}

# 创建子目录
for d in sub_dirs:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

# 创建顶层文件
for name, content in files.items():
    filepath = os.path.join(base_dir, name)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {filepath}')

# 创建 07-coding-standards 子文件
for name, content in coding_files.items():
    filepath = os.path.join(coding_standards_dir, name)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {filepath}')

print('Done!')
```

### 第三步：生成 `.trae/rules/` 规则文件（可选）

如项目使用支持规则文件自动加载的 IDE（如 Trae），在项目规则目录 `.trae/rules/` 下创建：

1. `<项目名>-shared-rules.md` — 项目共享规则（技术栈、编码规范摘要、工作流、禁止行为）
2. 如需项目专属 Trae 配置，可创建 `<项目名>-00-init.md`

参考模板见 `shared-memory-bank` Skill 中的「第三步：创建项目规则文件」。

### 第四步：更新全局记录

- 将新项目追加到 `memory-bank/README.md` 的项目速览表
- 如有跨项目关联，追加到 `shared/01-cross-project-map.md`

---

## 使用示例

**用户说**：
> "帮我初始化 demo 项目的记忆库"

**执行步骤**：
1. 确认项目信息（名称、路径、技术栈）
2. 执行上述 Python 脚本创建完整记忆库
3. 询问是否需要同时创建 `.trae/rules/` 规则文件（位于项目规则目录 `.trae/rules/`）
4. 询问是否需要扫描项目代码自动填充部分文档

---

## 注意事项

- 所有文件默认使用 UTF-8 编码
- `<项目名>`、`<项目中文全称>`、`<代码路径>`、`<技术栈>` 需替换为实际值
- `07-coding-standards/` 子文件内容为通用模板，项目特有规范后续补充到 `11-project-specific.md`
- 历史项目迁移时，保留原有 `07-coding-standards.md` 内容为索引文件，将各章节拆分到子目录
