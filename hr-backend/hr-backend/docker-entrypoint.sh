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

echo "Ensuring agent database exists..."
python -c "
import asyncio
from sqlalchemy import text
from models import engine
async def ensure_agent_db():
    async with engine.connect() as conn:
        await conn.execute(text('commit'))
        result = await conn.execute(text(\"SELECT 1 FROM pg_database WHERE datname = 'hr_system_agent'\"))
        if not result.fetchone():
            await conn.execute(text('CREATE DATABASE hr_system_agent'))
            print('Created database: hr_system_agent')
        else:
            print('Database hr_system_agent already exists')
asyncio.run(ensure_agent_db())
"

echo "Seeding initial data..."
python init_data.py

echo "Starting Gunicorn..."
exec gunicorn main:app -c gunicorn.conf.py
