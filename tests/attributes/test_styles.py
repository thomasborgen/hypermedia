from hypermedia import Div


def test_style_renders_correctly() -> None:
    assert (
        Div(style={"color": "red", "font-size": "10px"}).dump()
        == "<div style='color:red;font-size:10px;'></div>"
    )
