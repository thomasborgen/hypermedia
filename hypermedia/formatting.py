from hypermedia.models import BaseElement, VoidElement


class Abbr(BaseElement):
    """Defines an abbreviation or an acronym."""

    tag: str = "abbr"


class Abbreviation(Abbr):
    """Alias for `Abbr`."""


class Address(BaseElement):
    """Defines contact information for the author of a document/article."""

    tag: str = "address"


class B(BaseElement):
    """Defines bold text."""

    tag: str = "b"


class Bold(B):
    """Alias for `B`."""


class Bdi(BaseElement):
    """
    BDI stands for Bi-Directional Isolation.

    Isolates a part of text that might be formatted in a different direction
    from other text outside it.
    """

    tag: str = "bdi"


class BiDirectionalIsolation(Bdi):
    """Alias for `Bdi`."""


class Bdo(BaseElement):
    """
    BDO stands for Bi-Directional Override.

    Overrides the current text direction.
    """

    tag: str = "bdo"


class BiDirectionalOverride(Bdo):
    """Alias for `Bdo`."""


class Blockquote(BaseElement):
    """Defines a section that is quoted from another source."""

    tag: str = "blockquote"


class Cite(BaseElement):
    """Defines the title of a work."""

    tag: str = "cite"


class Code(BaseElement):
    """Defines a piece of computer code."""

    tag: str = "code"


class Del(BaseElement):
    """Defines text that has been deleted from a document."""

    tag: str = "del"


class Deleted(Del):
    """Alias for del tag."""


class Dfn(BaseElement):
    """
    DFN stands for definition element.

    Specifies a term that is going to be defined within the content.
    """

    tag: str = "dfn"


class DefinitionElement(Dfn):
    """Alias for `Dfn`."""


class Em(BaseElement):
    """Defines emphasized text ."""

    tag: str = "em"


class Emphasized(Em):
    """Alias for `Em`."""


class I(BaseElement):  # noqa: E742
    """Defines a part of text in an alternate voice or mood."""

    tag: str = "i"


class Italic(I):
    """Alias for `I`."""


class Ins(BaseElement):
    """Defines a text that has been inserted into a document."""

    tag: str = "ins"


class Inserted(Ins):
    """Alias for `Ins`."""


class Kbd(BaseElement):
    """Defines keyboard input."""

    tag: str = "kbd"


class Keyboard(Kbd):
    """Alias for `Kbd`."""


class Mark(BaseElement):
    """Defines marked/highlighted text."""

    tag: str = "mark"


class Meter(BaseElement):
    """Defines a scalar measurement within a known range (a gauge)."""

    tag: str = "meter"


class Pre(BaseElement):
    """Defines preformatted text."""

    tag: str = "pre"


class Preformatted(Pre):
    """Alias for `Pre`."""


class Progress(BaseElement):
    """Represents the progress of a task."""

    tag: str = "progress"


class Q(BaseElement):
    """Defines a short quotation."""

    tag: str = "q"


class Quotation(Q):
    """Alias for `Abbr`."""


class Rp(BaseElement):
    """Defines what to show in browsers that don't support ruby annotations."""

    tag: str = "rp"


class Rt(BaseElement):
    """Defines an explanation/pronunciation of characters."""

    tag: str = "rt"


class ruby(BaseElement):
    """Defines a ruby annotation (for East Asian typography)."""

    tag: str = "ruby"


class S(BaseElement):
    """Defines text that is no longer correct."""

    tag: str = "s"


class StrikeThrough(S):
    """Alias for `S`."""


class Samp(BaseElement):
    """Defines sample output from a computer program."""

    tag: str = "samp"


class SampleOutput(Samp):
    """Alias for `Samp`."""


class Small(BaseElement):
    """Defines smaller text."""

    tag: str = "small"


class Strong(BaseElement):
    """Defines important text."""

    tag: str = "strong"


class Sub(BaseElement):
    """Defines subscripted text."""

    tag: str = "sub"


class Subscripted(Sub):
    """Alias for `Sub`."""


class Sup(BaseElement):
    """Defines superscripted text."""

    tag: str = "sup"


class Superscripted(Sup):
    """Alias for `Sup`."""


class Template(BaseElement):
    """Defines a container for content, that should be hidden on page load."""

    tag: str = "template"


class Time(BaseElement):
    """Defines a specific time (or datetime)."""

    tag: str = "time"


class U(BaseElement):
    """
    Defines unarticulated text.

    This is also styled differently from normal text.
    """

    tag: str = "u"


class Unarticulated(U):
    """Alias for `U`."""


class Var(BaseElement):
    """Defines a variable."""

    tag: str = "var"


class Variable(Var):
    """Alias for `Var`."""


class Wbr(VoidElement):
    """
    Defines a possible line-break.

    WBR stands for Word Break Opportunity.
    """

    tag: str = "wbr"


class WordBreakOpportunity(Wbr):
    """Alias for `Wbr`."""
