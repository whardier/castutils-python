from typing import Any, Optional, Union

from castutils.builtins.strings import to_str
from castutils.exceptions import CastError, TransformError
from castutils.types import GenericType


# BOOL
def as_bool(obj: Any, /) -> bool:
    if isinstance(obj, bool):
        return obj
    else:
        raise CastError("Object is not of instance bool")


def as_bool_or(obj: Any, default: GenericType, /) -> Union[bool, GenericType]:
    try:
        return as_bool(obj)
    except CastError:
        return default


def to_bool(
    obj: Any,
    /,
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
) -> bool:

    try:
        if isinstance(obj, bool):
            return obj
        elif isinstance(obj, str):
            if isinstance(obj, bytes):
                obj = to_str(obj, encoding=encoding, errors=errors)
            if obj in ("y", "yes", "t", "true", "on", "word", "yah", "yay", "1"):
                return True
            elif obj in ("n", "no", "f", "false", "off", "nope", "nah", "nay", "0"):
                return False
        return bool(obj)
    except Exception as catchall_exception:
        raise TransformError("Object cannot transform to bool") from catchall_exception


def to_bool_or(
    obj: Any,
    default: Optional[bool] = None,
    /,
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
) -> Optional[bool]:

    try:
        return to_bool(obj, encoding=encoding, errors=errors)
    except TransformError as transform_exception:
        if isinstance(default, bool) or default is None:
            return default
        raise TransformError("Default is not of type int") from transform_exception
