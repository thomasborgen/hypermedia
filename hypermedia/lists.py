from hypermedia.models import BaseElement


class Menu(BaseElement):
    """Defines an alternative unordered list."""

    tag: str = "menu"


class Ul(BaseElement):
    """Defines an unordered list."""

    tag: str = "ul"


class UnorderedList(Ul):
    """Alias for `Ul`."""


class Ol(BaseElement):
    """Defines an ordered list."""

    tag: str = "ol"


class OrderedList(Ol):
    """Alias for `Ol`."""


class Li(BaseElement):
    """Defines a list item."""

    tag: str = "li"


class ListItem(Li):
    """Alias for `Li`."""


class Dl(BaseElement):
    """Defines a description list."""

    tag: str = "dl"


class DescriptionList(Dl):
    """Alias for `Dl`."""


class Dt(BaseElement):
    """Defines a term/name in a description list."""

    tag: str = "dt"


class DescriptionListTerm(Dt):
    """Alias for `Dt`."""


class Dd(BaseElement):
    """Defines a description of a term/name in a description list."""

    tag: str = "dd"


class DescriptionListTermDescription(Dd):
    """Alias for `Dd`."""
