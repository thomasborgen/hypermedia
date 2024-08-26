from hypermedia.styles_and_semantics import Div
from hypermedia.types.types import SafeString


def test_safe_string_does_not_escape() -> None:
    assert Div(SafeString("<>")).dump() == "<div><></div>"
