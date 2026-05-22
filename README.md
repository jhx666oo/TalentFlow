# TalentFlow 智能招聘系统

AI 驱动的全流程智能招聘管理平台，支持简历自动解析、候选人管理、面试协同调度。

**在线体验**：[www.ai-bot.icu](https://www.ai-bot.icu)

## 技术栈

| 层 | 技术 |
|---|---|
| 前端 | Vue 3 + TypeScript + Element Plus + Tailwind CSS |
| 后端 | FastAPI + SQLAlchemy + PostgreSQL + Redis |
| AI | LangChain + Qwen OCR + PaddleOCR |
| 基础设施 | Docker + Gunicorn + Uvicorn |

## 项目结构

```
TalentFlow/
├── hr-backend/hr-backend/     # 后端服务
│   ├── agents/                # AI Agent（简历解析、候选人评估）
│   ├── core/                  # 核心模块（OCR、认证、缓存、邮件）
│   ├── models/                # 数据库模型
│   ├── routers/               # API 路由
│   ├── schemas/               # Pydantic 数据模型
│   ├── repository/            # 数据访问层
│   ├── tasks/                 # 异步任务
│   ├── settings/              # 配置管理
│   └── alembic/               # 数据库迁移
├── hr-frontend/hr-frontend-src/  # 前端
│   └── src/
│       ├── components/        # 公共组件
│       ├── pages/             # 页面
│       ├── apis/              # API 请求
│       ├── router/            # 路由
│       └── stores/            # 状态管理 (Pinia)
└── .gitignore
```

## 功能特性

- **AI 简历解析** — 上传 PDF/Word/图片简历，自动提取姓名、学历、工作经历、技能等关键信息
- **智能评分** — AI Agent 对候选人进行综合评估打分
- **全流程管理** — 从简历筛选 → AI 初筛 → 面试 → 入职，状态流转跟踪
- **多角色协同** — 超级管理员、HR、部门面试官权限隔离
- **面试调度** — 邮件通知候选人协商面试时间，钉钉日程同步
- **数据看板** — 招聘数据可视化

## 快速开始

### 环境要求

- Python 3.13+
- PostgreSQL
- Redis
- Node.js 20+

### 后端

```bash
cd hr-backend/hr-backend

# 创建虚拟环境
python3.13 -m venv .venv-macos

# 安装依赖
./.venv-macos/bin/pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入数据库、Redis、API Key 等配置

# 数据库迁移
./.venv-macos/bin/alembic upgrade head

# 初始化种子数据
./.venv-macos/bin/python init_data.py

# 启动服务
./.venv-macos/bin/uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 前端

```bash
cd hr-frontend/hr-frontend-src

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

访问 http://localhost:5173 即可使用。

## 默认账号

| 账号 | 密码 | 角色 |
|------|------|------|
| boss@qq.com | 111111 | 超级管理员 |
| hr@qq.com | 111111 | HR |
| tech@qq.com | 111111 | 技术面试官 |

## API 文档

启动后端后访问 http://127.0.0.1:8000/docs 查看 Swagger API 文档。

## 线上部署

| 服务 | 地址 |
|------|------|
| 前端 | [www.ai-bot.icu](https://www.ai-bot.icu) (Vercel) |
| API | [api.ai-bot.icu](https://api.ai-bot.icu) (阿里云 ECS + Docker) |

### Docker 部署

```bash
# 在项目根目录
docker compose up -d
```

服务包括：PostgreSQL 16、Redis 7、FastAPI 后端（Gunicorn + Uvicorn）、Caddy（自动 SSL）。
