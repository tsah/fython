import random
from typing import Optional

from fython.foptional import option, FOptional, FSome, FNone


def test_basic() -> None:
    val: Optional[float] = None
    none_option: FOptional[float] = option(val)
    assert none_option.is_none()
    assert not none_option.is_some()
    assert none_option.get() is None
    r = random.random()
    assert none_option.get_or_else(r) == r
    assert none_option.map(lambda x: x).is_none()
    assert none_option.flatmap(lambda x: FSome(x)).is_none()


def test_map() -> None:
    float_option = option(1)
    assert float_option.map(str).get() == '1'


def test_flatmap() -> None:
    float_option = option(1)
    assert float_option.flatmap(lambda x: FSome(str(x))).get() == '1'
    assert float_option.flatmap(lambda x: FNone()).get() is None
