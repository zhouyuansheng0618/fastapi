"""
!/usr/bin/env python
-*- coding: utf-8 -*-
author： zhouys
email： zhouys618@163.com
datetime： 2022/5/23 22:25 
ide： PyCharm
"""
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
import os

class Settings(BaseSettings):
    # 开发模式配置
    DEBUG: bool = True
    # 项目文档
    TITLE: str = "FastAPI+MySQL项目生成"
    DESCRIPTION: str = "更多FastAPI知识，请关注我的个人网站 https://www.charmcode.cn/"
    # 文档地址 默认为docs 生产环境关闭 None
    DOCS_URL: str = "/api/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/api/redoc"
    # token过期时间 分钟
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # # 生成token的加密算法
    # ALGORITHM: str = "HS256"

    # 生产环境保管好 SECRET_KEY
    # SECRET_KEY: str = 'xxxxxxxx'

    # 项目根路径
    BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = "fastapi"
    MYSQL_PASSWORD: str = "FastApi_test"
    MYSQL_HOST: str = "rm-uf6z20c639x3cwczwwo.mysql.rds.aliyuncs.com"
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = 'fastapi_db'
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost", "http://localhost:4200", "http://localhost:3000",
                                              "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str
    SENTRY_DSN: Optional[HttpUrl] = None

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if len(v) == 0:
            return None
        return v


    class Config:
        case_sensitive = True


settings = Settings()
