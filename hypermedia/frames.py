from hypermedia.models import BaseElement


class IFrame(BaseElement):
    """Defines an inline frame."""

    tag: str = "iframe"
