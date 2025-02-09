from hypermedia.models import BasicElement, Element, VoidElement
from hypermedia.models.elements import XMLVoidElement
from hypermedia.types.attributes import GlobalAttrs
from hypermedia.types.types import AnyChildren, SafeString


class TestElement(Element):  # noqa: D101
    __test__ = False  # Not an executable test class

    def dump(self) -> SafeString:  # noqa: D102
        return SafeString(self)


class TestBasicElement(BasicElement[AnyChildren, GlobalAttrs]):  # noqa: D101
    __test__ = False  # Not an executable test class

    tag: str = "test"


class TestVoidElement(VoidElement[GlobalAttrs]):  # noqa: D101
    __test__ = False  # Not an executable test class
    tag: str = "test"


class TestXMLVoidElement(XMLVoidElement[GlobalAttrs]):  # noqa: D101
    __test__ = False  # Not an executable test class
    tag: str = "test"
