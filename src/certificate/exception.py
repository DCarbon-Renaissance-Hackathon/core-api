from fastapi import status

from src.exceptions import DetailedHTTPException


class InvalidCertificate(DetailedHTTPException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Invalid certificate"
