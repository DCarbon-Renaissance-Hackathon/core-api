from datetime import timedelta
from typing import Optional

from redis.asyncio import Redis
from src.schemas import ORJSONModel

redis_client: Redis = None  # type: ignore


class RedisData(ORJSONModel):
    key: bytes | str
    value: bytes | str
    ttl: Optional[int | timedelta]


async def set_redis_key(key, value, ttl=None, *, is_transaction: bool = False) -> None:
    async with redis_client.pipeline(transaction=is_transaction) as pipe:
        await pipe.set(key, value)
        if ttl:
            await pipe.expire(key, ttl)

        await pipe.execute()


async def get_by_key(key: str) -> Optional[str]:
    return await redis_client.get(key)


async def delete_by_key(key: str) -> None:
    return await redis_client.delete(key)
