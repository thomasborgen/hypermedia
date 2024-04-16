import pytest

from pal.base_models import Element


class WithDump(Element):
    def dump(self) -> str:
        return str(self)


def test_with_dump_allowed() -> None:
    assert WithDump()


def test_can_have_children() -> None:
    child = WithDump()

    parent = WithDump(child)

    assert parent.children == [child]


def test_can_have_a_slot() -> None:
    element = WithDump(slot="my_slot")

    assert element.slot == "my_slot"


def test_raises_when_wrong_slot_name() -> None:
    element = WithDump(slot="my_slot")

    with pytest.raises(ValueError) as excinfo:
        element.extend("wrong_slot_name", WithDump())

    assert "wrong_slot_name" in str(excinfo.value)


def test_slots_return_own_slot() -> None:
    element = WithDump(slot="my_slot")

    assert element.slots == {"my_slot": element}


def test_slots_return_childs_slot() -> None:
    child = WithDump(slot="my_slot")
    element = WithDump(child)

    assert element.slots == {"my_slot": child}


def test_slots_return_all_descendants_slots() -> None:
    grandchild = WithDump(slot="grandchild_slot")
    child = WithDump(grandchild, slot="child_slot")
    element = WithDump(child)

    assert element.slots == {
        "child_slot": child,
        "grandchild_slot": grandchild,
    }


def test_extend_adds_child_to_slot() -> None:
    element = WithDump(slot="my_slot")
    child = WithDump()

    element.extend("my_slot", child)

    assert element.children == [child]


def test_extend_adds_children_to_slot() -> None:
    element = WithDump(slot="my_slot")
    child_1 = WithDump()
    child_2 = WithDump()

    element.extend("my_slot", child_1, child_2)

    assert element.children == [child_1, child_2]


def test_extend_adds_child_to_any_descendant_slot() -> None:
    child = WithDump(slot="descendant_slot")
    parent = WithDump(child)
    element = WithDump()

    parent.extend("descendant_slot", element)

    assert child.children == [element]


def test_kwargs_stored_in_attributes() -> None:
    element = WithDump(test="green")

    assert element.attributes["test"] == "green"


def test_render_attributes() -> None:
    element = WithDump(test="green")

    assert element._render_attributes() == ' test="green"'


def test_render_multiple_attributes_separated_by_space() -> None:
    element = WithDump(one="one", two="two")

    assert element._render_attributes() == ' one="one" two="two"'


def test_false_value_is_skipped() -> None:
    element = WithDump(test=False)

    assert element._render_attributes() == ""


def test_true_value_is_added_as_key_only() -> None:
    element = WithDump(test=True)

    assert element._render_attributes() == " test"


def test_htmx_keys_added_with_hyphen() -> None:
    element = WithDump(hx_get="url")

    assert element._render_attributes() == ' hx-get="url"'


def test_render_children_calls_dump() -> None:
    """
    Test that all children are rendered.

    Our custom WithDump().dump() just returns str(self) so we can
    expect str(child_1) + str(child_2) as output.
    """
    child_1 = WithDump()
    child_2 = WithDump()
    element = WithDump(child_1, child_2)

    assert element._render_children() == str(child_1) + str(child_2)
