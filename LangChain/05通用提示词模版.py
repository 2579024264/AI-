from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
# zero-shot思想下使用PromptTemplate
prompt_template = PromptTemplate.from_template("我的领居姓{last_name}，名字叫{first_name}")
model = Tongyi(model="qwen-max")

# 调用format来注入信息
# prompt_text=prompt_template.format(last_name="王", first_name="小明")
# res = model.invoke(input=prompt_text)
# print(res)


# 链的方式
chain = prompt_template | model
res = chain.invoke(input={"last_name": "王", "first_name": "小明"})
print(res)