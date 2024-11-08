import pytest

from hypermedia.models.base import Element
from hypermedia.models.elements import (
    BasicElement,
    ElementList,
    ElementStrict,
    VoidElement,
    XMLVoidElement,
)
from hypermedia.types.types import SafeString
from tests.utils import TestBasicElement


def test_tag_rendering() -> None:
    assert TestBasicElement().dump() == "<test></test>"


def test_id_rendering() -> None:
    assert TestBasicElement(id="test").dump() == "<test id='test'></test>"


def test_class_rendering() -> None:
    assert TestBasicElement(classes=["one", "two"]).dump() == (
        "<test class='one two'></test>"
    )


def test_attribute_rendering() -> None:
    assert (
        TestBasicElement(test="green").dump() == "<test test='green'></test>"
    )


def test_all_attributes() -> None:
    assert TestBasicElement(
        id="test", classes=["one", "two"], test="green"
    ).dump() == ("<test id='test' test='green' class='one two'></test>")


def test_text_rendering() -> None:
    assert TestBasicElement("test").dump() == "<test>test</test>"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("&", "&amp;"),
        ("<", "&lt;"),
        (">", "&gt;"),
        ('"', "&quot;"),
        ("'", "&#x27;"),
    ],
)
def test_text_escaping_rendering(test_input: str, expected: str) -> None:
    assert TestBasicElement(test_input).dump() == f"<test>{expected}</test>"


def test_children_rendering() -> None:
    child = TestBasicElement()
    element = TestBasicElement(child)

    assert element.dump() == "<test><test></test></test>"


def test_children_rendering_with_text() -> None:
    child = TestBasicElement("test")
    element = TestBasicElement(child)

    assert element.dump() == "<test><test>test</test></test>"


def test_child_renders_after_text() -> None:
    element = TestBasicElement("test", TestBasicElement())

    assert element.dump() == "<test>test<test></test></test>"


def test_child_renders_before_text() -> None:
    element = TestBasicElement(TestBasicElement(), "test")

    assert element.dump() == "<test><test></test>test</test>"


def test_all_subclasses_dumps_to_safestring() -> None:
    """Make sure everything dumps to SafeString."""
    assert all(
        isinstance(sub().dump(), SafeString)
        for sub in BasicElement.__subclasses__()
    )

    assert all(
        isinstance(sub("test").dump(), SafeString)
        for sub in ElementStrict.__subclasses__()
    )

    assert all(
        isinstance(sub().dump(), SafeString)
        for sub in VoidElement.__subclasses__()
    )

    assert all(
        isinstance(sub().dump(), SafeString)
        for sub in XMLVoidElement.__subclasses__()
    )

    assert isinstance(ElementList().dump(), SafeString)

    skip = {
        "BasicElement",
        "ElementList",
        "ElementStrict",
        "VoidElement",
        "XMLVoidElement",
    }
    assert all(
        isinstance(sub().dump(), SafeString)  # type: ignore
        for sub in Element.__subclasses__()
        if sub.__name__ not in skip
    )
