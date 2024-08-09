from typing import Unpack

from hypermedia.models import Element, VoidElement
from hypermedia.models.types import AnyChildren, ComplexChildren
from hypermedia.types.attributes import ColAttrs, GlobalAttrs, TdAttrs, ThAttrs


class Table(Element[ComplexChildren, GlobalAttrs]):
    """Defines a table."""

    tag: str = "table"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Caption(Element[AnyChildren, GlobalAttrs]):
    """Defines a table caption."""

    tag: str = "caption"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Th(Element[AnyChildren, ThAttrs]):
    """Defines a header cell in a table."""

    tag: str = "th"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[ThAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableHeader(Th):
    """Alias for `Th`."""


class Tr(Element[ComplexChildren, GlobalAttrs]):
    """Defines a row in a table."""

    tag: str = "tr"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableRow(Tr):
    """Alias for `Tr`."""


class Td(Element[AnyChildren, TdAttrs]):
    """Defines a cell in a table."""

    tag: str = "td"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[TdAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableData(Td):
    """Alias for `Td`."""


class THead(Element[ComplexChildren, GlobalAttrs]):
    """Groups the header content in a table."""

    tag: str = "thead"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableHead(THead):
    """Alias for `THead`."""


class TBody(Element[ComplexChildren, GlobalAttrs]):
    """Groups the body content in a table."""

    tag: str = "tbody"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableBody(TBody):
    """Alias for `TBody`."""


class TFoot(Element[ComplexChildren, GlobalAttrs]):
    """Groups the footer content in a table."""

    tag: str = "tfoot"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableFoot(TFoot):
    """Alias for `TFoot`."""


class Col(VoidElement[ColAttrs]):
    """
    Specifies column properties.

    For each column within a `colgroup` element.
    """

    tag: str = "col"

    def __init__(self, **attributes: Unpack[ColAttrs]) -> None:
        super().__init__(**attributes)


class Column(Col):
    """Alias for `Col`."""


class ColGroup(Element[AnyChildren, GlobalAttrs]):
    """Specifies a group of one or more columns in a table for formatting."""

    tag: str = "colgroup"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class ColumnGroup(ColGroup):
    """Alias for `ColGroup`."""
