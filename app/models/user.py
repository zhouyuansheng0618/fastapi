"""
!/usr/bin/env python
-*- coding: utf-8 -*-
author： zhouys
email： zhouys618@163.com
datetime： 2022/5/23 21:46 
ide： PyCharm
"""
from typing import Optional, Iterable,TYPE_CHECKING

from tortoise import models, BaseDBAsyncClient
from tortoise import fields


from app.utils.core import get_password_hash


class User(models.Model):
    username = fields.CharField(max_length=20, null=False, description="账号", unique=True)
    password = fields.CharField(max_length=128, null=False, description="密码")
    nickname = fields.CharField(max_length=20, null=True, description="昵称", default="你好")

    async def save(
        self,
        using_db: Optional[BaseDBAsyncClient] = None,
        update_fields: Optional[Iterable[str]] = None,
        force_create: bool = False,
        force_update: bool = False,
    ) -> None:
        if force_create or "password" in update_fields:
            self.password = get_password_hash(self.password)

        await super(User, self).save(using_db, update_fields, force_create, force_update)







