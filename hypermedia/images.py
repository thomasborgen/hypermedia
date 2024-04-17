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
