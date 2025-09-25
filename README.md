# Python 后端冲刺营 - Week1 命令行通讯录

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-passed-4success)](https://github.com/pytest-dev/pytest)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 功能一览（终端即用）
| 命令 | 说明 |
| ---- | ---- |
| `contact add 张三 13900139000 zhang@qq.com` | 添加联系人 |
| `contact list` | 列出所有 |
| `contact find 13900139000` | 按手机号查找 |
| `contact remove 13900139000` | 删除联系人 |

## 一键安装 & 运行
```bash
# 克隆仓库
git clone https://github.com/CharlesAi478/python-week1.git
cd python-week1/contact-cli

# 创建虚拟环境并安装
python -m venv venv
.\venv\Scripts\activate   # mac/linux: source venv/bin/activate
pip install -e .
# 或直接运行
python -m contact_cli.main --help
