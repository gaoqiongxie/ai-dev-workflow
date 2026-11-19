"""共享记忆库写入脚本（模板）：把一段 Markdown 内容写入指定记忆库文件。
用法（直接复制/引用本脚本执行）：
  python write_memory_template.py --target="memory-bank/<项目>/99-dialogue-logs/YYYY-MM-DD_主题.md" --content-file="ai-temp/mem_content.md"
  --target=          目标文件路径（缺省打印默认提示路径）
  --content-file=     内容来源 .md 文件（缺省写入内置占位模板）
说明：
- 记忆库根目录（如 memory-bank/）可能位于 IDE 工作目录外，Write 工具不可直写，必须经本脚本中转
- 写入前检查目标目录存在，缺失则创建
- 写入后打印大小供校验；执行方式遵循 shared-memory-bank SKILL.md（临时内容文件用完删除，本模板常驻 skill 目录）
"""
import os
import sys


def resolve_target() -> str:
    """目标路径：优先 --target= 参数，否则取默认共享对话日志（按当日日期）"""
    for arg in sys.argv[1:]:
        if arg.startswith('--target='):
            return arg[len('--target='):]
    # 默认：shared/99-dialogue-logs/YYYY-MM-DD_主题.md（执行前请改成实际路径）
    import datetime
    default = os.path.join(
        'memory-bank', 'shared', '99-dialogue-logs',
        f"{datetime.date.today().isoformat()}_template.md")
    print(f'[默认目标] 未提供 --target=，将写入：{default}')
    print('            请在本模板处将默认路径改为真实目标路径后再执行。')
    return default


def read_content() -> str:
    """内容来源：优先 --content-file= 指定的 .md 文件，否则读取模板备份内容"""
    for arg in sys.argv[1:]:
        if arg.startswith('--content-file='):
            f = arg[len('--content-file='):]
            with open(f, encoding='utf-8') as fh:
                return fh.read()
    # 占位模板：执行前将在这里替换为真实 Markdown 内容（或用 --content-file= 指向内容文件）
    return '''# 标题

> 日期: {date}
> 项目: <项目名>

## 结论

...

## 证据链

...

## 待办

- [ ] ...
'''


def main():
    path = resolve_target()
    content = read_content()
    # content 中的占位日期做一次替换（若有）
    import datetime
    content = content.replace('{date}', datetime.date.today().isoformat())

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written to {path}, size={os.path.getsize(path)} bytes')


if __name__ == '__main__':
    main()