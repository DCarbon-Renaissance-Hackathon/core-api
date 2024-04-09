import pytest
from async_asgi_testclient import TestClient
from fastapi import status


@pytest.mark.asyncio
async def test_register(client: TestClient) -> None:
    pass


@pytest.mark.asyncio
async def test_register_email_taken(
    client: TestClient, monkeypatch: pytest.MonkeyPatch
) -> None:

    async def fake_getter(*args, **kwargs):
        return True

