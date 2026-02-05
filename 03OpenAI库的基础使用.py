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
        {"role": "system", "content": "你是一个Python编程工程师，并且话不多"},
        {"role": "assistant", "content": "好的，我是一个Python编程工程师，并且话不多，你要问什么？"},
        {"role": "user", "content": "输出1-10的数字，用Python代码"},
    ],
    stream=True # 开启流式返回
)
# 3.处理模型返回结果
for chunk in completion:
    print(chunk.choices[0].delta.content, 
    end="", # 每一段之间用空格分隔
    flush=True) # 立即刷新输出