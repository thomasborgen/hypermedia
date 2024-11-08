from tests.utils import TestXMLVoidElement


def test_tag_rendering() -> None:
    assert TestXMLVoidElement().dump() == "<test />"


def test_id_rendering() -> None:
    assert TestXMLVoidElement(id="test").dump() == "<test id='test' />"


def test_class_rendering() -> None:
    assert TestXMLVoidElement(classes=["one", "two"]).dump() == (
        "<test class='one two' />"
    )


def test_attribute_rendering() -> None:
    assert TestXMLVoidElement(test="green").dump() == "<test test='green' />"


def test_all_attributes() -> None:
    assert TestXMLVoidElement(
        id="test", classes=["one", "two"], test="green"
    ).dump() == ("<test id='test' test='green' class='one two' />")


def test_to_string() -> None:
    assert str(TestXMLVoidElement()) == "test"
