from hypermedia.models import BaseElement, VoidElement


class Script(BaseElement):
    """Defines a client-side script."""

    tag: str = "script"


class NoScript(BaseElement):
    """Defines alternate content when client-side scripts aren't supported."""

    tag: str = "noscript"


class Embed(VoidElement):
    """Defines a container for an external (non-HTML) application."""

    tag: str = "embed"


class Object(BaseElement):
    """Defines an embedded object."""

    tag: str = "object"
