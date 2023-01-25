from __future__ import annotations

from typing import Optional, List


# NOTE: This must be iterative, not recursive.  You should *not* modify
# the input list in any way.
def max_iterative(lst: Optional[list[float]]) -> Optional[float]:
    """Returns the maximum value in the given list.

    If the given list is empty, returns None.  If the given list is
    None, raises a ValueError.
    """
    if lst is None:
        raise ValueError('error. list cannot equal None')

    if len(lst) == 0:
        return None

    max_val = 0
    for num in lst:
        if num >= max_val:
            max_val = num
    return max_val


# NOTE: This must be iterative, not recursive.  You should *not* modify
# the input list in any way, it will return a new list.
def reverse_list_iterative(lst: Optional[list[float]]) -> list[float]:
    """Reverses the given list.

    If the given list is None, raises a ValueError.
    """
    if lst is None:
        raise ValueError('error. list cannot equal None')

    new_list = []
    length = len(lst)
    for i in range(len(lst)):
        new_list.append(lst[length - i - 1])
    return new_list


# NOTE: This must be recursive, not iterative.  You should *not* modify
# the input list in any way, it will return a new list.
# NOTE: This will be inefficient, please never do this outside of this
# lab.  In the future, we will quantify just how inefficient this is.
def reverse_list_recursive(lst: Optional[list[float]]) -> list[float]:
    """Reverses the given list.

    If the given list is None, raises a ValueError.
    """
    if lst == None:
        raise ValueError('error. list cannot equal None')

    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list_recursive(lst[:-1])
