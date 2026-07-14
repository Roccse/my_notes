# Hermes Agent 架构

## 三层架构

### 第一层：微信客户端
用户发消息的入口。

### 第二层：Hermes Gateway（网关层）
- 负责消息的收发
- 通过轮询（Long Polling）腾讯 iLink 的 `getupdates` 接口接收消息
- 通过 `sendmessage` 接口发送回复
- 每个平台有独立的适配器（`gateway/platforms/weixin.py`）

### 第三层：Hermes Agent（代理层）
- 收到消息后调用 LLM 分析问题
- 支持 Tool Calling — LLM 可以选择调用预注册的工具
- 执行工具后将结果返回给 Gateway

## 名词对照

| 术语 | 说明 |
|------|------|
| Gateway | 消息网关，对接各聊天平台 |
| Agent | AI 代理，负责调用 LLM 和工具 |
| Provider | LLM 供应商（如 DeepSeek、OpenRouter） |
| Tool Calling | LLM 调用预定义函数的机制 |
| iLink API | 腾讯提供的微信 Bot 消息接口 |

## 完整链路

用户微信发消息 → iLink 服务器 → Gateway（轮询 getupdates）
→ Agent → LLM（DeepSeek）→ Agent 执行工具（可选）
→ Gateway（sendmessage）→ iLink 服务器 → 用户微信收到回复


---
相关笔记：[[微信 iLink Bot 工作原理]] | [[Tool Calling 机制]] | [[Windows SSL 证书问题]]
