from typing_extensions import Unpack

from hypermedia.models import VoidElement
from hypermedia.types.attributes import BaseAttrs, MetaAttrs


class Meta(VoidElement[MetaAttrs]):
    """Defines metadata about an HTML document."""

    tag: str = "meta"

    def __init__(self, **attributes: Unpack[MetaAttrs]) -> None:
        super().__init__(**attributes)


class Base(VoidElement[BaseAttrs]):
    """Specifies the base URL/target for all relative URLs in a document."""

    tag: str = "base"

    def __init__(self, **attributes: Unpack[BaseAttrs]) -> None:
        super().__init__(**attributes)
