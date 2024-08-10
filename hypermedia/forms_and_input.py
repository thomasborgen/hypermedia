from typing_extensions import Unpack

from hypermedia.models import BasicElement, VoidElement
from hypermedia.types.attributes import (
    ButtonAttrs,
    FieldsetAttrs,
    FormAttrs,
    GlobalAttrs,
    InputAttrs,
    LabelAttrs,
    OptgroupAttrs,
    OptionAttrs,
    OutputAttrs,
    SelectAttrs,
    TextAreaAttrs,
)
from hypermedia.types.types import AnyChildren, PrimitiveChildren


class Form(BasicElement[AnyChildren, FormAttrs]):
    """Defines an HTML form for user input."""

    tag: str = "form"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[FormAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Input(VoidElement[InputAttrs]):
    """Defines an input control."""

    tag: str = "input"

    def __init__(self, **attributes: Unpack[InputAttrs]) -> None:
        super().__init__(**attributes)


class TextArea(BasicElement[AnyChildren, TextAreaAttrs]):
    """Defines a multiline input control (text area)."""

    tag: str = "textarea"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[TextAreaAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Button(BasicElement[AnyChildren, ButtonAttrs]):
    """Defines a clickable button."""

    tag: str = "button"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[ButtonAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Select(BasicElement[AnyChildren, SelectAttrs]):
    """Defines a drop-down list."""

    tag: str = "select"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[SelectAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class OptGroup(BasicElement[AnyChildren, OptgroupAttrs]):
    """Defines a group of related options in a drop-down list."""

    tag: str = "optgroup"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[OptgroupAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class OptionGroup(OptGroup):
    """Alias for `OptGroup`."""


class Option(BasicElement[PrimitiveChildren, OptionAttrs]):
    """Defines an option in a drop-down list."""

    tag: str = "option"

    def __init__(
        self, *children: PrimitiveChildren, **attributes: Unpack[OptionAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Label(BasicElement[AnyChildren, LabelAttrs]):
    """Defines a label for an `input` element."""

    tag: str = "label"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[LabelAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Fieldset(BasicElement[AnyChildren, FieldsetAttrs]):
    """Groups related elements in a form."""

    tag: str = "fieldset"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[FieldsetAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Legend(BasicElement[PrimitiveChildren, GlobalAttrs]):
    """Defines a caption for a `fieldset` element."""

    tag: str = "legend"

    def __init__(
        self, *children: PrimitiveChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class DataList(BasicElement[AnyChildren, GlobalAttrs]):
    """Specifies a list of pre-defined options for input controls."""

    tag: str = "datalist"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[GlobalAttrs]
    ) -> None:
        super().__init__(*children, **attributes)


class Output(BasicElement[AnyChildren, OutputAttrs]):
    """Defines the result of a calculation."""

    tag: str = "output"

    def __init__(
        self, *children: AnyChildren, **attributes: Unpack[OutputAttrs]
    ) -> None:
        super().__init__(*children, **attributes)
