import pytest

from hypermedia.basic import (
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    Body,
    Br,
    Break,
    Comment,
    Doctype,
    Head,
    Header1,
    Header2,
    Header3,
    Header4,
    Header5,
    Header6,
    HorizontalRule,
    Hr,
    Html,
    P,
    Paragraph,
    Title,
)


def test_basic_elements() -> None:
    """Test that basic html elements work."""
    assert (
        Html(
            Head(
                Title("Hypermedia"),
            ),
            Body(
                P("Hello world!"),
            ),
        ).dump()
        == "<html><head><title>Hypermedia</title></head><body><p>Hello world!</p></body></html>"  # noqa: E501
    )


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (H1, Header1, "<h1>Test</h1>"),
        (H2, Header2, "<h2>Test</h2>"),
        (H3, Header3, "<h3>Test</h3>"),
        (H4, Header4, "<h4>Test</h4>"),
        (H5, Header5, "<h5>Test</h5>"),
        (H6, Header6, "<h6>Test</h6>"),
        (P, Paragraph, "<p>Test</p>"),
    ],
)
def test_normal_elements_and_aliases(
    element: type, alias: type, result: str
) -> None:
    assert element("Test").dump() == result
    assert alias("Test").dump() == result


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (Br, Break, "<br>"),
        (Hr, HorizontalRule, "<hr>"),
    ],
)
def test_void_elements_and_aliases(
    element: type, alias: type, result: str
) -> None:
    assert element().dump() == result
    assert alias().dump() == result


def test_special_elements() -> None:
    assert Comment("Test").dump() == "<!-- Test -->"
    assert Doctype().dump() == "<!DOCTYPE html>"
