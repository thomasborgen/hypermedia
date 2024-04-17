from hypermedia.models import VoidElement


class Meta(VoidElement):
    """Defines metadata about an HTML document."""

    tag: str = "meta"


class Base(VoidElement):
    """Specifies the base URL/target for all relative URLs in a document."""

    tag: str = "base"
