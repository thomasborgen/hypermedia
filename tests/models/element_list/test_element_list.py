from hypermedia.models import ElementList
from tests.utils import TestBasicElement, TestVoidElement


def test_children_are_rendered() -> None:
    """Test that all children are rendered."""
    child_1 = TestBasicElement()
    child_2 = TestVoidElement()
    element = ElementList(child_1, child_2)

    assert element.dump() == "<test></test><test>"
