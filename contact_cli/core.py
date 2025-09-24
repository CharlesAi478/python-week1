"""业务核心：Contact 数据对象 + ContactBook 增删查改 + 本地 JSON 持久化"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List, Optional


class Contact:
    """值对象：单条联系人"""
    def __init__(self, name: str, phone: str, email: str):
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip()

    def to_dict(self) -> Dict[str, str]:
        return {"name": self.name, "phone": self.phone, "email": self.email}


class ContactBook:
    """实体：通讯录本体（增删查改 + 自动落盘）"""
    def __init__(self, json_path: Path = Path("contacts.json")) -> None:
        self.json_path = json_path
        self.contacts: List[Contact] = []
        self._load()          # 启动时自动读档

    def _load(self) -> None:
        """私有方法：从 JSON 载入内存"""
        if self.json_path.exists():
            with self.json_path.open("r", encoding="utf-8") as f:
                data: List[Dict[str, str]] = json.load(f)
                self.contacts = [Contact(**item) for item in data]

    def _save(self) -> None:
        """私有方法：内存写入 JSON（覆盖写）"""
        with self.json_path.open("w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contacts], f, ensure_ascii=False, indent=2)

    # === 下面四个方法是外部唯一入口 ===
    def add(self, contact: Contact) -> bool:
        """添加成功返回 True；手机号重复返回 False"""
        if any(c.phone == contact.phone for c in self.contacts):
            return False
        self.contacts.append(contact)
        self._save()
        return True

    def remove(self, phone: str) -> bool:
        """根据手机号删除；成功返回 True"""
        for idx, c in enumerate(self.contacts):
            if c.phone == phone:
                del self.contacts[idx]
                self._save()
                return True
        return False

    def find(self, phone: str) -> Optional[Contact]:
        """查找单条联系人"""
        return next((c for c in self.contacts if c.phone == phone), None)

    def list_all(self) -> List[Contact]:
        """返回全部联系人（内存列表）"""
        return self.contacts