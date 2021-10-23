# -*- coding: utf-8 -*-
#
# 全局入口文件
# Author: caiyingyao
# Email: cyy0523xc@gmail.com
# Created Time: 2021-10-23
from fastapi import FastAPI
# from fastapi import Depends
# from fastapi.middleware.cors import CORSMiddleware

from settings import DEBUG
from utils import parse_readme
from schema import VersionResp

version = "0.5.0"     # 系统版本号
title, description = parse_readme()
app = FastAPI(
    debug=DEBUG,
    title=title,
    description=description,
    version=version,
    # dependencies=[Depends(get_query_token),
)

# 跨域问题
"""
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""

# redis连接
# from common.connections import init_redis
# init_redis('192.168.1.242')   # 配置redis host

from dataset_module.router import router as dataset_router
app.include_router(dataset_router, prefix="/dataset", tags=["数据集模块"])

from keyword_module.router import router as keyword_router
app.include_router(keyword_router, prefix="/keyword", tags=["关键词模块"])

from metrics_module.router import router as metrics_router
app.include_router(metrics_router, prefix="/metrics", tags=["评估模块"])


@app.get("/version", summary='获取系统版本号',
         response_model=VersionResp)
async def version_api():
    """获取系统版本号"""
    return {"version": version}
