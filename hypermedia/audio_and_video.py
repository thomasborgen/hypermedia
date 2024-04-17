from hypermedia.models import BaseElement, VoidElement


class Audio(BaseElement):
    """Defines sound content."""

    tag: str = "audio"


class Source(VoidElement):
    """
    Defines multiple media resources for media elements.

    `video`, `audio` and `picture`.
    """

    tag: str = "source"


class Track(VoidElement):
    """Defines text tracks for media elements (`video` and `audio`)."""

    tag: str = "track"


class Video(BaseElement):
    """Defines a video or movie."""

    tag: str = "video"
