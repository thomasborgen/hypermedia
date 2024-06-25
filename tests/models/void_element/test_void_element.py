from tests.utils import TestVoidElement


def test_tag_rendering() -> None:
    assert TestVoidElement().dump() == "<test>"


def test_id_rendering() -> None:
    assert TestVoidElement(id="test").dump() == "<test id='test'>"


def test_class_rendering() -> None:
    assert TestVoidElement(classes=["one", "two"]).dump() == (
        "<test class='one two'>"
    )


def test_attribute_rendering() -> None:
    assert TestVoidElement(test="green").dump() == "<test test='green'>"


def test_all_attributes() -> None:
    assert TestVoidElement(
        id="test", classes=["one", "two"], test="green"
    ).dump() == ("<test id='test' class='one two' test='green'>")


def test_to_string() -> None:
    assert str(TestVoidElement()) == "test"
