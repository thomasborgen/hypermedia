from typing import Annotated

import pytest
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.testclient import TestClient

from hypermedia.fastapi import LazyElement, add_htmx_middleware, full, htmx
from hypermedia.models import Element
from tests.fastapi.index import render_index, render_index_partial


@pytest.fixture
def app() -> FastAPI:
    _app = FastAPI(
        title="test",
        description="testing app",
    )

    @_app.get("/", response_class=HTMLResponse)
    @htmx
    async def index(
        request: Request,
        partial: Annotated[Element, Depends(render_index_partial)],
        full: Annotated[LazyElement, Depends(full(render_index))],
    ) -> None:
        """Return the index page."""
        pass

    @_app.get("/partial", response_class=HTMLResponse)
    @htmx
    async def index(
        request: Request,
        partial: Annotated[Element, Depends(render_index_partial)],
    ) -> None:
        """Return the index page."""
        pass

    return _app


@pytest.fixture
def client(
    app: FastAPI,
) -> TestClient:
    """Test client."""
    return TestClient(app)


@pytest.fixture
def htmx_enabled_client(
    app: FastAPI,
) -> TestClient:
    """Test client with htmx middleware added."""
    add_htmx_middleware(app)
    return TestClient(app)
