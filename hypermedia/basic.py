from html import escape

from typing_extensions import Unpack

from hypermedia.models import BasicElement, Element, VoidElement
from hypermedia.models.elements import ElementStrict
from hypermedia.types.attributes import (
    GlobalAttrs,
    HtmlTagAttrs,
    HypermediaAttrs,
    NoAttrs,
)
from hypermedia.types.types import AnyChildren, PrimitiveChildren

"""
All basic html tags as defined by W3Schools.
"""


class Doctype(Element):
    """Defines the document type."""

    def dump(self) -> str:
        """Dump doctype string."""
        return "<!DOCTYPE html>"


class Html(ElementStrict["Head", "Body", HtmlTagAttrs]):
    """Defines an HTML document."""

    tag: str = "html"

    def __init__(
        self,
        *children: Unpack[tuple["Head", "Body"]],
        **attributes: Unpack[HtmlTagAttrs],
    ) -> None:
        super().__init__(*children, **attributes)


class Head(BasicElement[AnyChildren, HypermediaAttrs]):
    """Contains metadata/information for the document."""

    tag: str = "head"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[HypermediaAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Title(BasicElement[PrimitiveChildren, NoAttrs]):
    """Defines a title for the document."""

    tag: str = "title"

    def __init__(
        self, *children: PrimitiveChildren, **attributes: Unpack[NoAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Body(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines the document's body."""

    tag: str = "body"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class H1(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines HTML heading 1."""

    tag: str = "h1"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Header1(H1):
    """Alias for h1 tag."""


class H2(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines HTML heading 2."""

    tag: str = "h2"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Header2(H2):
    """Alias for h2 tag."""


class H3(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines HTML heading 3."""

    tag: str = "h3"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Header3(H3):
    """Alias for h3 tag."""


class H4(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines HTML heading 4."""

    tag: str = "h4"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Header4(H4):
    """Alias for h4 tag."""


class H5(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines HTML heading 5."""

    tag: str = "h5"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Header5(H5):
    """Alias for h5 tag."""


class H6(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines HTML heading 6."""

    tag: str = "h6"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Header6(H6):
    """For h6 tag."""


class P(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines a paragraph."""

    tag: str = "p"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Paragraph(P):
    """Alias for p tag."""


class Br(VoidElement[GlobalAttrs]):
    """Inserts a single line break."""

    tag: str = "br"

    def __init__(self, **attributes: Unpack[GlobalAttrs]) -> None:
        super().__init__(**attributes)


class Break(Br):
    """Alias for br tag."""


class Hr(VoidElement[GlobalAttrs]):
    """Defines a thematic change in the content."""

    tag: str = "hr"

    def __init__(self, **attributes: Unpack[GlobalAttrs]) -> None:
        super().__init__(**attributes)


class HorizontalRule(Hr):
    """Alias for hr tag."""


class Comment(ElementStrict[PrimitiveChildren, NoAttrs]):
    """Defines a comment."""

    children = list[str]

    def __init__(self, *children: PrimitiveChildren) -> None:
        """Initialize class."""
        super().__init__(*children)

    def dump(self) -> str:
        """Dump to html."""
        return "<!-- {text} -->".format(
            text="".join(escape(child) for child in self.children)  # type: ignore
        )


# william <- my son writing his name.
