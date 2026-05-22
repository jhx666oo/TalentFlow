import os

# 绑定地址，0.0.0.0 允许 Docker 外部访问
bind = "0.0.0.0:8000"

# Docker 容器中固定 worker 数，由副本数控制并发
workers = int(os.getenv("GUNICORN_WORKERS", "2"))
threads = 1

worker_class = "uvicorn.workers.UvicornWorker"

timeout = 120
graceful_timeout = 30
keepalive = 5

# Docker 日志输出到 stdout/stderr，由 docker logs 收集
accesslog = "-"
errorlog = "-"
loglevel = os.getenv("GUNICORN_LOG_LEVEL", "info")

limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

preload_app = False