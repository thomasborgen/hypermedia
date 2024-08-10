import pytest

from tests.utils import TestBaseElement


def test_tag_rendering() -> None:
    assert TestBaseElement().dump() == "<test></test>"


def test_id_rendering() -> None:
    assert TestBaseElement(id="test").dump() == "<test id='test'></test>"


def test_class_rendering() -> None:
    assert TestBaseElement(classes=["one", "two"]).dump() == (
        "<test class='one two'></test>"
    )


def test_attribute_rendering() -> None:
    assert TestBaseElement(test="green").dump() == "<test test='green'></test>"


def test_all_attributes() -> None:
    assert TestBaseElement(
        id="test", classes=["one", "two"], test="green"
    ).dump() == ("<test id='test' test='green' class='one two'></test>")


def test_text_rendering() -> None:
    assert TestBaseElement("test").dump() == "<test>test</test>"


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
    assert TestBaseElement(test_input).dump() == f"<test>{expected}</test>"


def test_children_rendering() -> None:
    child = TestBaseElement()
    element = TestBaseElement(child)

    assert element.dump() == "<test><test></test></test>"


def test_children_rendering_with_text() -> None:
    child = TestBaseElement("test")
    element = TestBaseElement(child)

    assert element.dump() == "<test><test>test</test></test>"


def test_child_renders_after_text() -> None:
    element = TestBaseElement("test", TestBaseElement())

    assert element.dump() == "<test>test<test></test></test>"


def test_child_renders_before_text() -> None:
    element = TestBaseElement(TestBaseElement(), "test")

    assert element.dump() == "<test><test></test>test</test>"
