"""
!/usr/bin/env python
-*- coding: utf-8 -*-
author： zhouys
email： zhouys618@163.com
datetime： 2022/5/23 22:36 
ide： PyCharm
"""
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()