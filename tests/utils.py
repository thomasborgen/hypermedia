from hypermedia.models import BasicElement, Element, VoidElement
from hypermedia.types.attributes import GlobalAttrs
from hypermedia.types.types import AnyChildren


class TestElement(Element):
    def dump(self) -> str:
        return str(self)


class TestBaseElement(BasicElement[AnyChildren, GlobalAttrs]):
    tag: str = "test"


class TestVoidElement(VoidElement[GlobalAttrs]):
    tag: str = "test"
