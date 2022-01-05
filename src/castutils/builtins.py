from typing import Any, Optional
from uuid import UUID

from castutils.exceptions import CastError, TransformError


# BOOL
def as_bool(obj: Any, /) -> bool:
    if isinstance(obj, bool):
        return obj
    else:
        raise CastError("Object is not of instance bool")


def as_bool_or(obj: Any, default: Optional[bool] = None, /) -> Optional[bool]:

    try:
        return as_bool(obj)
    except CastError as cast_exception:
        if isinstance(default, bool) or default is None:
            return default
        raise CastError("Default is not of instance bool") from cast_exception


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


# STR
def as_str(obj: Any, /) -> str:
    if isinstance(obj, str):
        return obj
    else:
        raise CastError("Object is not of instance str")


def as_str_or(obj: Any, default: Optional[str] = None, /) -> Optional[str]:

    try:
        return as_str(obj)
    except CastError as cast_exception:
        if isinstance(default, str) or default is None:
            return default
        raise CastError("Default is not of instance str") from cast_exception


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
    default: Optional[str] = None,
    /,
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
) -> Optional[str]:

    try:
        return to_str(obj, encoding=encoding, errors=errors)
    except TransformError as transform_exception:
        if isinstance(default, str) or default is None:
            return default
        raise TransformError("Default is not of type int") from transform_exception


# INT
def as_int(obj: Any, /) -> int:
    if isinstance(obj, int):
        return obj
    else:
        raise CastError("Object is not of instance int")


def as_int_or(obj: Any, default: Optional[int] = None, /) -> Optional[int]:

    try:
        return as_int(obj)
    except CastError as cast_exception:
        if isinstance(default, int) or default is None:
            return default
        raise CastError("Default is not of instance int") from cast_exception


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
    default: Optional[int] = None,
    /,
    encoding: Optional[str] = None,
    errors: Optional[str] = None,
) -> Optional[int]:

    try:
        return to_int(obj, encoding=encoding, errors=errors)
    except TransformError as transform_exception:
        if isinstance(default, int) or default is None:
            return default
        raise TransformError("Default is not of type int") from transform_exception
