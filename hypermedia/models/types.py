from typing import Never, TypeAlias, TypeVar, TypeVarTuple

from hypermedia.types.attributes import Attrs, NoAttrs, URLType
from hypermedia.types.styles import CSSProperties

from .base import BaseElement

NoChildren: TypeAlias = Never
"""Type alias for elements that are not allowed to have children."""

PrimitiveChildren: TypeAlias = str | bool | int | float
"""Type alias for elements that are allowed to have only primitive children.

Primitive children are ``str``, ``bool``, ``int`` and ``float``.
"""

ComplexChildren: TypeAlias = BaseElement
"""Type alias for elements that are allowed to have only non-primitive children."""  # noqa: E501

AnyChildren: TypeAlias = PrimitiveChildren | ComplexChildren
"""Type alias for elements that are allowed to have any children."""

TChildren = TypeVar("TChildren", bound=AnyChildren, covariant=True)
"""Type variable for elements representing type of children. (*args)"""

TChildrenArgs = TypeVarTuple("TChildrenArgs")
"""Type variable for strict elements representing type of children. (*args)"""

TAttrs = TypeVar("TAttrs", bound=Attrs | NoAttrs, covariant=True)
"""Type variable for elements representing type of attributes. (**kwargs)"""


__all__ = (
    "AnyChildren",
    "ComplexChildren",
    "CSSProperties",
    "URLType",
    "NoChildren",
    "PrimitiveChildren",
    "TAttrs",
    "TChildren",
    "TChildrenArgs",
)
