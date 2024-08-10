import inspect
from abc import ABCMeta, abstractmethod
from functools import lru_cache
from html import escape
from typing import (
    Any,
    Mapping,
    Sequence,
    Union,
    get_type_hints,
)

from typing_extensions import Self


@lru_cache
def _load_attribute_aliases() -> Mapping[str, str]:  # noqa: C901
    """
    Get a mapping of attribute names to their aliases.

    Taken from Ludic:
    https://github.com/getludic/ludic/blob/main/ludic/format.py
    """
    from hypermedia.types import attributes

    result = {}
    for name, cls in inspect.getmembers(attributes, inspect.isclass):
        if not name.endswith("Attrs"):
            continue

        hints = get_type_hints(cls, include_extras=True)
        for key, value in hints.items():
            if metadata := getattr(value, "__metadata__", None):
                for meta in metadata:
                    if isinstance(meta, attributes.Alias):
                        result[key] = str(meta)

    return result


def get_child_slots(
    slots: dict[str, "Element"],
    children: Sequence[Union[str, "Element"]],
) -> dict[str, "Element"]:
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
    element: "Element",
) -> dict[str, "Element"]:
    """Calculate slots."""
    slots: dict[str, "Element"] = {}

    if element.slot:
        slots[element.slot] = element

    if element.children:
        get_child_slots(slots, element.children)

    return slots


class Element(metaclass=ABCMeta):
    """
    Base class for all elements.

    This handles handles slot extension, children, attributes and
    css classes.
    """

    children: tuple[Any, ...]
    slot: str | None = None
    slots: dict[str, "Element"]
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
        self.slots = get_slots(self)
        self.attributes = attributes

    @abstractmethod
    def dump(self) -> str:
        """Dump the objects to a html document string."""
        pass

    def extend(self, slot: str, *children: Union[str, "Element"]) -> Self:
        """Extend the child with the given slots children."""
        if slot not in self.slots:
            raise ValueError(f"Could not find a slot with name: {slot}")
        element = self.slots[slot]
        element.children = element.children + children

        get_child_slots(self.slots, list(children))
        return self

    def _render_attributes(self) -> str:  # noqa: C901
        result = []

        attribute_aliases = _load_attribute_aliases()

        for key, value in self.attributes.items():
            # Skip None values, use `True` for key only values
            if value is None:
                continue
            # Skip false boolean attributes
            if value is False:
                continue

            alias = attribute_aliases.get(key, key)

            # Add true boolean attributes as key only.
            if value is True:
                result.append(alias)
                continue

            # Add css classes
            if alias == "class" and len(value) > 0:
                result.append(f"{alias}='{' '.join(value)}'")
                continue

            result.append(f"{alias}='{value}'")

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
