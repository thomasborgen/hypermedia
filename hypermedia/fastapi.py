from functools import wraps
from typing import (
    Any,
    Callable,
    Coroutine,
    Protocol,
    TypeAlias,
    TypeVar,
)

from hypermedia.models import Element

try:
    from fastapi import FastAPI, Request, Response
except ImportError as ie:
    raise ImportError(
        "The 'fastapi' helpers function requires fastapi. "
        "Install it with: `pip install 'hypermedia[fastapi]'`. "
        "Or `uv add hypermedia --extras fastapi`"
    ) from ie


T = TypeVar("T", bound="Element")
LazyElement: TypeAlias = Callable[..., Element]


class PartialHTMXRequest(Protocol):
    """Requires, `request`, `partial` args on decorated function."""

    def __call__(  # noqa: D102
        self,
        request: Request,
        partial: Element,
    ) -> Coroutine[Any, Any, None]: ...


class FullHTMXRequest(Protocol):
    """Requires, `request`, `partial` and `full` args on decorated function."""

    def __call__(  # noqa: D102
        self,
        request: Request,
        partial: Element,
        full: LazyElement,
    ) -> Coroutine[Any, Any, None]: ...


def htmx(
    func: PartialHTMXRequest | FullHTMXRequest,
) -> PartialHTMXRequest | FullHTMXRequest:
    """Wrap a FastAPI endpoint, to enable partial and full rendering.

    The endpoint function _must_ have a partial render dependency, and
    _can_ have a full render dependency.

    When htmx makes a request from the the users browser, the partial render
    is called and returned. Otherwise, the full renderer is called.

    Use FastAPI dependency injection to resolve data for your templates.

    Make sure to use the `@full` decorator on the full renderer to prevent
    it from being evaluated before it is needed.
    """

    @wraps(func)
    async def wrapper(
        *,
        request: Request,
        partial: Element,
        full: None | Callable[..., Element] = None,
    ) -> str:
        """Wrap function."""
        hx_request = "HX-Request" in request.headers
        if hx_request:
            return partial.dump()

        # Return partial if full render is not available.
        if full is None:
            return partial.dump()

        return full().dump()

    return wrapper  # type: ignore


def full(func: Callable[..., T]) -> Callable[..., Callable[..., T]]:
    """Mark a function as a full renderer.

    This will prevent the function from being evaluated before it is needed
    """

    @wraps(func)
    def deferred_renderer(*args: Any, **kwargs: Any) -> Callable[..., T]:
        return lambda: func(*args, **kwargs)

    return deferred_renderer


def add_htmx_middleware(app: FastAPI) -> None:
    """Add middleware to the app that adds the Vary: Accept header.

    This allows the browser to cache the responses based on caller,
    which should prevent the browser from caching htmx responses as a full page
    """
    if getattr(app.state, "hypermedia_htmx_middleware", False):
        return

    @app.middleware("http")
    async def add_vary_accept_header(  # type: ignore
        request: Request,
        call_next,
    ) -> Response:
        response: Response = await call_next(request)
        response.headers["Vary"] = "Accept"
        return response

    app.state.hypermedia_htmx_middleware = True
