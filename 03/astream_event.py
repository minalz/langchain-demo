import asyncio
import os

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    api_key=os.getenv("API-KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus"  # 模型名称可按需更换
)


async def async_stream():
    events = []
    async for event in model.astream_events("hello", version="v2"):
        events.append(event)
    print(events)


# 运行异步流处理
asyncio.run(async_stream())
