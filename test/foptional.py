import random
from typing import Optional

import pytest

from fython.foptional import option, FOptional, FSome, FNone


def test_none() -> None:
    val: Optional[float] = None
    none_option: FOptional[float] = option(val)
    assert none_option.is_none()
    assert not none_option.is_some()
    assert none_option.get() is None
    r = random.random()
    assert none_option.get_or_else(r) == r
    assert none_option.map(lambda x: x).is_none()
    assert none_option.flatmap(lambda x: FSome(x)).is_none()
    assert none_option.get_or_else_lazy(lambda: r) == r
    with pytest.raises(AssertionError):
        none_option.get_or_throw()


def test_some() -> None:
    some_option = option(1)
    assert some_option.get() == 1
    assert some_option.get_or_else(2) == 1
    assert some_option.get_or_else_lazy(lambda x: 2) == 1

    def raise_():
        raise AssertionError
    assert some_option.get_or_else_lazy(raise_) == 1
    assert some_option.get_or_throw() == 1
    assert some_option.map(str).get() == '1'
    assert some_option.flatmap(lambda x: FSome(str(x))).get() == '1'
    assert some_option.flatmap(lambda x: FNone()).get() is None
