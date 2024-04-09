from fastapi import APIRouter, Request, status
from authen.jwt_middleware import authentication_middleaware
from src.certificate.service import CertificateService

from .schema import (
    SubmitCertificateCorporateRequestSchema,
    SubmitCertificateIndividualRequestSchema,
)
import traceback
import logging

router = APIRouter()


# @router.post("", response_model=list[GetAllUsersResponseSchema], status_code=status.HTTP_200_OK)
@router.post("/individual", status_code=status.HTTP_201_CREATED)
async def submit_certificate_individual(
    body: SubmitCertificateIndividualRequestSchema, request: Request
):
    try:
        decode_data = authentication_middleaware.get_info_by_token(
            request.headers.get("authorization").split(" ")[1]
        )
        return await CertificateService.submit_certificate_individual(
            body, decode_data.get("user_id")
        )
    except Exception as e:
        traceback.print_exc()
        raise e


@router.post("/corporate", status_code=status.HTTP_201_CREATED)
async def submit_certificate_corporate(
    body: SubmitCertificateCorporateRequestSchema, request: Request
):
    try:
        decode_data = authentication_middleaware.get_info_by_token(
            request.headers.get("authorization").split(" ")[1]
        )
        return await CertificateService.submit_certificate_corporate(
            body, decode_data.get("user_id")
        )
    except Exception as e:
        traceback.print_exc()
        raise e


@router.get("/me", status_code=status.HTTP_200_OK)
async def get_cerificates_by_user(request: Request):
    try:
        decode_data = authentication_middleaware.get_info_by_token(
            request.headers.get("authorization").split(" ")[1]
        )
        return await CertificateService.get_cerificates_by_user(
            decode_data.get("user_id")
        )
    except Exception as e:
        traceback.print_exc()
        raise e


@router.get("/detail/{id}", status_code=status.HTTP_200_OK)
async def get_cerificates_by_user(id: str):
    try:
        return await CertificateService.get_cerificates_detail(id)
    except Exception as e:
        traceback.print_exc()
        raise e


@router.get("/transaction/me", status_code=status.HTTP_200_OK)
async def get_transaction_by_user(request: Request):
    try:
        decode_data = authentication_middleaware.get_info_by_token(
            request.headers.get("authorization").split(" ")[1]
        )
        return await CertificateService.get_transactions_by_user(
            decode_data.get("address")
        )
    except Exception as e:
        traceback.print_exc()
        raise e
