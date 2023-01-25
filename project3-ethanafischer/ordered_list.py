from __future__ import annotations

from typing import Any, Optional


class Node:
    """Represents a node to be used in a doubly linked list."""

    def __init__(
            self,
            value: Any,
            prev: Optional[Node] = None,
            nxt: Optional[Node] = None):
        self.value = value

        # NOTE: This means that if prev and nxt are None, self.prev and
        # self.next will be self.  You may find this useful.  This means
        # that self.prev and self.next aren't Optional Nodes, they are
        # always Nodes.
        self.prev: Node = prev or self
        self.next: Node = nxt or self


class OrderedList:
    """A circular, doubly linked list of items, from lowest to highest.

    The contents of the list *must* have an accurate notation of less
    than and of equality.  That is to say, the contents of the list must
    implement both __lt__ and __eq__.  This *does not* mean that your
    OrderedList (or your Nodes) should have __lt__ and __eq__.

    Your implementation should use a single dummy node as the "head".
    """

    def __init__(self):
        self.head = Node("dummy")
        self.size = 0


def insert(lst: OrderedList, value: Any) -> None:
    """Inserts the value into the list in the proper (ordered) location."""
    cur = lst.head.next

    while cur != lst.head and value >= cur.value:
        cur = cur.next
    cur.prev.next = Node(value, cur.prev, cur)
    cur.prev = cur.prev.next
    lst.size += 1


def remove(lst: OrderedList, value: Any) -> None:
    """Removes the first occurrence of value from the list.

    Raises ValueError if the value is not present.
    """
    cur = lst.head.next
    while cur != lst.head and cur.value != value:
        cur = cur.next
    if cur.value != value:
        raise ValueError("value is not present")
    cur.prev.next = cur.next
    cur.next.prev = cur.prev
    lst.size -= 1


def contains(lst: OrderedList, value: Any) -> bool:
    """Returns True if the value is in the list, False otherwise."""
    cur = lst.head.next
    while cur != lst.head and value > cur.value:
        cur = cur.next
    if cur.value == value:
        return True
    return False


def index(lst: OrderedList, value: Any) -> int:
    """Returns the index of the first occurrence of value in the list.

    Raises ValueError if the value is not present.
    """
    cur = lst.head.next
    index = 0
    while cur != lst.head:
        if cur.value == value:
            return index
        cur = cur.next
        index += 1
    raise ValueError("value is not present")


def get(lst: OrderedList, index: int) -> Any:
    """Returns the value at index in the list.

    Raises IndexError if the index is out of range.
    """
    cur = lst.head.next
    if index >= lst.size:
        raise IndexError("index is out of range")
    for i in range(index):
        cur = cur.next
    return cur.value


def pop(lst: OrderedList, index: int) -> Any:
    """Removes and returns the value at index in the list.

    Raises IndexError if the index is out of range.
    """
    if index >= lst.size:
        raise IndexError("index is out of range")

    cur = lst.head.next
    cur_index = 0
    while cur_index < lst.size and cur_index != index:
        cur = cur.next
        cur_index += 1
    removed = cur.value
    cur.prev.next = cur.next
    cur.next.prev = cur.prev
    lst.size -= 1
    return removed


def is_empty(lst: OrderedList) -> bool:
    """Returns True if the list is empty, False otherwise."""
    if lst.size == 0:
        return True
    return False


def size(lst: OrderedList) -> int:
    """Returns the number if items in the list."""
    return lst.size
