from hypermedia.models import BaseElement, Element, VoidElement

"""
All basic html tags as defined by W3Schools.
"""


class Doctype(Element):
    """Defines the document type."""

    def dump(self) -> str:
        """Dump doctype string."""
        return "<!DOCTYPE html>"


class Html(BaseElement):
    """Defines an HTML document."""

    tag: str = "html"


class Head(BaseElement):
    """Contains metadata/information for the document."""

    tag: str = "head"


class Title(BaseElement):
    """Defines a title for the document."""

    tag: str = "title"


class Body(BaseElement):
    """Defines the document's body."""

    tag: str = "body"


class H1(BaseElement):
    """Defines HTML heading 1."""

    tag: str = "h1"


class Header1(H1):
    """Alias for h1 tag."""


class H2(BaseElement):
    """Defines HTML heading 2."""

    tag: str = "h2"


class Header2(H2):
    """Alias for h2 tag."""


class H3(BaseElement):
    """Defines HTML heading 3."""

    tag: str = "h3"


class Header3(H3):
    """Alias for h3 tag."""


class H4(BaseElement):
    """Defines HTML heading 4."""

    tag: str = "h4"


class Header4(H4):
    """Alias for h4 tag."""


class H5(BaseElement):
    """Defines HTML heading 5."""

    tag: str = "h5"


class Header5(H5):
    """Alias for h5 tag."""


class H6(BaseElement):
    """Defines HTML heading 6."""

    tag: str = "h6"


class Header6(H6):
    """For h6 tag."""


class P(BaseElement):
    """Defines a paragraph."""

    tag: str = "p"


class Paragraph(P):
    """Alias for p tag."""


class Br(VoidElement):
    """Inserts a single line break."""

    tag: str = "br"


class Break(Br):
    """Alias for br tag."""


class Hr(VoidElement):
    """Defines a thematic change in the content."""

    tag: str = "hr"


class HorizontalRule(Hr):
    """Alias for hr tag."""


class Comment(BaseElement):
    """Defines a comment."""

    def dump(self) -> str:
        """Dump to html."""
        return "<!-- {text} -->".format(text=self.text or "")


# william <- my son writing his name.
