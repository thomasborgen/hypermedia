from hypermedia.models import BaseElement, VoidElement


class Form(BaseElement):
    """Defines an HTML form for user input."""

    tag: str = "form"


class Input(VoidElement):
    """Defines an input control."""

    tag: str = "input"


class TextArea(BaseElement):
    """Defines a multiline input control (text area)."""

    tag: str = "textarea"


class Button(BaseElement):
    """Defines a clickable button."""

    tag: str = "button"


class Select(BaseElement):
    """Defines a drop-down list."""

    tag: str = "select"


class OptGroup(BaseElement):
    """Defines a group of related options in a drop-down list."""

    tag: str = "optgroup"


class OptionGroup(OptGroup):
    """Alias for `OptGroup`."""


class Option(BaseElement):
    """Defines an option in a drop-down list."""

    tag: str = "option"


class Label(BaseElement):
    """Defines a label for an `input` element."""

    tag: str = "label"


class Fieldset(BaseElement):
    """Groups related elements in a form."""

    tag: str = "fieldset"


class Legend(BaseElement):
    """Defines a caption for a `fieldset` element."""

    tag: str = "legend"


class DataList(BaseElement):
    """Specifies a list of pre-defined options for input controls."""

    tag: str = "datalist"


class Output(BaseElement):
    """Defines the result of a calculation."""

    tag: str = "output"
