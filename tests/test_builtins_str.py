from random import Random
from uuid import UUID

from hypothesis import given
from hypothesis.strategies import (
    binary,
    integers,
    randoms,
    text,
    uuids,
    lists,
)
import pytest

from castutils.builtins.strings import as_str, as_str_or, to_str


@given(text())
def test_builtin_str_as_str__text(obj: str) -> None:
    assert obj == as_str(obj)


@given(text(), text())
def test_builtin_str_as_str_or__text(obj: str, default: str) -> None:
    assert obj == as_str_or(obj, default)
    assert default == as_str_or(object(), default)


@given(text())
def test_builtin_str_to_str__text(obj: str) -> None:
    assert obj == to_str(obj)


@given(binary())
def test_builtin_str_to_str__binary(obj: bytes) -> None:
    encoding = "utf-8"
    errors = "ignore"
    assert obj.decode(encoding, errors=errors) == to_str(
        obj, encoding=encoding, errors=errors
    )


@given(integers())
def test_builtin_str_to_str__integers(obj: int) -> None:
    assert str(obj) == to_str(obj)


@given(uuids())
def test_builtin_str_to_str__uuids(obj: UUID) -> None:
    assert str(obj) == to_str(obj)


@given(uuids(), randoms())
def test_builtin_str_to_str__uuids__form_short(obj: UUID, rand: Random) -> None:
    form = rand.choice(["short", "long"])
    if form == "short":
        assert obj.hex == to_str(obj, form=form)
    elif form == "long":
        assert str(obj) == to_str(obj, form=form)


@given(
    lists(integers(min_value=128, max_value=255), min_size=10, max_size=20).map(bytes)
)
def test_builtin_str_to_str__bytes__non_ascii(obj: UUID) -> None:
    with pytest.raises(ValueError):
        to_str(obj, encoding="ascii")
