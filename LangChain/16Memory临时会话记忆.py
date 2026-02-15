# 如果想要封装历史记录，除了自行维护历史消息外，也可以借助LangChain内置的历史记录附加功能
# LangChain提供了History功能，帮助模型在有历史记忆的情况下回答
# 基于RunnableWithMessageHistory在原有链的基础上创建带有历史记录功能的新链
# 基于InMemoryChatMessageHistory为历史记录提供内存存储
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory 

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个助手，需要根据会话历史回应用户问题。"),
    ("placeholder", "{chat_history}"),
    ("human", "{input}")
])
str_parser = StrOutputParser()

def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt
base_chain= prompt | print_prompt | model | str_parser

store = {}  # key就是session,value就是InMemoryChatMessageHistory类对象
# 实现通过会话id获取InMemoryChatMessageHistory类对象
def get_history(session_id: str):
   if session_id not in store:
       store[session_id] = InMemoryChatMessageHistory()
   return store[session_id]

# 基于RunnableWithMessageHistory在原有链的基础上创建带有历史记录功能的新链
conversation_chain = RunnableWithMessageHistory(
    base_chain,
    # 通过会话id获取InMemoryChatMessageHistory类对象
    get_history,
    # 用户输入在模版中的占位符
    input_message_key="input",
    # 历史消息在模版中的占位符
    history_message_key="chat_history",
)

if __name__ == "__main__":
    # 固定格式，添加LangChain的配置，为当前程序配置所属的session_id
    session_config = { 
        "configurable": {"session_id": "user_001"}
    }
    res = conversation_chain.invoke({"input": "小明有1只猫"}, session_config)
    print("第1次执行：",res)
    res = conversation_chain.invoke({"input": "小刚有2只狗"}, session_config)
    print("第2次执行：",res)
    res = conversation_chain.invoke({"input": "总共有几只宠物"}, session_config)
    print("第3次执行：",res)
