import pytest

from hypermedia.images import (
    Area,
    Canvas,
    Circle,
    Ellipse,
    FigCaption,
    Figure,
    FigureCaption,
    Image,
    Img,
    Line,
    Map,
    Path,
    Picture,
    Polygon,
    Polyline,
    Rect,
    Rectangle,
    Svg,
)


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (FigCaption, FigureCaption, "<figcaption>test</figcaption>"),
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
        (Canvas, "<canvas>test</canvas>"),
        (Figure, "<figure>test</figure>"),
        (Map, "<map>test</map>"),
        (Picture, "<picture>test</picture>"),
        (Svg, "<svg>test</svg>"),
    ],
)
def test_normal_elements(element: type, result: str) -> None:
    assert element("test").dump() == result


@pytest.mark.parametrize(
    "element,result",
    [
        (Area, "<area>"),
        (Img, "<img>"),
        (Image, "<img>"),
    ],
)
def test_void_elements(element: type, result: str) -> None:
    assert element().dump() == result


@pytest.mark.parametrize(
    "element,result",
    [
        (Circle, "<circle />"),
        (Ellipse, "<ellipse />"),
        (Line, "<line />"),
        (Path, "<path />"),
        (Polygon, "<polygon />"),
        (Polyline, "<polyline />"),
        (Rect, "<rect />"),
        (Rectangle, "<rect />"),
    ],
)
def test_xml_void_elements(element: type, result: str) -> None:
    assert element().dump() == result
