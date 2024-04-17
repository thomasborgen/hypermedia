import pytest

from tests.utils import TestElement


def test_can_have_a_slot() -> None:
    element = TestElement(slot="my_slot")

    assert element.slot == "my_slot"


def test_raises_when_wrong_slot_name() -> None:
    element = TestElement(slot="my_slot")

    with pytest.raises(ValueError) as excinfo:
        element.extend("wrong_slot_name", TestElement())

    assert "wrong_slot_name" in str(excinfo.value)


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
