from hypermedia import Body, Div, Doctype, ElementList, Head, Html, Meta, Title


def test_create_basic_html_page() -> None:
    hypermedia = ElementList(
        Doctype(),
        Html(
            Head(Title("Basic HTML Page"), Meta(charset="UTF-8"), slot="head"),
            Body(Div("Hello World"), hx_boost="true"),
        ),
    ).dump()

    assert (
        hypermedia
        == "<!DOCTYPE html><html><head><title>Basic HTML Page</title><meta charset='UTF-8'></head><body hx-boost='true'><div>Hello World</div></body></html>"  # noqa: E501
    )
