# -*- coding: utf-8 -*-
#
# 关键词相关函数
# Author: caiyingyao
# Email: cyy0523xc@gmail.com
# Created Time: 2021-10-23
import requests
from typing import List, Tuple
# import numpy as np
# import pandas as pd
from settings import count_url, person_field, machine_field
from utils import get_string_query, get_terms_query, init_query, add_child_query


def check_keyword(keyword: str, person_tags: List[str], machine_tags: List[str]) -> Tuple[int, int]:
    string_query = get_string_query(keyword)
    terms_query = get_terms_query(person_field, person_tags)
    query = init_query()
    query = add_child_query(query, terms_query)
    query = add_child_query(query, string_query)
    resp = requests.get(count_url, json=query).json()
    person_count = resp['count']

    # 机器识别结果
    terms_query = get_terms_query(machine_field, machine_tags)
    query = init_query()
    query = add_child_query(query, terms_query)
    query = add_child_query(query, string_query)
    resp = requests.get(count_url, json=query).json()
    machine_count = resp['count']
    return person_count, machine_count


def check_keyword_and(keyword: str, person_tags: List[str], machine_tags: List[str]) -> int:
    string_query = get_string_query(keyword)
    person_terms = get_terms_query(person_field, person_tags)
    machine_terms = get_terms_query(machine_field, machine_tags)
    query = init_query()
    query = add_child_query(query, person_terms)
    query = add_child_query(query, machine_terms)
    query = add_child_query(query, string_query)
    resp = requests.get(count_url, json=query).json()
    return resp['count']
