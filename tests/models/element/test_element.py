from tests.utils import TestElement


def test_with_dump_allowed() -> None:
    assert TestElement()


def test_can_have_children() -> None:
    child = TestElement()

    parent = TestElement(child)

    assert parent.children == [child]
