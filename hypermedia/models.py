from abc import ABCMeta, abstractmethod
from enum import StrEnum
from html import escape
from typing import Any, AnyStr, Generic, Literal, TypeAlias, TypeVar, Union

from typing_extensions import Self

Attribute: TypeAlias = str | bool | None

Child: TypeAlias = Union["Element", str]
Children: TypeAlias = list[Child]


def get_child_slots(
    slots: dict[str, "Element"], children: Children
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
    elements: Children,
) -> dict[str, "Element"]:
    """Calculate slots."""
    slots: dict[str, "Element"] = {}
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


class Element(metaclass=ABCMeta):
    """
    Base class for all elements.

    This handles handles slot extension, children, attributes and
    css classes.
    """

    children: Children
    slot: str | None = None
    slots: dict[str, "Element"]
    attributes: dict[str, Attribute]

    def __init__(
        self,
        *children: Child,
        slot: str | None = None,
        **attributes: Attribute,
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

    def extend(self, slot: str, *children: Child) -> Self:
        """Extend the child with the given slots children."""
        if slot not in self.slots:
            raise ValueError(f"Could not find a slot with name: {slot}")
        element = self.slots[slot]
        element.children.extend(children)

        get_child_slots(self.slots, list(children))
        return self

    def _parse_attributes(
        self, attributes: dict[str, Attribute]
    ) -> dict[str, Attribute]:
        hx_keys = [key for key in attributes.keys() if key.startswith("hx_")]
        for key in hx_keys:
            new_key = key.replace("_", "-")
            attributes[new_key] = attributes.pop(key)
        return attributes

    def _render_attributes(self) -> str:
        result = []
        for key, value in self.attributes.items():
            # Skip None values, use `True` for key only values or empty string
            # if you need an empty string attribute.
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


class ElementList(Element):
    """Does not yield encompassing tag, only dumps children."""

    def dump(self) -> str:
        """Dump the objects to a html document string."""
        return self._render_children()


# String: TypeAlias = str

String = TypeVar("String", bound=str)


class SwapOptions(StrEnum):
    """Swap options."""

    innerHTML = "innerHTML"
    outerHTML = "outerHTML"
    beforebegin = "beforebegin"
    afterbegin = "afterbegin"
    beforeend = "beforeend"
    afterend = "afterend"
    delete = "delete"


class HtmxElement(Element):
    """Htmx element."""

    hx_get: str
    hx_post: str
    hx_push_url: Literal["true"] | str
    hx_select: str

    hx_swap: Literal[
        "innerHTML",
        "outerHTML",
        "beforebegin",
        "afterbegin",
        "beforeend",
        "afterend",
        "delete",
    ]

    hx_target: str

    hx_request: str
    hx_trigger: (
        Literal["load", "click", "dblclick", "hover", "focus", "blur"] | str
    )

    hx_include: str
    hx_indicator: str
    hx_params: Literal["*", "none"] | list[str]
    hx_prompt: str
    hx_sse: str  # URL to open a Server-Sent Events connection.
    hx_ws: str  # URL to open a WebSocket connection.
    hx_boost: Literal[
        "true", "false"
    ]  # Enables htmx to boost links and forms.
    hx_swap_oob: Literal["true", "false"]  # Allows out-of-band swaps.

    hx_headers: dict[
        str, Any
    ]  # JSON object to add custom headers to the request.
    hx_encoding: Literal[
        "text/plain",
        "application/x-www-form-urlencoded",
        "multipart/form-data",
    ]  # Specifies how to encode the request. Possible values:

    hx_vals: dict[
        str, Any
    ]  # JSON object to send additional values with the request.

    hx_history_elt: (
        str  # CSS selector to specify an element for history handling.
    )

    def __init__(  # noqa: PLR0913
        self,
        hx_get: str,
        hx_post: str,
        hx_push_url: Literal["true"] | String,
        hx_select: str,
        hx_swap: SwapOptions,
        hx_target: str,
        hx_request: str,
        hx_trigger: (
            Literal["load", "click", "dblclick", "hover", "focus", "blur"]
            | String
        ),
        hx_include: str,
        hx_indicator: str,
        hx_params: Literal["*", "none"] | list[str],
        hx_prompt: str,
        hx_sse: str,
        hx_ws: str,
        hx_boost: Literal["true", "false"],
        hx_swap_oob: Literal["true", "false"],
        hx_headers: dict[str, Any],
        hx_encoding: Literal[
            "text/plain",
            "application/x-www-form-urlencoded",
            "multipart/form-data",
        ],
        hx_vals: dict[str, Any],
        hx_history_elt: str,
    ) -> None:
        self.hx_get = hx_get
        self.hx_post = hx_post
        self.hx_push_url = hx_push_url
        self.hx_select = hx_select
        self.hx_swap = hx_swap
        self.hx_target = hx_target
        self.hx_request = hx_request
        self.hx_trigger = hx_trigger
        self.hx_include = hx_include
        self.hx_indicator = hx_indicator
        self.hx_params = hx_params
        self.hx_prompt = hx_prompt
        self.hx_sse = hx_sse
        self.hx_ws = hx_ws
        self.hx_boost = hx_boost
        self.hx_swap_oob = hx_swap_oob
        self.hx_headers = hx_headers
        self.hx_encoding = hx_encoding
        self.hx_vals = hx_vals
        self.hx_history_elt = hx_history_elt


HtmxElement(hx_push_url="test")


class BaseElement(Element):
    """Baseclass for all html tags."""

    tag: str
    id: str | None
    classes: list[str]
    text: str | None
    composed_text: list[str | Element] | None

    def __init__(
        self,
        *children: Child,
        id: str | None = None,
        classes: list[str] | None = None,
        composed_text: list[str | Element] | None = None,
        slot: str | None = None,
        **properties: str | bool,
    ) -> None:
        """Initialize class."""
        super().__init__(*children, slot=slot, **properties)
        self.id = id
        self.classes = classes or []

    def dump(self) -> str:
        """Dump to html, while escaping text data."""
        return "<{tag}{id}{classes}{attributes}>{children}</{tag}>".format(
            tag=self.tag,
            id=f" id='{self.id}'" if self.id else "",
            classes=self._render_classes(),
            attributes=self._render_attributes(),
            children=self._render_children(),
        )

    def _render_classes(self) -> str:
        if not self.classes:
            return ""
        return f" class='{' '.join(self.classes)}'"

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
    attributes: dict[str, Attribute]

    def __init__(
        self,
        *,
        id: str | None = None,
        classes: list[str] | None = None,
        **attributes: Attribute,
    ) -> None:
        """Initialize class."""
        super().__init__(**attributes)  # type: ignore
        self.id = id
        self.classes = classes or []

    def dump(self) -> str:
        """Dump to html."""
        return """<{tag}{id}{classes}{attributes}>""".format(
            tag=self.tag,
            id=f" id='{self.id}'" if self.id else "",
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
