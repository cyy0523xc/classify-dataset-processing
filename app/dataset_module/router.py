# -*- coding: utf-8 -*-
#
# 模块路由文件
# Author: caiyingyao
# Email: cyy0523xc@gmail.com
# Created Time: 2021-10-23
# from typing import Dict
from fastapi import APIRouter
# from fastapi import Depends, HTTPException
from schema import MessageResp     # 通用schema

router = APIRouter(
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/", summary='模块测试API',
            response_model=MessageResp)
async def test_api():
    """模块测试API"""
    return {'message': 'ok'}


async def filter_api():
    """过滤目标数据集\n
    根据标签进行过滤
    """
    return {'message': 'ok'}
