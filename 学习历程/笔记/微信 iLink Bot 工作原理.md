# 微信 iLink Bot 工作原理

## Bot 是什么

iLink Bot 是一个绑定在个人微信上的 Bot 身份。通过扫码登录绑定，别人不需要添加 Bot 为好友。

## 通信方式：轮询（非 Webhook）

微信 Bot 使用 **Long Polling（长轮询）** 而非 Webhook。
- Webhook：服务器有公网地址，平台主动推送消息过来
- 轮询：Bot 定时去腾讯服务器查有没有新消息

## 核心 API

| 接口 | 用途 |
|------|------|
| `get_bot_qrcode` | 获取登录二维码 |
| `get_qrcode_status` | 查询扫码状态 |
| `getupdates` | 拉取新消息 |
| `sendmessage` | 发送消息 |

## 登录流程

1. 调用 `get_bot_qrcode` 拿到二维码值和图片 URL
2. 生成二维码图片，用户扫码
3. 轮询 `get_qrcode_status` 直到状态变为 `confirmed`
4. 获取 `ilink_bot_id` 和 `bot_token`，保存到 `.env`

## 收发消息

### 收消息
```python
async def _get_updates(session, base_url, token, sync_buf, timeout_ms):
    # sync_buf 类似于"读到哪了"的指针
    # 发送给 iLink 服务器，返回新消息列表
    return await _api_post(session, endpoint="getupdates", ...)
```

### 发消息
```python
async def _send_message(session, base_url, token, to, text, context_token, client_id):
    # 构造消息体，包含 to_user_id、text 等字段
    # context_token 用于保持对话上下文
    return await _api_post(session, endpoint="sendmessage", ...)
```


---
相关笔记：[[Hermes Agent 架构]] | [[Windows SSL 证书问题]]
