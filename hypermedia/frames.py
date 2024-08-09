from typing import Unpack

from hypermedia.models.elements import Element
from hypermedia.models.types import NoChildren
from hypermedia.types.attributes import IframeAttrs


class IFrame(Element[NoChildren, IframeAttrs]):
    """Defines an inline frame."""

    tag: str = "iframe"

    def __init__(self, **attributes: Unpack[IframeAttrs]) -> None:
        super().__init__(**attributes)
