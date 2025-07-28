import os

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
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

def get_session_history(user_id: str, conversation_id: str) -> BaseChatMessageHistory:
    if (user_id, conversation_id) not in store:
        store[(user_id, conversation_id)] = ChatMessageHistory()
    return store[(user_id, conversation_id)]

with_message_history = RunnableWithMessageHistory(
    runnable,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
    history_factory_config=[
        ConfigurableFieldSpec(
            id="user_id",
            annotation=str,
            name="User ID",
            description="用户的唯一标识符。",
            default="",
            is_shared=True,
        ),
        ConfigurableFieldSpec(
            id="conversation_id",
            annotation=str,
            name="Conversation ID",
            description="对话的唯一标识符。",
            default="",
            is_shared=True,
        ),
    ],
)
response = with_message_history.invoke(
    {"ability": "math", "input": "余弦是什么意思？"},
    config={"configurable": {"user_id": "123", "conversation_id": "1"}},
)

print(response)

# 记住
response = with_message_history.invoke(
    {"ability": "math", "input": "什么?"},
    config={"configurable": {"user_id": "123", "conversation_id": "1"}},
)

print(response)

