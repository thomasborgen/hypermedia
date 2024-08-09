import pytest

from hypermedia.lists import (
    Dd,
    DescriptionList,
    DescriptionListTerm,
    DescriptionListTermDescription,
    Dl,
    Dt,
    Li,
    ListItem,
    Menu,
    Ol,
    OrderedList,
    Ul,
    UnorderedList,
)


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (Dd, DescriptionListTermDescription, "<dd>test</dd>"),
        (Dt, DescriptionListTerm, "<dt>test</dt>"),
        (Dl, DescriptionList, "<dl>test</dl>"),
        (Li, ListItem, "<li>test</li>"),
        (Ol, OrderedList, "<ol>test</ol>"),
        (Ul, UnorderedList, "<ul>test</ul>"),
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
        (Menu, "<menu>test</menu>"),
    ],
)
def test_normal_elements(element: type, result: str) -> None:
    assert element("test").dump() == result
