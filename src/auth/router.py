from fastapi import APIRouter, Request, HTTPException, status
from .schemas import (
    SignInRequestSchema,
    SignInReponseSchema,
    SignReponseSchema,
)
from src.auth.service import AuthService

router = APIRouter()


@router.get("/sign", status_code=status.HTTP_200_OK)
async def sign() -> SignReponseSchema:
    msg, nonce = AuthService.get_validate_msg()
    return {"sign_message": msg, "nonce": nonce}


@router.post("/sign_in", status_code=status.HTTP_200_OK)
async def sign_in(body: SignInRequestSchema, request: Request) -> SignInReponseSchema:
    _signature = body.signature

    _nonce = body.nonce

    _access_token, _nonce = await AuthService.verify(
        signature=_signature,
        address=body.address,
        session={
            "signature": _signature,
            "address": body.address,
            "nonce": _nonce,
        },
    )
    if not _access_token:
        raise HTTPException(
            status_code=400, detail="Invalid params. Signature invalid."
        )

    return {
        "signature": _signature,
        "address": body.address,
        "access_token": _access_token,
        "nonce": _nonce,
    }
