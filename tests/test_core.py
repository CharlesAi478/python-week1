"""pytest 单元测试：核心逻辑 & 工具函数"""

import pytest
from contact_cli.core import Contact, ContactBook
from contact_cli.utils import validate_phone


@pytest.fixture
def book(tmp_path):
    """每个测试用例独享临时 json 文件"""
    return ContactBook(json_path=tmp_path / "test.json")


def test_add_contact(book):
    book.add(Contact("Tom", "13800138000", "tom@qq.com"))
    assert len(book.list_all()) == 1


def test_duplicate_phone(book):
    c = Contact("Tom", "13800138000", "tom@qq.com")
    book.add(c)
    assert book.add(c) is False  # 重复添加应失败


def test_remove(book):
    book.add(Contact("Tom", "13800138000", "tom@qq.com"))
    assert book.remove("13800138000") is True
    assert len(book.list_all()) == 0


def test_validate_phone():
    assert validate_phone("13800138000") is True
    assert validate_phone("123") is False