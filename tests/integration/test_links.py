import pytest

from hypermedia.links import (
    A,
    Anchor,
    Link,
    Nav,
)


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (A, Anchor, "<a>test</a>"),
    ],
)
def test_normal_elements_and_aliases(
    element: type, alias: type, result: str
) -> None:
    assert element("test").dump() == result
    assert alias("test").dump() == result


@pytest.mark.parametrize(
    "element,result",
    [
        (Nav, "<nav>test</nav>"),
    ],
)
def test_normal_elements(element: type, result: str) -> None:
    assert element("test").dump() == result


@pytest.mark.parametrize(
    "element,result",
    [
        (Link, "<link>"),
    ],
)
def test_void_elements(element: type, result: str) -> None:
    assert element().dump() == result
