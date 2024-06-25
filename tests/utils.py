from hypermedia.models import Element, BaseElement, VoidElement


class TestElement(Element):
    def dump(self) -> str:
        return str(self)


class TestBaseElement(BaseElement):
    tag: str = "test"


class TestVoidElement(VoidElement):
    tag: str = "test"
