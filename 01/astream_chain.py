import os

from langchain_openai import ChatOpenAI
# 为了支持异步调用
import asyncio
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("给我讲一个{topic}的笑话")
model = ChatOpenAI(
    api_key=os.getenv("API-KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus"  # 模型名称可按需更换
)

parser = StrOutputParser()
chain = prompt | model | parser

async def async_stream():
    async for chunk in chain.astream({"topic": "鹦鹉"}):
        print(chunk, end="|", flush=True)


# 运行异步流处理
asyncio.run(async_stream())