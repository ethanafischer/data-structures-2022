from __future__ import annotations
import unittest
from typing import Optional


# Linked list
# a NumList is one of
# - "mt", or
# - Pair(first, rest)
# my_list = Pair(12, Pair(3, "mt"))
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


# NumList int -> bool
def contains(num_list: NumList, value: int) -> bool:
    """Returns True if the value is in the list, False otherwise"""
    if num_list is None:
        return False
    else:
        return value == num_list.first or contains(num_list.rest, value)


def length(num_list: NumList) -> int:
    """Returns the number of elements in the list."""
    if num_list is None:
        return 0
    else:
        return 1 + length(num_list.rest)


def length_acc(num_list: NumList, cur_length: int = 0) -> int:
    """Returns the number of elements in the list."""
    if num_list is None:
        return cur_length
    else:
        return length_acc(num_list.rest, cur_length + 1)


def double_list(num_list: NumList) -> NumList:
    """Returns a new list of all the values in the given list, doubled."""
    if num_list is None:
        return None
    else:
        return Pair(2 * num_list.first, double_list(num_list.rest))


def filter_positive(num_list: NumList) -> NumList:
    """Returns a new list with only the positive values from the given list."""
    if num_list is None:
        return None

    if num_list.first > 0:
        return Pair(num_list.first, filter_positive(num_list.rest))

    return filter_positive(num_list.rest)


def add(num_list: NumList) -> int:
    if num_list is None:
        return 0
    else:
        return num_list.first + add(num_list.rest)


def get(num_list: NumList, index) -> int:
    if num_list is None:
        return None
    while j < index:
        j += 1
        return get(num_list.rest)


my_list = Pair(12, Pair(3, Pair(-4, Pair(5, None))))
print(add(my_list))

if __name__ == '__main__':
    unittest.main()
