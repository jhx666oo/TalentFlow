#!/bin/bash
set -e

echo "Running database migrations..."
if ! alembic upgrade head 2>/dev/null; then
    echo "Alembic migration failed, creating tables from models..."
    python -c "
import asyncio
from models import engine, Base
async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
asyncio.run(init())
"
fi

echo "Starting Gunicorn..."
exec gunicorn main:app -c gunicorn.conf.py
