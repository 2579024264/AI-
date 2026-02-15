# 文档加载器提供了一套标准的接口，用于将不同来源（如CSV、PDF、DOCX等）的数据读取为LangChain的文档格式。这确保了无论数据来源如何，都能对其进行一致性处理。
# 文档加载器（内置或自行实现）需实现BaseLoader接口

# Class Document,是LangChain内文档的统一载体，所有文档加载器最终返回此类的实例
# 不同的文档加载器可能定义了不同的参数，但是其都实现了统一的接口
    # - load()方法：负责从指定数据源加载文档内容。
    # - lazy_load()方法：延迟流式传输文档，对大型数据集很有用，避免内存溢出

from langchain_community.document_loaders import CSVLoader
import os

# 获取当前脚本所在目录的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建CSV文件的绝对路径
csv_path = os.path.join(script_dir, "data", "stu.csv")
loader = CSVLoader(file_path=csv_path,encoding="utf-8")

# 批量加载 .load -> [Document,Document,...]
# documents = loader.load()
# print(documents)

# 懒加载 .lazy_load() -> 迭代器 [Document]
for document in loader.lazy_load():
    print(document)
