from hypermedia.models import BaseElement, VoidElement


class Img(VoidElement):
    """Defines an image."""

    tag: str = "img"


class Image(Img):
    """Alias for `Img`."""


class Map(BaseElement):
    """Defines a client-side image map."""

    tag: str = "map"


class Area(VoidElement):
    """Defines an area inside an image map."""

    tag: str = "area"


class Canvas(BaseElement):
    """Used to draw graphics, on the fly, via scripting."""

    tag: str = "canvas"


class FigCaption(BaseElement):
    """Defines a caption for a `figure` element."""

    tag: str = "figcaption"


class FigureCaption(FigCaption):
    """Alias for `FigCaption`."""


class Figure(BaseElement):
    """Specifies self-contained content."""

    tag: str = "figure"


class Picture(BaseElement):
    """Defines a container for multiple image resources."""

    tag: str = "picture"


class Svg(BaseElement):
    """Defines a container for SVG graphics."""

    tag: str = "svg"


# Basic SVG elements. These should hopefully cover most use cases.
# If they don't, feel free to add them.
# Alternatively, consider using Image with a `src="my.svg` or css.
class Path(VoidElement):
    """Element used to define paths for SVG graphics."""

    tag: str = "path"


class Rect(VoidElement):
    """Element used to define rectangles for SVG graphics."""

    tag: str = "rect"


class Rectangle(Rect):
    """Alias for `Rect`."""


class Circle(VoidElement):
    """Element used to define circles for SVG graphics."""

    tag: str = "circle"


class Ellipse(VoidElement):
    """Element used to define ellipses for SVG graphics."""

    tag: str = "ellipse"


class Line(VoidElement):
    """Element used to define lines for SVG graphics."""

    tag: str = "line"


class Polyline(VoidElement):
    """Element used to define polylines for SVG graphics."""

    tag: str = "polyline"


class Polygon(VoidElement):
    """Element used to define polygons for SVG graphics."""

    tag: str = "polygon"
