from abc import ABCMeta, abstractmethod
from html import escape
from typing import Any, Mapping, Sequence, Union

from typing_extensions import Self


def get_child_slots(
    slots: dict[str, "BaseElement"],
    children: Sequence[Union[str, "BaseElement"]],
) -> dict[str, "BaseElement"]:
    """Get slots from direct child."""
    slot_keys = slots.keys()

    for child in children:
        if isinstance(child, str):
            continue

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
    elements: Sequence[Union[str, "BaseElement"]],
) -> dict[str, "BaseElement"]:
    """Calculate slots."""
    slots: dict[str, "BaseElement"] = {}
    for child in elements:
        if isinstance(child, str):
            continue
        if child.slot:
            if child.slot in slots:
                raise ValueError(
                    f"All slot names must be unique: {child.slot}"
                )
            slots[child.slot] = child
        if child.children:
            get_child_slots(slots, child.children)

    return slots


class BaseElement(metaclass=ABCMeta):
    """
    Base class for all elements.

    This handles handles slot extension, children, attributes and
    css classes.
    """

    children: tuple[Any, ...]
    slot: str | None = None
    slots: dict[str, "BaseElement"]
    attributes: Mapping[str, Any]

    def __init__(
        self,
        *children: Any,
        slot: str | None = None,
        **attributes: Any,
    ) -> None:
        """Initialize Root with children."""
        self.children = children
        self.slot = slot
        self.slots = get_slots([self])
        self.attributes = self._parse_attributes(attributes)

    @abstractmethod
    def dump(self) -> str:
        """Dump the objects to a html document string."""
        pass

    def extend(self, slot: str, *children: Union[str, "BaseElement"]) -> Self:
        """Extend the child with the given slots children."""
        if slot not in self.slots:
            raise ValueError(f"Could not find a slot with name: {slot}")
        element = self.slots[slot]
        element.children = element.children + children

        get_child_slots(self.slots, list(children))
        return self

    def _parse_attributes(self, attributes: dict[str, Any]) -> dict[str, Any]:
        hx_keys = [key for key in attributes.keys() if key.startswith("hx_")]
        for key in hx_keys:
            new_key = key.replace("_", "-")
            attributes[new_key] = attributes.pop(key)
        return attributes

    def _render_attributes(self) -> str:
        result = []
        for key, value in self.attributes.items():
            # Skip None values, use `True` for key only values
            if value is None:
                continue
            # Skip false boolean attributes
            if value is False:
                continue
            # Add true boolean attributes as key only.
            if value is True:
                result.append(key)
                continue
            result.append(f"{key}='{value}'")
        if result:
            return " " + " ".join(result)
        return ""

    def _render_children(self) -> str:
        return "".join(
            [
                escape(child) if isinstance(child, str) else child.dump()
                for child in self.children
            ]
        )
