from typing import Annotated
import pytest
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient

from hypermedia import Div, Element
from hypermedia.fastapi import add_htmx_middleware, full, htmx


def render_partial() -> Element:
    return Div("partial")


def render_full(
    partial: Annotated[Element, Depends(render_partial)],
) -> Element:
    return Div("full", partial)


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

    @_app.get("/hypermedia", response_class=HTMLResponse)
    @htmx
    async def hypermedia(
        request: Request,
        partial: Annotated[Element, Depends(render_partial)],
        full: Annotated[Element, Depends(full(render_full))],
    ) -> str:
        """HTMX."""

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
