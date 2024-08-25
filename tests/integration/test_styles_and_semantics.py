import pytest

from hypermedia.styles_and_semantics import (
    Article,
    Aside,
    Data,
    Details,
    Dialog,
    Div,
    Footer,
    Header,
    HeaderGroup,
    HGroup,
    Main,
    Search,
    Section,
    Span,
    Style,
    Summary,
)


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (HGroup, HeaderGroup, "<hgroup>test</hgroup>"),
    ],
)
def test_normal_elements_and_aliases(
    element: type, alias: type, result: str
) -> None:
    assert element("test").dump() == result
    assert alias("test").dump() == result


@pytest.mark.parametrize(
    "element,result",
    [
        (Article, "<article>test</article>"),
        (Aside, "<aside>test</aside>"),
        (Data, "<data>test</data>"),
        (Details, "<details>test</details>"),
        (Dialog, "<dialog>test</dialog>"),
        (Div, "<div>test</div>"),
        (Footer, "<footer>test</footer>"),
        (Header, "<header>test</header>"),
        (Main, "<main>test</main>"),
        (Search, "<search>test</search>"),
        (Section, "<section>test</section>"),
        (Span, "<span>test</span>"),
        (Style, "<style>test</style>"),
        (Summary, "<summary>test</summary>"),
    ],
)
def test_normal_elements(element: type, result: str) -> None:
    assert element("test").dump() == result


def test_style_is_not_escaped() -> None:
    assert Style('"<>').dump() == '<style>"<></style>'
