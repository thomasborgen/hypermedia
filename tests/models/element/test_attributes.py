from tests.utils import TestElement


def test_kwargs_stored_in_attributes() -> None:
    element = TestElement(test="green")

    assert element.attributes["test"] == "green"


def test_render_attributes() -> None:
    element = TestElement(test="green")

    assert element._render_attributes() == " test='green'"


def test_render_multiple_attributes_separated_by_space() -> None:
    element = TestElement(one="one", two="two")

    assert element._render_attributes() == " one='one' two='two'"


def test_false_value_is_skipped() -> None:
    element = TestElement(test=False)

    assert element._render_attributes() == ""


def test_none_value_is_skipped() -> None:
    element = TestElement(test=None)

    assert element._render_attributes() == ""


def test_true_value_is_added_as_key_only() -> None:
    element = TestElement(test=True)

    assert element._render_attributes() == " test"


def test_class_and_classes_are_combined() -> None:
    element = TestElement(class_="three", classes=["one", "two"])

    assert element._render_attributes() == " class='one two three'"


def test_class_and_classes_disappear() -> None:
    element = TestElement(class_="three", classes=["one", "two"])

    element._render_attributes()

    assert element.attributes["class_"] == "three"
    assert element.attributes["classes"] == ["one", "two"]


def test_aliased_keys() -> None:
    element = TestElement(on_afterprint="test")

    assert element._render_attributes() == " onafterprint='test'"


def test_underscored_keys_added_with_hyphen() -> None:
    element = TestElement(hx_get="url")

    assert element._render_attributes() == " hx-get='url'"


def test_custom_attributes_with_dollarsign() -> None:
    element = TestElement(**{"$data-show.duration_500ms": "$show"})
    assert element._render_attributes() == " data-show.duration_500ms='$show'"


def test_custom_attributes_with_normal_ones() -> None:
    element = TestElement(test="green", **{"$$@-.%": "test"}, bob="bob")
    assert (
        element._render_attributes() == " test='green' $@-.%='test' bob='bob'"
    )
