from hypermedia.models import BaseElement


class Style(BaseElement):
    """Defines style information for a document."""

    tag: str = "style"


class Div(BaseElement):
    """Defines a section in a document."""

    tag: str = "div"


class Span(BaseElement):
    """Defines a section in a document."""

    tag: str = "span"


class Header(BaseElement):
    """Defines a header for a document or section."""

    tag: str = "header"


class HGroup(BaseElement):
    """Defines a header and related content."""

    tag: str = "hgroup"


class HeaderGroup(HGroup):
    """Alias for `HGroup`."""


class Footer(BaseElement):
    """Defines a footer for a document or section."""

    tag: str = "footer"


class Main(BaseElement):
    """Specifies the main content of a document."""

    tag: str = "main"


class Section(BaseElement):
    """Defines a section in a document."""

    tag: str = "section"


class Search(BaseElement):
    """Defines a search section."""

    tag: str = "search"


class Article(BaseElement):
    """Defines an article."""

    tag: str = "article"


class Aside(BaseElement):
    """Defines content aside from the page content."""

    tag: str = "aside"


class Details(BaseElement):
    """Defines additional details that the user can view or hide."""

    tag: str = "details"


class Dialog(BaseElement):
    """Defines a dialog box or window."""

    tag: str = "dialog"


class Summary(BaseElement):
    """Defines a visible heading for a `details` element."""

    tag: str = "summary"


class Data(BaseElement):
    """Adds a machine-readable translation of a given content."""

    tag: str = "data"
