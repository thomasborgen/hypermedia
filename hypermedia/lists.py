from typing import Unpack

from hypermedia.models import Element
from hypermedia.models.types import AnyChildren, ComplexChildren
from hypermedia.types.attributes import GlobalAttrs, LiAttrs, OlAttrs


class Menu(Element[AnyChildren, GlobalAttrs]):
    """Defines an alternative unordered list."""

    tag: str = "menu"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Ul(Element[ComplexChildren, GlobalAttrs]):
    """Defines an unordered list."""

    tag: str = "ul"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class UnorderedList(Ul):
    """Alias for `Ul`."""


class Ol(Element[ComplexChildren, OlAttrs]):
    """Defines an ordered list."""

    tag: str = "ol"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[OlAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class OrderedList(Ol):
    """Alias for `Ol`."""


class Li(Element[AnyChildren, LiAttrs]):
    """Defines a list item."""

    tag: str = "li"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[LiAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class ListItem(Li):
    """Alias for `Li`."""


class Dl(Element[ComplexChildren, GlobalAttrs]):
    """Defines a description list."""

    tag: str = "dl"

    def __init__(
        self, *children: ComplexChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class DescriptionList(Dl):
    """Alias for `Dl`."""


class Dt(Element[AnyChildren, GlobalAttrs]):
    """Defines a term/name in a description list."""

    tag: str = "dt"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class DescriptionListTerm(Dt):
    """Alias for `Dt`."""


class Dd(Element[AnyChildren, GlobalAttrs]):
    """Defines a description of a term/name in a description list."""

    tag: str = "dd"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class DescriptionListTermDescription(Dd):
    """Alias for `Dd`."""
