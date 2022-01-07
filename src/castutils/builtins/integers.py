from typing import Any, Optional, Union

from castutils.builtins.strings import to_str
from castutils.exceptions import CastError, TransformError
from castutils.types import GenericType


def as_int(obj: Any, /) -> int:
    if isinstance(obj, int):
        return obj
    else:
        raise CastError("Object is not of instance int")


def as_int_or(obj: Any, default: GenericType, /) -> Union[int, GenericType]:

    try:
        return as_int(obj)
    except CastError:
        return default


def to_int(
    obj: Any,
    /,
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
) -> int:

    try:
        return int(obj)
    except CastError as cast_exception:
        try:
            return int(to_str(obj, encoding=encoding, errors=errors))
        except Exception as catchall_exception:
            raise TransformError(
                "Object cannot transform to int"
            ) from cast_exception and catchall_exception


def to_int_or(
    obj: Any,
    default: GenericType,
    /,
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
) -> Union[int, GenericType]:

    try:
        return to_int(obj, encoding=encoding, errors=errors)
    except TransformError:
        return default
