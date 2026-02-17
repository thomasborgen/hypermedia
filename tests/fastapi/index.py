from typing import Annotated

from fastapi import Depends

from hypermedia import Div, Element


def render_index_partial() -> Element:
    """Return partial HTML."""
    print("HEI HEI HHALLO PARTIAL")
    return Div("partial")


def render_index(
    partial: Annotated[Element, Depends(render_index_partial)],
) -> Element:
    """Return full HTML."""

    print("HEI HEI HALO FULL")
    return Div("full", partial)
