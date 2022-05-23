"""
!/usr/bin/env python
-*- coding: utf-8 -*-
author： zhouys
email： zhouys618@163.com
datetime： 2022/5/19 22:08 
ide： PyCharm
"""
from  fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from .v1 import v1
from app.utils.core import settings
app = FastAPI(title=settings.TITLE, description=settings.DESC)


app.include_router(v1, prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


register_tortoise(
    app,
    db_url="sqlite://watch.sqlite",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
# from fastapi import FastAPI
# from app.api import v1
#
#
# def creat_app():
#     app = FastAPI(
#         title="fastapi",
#         description="http地址",
#         version="v0.1",
#         docs_url="/api/v1/docs",  # 自定义文档地址
#         openapi_url="/api/v1/openapi.json",
#         redoc_url=None  # 禁用redoc文档
#     )
#     # 导入路由, 前缀设置
#     app.include_router(
#         v1,
#         prefix="/api/v1/mall",
#     )
#
#     # 异常捕获
#     register_exception(app)
#
#     # 跨域设置
#     register_cors(app)
#
#     return app