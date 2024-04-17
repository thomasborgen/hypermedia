from hypermedia.models import Element


class TestElement(Element):
    def dump(self) -> str:
        return str(self)
