"""
!/usr/bin/env python
-*- coding: utf-8 -*-
author： zhouys
email： zhouys618@163.com
datetime： 2022/5/19 22:21 
ide： PyCharm

"""

from fastapi import APIRouter

from .endpoints import *

v1 = APIRouter(prefix="/v1")
v1.include_router(user)
