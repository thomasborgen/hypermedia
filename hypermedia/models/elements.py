from typing import (
    Generic,
    Unpack,
)

from hypermedia.models.base import BaseElement
from hypermedia.types.attributes import NoAttrs
from hypermedia.types.types import TAttrs, TChildren, TChildrenArgs


class Element(Generic[TChildren, TAttrs], BaseElement):
    """Base class for Hypermedia elements."""

    children: tuple[TChildren, ...]
    attributes: TAttrs

    tag: str

    def __init__(  # type: ignore
        self,
        *children: TChildren,
        # FIXME: https://github.com/python/typing/issues/1399
        **attributes: Unpack[TAttrs],  # type: ignore
    ) -> None:
        super().__init__(*children, **attributes)
        self.slot = attributes.pop("slot", None)

    def dump(self) -> str:
        """Dump to html, while escaping text data."""
        return "<{tag}{attributes}>{children}</{tag}>".format(
            tag=self.tag,
            attributes=self._render_attributes(),
            children=self._render_children(),
        )


class ElementStrict(Generic[Unpack[TChildrenArgs], TAttrs], BaseElement):
    """
    Base class for strict elements (elements with concrete types of children).

    Args:
    ----
        *children: (*TChildTuple): The children of the element.
        **attributes: (Unpack[TAttrs]): The attributes of the element.

    """

    children: tuple[Unpack[TChildrenArgs]]
    attributes: TAttrs

    tag: str

    def __init__(  # type: ignore
        self,
        *children: Unpack[TChildrenArgs],
        # FIXME: https://github.com/python/typing/issues/1399
        **attributes: Unpack[TAttrs],  # type: ignore
    ) -> None:
        super().__init__(*children, **attributes)

    def dump(self) -> str:
        """Dump to html, while escaping text data."""
        return "<{tag}{attributes}>{children}</{tag}>".format(
            tag=self.tag,
            attributes=self._render_attributes(),
            children=self._render_children(),
        )


class ElementList(Element[TChildren, NoAttrs]):
    """Use to render a list of child elements without a parent."""

    def dump(self) -> str:
        """Dump the objects to a html document string."""
        return self._render_children()


class VoidElement(Generic[TAttrs], BaseElement):
    """
    A void element is an element in HTML that cannot have any child nodes.

    Void elements only have a start tag; end tags must not be specified for
    void elements.
    """

    attributes: TAttrs

    tag: str

    def __init__(  # type: ignore
        self,
        *,
        slot: str | None = None,
        # FIXME: https://github.com/python/typing/issues/1399
        **attributes: Unpack[TAttrs],  # type: ignore
    ) -> None:
        super().__init__(slot=slot, **attributes)

    def dump(self) -> str:
        """Dump to html."""
        return """<{tag}{attributes}>""".format(
            tag=self.tag,
            attributes=self._render_attributes(),
        )

    def __str__(self) -> str:
        """Return tag."""
        return self.tag
