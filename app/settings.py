# -*- coding: utf-8 -*-
#
# 全局配置
# Author: caiyingyao
# Email: cyy0523xc@gmail.com
# Created Time: 2021-10-23

# 全局测试状态
DEBUG = False

# es相关配置
host = '192.168.1.240:56201'
index_name = 'xiaopeng_20211022'
count_url = "http://%s/%s/_count" % (host, index_name)
person_field = 'person_tag'   # 人工标注字段
machine_field = 'tag'         # 模型识别结果字段
text_field = 'text'           # 文本字段
