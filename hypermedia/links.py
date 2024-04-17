from hypermedia.models import BaseElement, VoidElement


class A(BaseElement):
    """Defines a hyperlink."""

    tag: str = "a"


class Anchor(A):
    """Alias for `A`."""


class Link(VoidElement):
    """
    Defines the relationship between a document and an external resource.

    (most used to link to style sheets).
    """

    tag: str = "link"


class Nav(BaseElement):
    """Defines navigation links."""

    tag: str = "nav"
