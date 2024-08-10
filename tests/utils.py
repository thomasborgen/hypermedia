from hypermedia.models import BaseElement, Element, VoidElement
from hypermedia.types.attributes import GlobalAttrs
from hypermedia.types.types import AnyChildren


class TestElement(BaseElement):
    def dump(self) -> str:
        return str(self)


class TestBaseElement(Element[AnyChildren, GlobalAttrs]):
    tag: str = "test"


class TestVoidElement(VoidElement[GlobalAttrs]):
    tag: str = "test"
