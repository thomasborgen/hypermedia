from typing_extensions import Unpack

from hypermedia.models.elements import BasicElement
from hypermedia.types.attributes import IframeAttrs
from hypermedia.types.types import NoChildren


class IFrame(BasicElement[NoChildren, IframeAttrs]):
    """Defines an inline frame."""

    tag: str = "iframe"

    def __init__(self, **attributes: Unpack[IframeAttrs]) -> None:
        super().__init__(**attributes)
