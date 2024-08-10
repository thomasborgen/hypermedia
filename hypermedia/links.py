from typing_extensions import Unpack

from hypermedia.models import BasicElement, VoidElement
from hypermedia.types.attributes import (
    GlobalAttrs,
    HeadLinkAttrs,
    HyperlinkAttrs,
)
from hypermedia.types.types import AnyChildren


class A(BasicElement[AnyChildren, HyperlinkAttrs]):
    """Defines a hyperlink."""

    tag: str = "a"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[HyperlinkAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Anchor(A):
    """Alias for `A`."""


class Link(VoidElement[HeadLinkAttrs]):
    """
    Defines the relationship between a document and an external resource.

    (most used to link to style sheets).
    """

    tag: str = "link"

    def __init__(self, **attributes: Unpack[HeadLinkAttrs]) -> None:
        super().__init__(**attributes)


class Nav(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines navigation links."""

    tag: str = "nav"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)
