from datetime import datetime
import random

from src.user.schema import UpdateProfileRequestSchema
from .model import User
from src.config import settings


class UserSevice:
    async def create_user_if_needed(address: str):
        user_data = await User.find_one({"address": address})

        if not user_data:
            user_data = User(
                name="Unnamed",
                avatar=settings.DEFAULT_AVATARS[
                    random.randint(0, len(settings.DEFAULT_AVATARS) - 1)
                ],
                address=address,
                fund=0,
                offset=0,
                created_time=datetime.now(),
            )
            await user_data.insert()
            await user_data.save()
        return user_data

    @classmethod
    async def update_user(cls, address: str, body: UpdateProfileRequestSchema):
        user_data = await User.find_one({"address": address})
        data = body.model_dump(exclude_none=True)
        return await user_data.set(data)
