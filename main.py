# -*- coding: utf-8 -*- 
# @Time : 2022/5/19 13:33 
# @Author : zhouys618@163.com 
# @File : main.py 
# @desc:
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/hello/{name}")
async def say_hello111(name: str):
    return {"message": f"Hello {name}"}
