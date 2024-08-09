from typing import Unpack

from hypermedia.models import Element
from hypermedia.models.types import (
    AnyChildren,
    ComplexChildren,
    PrimitiveChildren,
)
from hypermedia.types.attributes import (
    DataAttrs,
    DetailsAttrs,
    DialogAttrs,
    GlobalAttrs,
)


class Style(Element[PrimitiveChildren, GlobalAttrs]):
    """Defines style information for a document."""

    tag: str = "style"

    def __init__(
        self, *children: PrimitiveChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Div(Element[AnyChildren, GlobalAttrs]):
    """Defines a section in a document."""

    tag: str = "div"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Span(Element[AnyChildren, GlobalAttrs]):
    """Defines a section in a document."""

    tag: str = "span"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Header(Element[AnyChildren, GlobalAttrs]):
    """Defines a header for a document or section."""

    tag: str = "header"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class HGroup(Element[ComplexChildren, GlobalAttrs]):
    """Defines a header and related content."""

    tag: str = "hgroup"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class HeaderGroup(HGroup):
    """Alias for `HGroup`."""


class Footer(Element[AnyChildren, GlobalAttrs]):
    """Defines a footer for a document or section."""

    tag: str = "footer"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Main(Element[AnyChildren, GlobalAttrs]):
    """Specifies the main content of a document."""

    tag: str = "main"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Section(Element[AnyChildren, GlobalAttrs]):
    """Defines a section in a document."""

    tag: str = "section"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Search(Element[AnyChildren, GlobalAttrs]):
    """Defines a search section."""

    tag: str = "search"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Article(Element[AnyChildren, GlobalAttrs]):
    """Defines an article."""

    tag: str = "article"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Aside(Element[AnyChildren, GlobalAttrs]):
    """Defines content aside from the page content."""

    tag: str = "aside"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Details(Element[AnyChildren, DetailsAttrs]):
    """Defines additional details that the user can view or hide."""

    tag: str = "details"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[DetailsAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Dialog(Element[AnyChildren, DialogAttrs]):
    """Defines a dialog box or window."""

    tag: str = "dialog"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[DialogAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Summary(Element[AnyChildren, GlobalAttrs]):
    """Defines a visible heading for a `details` element."""

    tag: str = "summary"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Data(Element[AnyChildren, DataAttrs]):
    """Adds a machine-readable translation of a given content."""

    tag: str = "data"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[DataAttrs]
    ) -> None:
        super().__init__(*children, **attributes)
