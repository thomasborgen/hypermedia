from typing_extensions import Unpack

from hypermedia.models import BasicElement, VoidElement
from hypermedia.types.attributes import ColAttrs, GlobalAttrs, TdAttrs, ThAttrs
from hypermedia.types.types import AnyChildren, ComplexChildren


class Table(BasicElement[ComplexChildren, GlobalAttrs]):
    """Defines a table."""

    tag: str = "table"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Caption(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines a table caption."""

    tag: str = "caption"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Th(BasicElement[AnyChildren, ThAttrs]):
    """Defines a header cell in a table."""

    tag: str = "th"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[ThAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableHeader(Th):
    """Alias for `Th`."""


class Tr(BasicElement[ComplexChildren, GlobalAttrs]):
    """Defines a row in a table."""

    tag: str = "tr"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableRow(Tr):
    """Alias for `Tr`."""


class Td(BasicElement[AnyChildren, TdAttrs]):
    """Defines a cell in a table."""

    tag: str = "td"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[TdAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableData(Td):
    """Alias for `Td`."""


class THead(BasicElement[ComplexChildren, GlobalAttrs]):
    """Groups the header content in a table."""

    tag: str = "thead"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableHead(THead):
    """Alias for `THead`."""


class TBody(BasicElement[ComplexChildren, GlobalAttrs]):
    """Groups the body content in a table."""

    tag: str = "tbody"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class TableBody(TBody):
    """Alias for `TBody`."""


class TFoot(BasicElement[ComplexChildren, GlobalAttrs]):
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


class ColGroup(BasicElement[AnyChildren, GlobalAttrs]):
    """Specifies a group of one or more columns in a table for formatting."""

    tag: str = "colgroup"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class ColumnGroup(ColGroup):
    """Alias for `ColGroup`."""
