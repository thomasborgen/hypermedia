import pytest

from hypermedia.meta_info import Base, Meta


@pytest.mark.parametrize(
    "element,result",
    [
        (Base, "<base>"),
        (Meta, "<meta>"),
    ],
)
def test_void_elements(element: type, result: str) -> None:
    assert element().dump() == result
