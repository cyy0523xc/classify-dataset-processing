# -*- coding: utf-8 -*-
#
# 模块路由文件
# Author: caiyingyao
# Email: cyy0523xc@gmail.com
# Created Time: 2021-10-23
# from typing import Dict
# from typing import Optional
from fastapi import APIRouter, Form
# from fastapi import Depends, HTTPException
from .keywords import check_keyword

router = APIRouter(
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.post("/analyse", summary='验证关键词的区分效果')   # , response_model=MessageResp)
async def analyse_api(
    keyword: str = Form(..., description='需要验证的关键词'),
    person_tags: str = Form(..., description='人工标注的标签，使用逗号进行分隔'),
    machine_tags: str = Form(..., description='机器识别标注的标签，使用逗号进行分隔'),
):
    """验证关键词的区分效果
    """
    keyword = keyword.strip()
    person_tags = person_tags.replace('，', ',')
    machine_tags = machine_tags.replace('，', ',')
    person_tags = [tag.strip() for tag in person_tags.split(',')]
    machine_tags = [tag.strip() for tag in machine_tags.split(',')]
    person_count, machine_count = check_keyword(keyword, person_tags, machine_tags)
    return {
        "person_count": person_count,
        "machine_count": machine_count,
    }
