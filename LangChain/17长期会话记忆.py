# 使用InMemoryChatMessageHistory仅可以在内存中临时存储会话记忆，一旦程序退出，则记忆丢失
# InMemoryChatMessageHistory类继承自BaseChatMessageHistory类

import os,json
from typing import Sequence
from langchain_core.messages import message_to_dict,messages_from_dict,BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
# message_to_dict:将消息对象转换为字典
# messages_from_dict:[字典、字典...]->[消息、消息...]
# AIMessage、HumanMessage、SystemMessage 都是BaseMessage的子类

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id:str,storage_path:str):
        self.session_id = session_id   # 会话id
        self.storage_path = storage_path # 不同会话id的存储文件，所在的文件夹路径
        # 完整的文件路径
        self.file_path = os.path.join(self.storage_path,self.session_id)
        # 确保文件夹的存在的
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        # Sequence序列 类似list、tuple
        all_messages = list(self.messages)
        all_messages.extend(messages)

        # 将数据同步写入到本地文件中
        # 类对象写入文件 -> 一堆二进制
        # 为了方便，可以讲BaseMessage消息转为字典，再写入文件
        # 官方提供的message_to_dict:单个消息对象（BaseMessage类实例）-> 字典
        with open(self.file_path,"w",encoding="utf-8") as f :
            json.dump([message_to_dict(msg) for msg in all_messages],f,ensure_ascii=False,indent=2)
    @property
    def messages(self) -> list[BaseMessage]:
        try:
            # 从文件中读取数据
            with open(self.file_path,"r",encoding="utf-8") as f :
                data = json.load(f)
                 # 从字典转换为消息对象
                return messages_from_dict(data)
        except FileNotFoundError:
            # 如果文件不存在，返回空列表
            return []
    def clear(self) -> None:
        with open(self.file_path,"w",encoding="utf-8") as f :
            json.dump([],f,ensure_ascii=False,indent=2)


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

# 实现通过会话id获取FileChatMessageHistory类对象
def get_history(session_id: str):
     return FileChatMessageHistory(session_id=session_id,storage_path="./chat_history")
# 基于RunnableWithMessageHistory在原有链的基础上创建带有历史记录功能的新链
conversation_chain = RunnableWithMessageHistory(
    base_chain,
    # 通过会话id获取FileChatMessageHistory类对象
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
    # res = conversation_chain.invoke({"input": "小明有1只猫"}, session_config)
    # print("第1次执行：",res)
    # res = conversation_chain.invoke({"input": "小刚有2只狗"}, session_config)
    # print("第2次执行：",res)
    res = conversation_chain.invoke({"input": "总共有几只宠物"}, session_config)
    print("第3次执行：",res)
