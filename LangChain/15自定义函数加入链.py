# 想要完成这个功能，可以基于RunnableLambda类实现
# RunnableLamdba类是LangChain内置的，将普通函数等转换为Runnable接口实例，方便自定义函数加入chain.
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda

str_parser = StrOutputParser()

model = ChatTongyi(model="qwen3-max")

first_prompt = PromptTemplate.from_template("我邻居姓：{last_name}，刚生了：{gender},请起名，仅告知我名字无需其它内容.")

second_prompt = PromptTemplate.from_template("姓名:{name}，请帮我解析含义")

# 函数的入参： AIMessage -> dict ("name": "xxx")
my_func = RunnableLambda(lambda ai_message: {"name": ai_message.content})

chain = first_prompt | model | my_func | second_prompt | model | str_parser

for chunk in chain.stream({"last_name": "曹", "gender": "女"}):
    print(chunk, end="", flush=True)
