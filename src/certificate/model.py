from datetime import datetime
from typing import Optional

from bson import ObjectId
from ..base import BaseDocument


class Certificate(BaseDocument):
    class Settings:
        name = "certificates"

    _id: Optional[ObjectId] = None
    name: str
    amount: float
    project_type: str
    project_location: str
    reason: str
    project_id: str
    device_id: str
    country: Optional[str] = None
    address: Optional[str] = None
    is_corporate: Optional[bool] = None
    created_time: datetime
    tx_signature: Optional[str] = ""
    user: Optional[str] = ""

    class Config:
        arbitrary_types_allowed = True


class TxLog(BaseDocument):
    class Settings:
        name = "tx_logs"

    _id: Optional[ObjectId] = None
    amount: float
    type: str
    created_time: datetime
    tx_signature: str
    from_address: str
    to_address: Optional[str] = ""
    token: str
    project_id: str

    class Config:
        arbitrary_types_allowed = True
