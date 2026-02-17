import pytest
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient

from hypermedia.fastapi import add_htmx_middleware


@pytest.fixture
def app() -> FastAPI:
    _app = FastAPI(
        title="test",
        description="testing app",
    )

    @_app.get("/", response_class=HTMLResponse)
    async def root() -> str:
        """Root."""
        return "root"

    return _app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    """Test client."""
    return TestClient(app)


@pytest.fixture
def instrumented_client(
    app: FastAPI,
) -> TestClient:
    """Instrumented Test client."""
    add_htmx_middleware(app)
    return TestClient(app)
