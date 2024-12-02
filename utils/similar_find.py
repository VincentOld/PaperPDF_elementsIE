# -*- coding: utf-8 -*-
"""
@Time ： 2023/7/13 0:08
@Auth ： vincent
@File ：similar_find.py
@IDE ：PyCharm
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

#功能：找到字典中与reference_array最相似的键值对
def find_most_similar_key_value(A):
    B = ["abstract", 'Introduction', "method", 'Approach', 'Conclusion', 'Experiments', 'Results', 'Discussion',
         'Related Work', 'Conclusion', 'Acknowledgements', 'References']
    max_ratio = 0
    max_key = None
    max_value = None
    B_str = ' '.join(B)
    for key, values in A.items():
        values_str = ' '.join(values)
        ratio = difflib.SequenceMatcher(None, values_str, B_str).ratio()
        if ratio > max_ratio:
            max_ratio = ratio
            max_key = key
            max_value = values
    return max_key, max_value


#todo 风险点：可能全都不相似
#功能：找到数组A中与arrayB最相似的元素
def find_similar_element(arrayA):
    if arrayA is None:
        return
    arrayB = ["abstract", 'Introduction', "method", 'Approach', 'Conclusion', 'Experiments', 'Results', 'Discussion',
              'Related Work', 'Conclusion', 'Acknowledgements', 'References']
    # 创建TF-IDF向量化器
    vectorizer = TfidfVectorizer()

    arrayB_vector = vectorizer.fit_transform(arrayB)

    for i, elementA in enumerate(arrayA):
        elementA_text = str(elementA)
        # 计算当前元素与arrayB的相似度
        elementA_vector = vectorizer.transform([elementA_text])
        # 计算当前元素与arrayB的余弦相似度
        similarity = cosine_similarity(elementA_vector, arrayB_vector)
        # 检查相似度是否大于阈值（这里设定为0.5）
        if similarity.max() > 0.5:
            arrayC = arrayA[i:]
            author = " ".join(arrayA[:i])
            return arrayC, author
    # 如果没有找到相似元素，返回空数组和空字符串
    return [], ""
