"""
!/usr/bin/env python
-*- coding: utf-8 -*-
author： zhouys
email： zhouys618@163.com
datetime： 2022/5/19 22:21 
ide： PyCharm

"""
from fastapi import APIRouter

from app.api.v1.endpoints import user

api_router = APIRouter()
api_router.include_router(user.router, tags=["user"])
