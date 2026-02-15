# 想要以第一次模型的输出结果，第二次去询问模型 
# prompt的结果是PromptValue类型，输入给了model,model的输出结果是AIMessage
# 模型源码中关于invoke方法明确指定了input的类型：PromptValue | str |Sequence[MessageLikeRepresentation]
#  模型输出：AIMessage 提示词模版输入：要求是字典 提示词模版输出：PromptValue对象  
# StrOutputParser:AIMessage -> str
# JsonOutputParser:AIMessage -> dict
# 需要做类型转换：借助LangChain内置的解析器 StrOutputParser字符串输出解析器

from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template("我邻居姓：{last_name}，刚生了：{gender},请起名，仅告知我名字无需其它内容。")

chain = prompt | model |  parser | model
res = chain.invoke({"last_name": "王", "gender": "男"})

print(res.content);