from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi
example_template = PromptTemplate.from_template("单词{word},反义词{antonym}")

# 示例的动态数据注入，要求是list内部套字典
examples = [
    {"word": "大", "antonym": "小"},
    {"word": "上", "antonym": "下"},
]
prefix = "请根据以下单词的反义词，按照如下示例"
suffix = "基于前面的示例告知我，{input_word}的反义词是"
few_shot_prompt_template = FewShotPromptTemplate(
    example_prompt= example_template, # 示例数据的模版
    examples= examples, # 示例数据
    prefix= prefix, # 示例之前的前缀
    suffix= suffix, # 示例之后的后缀
    input_variables=["input_word"], # 声明在前缀或后缀中所需注入的变量名
)
prompt_text = few_shot_prompt_template.invoke(input={"input_word": "好"})
print(prompt_text)
model = Tongyi(model="qwen-max")
res = model.invoke(input=prompt_text)
print(res)
