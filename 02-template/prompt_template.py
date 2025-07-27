from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "给我讲一个关于{content}的{adjective}笑话"
)

result = prompt_template.format(adjective = "冷", content = "猴子")
print(result)