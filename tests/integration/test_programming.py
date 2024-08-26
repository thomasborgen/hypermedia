import pytest

from hypermedia.programming import Embed, NoScript, Object, Script


@pytest.mark.parametrize(
    "element,result",
    [
        (NoScript, "<noscript>test</noscript>"),
        (Object, "<object>test</object>"),
        (Script, "<script>test</script>"),
    ],
)
def test_normal_elements(element: type, result: str) -> None:
    assert element("test").dump() == result


def test_script_is_not_escaped() -> None:
    assert Script('"<>').dump() == '<script>"<></script>'


def test_empty_script_is_okay() -> None:
    assert Script().dump() == "<script></script>"


@pytest.mark.parametrize(
    "element,result",
    [
        (Embed, "<embed>"),
    ],
)
def test_void_elements(element: type, result: str) -> None:
    assert element().dump() == result
