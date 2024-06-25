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
    ).dump() == ("<test id='test' class='one two' test='green'></test>")


def test_text_rendering() -> None:
    assert TestBaseElement(text="test").dump() == "<test>test</test>"


def test_children_rendering() -> None:
    child = TestBaseElement()
    element = TestBaseElement(child)

    assert element.dump() == "<test><test></test></test>"


def test_children_rendering_with_text() -> None:
    child = TestBaseElement(text="test")
    element = TestBaseElement(child)

    assert element.dump() == "<test><test>test</test></test>"


def test_child_renders_after_text() -> None:
    element = TestBaseElement(TestBaseElement(), text="test")

    assert element.dump() == "<test>test<test></test></test>"


def test_child_in_middle_of_text() -> None:
    """Note, useful for inline tags like <a>, <br> etc."""
    element = TestBaseElement(text=f"te{TestBaseElement().dump()}st")

    assert element.dump() == "<test>te<test></test>st</test>"


def test_to_string() -> None:
    assert str(TestBaseElement()) == "test"
