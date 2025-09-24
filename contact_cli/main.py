"""命令行入口：argparse 解析 → 调用核心 → 终端打印"""

import argparse
from pathlib import Path
from contact_cli.core import Contact, ContactBook
from contact_cli.utils import validate_phone, validate_email


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="contact", description="命令行通讯录")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # 1. 添加子命令
    p_add = sub.add_parser("add", help="添加联系人")
    p_add.add_argument("name", help="姓名")
    p_add.add_argument("phone", help="手机号")
    p_add.add_argument("email", help="邮箱")

    # 2. 删除子命令
    p_del = sub.add_parser("remove", help="删除联系人")
    p_del.add_argument("phone", help="手机号")

    # 3. 查找子命令
    p_find = sub.add_parser("find", help="查找联系人")
    p_find.add_argument("phone", help="手机号")

    # 4. 列表子命令
    sub.add_parser("list", help="列出所有联系人")

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    book = ContactBook()  # 自动加载 contacts.json

    if args.cmd == "add":
        if not validate_phone(args.phone):
            print("❌ 手机号格式错误")
            return
        if not validate_email(args.email):
            print("❌ 邮箱格式错误")
            return
        ok = book.add(Contact(args.name, args.phone, args.email))
        print("✅ 添加成功！" if ok else "⚠️  手机号已存在")

    elif args.cmd == "remove":
        ok = book.remove(args.phone)
        print("✅ 删除成功！" if ok else "⚠️  未找到该手机号")

    elif args.cmd == "find":
        c = book.find(args.phone)
        if c:
            print(f"{c.name}\t{c.phone}\t{c.email}")
        else:
            print("⚠️  未找到")

    elif args.cmd == "list":
        if not book.list_all():
            print("（通讯录为空）")
        for c in book.list_all():
            print(f"{c.name}\t{c.phone}\t{c.email}")


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(line_buffering=True)   # 强制实时刷新
    main()