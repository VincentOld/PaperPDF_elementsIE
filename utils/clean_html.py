# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/13 1:29
@Auth ： vincent
@File ：clean_html.py
@IDE ：PyCharm
"""
from bs4 import BeautifulSoup
import re

#功能：清洗html，提取出文章正文
def clean_html(page_content):
    # 使用get_text()方法提取所有的文本
    raw_text = page_content.get_text()

    # 使用正则表达式去除特殊字符，只保留字母、数字、空格和换行符
    cleaned_text = re.sub(r'[^a-zA-Z0-9 \n]', '', raw_text)

    # 去除多余的空白（连续的空格将被替换为一个空格，连续的换行符将被替换为一个换行符）
    cleaned_text = re.sub(r' +', ' ', cleaned_text)
    cleaned_text = re.sub(r'\n+', '\n', cleaned_text)

    # 使用strip()方法去除字符串首尾的空白
    cleaned_text = cleaned_text.strip()

    return cleaned_text
