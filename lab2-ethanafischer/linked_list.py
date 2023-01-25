from __future__ import annotations

from typing import Optional


class Pair:
    def __init__(self, first: object, rest: LinkedList):
        self.first = first
        self.rest = rest

    def __repr__(self) -> str:
        return 'Pair(%r, %r)' % (self.first, self.rest)

    def __eq__(self, other) -> bool:
        return (
                isinstance(other, Pair) and
                self.first == other.first and
                self.rest == other.rest
        )


LinkedList = Optional[Pair]


def empty_list() -> LinkedList:
    return None


def add(lst: LinkedList, index: int, value: object) -> LinkedList:
    if index == 0:
        return Pair(value, lst)
    if index < 0 or lst is None:
        raise IndexError

    return Pair(lst.first, add(lst.rest, index - 1, value))


def length(lst: LinkedList) -> int:
    if lst is None:
        return 0
    return 1 + length(lst.rest)


def get(lst: LinkedList, index: int) -> object:
    if index < 0 or lst is None:
        raise IndexError
    if index == 0:
        return lst.first
    return get(lst.rest, index - 1)


def setitem(lst: LinkedList, index: int, value: object) -> LinkedList:
    if index < 0 or lst is None:
        raise IndexError
    if index == 0:
        lst.first = value
        return lst

    return Pair(lst.first, setitem(lst.rest, index - 1, value))


def remove(lst: LinkedList, index: int) -> tuple[object, LinkedList]:
    if index < 0 or lst is None:
        raise IndexError
    if index == 0:
        return lst.first, lst.rest
    removed, rem_lst = remove(lst.rest, index - 1)
    return removed, Pair(lst.first, rem_lst)
