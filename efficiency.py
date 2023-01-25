from __future__ import annotations

from typing import Optional


class Pair:
    def __init__(self, first: int, rest: NumList):
        self.first = first  # an int
        self.rest = rest  # a NumList

    def __repr__(self) -> str:
        return 'Pair(%r, %r)' % (self.first, self.rest)

    def __eq__(self, other) -> bool:
        return (
                isinstance(other, Pair) and
                self.first == other.first and
                self.rest == other.rest
        )


NumList = Optional[Pair]


# It runs in constant time.
def f(x):
    return 7 * (24231 + (332 * 243))


# It runs in linear time.
def contains(lst: NumList, value: int) -> bool:
    if lst is None:
        return False

    return lst.first == value or contains(lst.rest, value)


#   command   array list  linked list
#   contains    linear      linear
#   get        constant     linear
#   prepend     linear     constant O(1)
#   append     constant     linear
#   remove       O(n)        O(n)


# It runs in linear time.
def index_of(lst: list[int], value: int) -> int:
    """Returns the index where the given value can be found."""
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    raise ValueError


# It runs in linear time.
def index_of2(lst: list[int], value: int) -> int:
    """Returns the index where the given value can be found."""
    return lst.index(value)
