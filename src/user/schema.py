from datetime import datetime
from typing import Optional
from src.schemas import ORJSONModel


class GetProfileResponseSchema(ORJSONModel):
    id: str
    name: str
    avatar: str
    fund: float
    offset: float
    address: str
    created_time: datetime


class UpdateProfileRequestSchema(ORJSONModel):
    name: Optional[str] = None
    avatar: Optional[str] = None
