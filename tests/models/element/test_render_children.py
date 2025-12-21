from decimal import Decimal

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


def test_primitive_types_are_rendered() -> None:
    assert TestElement(1)._render_children() == "1"
    assert TestElement(1.1)._render_children() == "1.1"
    assert TestElement(None)._render_children() == ""
    assert TestElement(True)._render_children() == "True"
    assert TestElement(False)._render_children() == "False"
    assert TestElement("test")._render_children() == "test"
    assert TestElement(Decimal("1.2"))._render_children() == "1.2"
