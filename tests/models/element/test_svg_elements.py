from hypermedia.images import Line, Polygon, Svg


def test_svg_renders_as_expected() -> None:
    assert Svg().dump() == "<svg></svg>"


def test_svg_renders_children_as_expected() -> None:
    assert (
        Svg(Line(fill="red"), Polygon(fill="blue")).dump()
        == "<svg><line fill='red' /><polygon fill='blue' /></svg>"
    )
