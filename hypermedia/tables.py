from hypermedia.models import BaseElement, VoidElement


class Table(BaseElement):
    """Defines a table."""

    tag: str = "table"


class Caption(BaseElement):
    """Defines a table caption."""

    tag: str = "caption"


class Th(BaseElement):
    """Defines a header cell in a table."""

    tag: str = "th"


class TableHeader(Th):
    """Alias for `Th`."""


class Tr(BaseElement):
    """Defines a row in a table."""

    tag: str = "tr"


class TableRow(Tr):
    """Alias for `Tr`."""


class Td(BaseElement):
    """Defines a cell in a table."""

    tag: str = "td"


class TableData(Td):
    """Alias for `Td`."""


class THead(BaseElement):
    """Groups the header content in a table."""

    tag: str = "thead"


class TableHead(THead):
    """Alias for `THead`."""


class TBody(BaseElement):
    """Groups the body content in a table."""

    tag: str = "tbody"


class TableBody(TBody):
    """Alias for `TBody`."""


class TFoot(BaseElement):
    """Groups the footer content in a table."""

    tag: str = "tfoot"


class TableFoot(TFoot):
    """Alias for `TFoot`."""


class Col(VoidElement):
    """
    Specifies column properties.

    For each column within a `colgroup` element.
    """

    tag: str = "col"


class Column(Col):
    """Alias for `Col`."""


class ColGroup(BaseElement):
    """Specifies a group of one or more columns in a table for formatting."""

    tag: str = "colgroup"


class ColumnGroup(ColGroup):
    """Alias for `ColGroup`."""
