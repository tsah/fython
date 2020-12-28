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
    for v in none_option:
        assert False, f"This shouldn't happen. None option contains {v}"
    assert sum([1 for _ in none_option]) == 0


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
    assert some_option.flatmap(str).get() == '1'
    assert some_option.flatmap(lambda x: None).get() is None

    i = 0
    for _ in some_option:
        i += 1
    assert i == 1
    assert sum([1 for _ in some_option]) == 1
