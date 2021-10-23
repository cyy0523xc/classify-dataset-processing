# -*- coding: utf-8 -*-
#
# 工具库
# Author: caiyingyao
# Email: cyy0523xc@gmail.com
# Created Time: 2021-10-23
from settings import text_field


def get_count_query(terms_query: dict = None, string_query: dict = None) -> dict:
    query_dsl = {
        "query": {
            "bool": {
                "must": [
                ]
            }
        }
    }
    if terms_query:
        query_dsl['query']['bool']['must'].append(terms_query)
    if string_query:
        query_dsl['query']['bool']['must'].append(string_query)
    return query_dsl


def get_terms_query(tag_field: str, values: list) -> dict:
    return {
        "terms": {
            tag_field: values
        }
    }


def get_string_query(string: str) -> dict:
    return {
        "query_string": {
            "query": "\"%s\"" % string,
            "default_field": text_field
        }
    }


def parse_readme(filename: str = 'readme.md'):
    """解释readme文件
    :param filename str: md文件名
    :return title str: 标题
    :return text  str: 文档内容
    """
    with open(filename, encoding='utf8') as r:
        text = r.readlines()
    title = text[0].strip('# \n').strip()
    text = ''.join(text[1:]).strip()
    return title, text
