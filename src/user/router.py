from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

from .schema import GetProfileResponseSchema, UpdateProfileRequestSchema
from .service import UserSevice
from authen.jwt_middleware import authentication_middleaware
import traceback
import logging

router = APIRouter()


@router.get("/me", status_code=status.HTTP_200_OK)
async def get_profile(request: Request):
    try:
        decode_data = authentication_middleaware.get_info_by_token(
            request.headers.get("authorization").split(" ")[1]
        )
        user_data = await UserSevice.create_user_if_needed(decode_data.get("address"))
        print("data:", decode_data)
        return GetProfileResponseSchema(
            id=str(user_data.id),
            name=user_data.name,
            avatar=user_data.avatar,
            fund=user_data.fund,
            offset=user_data.offset,
            address=user_data.address,
            created_time=user_data.created_time,
        )
    except Exception as e:
        traceback.print_exc()
        raise e


@router.put("/me", status_code=status.HTTP_202_ACCEPTED)
async def update_profile(body: UpdateProfileRequestSchema, request: Request):
    try:
        decode_data = authentication_middleaware.get_info_by_token(
            request.headers.get("authorization").split(" ")[1]
        )
        return await UserSevice.update_user(decode_data.get("address"), body)
    except Exception as e:
        traceback.print_exc()
        raise e
