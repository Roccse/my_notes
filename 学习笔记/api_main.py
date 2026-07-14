from fastapi import FastAPI
import os
import redis
import json

app = FastAPI()

NOTES_DIR = "D:/Obsidian/Repository/学习笔记"

# 连接 Redis（默认连本地 6379 端口）
cache = redis.Redis(host="localhost", port=6379, decode_responses=True)

@app.get("/notes")
def list_notes():
    """返回所有笔记文件名（带缓存，5秒过期）"""
    cached = cache.get("notes_list")
    if cached:
        return {"notes": json.loads(cached), "from": "cache"}

    files = []
    for f in os.listdir(NOTES_DIR):
        if f.endswith(".md"):
            files.append(f)

    # 写入缓存，5秒后过期
    cache.setex("notes_list", 5, json.dumps(files))
    return {"notes": files, "from": "disk"}

@app.get("/notes/{title}")
def get_note(title: str):
    """根据标题返回笔记内容（带缓存）"""
    cache_key = f"note:{title}"
    cached = cache.get(cache_key)
    if cached:
        return {"title": title, "content": cached, "from": "cache"}

    path = os.path.join(NOTES_DIR, f"{title}.md")
    if not os.path.exists(path):
        return {"error": "笔记不存在"}
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    cache.setex(cache_key, 5, content)
    return {"title": title, "content": content, "from": "disk"}

@app.get("/search")
def search_notes(q: str):
    """搜索笔记内容（带缓存）"""
    cache_key = f"search:{q}"
    cached = cache.get(cache_key)
    if cached:
        return {"query": q, "results": json.loads(cached), "from": "cache"}

    results = []
    for f in os.listdir(NOTES_DIR):
        if not f.endswith(".md"):
            continue
        path = os.path.join(NOTES_DIR, f)
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        if q.lower() in content.lower():
            results.append({
                "title": f.replace(".md", ""),
                "match_count": content.lower().count(q.lower())
            })

    cache.setex(cache_key, 5, json.dumps(results))
    return {"query": q, "results": results, "from": "disk"}
