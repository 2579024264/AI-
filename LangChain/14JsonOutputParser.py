from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

# 创建所需解析器
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

# 模型创建
model = ChatTongyi(model="qwen3-max")

# 第一个提示词模版
first_prompt = PromptTemplate.from_template("我邻居姓：{last_name}，刚生了：{gender},请起名，仅告知我名字无需其它内容。"
"并封装为JSON格式返回给我。要求key是name,value是你的名字，请严格遵守格式要求。")

# 第二个提示词模版
second_prompt = PromptTemplate.from_template("姓名:{name}，请帮我解析含义")

# 构建链
chain = first_prompt | model | json_parser | second_prompt | model | str_parser

res = chain.invoke({"last_name": "王", "gender": "男"})
print(res)
