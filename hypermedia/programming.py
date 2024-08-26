from typing_extensions import Never, Unpack

from hypermedia.models import BasicElement, VoidElement
from hypermedia.types.attributes import (
    EmbedAttrs,
    GlobalAttrs,
    ObjectAttrs,
    ScriptAttrs,
)
from hypermedia.types.types import AnyChildren, SafeString


class Script(BasicElement[str, ScriptAttrs]):
    """Defines a client-side script."""

    tag: str = "script"

    def __init__(
        self,
        child: str | None = None,
        *args: Never,
        **attributes: Unpack[ScriptAttrs],
    ) -> None:
        if child is None:
            super().__init__(**attributes)
        else:
            super().__init__(SafeString(child), **attributes)


class NoScript(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines alternate content when client-side scripts aren't supported."""

    tag: str = "noscript"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Embed(VoidElement[EmbedAttrs]):
    """Defines a container for an external (non-HTML) application."""

    tag: str = "embed"

    def __init__(self, **attributes: Unpack[EmbedAttrs]) -> None:
        super().__init__(**attributes)


class Object(BasicElement[AnyChildren, ObjectAttrs]):
    """Defines an embedded object."""

    tag: str = "object"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[ObjectAttrs]
    ) -> None:
        super().__init__(*children, **attributes)
