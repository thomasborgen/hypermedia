from hypermedia import Label


def test_for_renders_correctly():
    assert (
        Label("test", for_="test").dump() == "<label for='test'>test</label>"
    )
