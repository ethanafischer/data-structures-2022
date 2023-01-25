from __future__ import annotations


class ArrayList:
    # NOTE: Initial capacity is somewhat arbitrary.  To making testing
    # resizing easier, you'll probably want a small initial capacity.
    # In practice, you'd probably have an initial capacity of 5–10.
    def __init__(self, capacity: int = 1):
        self.arr: list[object] = [None] * capacity
        self.capacity = capacity
        self.size = 0


lst = ArrayList()
lst.arr = [0, 10, 20, 30, 40, 50, 60, 70, 8, 9]
lst.capacity = 10
lst.size = 10


def empty_list() -> ArrayList:
    return ArrayList()


def add(lst: ArrayList, index: int, value: object) -> ArrayList:
    if index < 0 or index > lst.size:
        raise IndexError
    if lst.size == lst.capacity:
        lst.capacity *= 2
        new_arr: list[object] = [None] * lst.capacity
        for i in range(0, lst.size):
            new_arr[i] = lst.arr[i]
        lst.arr = new_arr

    for i in range(lst.size, index, -1):
        lst.arr[i] = lst.arr[i - 1]
    lst.size += 1
    lst.arr[index] = value
    return lst


def length(lst: ArrayList) -> int:
    return lst.size


def get(lst: ArrayList, index: int) -> object:
    if index < 0 or index >= lst.size:
        raise IndexError
    return lst.arr[index]


def setitem(lst: ArrayList, index: int, value: object) -> ArrayList:
    if index < 0 or index >= lst.size:
        raise IndexError
    lst.arr[index] = value
    return lst


def remove(lst: ArrayList, index: int) -> tuple[object, ArrayList]:
    if index < 0 or index >= lst.size:
        raise IndexError
    lst.size -= 1
    removed = lst.arr[index]
    for i in range(index, lst.size):
        lst.arr[i] = lst.arr[i + 1]
    lst.arr[lst.size] = None
    return removed, lst
