import asyncio
import os

from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    api_key=os.getenv("API-KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus"  # 模型名称可按需更换
)

parser = StrOutputParser()
chain = (
        model | JsonOutputParser()
    # 由于Langchain旧版本中的一个错误，JsonOutputParser未能从某些模型中流式传输结果
)


async def async_stream():
    async for text in chain.astream(
            "以JSON 格式输出法国、西班牙、日本和中国的国家及其人口列表。"
            '使用一个带有“countries”外部键的字典，其中包含国家列表。'
            "每个国家都应该有键`name`和`population`"
    ):
        print(text, flush=True)

# 运行异步流处理
asyncio.run(async_stream())