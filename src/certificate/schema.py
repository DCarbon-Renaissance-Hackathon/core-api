from datetime import datetime
from typing import Optional
from src.schemas import ORJSONModel


class SubmitCertificateIndividualRequestSchema(ORJSONModel):
    name: str
    amount: float
    project_type: str
    project_location: str
    reason: str
    project_id: str
    device_id: str


class SubmitCertificateCorporateRequestSchema(ORJSONModel):
    name: str
    amount: float
    project_type: str
    project_location: str
    reason: str
    project_id: str
    device_id: str
    country: str
    address: str


class GetCertificatesResponseSchema(ORJSONModel):
    id: str
    name: str
    amount: float
    project_type: str
    project_location: str
    reason: str
    country: Optional[str] = None
    address: Optional[str] = None
    is_corporate: bool
    created_time: datetime
    tx_signature: str


class GetTransactionsResponseSchema(ORJSONModel):
    id: str
    amount: float
    type: str
    created_time: datetime
    tx_signature: str
    from_address: str
    to_address: Optional[str] = None
    token: str
    project_id: str
