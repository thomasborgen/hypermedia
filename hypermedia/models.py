from abc import ABCMeta, abstractmethod

from typing_extensions import Self


def get_child_slots(
    slots: dict[str, "Element"], children: list["Element"]
) -> dict[str, "Element"]:
    """Get slots from direct child."""
    slot_keys = slots.keys()

    for child in children:
        if duplicate_keys := [
            key for key in child.slots.keys() if key in slot_keys
        ]:
            raise ValueError(
                f"All slot names must be unique: {duplicate_keys}"
            )
        else:
            slots.update(child.slots)
    return slots


def get_slots(
    children: list["Element"],
) -> dict[str, "Element"]:
    """Calculate slots."""
    slots: dict[str, "Element"] = {}
    for child in children:
        if child.slot:
            if child.slot in slots:
                raise ValueError(
                    f"All slot names must be unique: {child.slot}"
                )
            slots[child.slot] = child
        if child.children:
            get_child_slots(slots, child.children)

    return slots


class Element(metaclass=ABCMeta):
    """
    Base class for all elements.

    This handles handles slot extension, children, attributes and
    css classes.
    """

    children: list["Element"]
    slot: str | None = None
    slots: dict[str, "Element"]
    attributes: dict[str, str | bool]

    def __init__(
        self,
        *children: "Element",
        slot: str | None = None,
        **attributes: str | bool,
    ) -> None:
        """Initialize Root with children."""
        self.children = list(children)
        self.slot = slot
        self.slots = get_slots([self])
        self.attributes = self._parse_attributes(attributes)

    @abstractmethod
    def dump(self) -> str:
        """Dump the objects to a html document string."""
        pass

    def extend(self, slot: str, *children: "Element") -> Self:
        """Extend the child with the given slots children."""
        if slot not in self.slots:
            raise ValueError(f"Could not find a slot with name: {slot}")
        element = self.slots[slot]
        element.children.extend(children)

        get_child_slots(self.slots, list(children))
        return self

    def _parse_attributes(
        self, attributes: dict[str, str | bool]
    ) -> dict[str, str | bool]:
        hx_keys = [key for key in attributes.keys() if key.startswith("hx_")]
        for key in hx_keys:
            new_key = key.replace("_", "-")
            attributes[new_key] = attributes.pop(key)
        return attributes

    def _render_attributes(self) -> str:
        result = []
        for key, value in self.attributes.items():
            # Skip false booleans attributes
            if value is False:
                continue
            if value is True:
                result.append(key)
                continue
            result.append(f"{key}='{value}'")
        if result:
            return " " + " ".join(result)
        return ""

    def _render_children(self) -> str:
        return "".join([child.dump() for child in self.children])


class ElementList(Element):
    """Does not yield encompassing tag, only dumps children."""

    def dump(self) -> str:
        """Dump the objects to a html document string."""
        return "".join(child.dump() for child in self.children)


class BaseElement(Element):
    """Baseclass for all html tags."""

    tag: str
    id: str | None
    classes: list[str]
    text: str | None

    def __init__(
        self,
        *children: "Element",
        id: str | None = None,
        classes: list[str] | None = None,
        text: str | None = None,
        slot: str | None = None,
        **properties: str | bool,
    ) -> None:
        """Initialize class."""
        super().__init__(*children, slot=slot, **properties)
        self.id = id
        self.classes = classes or []
        self.text = text

    def dump(self) -> str:
        """Dump to html."""
        return (
            "<{tag}{id}{classes}{attributes}>{text}{children}</{tag}>".format(
                tag=self.tag,
                id=f" id={self.id}" if self.id else "",
                classes=self._render_classes(),
                attributes=self._render_attributes(),
                text=self.text or "",
                children=self._render_children(),
            )
        )

    def _render_classes(self) -> str:
        if not self.classes:
            return ""
        return f' class="{" ".join(self.classes)}"'

    def __str__(self) -> str:
        """Return tag."""
        return self.tag


class VoidElement(Element):
    """
    A void element is an element in HTML that cannot have any child nodes.

    Void elements only have a start tag; end tags must not be specified for
    void elements.
    """

    tag: str
    id: str | None
    classes: list[str]
    kwargs: dict[str, str]

    def __init__(
        self,
        *,
        id: str | None = None,
        classes: list[str] | None = None,
        **kwargs: str,
    ) -> None:
        """Initialize class."""
        super().__init__(**kwargs)
        self.id = id
        self.classes = classes or []

    def dump(self) -> str:
        """Dump to html."""
        return """<{tag}{id}{classes}{attributes}>""".format(
            tag=self.tag,
            id=f" id={self.id}" if self.id else "",
            classes=self._render_classes(),
            attributes=self._render_attributes(),
        )

    def _render_classes(self) -> str:
        if not self.classes:
            return ""
        return f' class="{" ".join(self.classes)}"'

    def __str__(self) -> str:
        """Return tag."""
        return self.tag
