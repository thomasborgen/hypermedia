import pytest

from hypermedia.models import ElementList
from tests.utils import TestElement


def test_can_have_a_slot() -> None:
    element = TestElement(slot="my_slot")

    assert element.slot == "my_slot"


def test_raises_when_wrong_slot_name() -> None:
    element = TestElement(slot="my_slot")

    with pytest.raises(ValueError) as excinfo:
        element.extend("wrong_slot_name", TestElement())

    assert "wrong_slot_name" in str(excinfo.value)


def test_raises_when_duplicate_slot_names_element_list() -> None:
    with pytest.raises(ValueError) as excinfo:
        ElementList(
            TestElement(slot="my_slot"),
            TestElement(slot="my_slot"),
        )

    assert str(excinfo.value) == "All slot names must be unique: ['my_slot']"


def test_raises_when_duplicate_slot_names_in_extended_tree() -> None:
    with pytest.raises(ValueError) as excinfo:
        TestElement(slot="my_slot").extend(
            "my_slot", TestElement(slot="my_slot")
        )

    assert str(excinfo.value) == "All slot names must be unique: ['my_slot']"


def test_slots_return_own_slot() -> None:
    element = TestElement(slot="my_slot")

    assert element.slots == {"my_slot": element}


def test_slots_return_childs_slot() -> None:
    child = TestElement(slot="my_slot")
    element = TestElement(child)

    assert element.slots == {"my_slot": child}


def test_slots_return_all_descendants_slots() -> None:
    grandchild = TestElement(slot="grandchild_slot")
    child = TestElement(grandchild, slot="child_slot")
    element = TestElement(child)

    assert element.slots == {
        "child_slot": child,
        "grandchild_slot": grandchild,
    }


def test_non_element_children_are_safely_skipped() -> None:
    child = TestElement("test")
    element = TestElement("test", child)

    assert element.slots == {}
