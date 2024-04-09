from datetime import datetime
from typing import Optional

from bson import ObjectId
from ..base import BaseDocument


class User(BaseDocument):
    class Settings:
        name = "users"

    _id: Optional[ObjectId] = None
    name: str
    avatar: str
    fund: Optional[float] = 0
    offset: Optional[float] = 0
    address: str
    created_time: datetime

    class Config:
        arbitrary_types_allowed = True
