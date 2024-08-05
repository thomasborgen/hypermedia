import pytest

from hypermedia import Comment
from hypermedia.basic import Doctype


def test_comment_dump() -> None:
    assert Comment("foo").dump() == "<!-- foo -->"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("&", "&amp;"),
        ("<", "&lt;"),
        (">", "&gt;"),
        ('"', "&quot;"),
        ("'", "&#x27;"),
    ],
)
def test_comment_dump_is_escaped(test_input: str, expected: str) -> None:
    assert Comment(test_input).dump() == f"<!-- {expected} -->"


def test_doctype_dump() -> None:
    assert Doctype().dump() == "<!DOCTYPE html>"
