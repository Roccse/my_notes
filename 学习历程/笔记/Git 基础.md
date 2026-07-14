# Git 基础知识

## 为什么用 Git

把本地文件同步到远程仓库（如 GitHub），实现备份、版本管理和协作。

## 常用命令

| 命令 | 含义 | 类比 |
|------|------|------|
| `git init` | 把当前目录变成 Git 仓库 | 贴上"归 Git 管"的标签 |
| `git add .` | 把所有更改的文件加入待提交区 | 装进纸箱 |
| `git commit -m "说明"` | 打一个版本包 | 纸箱封箱贴标签 |
| `git push` | 上传到远程仓库 | 运到保险柜 |
| `git pull` | 从远程仓库拉取最新版本 | 从保险柜取回来 |

## 完整流程

```bash
cd 你的项目目录
git init                          # 初始化
git add .                         # 打包所有文件
git commit -m "第一次提交"         # 封箱
git remote add origin 仓库地址     # 关联远程仓库
git push -u origin main           # 推送到远程
```

以后每次修改后只需要：

```bash
git add .
git commit -m "更新了xxx"
git push
```

## 两种连接方式

| 方式 | 地址格式 | 需要配置 |
|------|---------|---------|
| HTTPS | `https://github.com/用户/仓库.git` | 可能需要配代理 |
| SSH | `git@github.com:用户/仓库.git` | 需要添加 SSH Key（推荐） |

## 代理问题

Windows 上 Git 走 HTTPS 可能遇到 SSL 问题，推荐：
- 用 SSH 代替 HTTPS
- 或者给 Git 配置代理：`git config --global http.proxy http://127.0.0.1:7890`


---
相关笔记：[[FastAPI 入门]]
