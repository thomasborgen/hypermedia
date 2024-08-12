from tests.utils import TestElement


def test_with_dump_allowed() -> None:
    assert TestElement()


def test_can_have_children() -> None:
    child = TestElement()

    parent = TestElement(child)

    assert parent.children == (child,)


def test_can_double_dump_safely() -> None:
    child = TestElement()

    parent = TestElement(
        child, test="test", slot="slot", classes=["a", "b"], class_="c"
    )

    assert parent.dump() == parent.dump()
