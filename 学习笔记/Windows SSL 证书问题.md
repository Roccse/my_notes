# Windows SSL 证书问题

## 问题现象

启动微信 Bot 时报错：
```
Cannot connect to host ilinkai.weixin.qq.com:443 ssl:default [None]
```

## 原因

### certifi 是什么
certifi 是 Python 的一个证书库，存了可信的证书颁发机构（CA）列表。Python 用它验证 HTTPS 连接的服务器是否可信。

### 证书验证的两步
1. 检查证书签名是否来自可信 CA（真伪）
2. 检查证书是否被吊销（查 CRL — 证书吊销列表）

### 为什么 Windows 上出问题
- 在 Linux/Mac 上，certifi 能正常访问 CRL 地址
- 在 Windows 上，certifi 访问 CRL 地址时网络不通
- 验证卡死 → 连接被拒绝

### schannel 是什么
Windows 系统自带的 SSL/TLS 实现。它查 CRL 的方式和 certifi 不同，走的是 Windows 系统更新通道，所以正常工作。

## 解决方法

修改 `weixin.py` 中的 `_make_ssl_connector` 函数：

```python
def _make_ssl_connector():
    import sys
    if sys.platform == "win32":
        return None  # Windows 上用 schannel，不用 certifi
    try:
        import ssl, certifi
    except ImportError:
        return None
    ssl_ctx = ssl.create_default_context(cafile=certifi.where())
    return aiohttp.TCPConnector(ssl=ssl_ctx)
```

## 总结
不是证书有问题，是"查证书的人"在 Windows 上不好使。换成 Windows 自己的 schannel 就解决了。


---
相关笔记：[[微信 iLink Bot 工作原理]] | [[Hermes Agent 架构]]
