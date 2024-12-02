# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/13 1:09
@Auth ： vincent
@File ：extract_between_elements.py
@IDE ：PyCharm
"""
from bs4 import BeautifulSoup

#功能：提取html中elements之间的内容
def extract_between_elements(page_content, elements):
    contents = {}
    text = page_content.get_text()
    for i in range(len(elements)-1):
        start = text.find(elements[i])
        end = text.find(elements[i+1])
        if start != -1 and end != -1:
            contents[elements[i]] = text[start+len(elements[i]):end].strip()
    return contents