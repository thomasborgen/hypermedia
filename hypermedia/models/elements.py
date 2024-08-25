from typing import Generic

from typing_extensions import Unpack

from hypermedia.models.base import Element
from hypermedia.types.types import SafeString, TAttrs, TChildren, TChildrenArgs


class BasicElement(Generic[TChildren, TAttrs], Element):
    """Base class for Hypermedia elements."""

    children: tuple[TChildren, ...]
    attributes: TAttrs

    tag: str

    def __init__(
        self,
        *children: TChildren,
        # FIXME: https://github.com/python/typing/issues/1399
        **attributes: Unpack[TAttrs],  # type: ignore
    ) -> None:
        super().__init__(*children, **attributes)

    def dump(self) -> SafeString:
        """Dump to html, while escaping text data."""
        return SafeString(
            "<{tag}{attributes}>{children}</{tag}>".format(
                tag=self.tag,
                attributes=self._render_attributes(),
                children=self._render_children(),
            )
        )


class ElementStrict(Generic[Unpack[TChildrenArgs], TAttrs], Element):
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

    def __init__(
        self,
        *children: Unpack[TChildrenArgs],
        # FIXME: https://github.com/python/typing/issues/1399
        **attributes: Unpack[TAttrs],  # type: ignore
    ) -> None:
        super().__init__(*children, **attributes)

    def dump(self) -> SafeString:
        """Dump to html, while escaping text data."""
        return SafeString(
            "<{tag}{attributes}>{children}</{tag}>".format(
                tag=self.tag,
                attributes=self._render_attributes(),
                children=self._render_children(),
            )
        )


class ElementList(Generic[TChildren], Element):
    """Use to render a list of child elements without a parent."""

    children: tuple[TChildren, ...]

    def __init__(
        self,
        *children: TChildren,
        slot: str | None = None,
    ) -> None:
        super().__init__(*children, slot=slot)

    def dump(self) -> SafeString:
        """Dump the objects to a html document string."""
        return SafeString(self._render_children())


class VoidElement(Generic[TAttrs], Element):
    """
    A void element is an element in HTML that cannot have any child nodes.

    Void elements only have a start tag; end tags must not be specified for
    void elements.
    """

    attributes: TAttrs

    tag: str

    def __init__(
        self,
        *,
        slot: str | None = None,
        # FIXME: https://github.com/python/typing/issues/1399
        **attributes: Unpack[TAttrs],  # type: ignore
    ) -> None:
        super().__init__(slot=slot, **attributes)

    def dump(self) -> SafeString:
        """Dump to html."""
        return SafeString(
            "<{tag}{attributes}>".format(
                tag=self.tag,
                attributes=self._render_attributes(),
            )
        )

    def __str__(self) -> str:
        """Return tag."""
        return self.tag
