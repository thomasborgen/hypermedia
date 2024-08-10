import pytest

from hypermedia.forms_and_input import (
    Button,
    DataList,
    Fieldset,
    Form,
    Input,
    Label,
    Legend,
    OptGroup,
    Option,
    OptionGroup,
    Output,
    Select,
    TextArea,
)


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (OptGroup, OptionGroup, "<optgroup>test</optgroup>"),
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
        (Button, "<button>test</button>"),
        (DataList, "<datalist>test</datalist>"),
        (Fieldset, "<fieldset>test</fieldset>"),
        (Form, "<form>test</form>"),
        (Label, "<label>test</label>"),
        (Legend, "<legend>test</legend>"),
        (Option, "<option>test</option>"),
        (Output, "<output>test</output>"),
        (Select, "<select>test</select>"),
        (TextArea, "<textarea>test</textarea>"),
    ],
)
def test_normal_elements(element: type, result: str) -> None:
    assert element("test").dump() == result


@pytest.mark.parametrize(
    "element,result",
    [
        (Input, "<input>"),
    ],
)
def test_void_elements(element: type, result: str) -> None:
    assert element().dump() == result
