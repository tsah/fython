from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar('T')
G = TypeVar('G')


class FOptional(Generic[T], metaclass=ABCMeta):
    @abstractmethod
    def get(self) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def get_or_else(self, else_: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def is_some(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def is_none(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def map(self, f: Callable[[T], G]) -> FOptional[G]:
        raise NotImplementedError

    @abstractmethod
    def flatmap(self, f: Callable[[T], FOptional[G]]) -> FOptional[G]:
        raise NotImplementedError


class FSome(FOptional):
    def __init__(self, val: T) -> None:
        self._val = val

    def get(self) -> Optional[T]:
        return self._val

    def get_or_else(self, else_: T) -> T:
        return self.get()

    def is_some(self) -> bool:
        return True

    def is_none(self) -> bool:
        return False

    def map(self, f: Callable[[T], G]) -> FOptional[G]:
        return FSome(f(self._val))

    def flatmap(self, f: Callable[[T], FOptional[G]]) -> FOptional[G]:
        return f(self._val)


class FNone(FOptional):
    def get(self) -> Optional[T]:
        return None

    def get_or_else(self, else_: T) -> T:
        return else_

    def is_some(self) -> bool:
        return False

    def is_none(self) -> bool:
        return True

    def map(self, f: Callable[[T], G]) -> FOptional[G]:
        return self

    def flatmap(self, f: Callable[[T], FOptional[G]]) -> FOptional[G]:
        return self


def option(val: Optional[T]) -> FOptional[T]:
    if val is None:
        return FNone()
    else:
        return FSome(val)
