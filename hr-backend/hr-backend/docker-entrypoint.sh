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
import psycopg
from settings import settings

# Parse the agent database name from the URL
agent_url = settings.DATABASE_AGENT_URL
# Create the agent database using the main connection
main_url = settings.DATABASE_URL
conn = psycopg.connect(main_url)
conn.autocommit = True
cur = conn.cursor()
cur.execute(\"SELECT 1 FROM pg_database WHERE datname = %s\", (settings.DB_AGENT_NAME,))
if not cur.fetchone():
    cur.execute(f'CREATE DATABASE {settings.DB_AGENT_NAME}')
    print(f'Created database: {settings.DB_AGENT_NAME}')
else:
    print(f'Database {settings.DB_AGENT_NAME} already exists')
cur.close()
conn.close()
"

echo "Seeding initial data..."
python init_data.py

echo "Starting Gunicorn..."
exec gunicorn main:app -c gunicorn.conf.py
