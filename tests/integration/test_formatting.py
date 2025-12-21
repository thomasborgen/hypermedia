import pytest

from hypermedia.formatting import (
    Abbr,
    Abbreviation,
    Address,
    B,
    Bdi,
    Bdo,
    BiDirectionalIsolation,
    BiDirectionalOverride,
    Blockquote,
    Bold,
    Cite,
    Code,
    DefinitionElement,
    Del,
    Deleted,
    Dfn,
    Em,
    Emphasized,
    I,
    Ins,
    Inserted,
    Italic,
    Kbd,
    Keyboard,
    Mark,
    Meter,
    Pre,
    Preformatted,
    Progress,
    Q,
    Quotation,
    Rp,
    Rt,
    S,
    Samp,
    SampleOutput,
    Small,
    StrikeThrough,
    Strong,
    Sub,
    Subscripted,
    Sup,
    Superscripted,
    Template,
    Time,
    U,
    Unarticulated,
    Var,
    Variable,
    Wbr,
    WordBreakOpportunity,
    ruby,
)


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (Abbr, Abbreviation, "<abbr>test</abbr>"),
        (Address, Address, "<address>test</address>"),
        (B, Bold, "<b>test</b>"),
        (Bdi, BiDirectionalIsolation, "<bdi>test</bdi>"),
        (Bdo, BiDirectionalOverride, "<bdo>test</bdo>"),
        (Blockquote, Blockquote, "<blockquote>test</blockquote>"),
        (Cite, Cite, "<cite>test</cite>"),
        (Code, Code, "<code>test</code>"),
        (Del, Deleted, "<del>test</del>"),
        (Dfn, DefinitionElement, "<dfn>test</dfn>"),
        (Em, Emphasized, "<em>test</em>"),
        (I, Italic, "<i>test</i>"),
        (Ins, Inserted, "<ins>test</ins>"),
        (Kbd, Keyboard, "<kbd>test</kbd>"),
        (Mark, Mark, "<mark>test</mark>"),
        (Meter, Meter, "<meter>test</meter>"),
        (Pre, Preformatted, "<pre>test</pre>"),
        (Progress, Progress, "<progress>test</progress>"),
        (Q, Quotation, "<q>test</q>"),
        (Rp, Rp, "<rp>test</rp>"),
        (Rt, Rt, "<rt>test</rt>"),
        (S, StrikeThrough, "<s>test</s>"),
        (Samp, SampleOutput, "<samp>test</samp>"),
        (Small, Small, "<small>test</small>"),
        (Strong, Strong, "<strong>test</strong>"),
        (Sub, Subscripted, "<sub>test</sub>"),
        (Sup, Superscripted, "<sup>test</sup>"),
        (Template, Template, "<template>test</template>"),
        (Time, Time, "<time>test</time>"),
        (U, Unarticulated, "<u>test</u>"),
        (Var, Variable, "<var>test</var>"),
        (ruby, ruby, "<ruby>test</ruby>"),
    ],
)
def test_normal_elements_and_aliases(
    element: type, alias: type, result: str
) -> None:
    assert element("test").dump() == result
    assert alias("test").dump() == result


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (Wbr, WordBreakOpportunity, "<wbr>"),
    ],
)
def test_void_elements_and_aliases(
    element: type, alias: type, result: str
) -> None:
    assert element().dump() == result
    assert alias().dump() == result


def test_none_children_are_skipped() -> None:
    assert Bold(None).dump() == "<b></b>"
    assert Bold("Test", None).dump() == "<b>Test</b>"
    assert Bold(None, "Test").dump() == "<b>Test</b>"
    assert Bold(None, None).dump() == "<b></b>"
