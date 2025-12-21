from tests.utils import TestElement


def test_extend_adds_child_to_slot() -> None:
    element = TestElement(slot="my_slot")
    child = TestElement()

    element.extend("my_slot", child)

    assert element.children == (child,)


def test_extend_adds_children_to_slot() -> None:
    element = TestElement(slot="my_slot")
    child_1 = TestElement()
    child_2 = TestElement()

    element.extend("my_slot", child_1, child_2)

    assert element.children == (child_1, child_2)


def test_extend_adds_child_to_any_descendant_slot() -> None:
    child = TestElement(slot="descendant_slot")
    parent = TestElement(child)
    element = TestElement()

    parent.extend("descendant_slot", element)

    assert child.children == (element,)
