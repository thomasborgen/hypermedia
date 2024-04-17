from tests.utils import TestElement


def test_render_children_calls_dump() -> None:
    """
    Test that all children are rendered.

    Our custom WithDump().dump() just returns str(self) so we can
    expect str(child_1) + str(child_2) as output.
    """
    child_1 = TestElement()
    child_2 = TestElement()
    element = TestElement(child_1, child_2)

    assert element._render_children() == str(child_1) + str(child_2)
