from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 得到模型对象,qwen3-max就是聊天模型
ChatModel = ChatTongyi(model="qwen3-max")

# 准备消息列表
messages = [
    SystemMessage(content="你是一个边塞诗人"),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="大漠孤烟直，长河落日圆。"),
    HumanMessage(content="按照你上一个回复的格式，再写一首唐诗"),

    # 以下是简写模式,跟上面的效果是一样的。且不需要导包，最重要的是支持变量的填充。可在运行时填充具体值。
    # ("system", "你是一个边塞诗人"),
    # ("human", "写一首唐诗"),
    # ("assistant", "大漠孤烟直，长河落日圆。"),
    # ("human", "按照你上一个回复的格式，再写一首唐诗"),
]


# 调用stream方法，流式输出
res = ChatModel.stream(input=messages)
# 处理模型返回结果,通过.content来获取内容
for chunk in res:
    print(chunk.content, end="", flush=True)


# 得到ollama模型对象
model = ChatOllama(model="qwen3:4b")

# 调用stream方法，流式输出
res = model.stream(input=messages)
# 处理模型返回结果,通过.content来获取内容
for chunk in res:
    print(chunk.content, end="", flush=True)
