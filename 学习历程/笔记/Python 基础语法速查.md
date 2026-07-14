# Python 基础：看懂项目代码需要知道的语法

## 基础语法对照表（Java → Python）

| Java | Python |
|------|--------|
| `;` 分号结尾 | 不需要分号 |
| `{ }` 代码块 | `:` + 缩进（通常4空格） |
| `int x = 1` | `x = 1`（不用声明类型） |
| `if (x == 1) { }` | `if x == 1:` |
| `try { } catch (Exception e) { }` | `try: ... except Exception as e:` |
| `System.out.println()` | `print()` |
| `// 注释` | `# 注释` |
| `null` | `None` |
| `&&` / `||` | `and` / `or` |

## async / await（异步编程）

```python
async def my_function():       # 定义异步函数
    result = await http_request()  # await = 等结果，不卡住程序
    return result
```

- `async def` 声明函数里有耗时操作
- `await` 等网络请求或计时器完成
- 两者必须配合使用

## f-string（格式化字符串）

```python
name = "张三"
print(f"我叫{name}")    # 输出：我叫张三
# 不加 f 则 {name} 会原样输出
```

## try / except（异常处理）

```python
try:
    resp = await session.get(url)       # 试试发请求
except Exception as e:                  # 如果出错了
    print(f"出错了：{e}")                # 打印错误，不崩溃
```

## data.get('key') / data.get('key') or ''（安全取值）

```python
# 从字典中取值，取不到返回 None
value = data.get('qrcode')

# 取不到就用空字符串代替（防止 None 拼进 URL 变成 "None"）
value = data.get('qrcode') or ''
```


---
相关笔记：[[FastAPI 入门]] | [[Git 基础]]
