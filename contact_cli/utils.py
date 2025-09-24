"""校验工具：手机号 & 邮箱正则"""

import re

def validate_phone(phone: str) -> bool:
    """返回 True 表示合法手机号"""
    return re.fullmatch(r"1[3-9]\d{9}", phone) is not None

def validate_email(email: str) -> bool:
    """简单邮箱正则"""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.fullmatch(pattern, email) is not None