from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate,ChatPromptTemplate

template = PromptTemplate.from_template("你好，{name}")

res = template.format(name="张三")
print(res)


res2 = template.invoke(name="张三")
print(res2)