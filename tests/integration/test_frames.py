import pytest

from hypermedia.frames import IFrame


@pytest.mark.parametrize(
    "element,result",
    [
        (IFrame, "<iframe></iframe>"),
    ],
)
def test_normal_elements(element: type, result: str) -> None:
    assert element().dump() == result
