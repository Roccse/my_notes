# Tool Calling（AI Agent 核心机制）

## 什么是 Tool Calling

Tool Calling 是 LLM Agent 和普通聊天机器人的本质区别。

- 普通聊天：LLM 基于训练数据回答
- Agent：LLM 可以**调用外部工具**获取实时数据或执行操作

## 工作流程

```
用户提问 → LLM 判断是否需要工具
  → 需要：返回 tool_call（工具名 + 参数）
  → Agent 执行工具，得到结果
  → 结果喂回 LLM，LLM 生成最终回复
  → 不需要：直接回复
```

## 工具注册

每个工具需要注册三样东西：

| 要素 | 例子 |
|------|------|
| 名字 | `web_search` |
| 描述 | "搜索互联网获取实时信息" |
| 参数 | query（搜索关键词） |

LLM 根据**描述**来判断用户的问题是否匹配这个工具。

## 实际例子

用户说："今天北京天气怎么样？"

1. LLM 看到 `web_search` 的描述是"搜索实时信息"
2. LLM 返回：调用 `web_search(query="北京天气")`
3. Agent 执行搜索，得到 "25°C，晴"
4. LLM 基于结果回复："北京今天 25°C，晴天"

## 你的 Bot 能用哪些工具

| 工具 | 作用 |
|------|------|
| web_search | 搜索实时信息 |
| web_extract | 提取网页内容 |
| read_file / write_file | 文件读写 |
| terminal | 执行 shell 命令 |


---
相关笔记：[[Hermes Agent 架构]] | [[微信 iLink Bot 工作原理]]
