from typing import Annotated

from fastapi import Depends

from hypermedia import Div, Element


def render_index_partial() -> Element:
    """Return partial HTML."""
    return Div("partial")


def render_index(
    partial: Annotated[Element, Depends(render_index_partial)],
) -> Element:
    """Return full HTML."""
    return Div("full", partial)
