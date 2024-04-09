from src.schemas import ORJSONModel
from pydantic import validator, BaseModel
from typing import Any


class SignReponseSchema(ORJSONModel):
    sign_message: str
    nonce: str


class SignInRequestSchema(BaseModel):
    signature: str
    address: str
    nonce: str


class SignInReponseSchema(BaseModel):
    signature: str
    address: str
    nonce: str
    access_token: str


class SignInGoogleRequestSchema(BaseModel):
    token: str


class SignInGoogleReponseSchema(BaseModel):
    device_id: str
    xrip: str
    access_token: str
