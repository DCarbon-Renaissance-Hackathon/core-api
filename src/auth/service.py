import codecs
import random
from random import choice
import string
from authen.jwt_middleware import authentication_middleaware
import base58
import base64
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from src.user.model import User
from src.config import settings
from src.user.service import UserSevice


class AuthService:
    def random_str(size=10, chars=string.ascii_letters + string.digits):
        return "".join(choice(chars) for x in range(size))

    def get_token(self):
        return

    async def verify(signature: str, address: str, session: dict):
        _nonce = session.get("nonce")
        _msg, _nonce = AuthService.get_validate_msg(nonce=_nonce)
        print("msg:", _msg)
        # _msg_hash = defunct_hash_message(text=_msg)
        if len(signature) == 128:
            signature = codecs.encode(codecs.decode(signature, "hex"), "base64")
            print("signature:", signature)

        public_key_bytes = base58.b58decode(address)
        signature_bytes = base64.b64decode(signature)
        verify_key = VerifyKey(public_key_bytes)
        try:
            _msg = _msg.encode("utf-8")
            verify_key.verify(_msg, signature_bytes)
        except BadSignatureError:
            return False, None

        user_data = await UserSevice.create_user_if_needed(address)

        _access_token = authentication_middleaware._gen_access_token(
            session={"address": address, "nonce": _nonce, "user_id": str(user_data.id)}
        )

        return _access_token, _nonce

    def get_validate_msg(nonce=None):
        if not nonce:
            nonce = AuthService.random_str(size=8, chars=string.digits)
        return f"I am signing with nonce: {nonce}", nonce
