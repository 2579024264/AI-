# RecursiveCharacterTextSplitter 递归字符文本分割器，主要用于按自然段落分割大文档
from langchain_community.document_loaders import TextLoader
from langchain_community.text_splitter import RecursiveCharacterTextSplitter
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建CSV文件的绝对路径
csv_path = os.path.join(script_dir, "data", "stu.txt")
loader = TextLoader(file_path=csv_path,encoding="utf-8")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # 分段的最大字符数
    chunk_overlap=50, # 分段之间允许重叠的字符数
    # 文本分段依据
    separators=["\n\n", "\n", "。", "！", "？", "，", "、", " "],
    # 字符统计依据（函数）
    length_function=len,
)
split_docs = splitter.split_documents(documents)
print(split_docs)
