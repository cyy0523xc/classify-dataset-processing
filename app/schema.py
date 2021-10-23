# -*- coding: utf-8 -*-
#
# 通用schema
# Author: caiyingyao
# Email: cyy0523xc@gmail.com
# Created Time: 2021-10-23
from pydantic import BaseModel, Field


class MessageResp(BaseModel):
    message: str = Field(..., title='提示信息', description='提示信息')


class VersionResp(BaseModel):
    version: str = Field(..., title='版本信息', description='版本信息')
