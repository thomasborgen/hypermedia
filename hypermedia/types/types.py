from typing import TYPE_CHECKING, TypeAlias, TypeVar, Union

from typing_extensions import Never, TypeVarTuple

from hypermedia.types.attributes import Attrs, NoAttrs

if TYPE_CHECKING:
    from hypermedia.models.base import Element


class SafeString(str):
    """No html escaping will be done."""


NoChildren: TypeAlias = Never
"""Type alias for elements that are not allowed to have children."""

PrimitiveChildren: TypeAlias = str | bool | int | float
"""Type alias for elements that are allowed to have only primitive children.

Primitive children are ``str``, ``bool``, ``int`` and ``float``.
"""

ComplexChildren: TypeAlias = "Element"
"""Type alias for elements that are allowed to have only non-primitive children."""  # noqa: E501

AnyChildren: TypeAlias = Union[PrimitiveChildren, ComplexChildren]
"""Type alias for elements that are allowed to have any children."""

# PLC0105 `TypeVar` name "TChildren" does not reflect its covariance;
# consider renaming it to "TChildren_co"
TChildren = TypeVar("TChildren", bound=AnyChildren, covariant=True)  # noqa: PLC0105  # type: ignore
"""Type variable for elements representing type of children. (*args)"""

TChildrenArgs = TypeVarTuple("TChildrenArgs")
"""Type variable for strict elements representing type of children. (*args)"""

# PLC0105 `TypeVar` name "TChildren" does not reflect its covariance;
# consider renaming it to "TChildren_co"
TAttrs = TypeVar("TAttrs", bound=Attrs | NoAttrs, covariant=True)  # noqa: PLC0105
"""Type variable for elements representing type of attributes. (**kwargs)"""
