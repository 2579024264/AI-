from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个边塞诗人，可以作诗"),
    MessagePlaceholder(variable_name="history"),
    ("human", "请再来一首唐诗"),
])

history_data = [
    ("human", "你来写一首唐诗"),
    ("ai", "窗前明月光，疑是地上霜。"),
    ("human", "请再写一首"),
    ("ai", "锄禾日当午，汗滴禾下土。"),
]

model = ChatTongyi(model="qwen3-max")

# 组成链，要求每一个组件都是Runnable接口的子类
chain = chat_prompt_template | model
# 通过链调用invoke或stream
res = chain.invoke({"history": history_data})
print(res.content)
# 通过stream流式输出
stream_res = chain.stream({"history": history_data})
for chunk in stream_res:
    print(chunk.content, end="", flush=True)
