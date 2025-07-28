import os

from langchain_core.chat_history import BaseChatMessageHistory
# 引入redis聊天消息存储类
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
# 引入langchain_core.runnables.history
from langchain_core.runnables import ConfigurableFieldSpec

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You're an assistant who's good at {ability}, Respond in 20 words or fewer"),
    # 历史消息占位符
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

model = ChatOpenAI(
    api_key=os.getenv("API-KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus"  # 模型名称可按需更换
)

runnable = prompt | model

store = {}

REDIS_URL = "redis://localhost:6379/0"

def get_message_history(session_id: str) -> RedisChatMessageHistory:
    return RedisChatMessageHistory(session_id, url=REDIS_URL)

with_message_history = RunnableWithMessageHistory(
    runnable,
    get_message_history,
    input_messages_key="input",
    history_messages_key="history",
)
response = with_message_history.invoke(
    {"ability": "math", "input": "余弦是什么意思？"},
    config={"configurable": {"session_id": "abc123"}},
)

print(response)

# 记住
response = with_message_history.invoke(
    {"ability": "math", "input": "什么?"},
    config={"configurable": {"session_id": "abc123"}},
)

print(response)

# 新的 session_id --> 不记得了。
response = with_message_history.invoke(
    {"ability": "math", "input": "什么?"},
    config={"configurable": {"session_id": "def234"}},
)

print(response)

