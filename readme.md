# PDF结构化解析工具

## 项目简介

本项目是一个强大的PDF解析工具，能够自动提取PDF文档的结构化内容，包括全文、标题、作者、摘要、引用、关键词、正文和参考文献等关键信息。

## 核心原理

本项目通过以下关键技术实现PDF文档结构化解析：

### 1. 多维特征提取

- **字体大小分析**：通过`extract_font_sizes_and_text()`函数提取PDF中不同字体大小的文本
- **基于字体出现频率的结构识别**：使用`Counter`统计字体大小出现次数，过滤出可能代表文档结构的字体

### 2. 相似度匹配算法

- **文本相似度计算**：使用`TF-IDF`和余弦相似度算法识别文档关键区域
- **difflib文本相似度**：通过`SequenceMatcher`匹配文档结构关键词

### 3. 内容提取策略

- **HTML解析**：利用BeautifulSoup解析PDF转换的HTML
- **区间提取**：通过`extract_between_elements()`函数提取文档不同区块的内容

### 4. 智能文本处理

- **文本清洗**：使用正则表达式去除特殊字符
- **空白规范化**：统一处理空格和换行符

## 功能特点

- 🔍 自动识别PDF文档的结构化内容
- 📄 提取文档的关键元素（标题、作者、摘要等）
- 🧩 支持复杂PDF文档的解析
- 🚀 解析速度快，单个PDF约5秒完成

## 技术栈

- Python 3.x
- BeautifulSoup
- langchain
- scikit-learn

## 依赖安装

```bash
pip install beautifulsoup4
pip install langchain
pip install scikit-learn
```

## 使用方法

```python
from pdf_structor import process_pdf

# 指定PDF文件路径
file_path = "your_pdf_file.pdf"

# 解析PDF
result = process_pdf(file_path)

# 打印解析结果
print(result)
```

## 模块说明

### 主要模块

1. `pdf_structor.py`: 核心解析逻辑
2. `clean_html.py`: HTML清洗模块
3. `extract_between_elements.py`: 内容提取模块
4. `similar_find.py`: 相似度匹配模块

### 解析流程

1. 使用PDFMinerPDFasHTMLLoader加载PDF
2. 提取文档元数据和正文
3. 分析字体大小和文本内容
4. 识别文档结构
5. 提取关键信息

## 注意事项

- 对于字体不规范的PDF可能存在解析准确性限制
- 建议处理学术论文和结构相对规范的文档

## 潜在风险

- 字体大小判断存在一定局限性
- 可能无法完美处理所有PDF文档格式

## 作者

Vincent - 初始版本开发

## 版本历史

- v1.0.0 初始发布
