from typing import Any, Optional, Union
from uuid import UUID

from castutils.exceptions import CastError, TransformError
from castutils.types import GenericType


def as_str(obj: Any, /) -> str:
    if isinstance(obj, str):
        return obj
    else:
        raise CastError("Object is not of instance str")


def as_str_or(obj: Any, fallback: GenericType, /) -> Union[str, GenericType]:
    try:
        return as_str(obj)
    except CastError:
        return fallback


def to_str(
    obj: Any,
    /,
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
    form: Optional[str] = None,
) -> str:

    encoding = encoding or "utf-8"
    errors = errors or "strict"

    try:
        if isinstance(obj, str):
            return obj
        elif isinstance(obj, bytes):
            return obj.decode(encoding, errors)
        elif isinstance(obj, UUID):
            if form == "short":
                return obj.hex
        return str(obj)
    except Exception as catchall_exception:
        raise TransformError("Object cannot transform to str") from catchall_exception


def to_str_or(
    obj: Any,
    fallback: GenericType,
    /,
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
) -> Union[str, GenericType]:

    try:
        return to_str(obj, encoding=encoding, errors=errors)
    except TransformError:
        return fallback
