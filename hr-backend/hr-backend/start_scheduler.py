import asyncio
import redis.asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from settings import settings
from scheduler import start_email_polling

async def main():
    redis_client = aioredis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        encoding="utf-8",
        decode_responses=True,
    )
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    print("Redis initialized, starting email polling...")
    await start_email_polling()
    # Keep the process alive
    while True:
        await asyncio.sleep(3600)

asyncio.run(main())
