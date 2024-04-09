from datetime import datetime

from bson import ObjectId
from .exception import InvalidCertificate
from .model import Certificate, TxLog
from .schema import (
    GetCertificatesResponseSchema,
    GetTransactionsResponseSchema,
    SubmitCertificateCorporateRequestSchema,
    SubmitCertificateIndividualRequestSchema,
)
import logging


class CertificateService:
    @classmethod
    async def submit_certificate_individual(
        cls, body: SubmitCertificateIndividualRequestSchema, user_id: str
    ):
        # print(await Certificate.find().to_list())
        cerfiticate = Certificate(
            name=body.name,
            amount=body.amount,
            project_type=body.project_type,
            project_location=body.project_location,
            reason=body.reason,
            project_id=body.project_id,
            device_id=body.device_id,
            user=user_id,
            is_corporate=False,
            created_time=datetime.now(),
        )
        # print("dump:", cerfiticate)
        return await cerfiticate.insert()

    @classmethod
    async def submit_certificate_corporate(
        cls, body: SubmitCertificateCorporateRequestSchema, user_id: str
    ):
        cerfiticate = Certificate(
            name=body.name,
            amount=body.amount,
            project_type=body.project_type,
            project_location=body.project_location,
            reason=body.reason,
            country=body.country,
            address=body.address,
            project_id=body.project_id,
            device_id=body.device_id,
            user=user_id,
            is_corporate=True,
            created_time=datetime.now(),
        )

        return await cerfiticate.insert()

    @classmethod
    async def get_cerificates_by_user(cls, user_id: str):
        certificates = (
            await Certificate.find({"user": user_id, "tx_signature": {"$ne": ""}})
            .sort("-_id")
            .to_list()
        )
        return list(
            map(
                lambda cer: GetCertificatesResponseSchema(
                    id=str(cer.id),
                    name=cer.name,
                    amount=cer.amount,
                    project_type=cer.project_type,
                    project_location=cer.project_location,
                    reason=cer.reason,
                    country=cer.country,
                    address=cer.address,
                    is_corporate=cer.is_corporate,
                    created_time=cer.created_time,
                    tx_signature=cer.tx_signature,
                ),
                certificates,
            )
        )

    @classmethod
    async def get_cerificates_detail(cls, id: str):
        certificate = await Certificate.find_one({"_id": ObjectId(id)})
        if not certificate:
            raise InvalidCertificate

        return GetCertificatesResponseSchema(
            id=str(certificate.id),
            name=certificate.name,
            amount=certificate.amount,
            project_type=certificate.project_type,
            project_location=certificate.project_location,
            reason=certificate.reason,
            country=certificate.country,
            address=certificate.address,
            is_corporate=certificate.is_corporate,
            created_time=certificate.created_time,
            tx_signature=certificate.tx_signature,
        )

    @classmethod
    async def get_transactions_by_user(cls, address: str):
        txLogs = (
            await TxLog.find(
                {"$or": [{"from_address": address}, {"to_address": address}]}
            )
            .sort("-_id")
            .to_list()
        )

        return list(
            map(
                lambda item: GetTransactionsResponseSchema(
                    id=str(item.id),
                    amount=item.amount,
                    type=item.type,
                    created_time=item.created_time,
                    tx_signature=item.tx_signature,
                    from_address=item.from_address,
                    to_address=item.to_address,
                    token=item.token,
                    project_id=item.project_id,
                ),
                txLogs,
            )
        )
