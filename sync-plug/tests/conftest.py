import pytest_asyncio
from starlette.testclient import TestClient

from app.main import app


@pytest_asyncio.fixture(scope="session")
async def test_client():
    with TestClient(app) as test_client:
        yield test_client