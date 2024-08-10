from typing_extensions import Unpack

from hypermedia.models import BasicElement, VoidElement
from hypermedia.types.attributes import (
    AudioAttrs,
    SourceAttrs,
    TrackAttrs,
    VideoAttrs,
)
from hypermedia.types.types import AnyChildren


class Audio(BasicElement[AnyChildren, AudioAttrs]):
    """Defines sound content."""

    tag: str = "audio"

    def __init__(self, **attributes: Unpack[AudioAttrs]) -> None:
        super().__init__(**attributes)


class Source(VoidElement[SourceAttrs]):
    """
    Defines multiple media resources for media elements.

    `video`, `audio` and `picture`.
    """

    tag: str = "source"

    def __init__(self, **attributes: Unpack[SourceAttrs]) -> None:
        super().__init__(**attributes)


class Track(VoidElement[TrackAttrs]):
    """Defines text tracks for media elements (`video` and `audio`)."""

    tag: str = "track"

    def __init__(self, **attributes: Unpack[TrackAttrs]) -> None:
        super().__init__(**attributes)


class Video(BasicElement[AnyChildren, VideoAttrs]):
    """Defines a video or movie."""

    tag: str = "video"

    def __init__(self, **attributes: Unpack[VideoAttrs]) -> None:
        super().__init__(**attributes)
