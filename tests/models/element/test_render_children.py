from hypermedia.types.types import SafeString
from tests.utils import TestElement


def test_render_children_calls_dump() -> None:
    """Test that all children are rendered.

    Our custom WithDump().dump() just returns str(self) so we can
    expect str(child_1) + str(child_2) as output.
    """
    child_1 = TestElement()
    child_2 = TestElement()
    element = TestElement(child_1, child_2)

    assert element._render_children() == str(child_1) + str(child_2)


def test_renders_string_children_escaped() -> None:
    """Test that string children are escaped correctly."""
    assert TestElement("<>")._render_children() == "&lt;&gt;"


def test_renders_safe_string_children_as_is() -> None:
    """Test that safe string children are not escaped."""
    assert TestElement(SafeString("<>"))._render_children() == "<>"
