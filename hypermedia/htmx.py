from functools import wraps
from typing import (
    Any,
    Callable,
    Coroutine,
    Mapping,
    ParamSpec,
    Protocol,
    TypeVar,
)

from hypermedia.models import Element

Param = ParamSpec("Param")
ReturnType = TypeVar("ReturnType")


class RequestWithHeaders(Protocol):
    """Protocol for FastAPI's Request class."""

    headers: Mapping[str, str]


class RequestPartialAndFull(Protocol):
    """Requires, `request`, `partial` and `full` args on decorated function."""

    def __call__(  # noqa: D102
        self, request: RequestWithHeaders, partial: Element, full: Element
    ) -> Coroutine[Any, Any, None]: ...


class RequestAndPartial(Protocol):
    """Requires, `request` and `partial` args on decorated function."""

    def __call__(  # noqa: D102
        self, request: RequestWithHeaders, partial: Element
    ) -> Coroutine[Any, Any, None]: ...


def htmx(
    func: RequestPartialAndFull | RequestAndPartial,
) -> Callable[..., str]:
    """
    Wrap a FastAPI endpoint, to enable partial and full rendering.

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
        request: RequestWithHeaders,
        partial: Element,
        full: None | Callable[..., Element] = None,
    ) -> str:
        """Wrap function."""
        hx_request = "HX-Request" in request.headers
        if hx_request:
            return partial.dump()

        # should probably return some http error if user tries to get a
        # full page load when its not expected.
        return full().dump() if full else ""

    return wrapper  # type: ignore


def full(
    func: Callable[Param, ReturnType],
) -> Callable[Param, Coroutine[Any, Any, Callable[[], ReturnType]]]:
    """Wrap the paru full page render dependency and makes it lazy."""

    @wraps(func)
    async def wrapper(
        *args: Param.args,
        **kwargs: Param.kwargs,
    ) -> Callable[[], ReturnType]:
        """Wrap function."""
        return lambda: func(*args, **kwargs)

    return wrapper
