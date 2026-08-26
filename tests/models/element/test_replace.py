from tests.utils import TestElement


def test_adds_child_to_slot() -> None:
    element = TestElement(slot="my_slot")
    child = TestElement()

    element.replace("my_slot", child)

    assert element.children == (child,)


def test_skips_adding_none_child_to_slot() -> None:
    element = TestElement(slot="my_slot")

    element.replace("my_slot", None)

    assert element.children == ()


def test_skips_only_none_values() -> None:
    element = TestElement(slot="my_slot")
    child = TestElement()

    element.replace("my_slot", child, None)

    assert element.children == (child,)


def test_adds_children_to_slot() -> None:
    element = TestElement(slot="my_slot")
    child_1 = TestElement()
    child_2 = TestElement()

    element.replace("my_slot", child_1, child_2)

    assert element.children == (child_1, child_2)


def test_replaces_children_in_slot() -> None:
    element = TestElement(TestElement("1"), slot="my_slot")
    child_2 = TestElement("2")

    element.replace("my_slot", child_2)

    assert element.children == (child_2,)


def test_children_slots_calculated_() -> None:
    element = TestElement(slot="my_slot")
    child_1 = TestElement("1", slot="child_slot")
    child_2 = TestElement("2")

    element.replace("my_slot", child_1)
    element.replace("child_slot", child_2)

    assert element.children == (child_1,)
    assert child_1.children == (child_2,)


def test_adds_child_to_any_descendant_slot() -> None:
    child = TestElement(slot="descendant_slot")
    parent = TestElement(child)
    element = TestElement()

    parent.replace("descendant_slot", element)

    assert child.children == (element,)
