from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是世界级的技术专家"),
    ("user", "{input}")
])

output_parse = StrOutputParser()

chain = prompt | llm | output_parse

result = chain.invoke({"input": "帮我写一篇关于AI的技术文章，100个字"})
print(result)