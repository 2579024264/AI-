import os
from openai import OpenAI

# 1.获取client对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
# 2.调用模型
completion = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是一个AI助理，回答很简洁"},
        {"role": "user", "content": "小明有两只宠物狗"},
        {"role": "assistant", "content": "好的，我知道了，你要问什么？"},
        {"role": "user", "content": "小红油两只猫咪"},
        {"role": "assistant", "content": "好的，我知道了，你要问什么？"},
        {"role": "user", "content": "总共有几只宠物？"},
    ],
    stream=True # 开启流式返回
)
# 3.处理模型返回结果
for chunk in completion:
    print(chunk.choices[0].delta.content, 
    end="", # 每一段之间用空格分隔
    flush=True) # 立即刷新输出


# 现在是调用大模型的时候将历史消息存放在message的List内，组织历史消息提供给模型
# 当前历史消息是一次性的，如果是生产系统可以将历史消息保存到文件、数据库持久化工具内，需要的时候提取使用。