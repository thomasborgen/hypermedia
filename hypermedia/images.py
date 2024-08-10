from typing_extensions import Unpack

from hypermedia.models import BasicElement, VoidElement
from hypermedia.types.attributes import (
    AreaAttrs,
    CanvasAttrs,
    CircleAttrs,
    EllipseAttrs,
    GlobalAttrs,
    ImgAttrs,
    LineAttrs,
    MapAttrs,
    PathAttrs,
    PolygonAttrs,
    PolylineAttrs,
    RectAttrs,
    SvgAttrs,
)
from hypermedia.types.types import AnyChildren


class Img(VoidElement[ImgAttrs]):
    """Defines an image."""

    tag: str = "img"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[ImgAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Image(Img):
    """Alias for `Img`."""


class Map(BasicElement[AnyChildren, MapAttrs]):
    """Defines a client-side image map."""

    tag: str = "map"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[MapAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Area(VoidElement[AreaAttrs]):
    """Defines an area inside an image map."""

    tag: str = "area"

    def __init__(self, **attributes: Unpack[AreaAttrs]) -> None:
        super().__init__(**attributes)


class Canvas(BasicElement[AnyChildren, CanvasAttrs]):
    """Used to draw graphics, on the fly, via scripting."""

    tag: str = "canvas"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[CanvasAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class FigCaption(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines a caption for a `figure` element."""

    tag: str = "figcaption"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class FigureCaption(FigCaption):
    """Alias for `FigCaption`."""


class Figure(BasicElement[AnyChildren, GlobalAttrs]):
    """Specifies self-contained content."""

    tag: str = "figure"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Picture(BasicElement[AnyChildren, GlobalAttrs]):
    """Defines a container for multiple image resources."""

    tag: str = "picture"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Svg(BasicElement[AnyChildren, SvgAttrs]):
    """Defines a container for SVG graphics."""

    tag: str = "svg"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[SvgAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


# Basic SVG elements. These should hopefully cover most use cases.
# If they don't, feel free to add them.
# Alternatively, consider using Image with a `src="my.svg` or css.
class Path(VoidElement[PathAttrs]):
    """Element used to define paths for SVG graphics."""

    tag: str = "path"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[PathAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Rect(VoidElement[RectAttrs]):
    """Element used to define rectangles for SVG graphics."""

    tag: str = "rect"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[RectAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Rectangle(Rect):
    """Alias for `Rect`."""


class Circle(VoidElement[CircleAttrs]):
    """Element used to define circles for SVG graphics."""

    tag: str = "circle"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[CircleAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Ellipse(VoidElement[EllipseAttrs]):
    """Element used to define ellipses for SVG graphics."""

    tag: str = "ellipse"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[EllipseAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Line(VoidElement[LineAttrs]):
    """Element used to define lines for SVG graphics."""

    tag: str = "line"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[LineAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Polyline(VoidElement[PolylineAttrs]):
    """Element used to define polylines for SVG graphics."""

    tag: str = "polyline"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[PolylineAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Polygon(VoidElement[PolygonAttrs]):
    """Element used to define polygons for SVG graphics."""

    tag: str = "polygon"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[PolygonAttrs]
    ) -> None:
        super().__init__(*children, **attributes)
