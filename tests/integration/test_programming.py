from hypermedia.programming import Embed, NoScript, Object, Script

import pytest


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


@pytest.mark.parametrize(
    "element,result",
    [
        (Embed, "<embed>"),
    ],
)
def test_void_elements(element: type, result: str) -> None:
    assert element().dump() == result
