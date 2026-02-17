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
def htmx_enabled_client(
    app: FastAPI,
) -> TestClient:
    """Test client with htmx middleware added."""
    add_htmx_middleware(app)
    return TestClient(app)
