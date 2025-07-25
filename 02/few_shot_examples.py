from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate


examples = [
  {
    "question": "谁的寿命更长，穆罕默德·阿里还是艾伦·图灵？",
    "answer":
"""
这里需要跟进问题吗：是的。
跟进：穆罕默德·阿里去世时多大？
中间答案：穆罕默德·阿里去世时74岁。
跟进：艾伦·图灵去世时多大？
中间答案：艾伦·图灵去世时41岁。
所以最终答案是：穆罕默德·阿里
"""
  },
  {
    "question": "craigslist的创始人是什么时候出生的？",
    "answer":
"""
这里需要跟进问题吗：是的。
跟进：craigslist的创始人是谁？
中间答案：craigslist由Craig Newmark创立。
跟进：Craig Newmark是什么时候出生的？
中间答案：Craig Newmark于1952年12月6日出生。
所以最终答案是：1952年12月6日
"""
  },
  {
    "question": "乔治·华盛顿的祖父母中的母亲是谁？",
    "answer":
"""
这里需要跟进问题吗：是的。
跟进：乔治·华盛顿的母亲是谁？
中间答案：乔治·华盛顿的母亲是Mary Ball Washington。
跟进：Mary Ball Washington的父亲是谁？
中间答案：Mary Ball Washington的父亲是Joseph Ball。
所以最终答案是：Joseph Ball
"""
  },
  {
    "question": "《大白鲨》和《皇家赌场》的导演都来自同一个国家吗？",
    "answer":
"""
这里需要跟进问题吗：是的。
跟进：《大白鲨》的导演是谁？
中间答案：《大白鲨》的导演是Steven Spielberg。
跟进：Steven Spielberg来自哪里？
中间答案：美国。
跟进：《皇家赌场》的导演是谁？
中间答案：《皇家赌场》的导演是Martin Campbell。
跟进：Martin Campbell来自哪里？
中间答案：新西兰。
所以最终答案是：不是
"""
  }
]

example_prompt = PromptTemplate(input_variables=["question", "answer"], template="问题：{question}\\n{answer}")

# 接收examples示例数组参数，通过example_prompt提示词模板批量渲染示例内容
# suffix和input_variables参数用于在提示词模板最后追加内容， input_variables用于定义suffix中包含的模板参数
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="问题：{input}",
    input_variables=["input"]
)

print(prompt.format(input="乔治·华盛顿的父亲是谁？"))