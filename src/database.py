from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src import models
from src.config import settings


async def initiate_database():
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(
        # Or db name client.[name]
        database=client.get_default_database(),
        document_models=models.__all__,
    )
