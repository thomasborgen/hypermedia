from typing import (
    Generic,
    Unpack,
)

from hypermedia.models.base import BaseElement
from hypermedia.models.types import TAttrs, TChildren, TChildrenArgs
from hypermedia.types.attributes import NoAttrs


class Element(Generic[TChildren, TAttrs], BaseElement):
    """Base class for Hypermedia elements."""

    children: tuple[TChildren, ...]
    attributes: TAttrs

    tag: str
    classes: list[str]

    def __init__(  # type: ignore
        self,
        *children: TChildren,
        classes: list[str] | None = None,
        # FIXME: https://github.com/python/typing/issues/1399
        **attributes: Unpack[TAttrs],  # type: ignore
    ) -> None:
        super().__init__(*children, **attributes)
        self.slot = attributes.pop("slot", None)
        self.classes = classes or []

    def dump(self) -> str:
        """Dump to html, while escaping text data."""
        return "<{tag}{classes}{attributes}>{children}</{tag}>".format(
            tag=self.tag,
            # id=f" id='{self.id}'" if self.id else "",
            classes=self._render_classes(),
            attributes=self._render_attributes(),
            children=self._render_children(),
        )

    def _render_classes(self) -> str:
        if not self.classes:
            return ""
        return f" class='{' '.join(self.classes)}'"


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
    classes: list[str]

    def __init__(  # type: ignore
        self,
        *children: Unpack[TChildrenArgs],
        classes: list[str] | None = None,
        # FIXME: https://github.com/python/typing/issues/1399
        **attributes: Unpack[TAttrs],  # type: ignore
    ) -> None:
        super().__init__(*children, **attributes)
        self.classes = classes or []

    def dump(self) -> str:
        """Dump to html, while escaping text data."""
        return "<{tag}{classes}{attributes}>{children}</{tag}>".format(
            tag=self.tag,
            # id=f" id='{self.id}'" if self.id else "",
            classes=self._render_classes(),
            attributes=self._render_attributes(),
            children=self._render_children(),
        )

    def _render_classes(self) -> str:
        if not self.classes:
            return ""
        return f" class='{' '.join(self.classes)}'"


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
    classes: list[str]

    def __init__(
        self,
        *,
        slot: str | None = None,
        # FIXME: https://github.com/python/typing/issues/1399
        classes: list[str] | None = None,
        **attributes: Unpack[TAttrs],  # type: ignore
    ) -> None:
        super().__init__(slot=slot, **attributes)
        self.classes = classes or []

    def dump(self) -> str:
        """Dump to html."""
        return """<{tag}{classes}{attributes}>""".format(
            tag=self.tag,
            # id=f" id='{self.id}'" if self.id else "",
            classes=self._render_classes(),
            attributes=self._render_attributes(),
        )

    def _render_classes(self) -> str:
        if not self.classes:
            return ""
        return f" class='{' '.join(self.classes)}'"

    def __str__(self) -> str:
        """Return tag."""
        return self.tag
