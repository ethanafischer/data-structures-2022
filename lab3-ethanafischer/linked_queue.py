from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, nxt: Optional[Node] = None):
        self.value = value
        self.next = nxt

    def __repr__(self):
        return 'Node(%r, %r)' % (self.value, self.next)


class LinkedQueue:
    def __init__(
            self,
            head: Optional[Node] = None,
            tail: Optional[Node] = None,
            size: int = 0):
        self.head = head
        self.tail = tail
        self.size = size


def empty_queue() -> LinkedQueue:
    return LinkedQueue()


def enqueue(queue: LinkedQueue, value: Any) -> None:
    if queue.head is None:
        queue.tail = Node(value, None)
        queue.head = queue.tail
        queue.size += 1
    else:
        queue.tail.next = Node(value, None)
        queue.tail = queue.tail.next
        queue.size += 1


def dequeue(queue: LinkedQueue) -> Any:
    if queue.head is None:
        raise IndexError
    removed = queue.head.value
    queue.head = queue.head.next
    queue.size -= 1
    return removed


def peek(queue: LinkedQueue) -> Any:
    if queue.head is None:
        raise IndexError
    return queue.head.value


def is_empty(queue: LinkedQueue) -> bool:
    if queue.head is None:
        return True
    return False


def size(queue: LinkedQueue) -> int:
    return queue.size
