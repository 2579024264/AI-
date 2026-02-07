from langchain_community.embeddings import DashScopeEmbeddings
from langchain_ollama import OllamaEmbeddings

# 创建模型对象 不传model默认用的是text-embedding-v1
embeddings = DashScopeEmbeddings()

# 不用invoke stream
# embed_query、embed_documents方法
query = "你好"
query_embedding = embeddings.embed_query(query)
print(query_embedding)

documents = ["你好", "你好吗"]
document_embeddings = embeddings.embed_documents(documents)
print(document_embeddings)



# model = OllamaEmbeddings(model="qwen3-embedding:4b")

# query = "你好"
# query_embedding = model.embed_query(query)
# print(query_embedding)

# documents = ["你好", "你好吗"]
# document_embeddings = model.embed_documents(documents)
# print(document_embeddings)