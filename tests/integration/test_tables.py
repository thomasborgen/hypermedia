import pytest

from hypermedia.tables import (
    Caption,
    Col,
    ColGroup,
    Column,
    ColumnGroup,
    Table,
    TableBody,
    TableData,
    TableFoot,
    TableHead,
    TableHeader,
    TableRow,
    TBody,
    Td,
    TFoot,
    Th,
    THead,
    Tr,
)


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (ColGroup, ColumnGroup, "<colgroup>test</colgroup>"),
        (THead, TableHead, "<thead>test</thead>"),
        (TBody, TableBody, "<tbody>test</tbody>"),
        (TFoot, TableFoot, "<tfoot>test</tfoot>"),
        (Th, TableHeader, "<th>test</th>"),
        (Tr, TableRow, "<tr>test</tr>"),
        (Td, TableData, "<td>test</td>"),
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
        (Caption, "<caption>test</caption>"),
        (Table, "<table>test</table>"),
    ],
)
def test_normal_elements(element: type, result: str) -> None:
    assert element("test").dump() == result


@pytest.mark.parametrize(
    "element,alias,result",
    [
        (Col, Column, "<col>"),
    ],
)
def test_void_elements(element: type, alias: type, result: str) -> None:
    assert element().dump() == result
    assert alias().dump() == result
