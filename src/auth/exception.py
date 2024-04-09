from fastapi import status

from src.exceptions import DetailedHTTPException


class TokenExpired(DetailedHTTPException):
    STATUS_CODE = status.HTTP_403_FORBIDDEN
    DETAIL = "Token expired"
