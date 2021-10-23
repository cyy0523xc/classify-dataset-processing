# -*- coding: utf-8 -*-
#
# 模块路由文件
# Author: caiyingyao
# Email: cyy0523xc@gmail.com
# Created Time: 2021-10-23
# from typing import Dict
import codecs
import pandas as pd
from fastapi import APIRouter, Form, UploadFile, File
# from fastapi import Depends, HTTPException
from schema import MessageResp     # 通用schema
from settings import person_field, machine_field

router = APIRouter(
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/", summary='模块测试API', response_model=MessageResp)
async def test_api():
    """模块测试API"""
    return {'message': 'ok'}


@router.post("/crosstab", summary='计算模型预测效果')
async def crosstab_api(
    file: UploadFile = File(..., title="上传的数据文件", description="需要上传的数据文件"),
    person_fieldname: str = Form(person_field, description="人工标注的字段名称"),
    machine_fieldname: str = Form(machine_field, description="机器预测标注的字段名称"),
) -> dict:
    """计算模型预测效果指标:\n
    1. 准确率\n
    2. 召回率
    """
    person_fieldname = person_fieldname.strip()
    machine_fieldname = machine_fieldname.strip()
    contents = await file.read()
    tmp_filename = '/tmp/classify-model.csv'
    with open(tmp_filename, 'wb') as f:
        f.write(contents)

    df = pd.read_csv(tmp_filename)
    # 计算机器预测的准确率
    data = pd.crosstab(df[person_fieldname], df[machine_fieldname])
    data = data.to_dict()
    metrics = {}
    for key, vals in data.items():
        true_count = vals[key] if key in vals else 0
        total = sum(vals.values())
        metrics[key] = {
            '准确率': true_count / total
        }

    # 计算召回率
    data = pd.crosstab(df[machine_fieldname], df[person_fieldname])
    data = data.to_dict()
    for key, vals in data.items():
        true_count = vals[key] if key in vals else 0
        total = sum(vals.values())
        if key not in metrics:
            metrics[key] = {
                '召回率': true_count / total
            }
        else:
            metrics[key]['召回率'] = true_count / total
    return metrics
