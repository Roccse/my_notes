# FastAPI 快速入门

## FastAPI 是什么

一个 Python Web 框架，帮你快速写 RESTful API。

不是现成的应用程序，而是一个 Python 库（框架）。

## 最小示例

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "你好"}
```

启动：

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

访问 `http://localhost:8000/hello` 就能看到结果。

## 参数说明

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
         ↑主文件  ↑变量名  ↑自动重载  ↑允许外网访问  ↑端口
```

## 三个核心概念

| 组件 | 角色 |
|------|------|
| FastAPI | 写接口逻辑（厨房） |
| uvicorn | 启动服务、收请求（服务员） |
| API 路由 | `@app.get("/path")` 定义路径和方法的对应关系 |


---
相关笔记：[[Python 基础语法速查]] | [[Git 基础]]
