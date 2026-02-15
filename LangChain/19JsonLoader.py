# 用于将JSON数据加载为Document类型对象
from langchain_community.document_loaders import JSONLoader
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建CSV文件的绝对路径
csv_path = os.path.join(script_dir, "data", "stu.json")
loader = JSONLoader(
    file_path=csv_path,jq_schema=".",text_content=False,
    # json_lines=True  告知JSONLoader 这是一个JSON Lines文件
    )
documents = loader.load()
print(documents)
