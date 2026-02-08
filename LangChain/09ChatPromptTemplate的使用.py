# ChatPromptTemplate支持注入任意数量的历史会话消息
#  历史会话消息并不是静态的，而是随着对话的进行不停地积攒，即动态的，所以，历史会话消息需要支持动态注入
from langchain_core.prompts import ChatPromptTemplate,MessagePlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
# 定义一个ChatPromptTemplate，它包含一个历史会话消息占位符
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的翻译"),
    MessagePlaceholder(variable_name="history"),
    ("human", "{input}"),
])

history_data = [
    ("human", "你好"),
    ("ai", "你好，我是一个专业的翻译"),
]

# 调用prompt.invoke方法，注入历史会话消息和用户输入
prompt_text = chat_prompt_template.invoke({"history": history_data, "input": "你好"})
print(prompt_text)

model = ChatTongyi(model="qwen3-max")
res = model.invoke(prompt_text)
print(res)
