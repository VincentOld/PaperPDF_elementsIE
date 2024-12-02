# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/12 22:28
@Auth ： vincent
@File ：pdf_structor.py
@IDE ：PyCharm
"""
from collections import Counter
from pprint import pprint

from bs4 import BeautifulSoup
from langchain.document_loaders import PDFMinerPDFasHTMLLoader
import re
from utils.similar_find import find_similar_element, find_most_similar_key_value
from utils.extract_between_elements import extract_between_elements
from utils.clean_html import clean_html
#功能：输入pdf，输出pdf的结构化数据包含全文、标题、作者、摘要、引用、关键词、正文、参考文献等
# 风险点1：默认标题的字体是特别的，如字号偏大等，且同一级的标题字号大小相同。但是有些文章的标题字号和正文字号是一样的，这样就会出现问题
# 风险点2：字体出现次数范围5-50不一定合理
#解析一个pdf大概五秒左右。

def process_pdf(file_path):
    global structured_contents
    try:
        # 解析为html
        loader = PDFMinerPDFasHTMLLoader(file_path)
        data = loader.load()[0]

        # 提取出文章正文，html格式
        page_content = BeautifulSoup(data.page_content, 'html.parser')
        # 提取出文章元数据
        page_metadata = data.metadata
        #提取出文章正文
        full_text = clean_html(page_content)

        # 提取出文章正文中的字体大小和文本内容
        fonts, text_by_font_size = extract_font_sizes_and_text(page_content)
        # 统计每个字体大小的个数
        counter = Counter(fonts)
        # print(counter)
        # 过滤掉字体大小小于3或者大于40的字体，以及字体大小小于7的字体
        #todo风险点，字体出现次数范围5-50不一定合理
        filtered_counter = {key: value for key, value in counter.items() if 5 <= value <= 50 and int(key[:-2]) >= 3}
        # print(filtered_counter)
        # Extract texts for filtered fonts
        font_texts_dict = {key: text_by_font_size[key] for key in filtered_counter.keys()}
        # 查找相似度最高的键和值
        most_similar_key, most_similar_value = find_most_similar_key_value(font_texts_dict)
        # print(most_similar_key, most_similar_value)
        most_similar_value,author = find_similar_element(most_similar_value)
        structured_contents = extract_between_elements(page_content,most_similar_value)
        structured_contents['author'] = author
        structured_contents['source'] = page_metadata['source']
        structured_contents['full_text'] = full_text
        structured_contents = {key: re.sub(r'\s+', ' ', value).strip() for key, value in structured_contents.items()}
        return structured_contents
    except Exception as e:
        structured_contents = {}
        print("An error occurred:", str(e))
        # 解析为html
        loader = PDFMinerPDFasHTMLLoader(file_path)
        data = loader.load()[0]

        # 提取出文章正文，html格式
        page_content = BeautifulSoup(data.page_content, 'html.parser')
        # 提取出文章元数据
        page_metadata = data.metadata
        # 提取出文章正文
        full_text = clean_html(page_content)
        structured_contents['full_text'] = full_text
        structured_contents['source'] = page_metadata['source']
        return structured_contents

#功能：
def extract_font_sizes_and_text(page_content):
    font_sizes = []
    text_values = []

    # 找到所有带有font-size属性的元素
    tags_with_font_size = page_content.select('[style*="font-size"]')

    # 遍历每个元素，提取font-size的值和文本内容
    for tag in tags_with_font_size:
        style = tag['style']
        styles = style.split(';')
        for style in styles:
            if 'font-size' in style:
                font_size = style.split(':')[1].strip()
                font_sizes.append(font_size)
                text = tag.get_text().strip()
                text_values.append(text)

    text_by_font_size = {}

    for font_size, text in zip(font_sizes, text_values):
        if font_size not in text_by_font_size:
            text_by_font_size[font_size] = []
        text_by_font_size[font_size].append(text)

    return font_sizes, text_by_font_size

if __name__ == '__main__':
    #在这里修改文件路径即可
    file_path = r"H:\desktop_moved\论文中期报告\paperGenerationGPT\Arxiv\AI-PDF\Towards Minimal Supervision BERTbased Grammar Error Correction.pdf"
    result = process_pdf(file_path)
    pprint(result)









