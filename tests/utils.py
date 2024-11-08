from hypermedia.models import BasicElement, Element, VoidElement
from hypermedia.models.elements import XMLVoidElement
from hypermedia.types.attributes import GlobalAttrs
from hypermedia.types.types import AnyChildren, SafeString


class TestElement(Element):
    __test__ = False  # Not an executable test class

    def dump(self) -> SafeString:
        return SafeString(self)


class TestBasicElement(BasicElement[AnyChildren, GlobalAttrs]):
    __test__ = False  # Not an executable test class

    tag: str = "test"


class TestVoidElement(VoidElement[GlobalAttrs]):
    __test__ = False  # Not an executable test class
    tag: str = "test"


class TestXMLVoidElement(XMLVoidElement[GlobalAttrs]):
    __test__ = False  # Not an executable test class
    tag: str = "test"
