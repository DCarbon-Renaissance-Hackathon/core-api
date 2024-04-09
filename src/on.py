from redis import asyncio as aioredis

from src import redis
from src.config import settings
from src.database import initiate_database


async def check_connect():
    pass


async def on_start():
    await initiate_database()


async def on_shutdown():
    await redis.redis_client.close()
