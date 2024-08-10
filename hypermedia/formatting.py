from typing_extensions import Unpack

from hypermedia.models import Element, VoidElement
from hypermedia.types.attributes import (
    BlockquoteAttrs,
    DelAttrs,
    GlobalAttrs,
    HtmlAttrs,
    InsAttrs,
    MeterAttrs,
    ProgressAttrs,
    QAttrs,
    TimeAttrs,
)
from hypermedia.types.types import AnyChildren


class Abbr(Element[AnyChildren, GlobalAttrs]):
    """Defines an abbreviation or an acronym."""

    tag: str = "abbr"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Abbreviation(Abbr):
    """Alias for `Abbr`."""


class Address(Element[AnyChildren, GlobalAttrs]):
    """Defines contact information for the author of a document/article."""

    tag: str = "address"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class B(Element[AnyChildren, GlobalAttrs]):
    """Defines bold text."""

    tag: str = "b"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Bold(B):
    """Alias for `B`."""


class Bdi(Element[AnyChildren, GlobalAttrs]):
    """
    BDI stands for Bi-Directional Isolation.

    Isolates a part of text that might be formatted in a different direction
    from other text outside it.
    """

    tag: str = "bdi"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class BiDirectionalIsolation(Bdi):
    """Alias for `Bdi`."""


class Bdo(Element[AnyChildren, GlobalAttrs]):
    """
    BDO stands for Bi-Directional Override.

    Overrides the current text direction.
    """

    tag: str = "bdo"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class BiDirectionalOverride(Bdo):
    """Alias for `Bdo`."""


class Blockquote(Element[AnyChildren, BlockquoteAttrs]):
    """Defines a section that is quoted from another source."""

    tag: str = "blockquote"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[BlockquoteAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Cite(Element[AnyChildren, GlobalAttrs]):
    """Defines the title of a work."""

    tag: str = "cite"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Code(Element[AnyChildren, GlobalAttrs]):
    """Defines a piece of computer code."""

    tag: str = "code"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Del(Element[AnyChildren, DelAttrs]):
    """Defines text that has been deleted from a document."""

    tag: str = "del"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[DelAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Deleted(Del):
    """Alias for del tag."""


class Dfn(Element[AnyChildren, GlobalAttrs]):
    """
    DFN stands for definition element.

    Specifies a term that is going to be defined within the content.
    """

    tag: str = "dfn"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class DefinitionElement(Dfn):
    """Alias for `Dfn`."""


class Em(Element[AnyChildren, GlobalAttrs]):
    """Defines emphasized text ."""

    tag: str = "em"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Emphasized(Em):
    """Alias for `Em`."""


class I(Element[AnyChildren, GlobalAttrs]):  # noqa: E742
    """Defines a part of text in an alternate voice or mood."""

    tag: str = "i"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Italic(I):
    """Alias for `I`."""


class Ins(Element[AnyChildren, InsAttrs]):
    """Defines a text that has been inserted into a document."""

    tag: str = "ins"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[InsAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Inserted(Ins):
    """Alias for `Ins`."""


class Kbd(Element[AnyChildren, GlobalAttrs]):
    """Defines keyboard input."""

    tag: str = "kbd"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Keyboard(Kbd):
    """Alias for `Kbd`."""


class Mark(Element[AnyChildren, GlobalAttrs]):
    """Defines marked/highlighted text."""

    tag: str = "mark"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Meter(Element[AnyChildren, MeterAttrs]):
    """Defines a scalar measurement within a known range (a gauge)."""

    tag: str = "meter"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[MeterAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Pre(Element[AnyChildren, GlobalAttrs]):
    """Defines preformatted text."""

    tag: str = "pre"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Preformatted(Pre):
    """Alias for `Pre`."""


class Progress(Element[AnyChildren, ProgressAttrs]):
    """Represents the progress of a task."""

    tag: str = "progress"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[ProgressAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Q(Element[AnyChildren, QAttrs]):
    """Defines a short quotation."""

    tag: str = "q"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[QAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Quotation(Q):
    """Alias for `Abbr`."""


class Rp(Element[AnyChildren, GlobalAttrs]):
    """Defines what to show in browsers that don't support ruby annotations."""

    tag: str = "rp"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Rt(Element[AnyChildren, GlobalAttrs]):
    """Defines an explanation/pronunciation of characters."""

    tag: str = "rt"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class ruby(Element[AnyChildren, GlobalAttrs]):
    """Defines a ruby annotation (for East Asian typography)."""

    tag: str = "ruby"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class S(Element[AnyChildren, GlobalAttrs]):
    """Defines text that is no longer correct."""

    tag: str = "s"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class StrikeThrough(S):
    """Alias for `S`."""


class Samp(Element[AnyChildren, GlobalAttrs]):
    """Defines sample output from a computer program."""

    tag: str = "samp"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class SampleOutput(Samp):
    """Alias for `Samp`."""


class Small(Element[AnyChildren, GlobalAttrs]):
    """Defines smaller text."""

    tag: str = "small"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Strong(Element[AnyChildren, GlobalAttrs]):
    """Defines important text."""

    tag: str = "strong"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Sub(Element[AnyChildren, GlobalAttrs]):
    """Defines subscripted text."""

    tag: str = "sub"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Subscripted(Sub):
    """Alias for `Sub`."""


class Sup(Element[AnyChildren, GlobalAttrs]):
    """Defines superscripted text."""

    tag: str = "sup"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Superscripted(Sup):
    """Alias for `Sup`."""


class Template(Element[AnyChildren, HtmlAttrs]):
    """Defines a container for content, that should be hidden on page load."""

    tag: str = "template"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[HtmlAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Time(Element[AnyChildren, TimeAttrs]):
    """Defines a specific time (or datetime)."""

    tag: str = "time"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[TimeAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class U(Element[AnyChildren, GlobalAttrs]):
    """
    Defines unarticulated text.

    This is also styled differently from normal text.
    """

    tag: str = "u"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Unarticulated(U):
    """Alias for `U`."""


class Var(Element[AnyChildren, GlobalAttrs]):
    """Defines a variable."""

    tag: str = "var"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Variable(Var):
    """Alias for `Var`."""


class Wbr(VoidElement[GlobalAttrs]):
    """
    Defines a possible line-break.

    WBR stands for Word Break Opportunity.
    """

    tag: str = "wbr"

    def __init__(self, **attributes: Unpack[GlobalAttrs]) -> None:
        super().__init__(**attributes)


class WordBreakOpportunity(Wbr):
    """Alias for `Wbr`."""
