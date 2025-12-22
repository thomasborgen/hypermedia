from hypermedia import (
    H1,
    Body,
    Button,
    Div,
    Footer,
    Head,
    Header,
    Html,
    Main,
    Paragraph,
    Title,
)
from hypermedia.models.base import Element


# --8<-- [start:snippet]
def base() -> Element:  # (1)
    """Your base html document. Written once. Reused anywhere."""
    return Html(
        Head(slot="head"),
        Body(
            Header(slot="header"),
            Main(slot="content"),
            Footer(slot="footer"),
        ),
    )


def user_header(user: str):
    return Div(user, Button("log out", hx_post="/logout"))


def partial() -> Element:
    return Div(H1("Welcome"), Paragraph("Lorem ipsum..."))


def full(user: str | None) -> Element:
    html = base()

    # add title:
    html.extend("head", Title("Welcome to test.com"))

    # If user is logged in add user header
    if user:
        html.extend("header", user_header(user))

    # Extend with index content
    html.extend(
        "content",
        partial(),
    )

    return html
