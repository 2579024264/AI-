# langchain_community
from langchain_community.llms.tongyi import Tongyi
# langchain_ollama
from langchain_ollama import OllamaLLM

# qwen-max大语言模型
model = Tongyi(model="qwen-max")

# 调用stream向模型提问，流式输出
res = model.stream(input="你是谁呀，能做什么？")
for chunk in res:
    print(chunk, end="", flush=True)




# 调用ollama模型
ollama_model = OllamaLLM(model="qwen3:4b")

# 调用ollama模型向模型提问
ollama_res = ollama_model.invoke(input="你是谁呀，能做什么？")
print(ollama_res)

