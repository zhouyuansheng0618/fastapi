# -*- coding: utf-8 -*- 
# @Time : 2022/5/19 13:33 
# @Author : zhouys618@163.com 
# @File : main.py 
# @desc:
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.setting.config import settings
from app.api.v1.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)