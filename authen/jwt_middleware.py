from fastapi.security import OAuth2PasswordBearer

from src.auth.exception import TokenExpired

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
import jwt
import traceback
from fastapi import HTTPException
from datetime import datetime, timedelta
from eth_account.messages import defunct_hash_message, encode_defunct
from src.config import settings


class authentication_middleaware:
    @classmethod
    def get_info_by_token(cls, token: str):
        try:
            decoded_token = jwt.decode(
                token,
                options={"verify_signature": False},
                algorithms=[settings.JWT_ALG],
            )

            if datetime.now() > datetime.strptime(
                decoded_token.get("expire").split(".")[0], "%Y-%m-%d %H:%M:%S"
            ):
                raise TokenExpired

            return decoded_token.get("payload")
        except Exception as e:
            traceback.print_exc()
            raise e

    @classmethod
    def _gen_access_token(cls, session: dict) -> str:
        _payload = {
            "payload": session,
            "init": str(datetime.now()),  # init time
            "expire": str(datetime.now() + timedelta(float(settings.JWT_EXP))),
        }

        _access_token = jwt.encode(
            _payload, settings.JWT_SECRET, algorithm=settings.JWT_ALG
        )
        return _access_token
