import pytest

from hypermedia.audio_and_video import Audio, Source, Track, Video


@pytest.mark.parametrize(
    "element,result",
    [
        (Audio, "<audio></audio>"),
        (Video, "<video></video>"),
        (Track, "<track>"),
        (Source, "<source>"),
    ],
)
def test_normal_elements_and_aliases(element: type, result: str) -> None:
    assert element().dump() == result
