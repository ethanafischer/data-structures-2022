from __future__ import annotations

from typing import Optional


class Node:  # Class formerly known as Pair
    def __init__(self, value, nxt: Optional[Node]):
        self.value = value
        self.next = nxt

    def __repr__(self):
        return 'Node(%r, %r)' % (self.value, self.next)


class LinkedQueue:
    def __init__(
            self,
            head: Optional[Node] = None,
            tail: Optional[Node] = None):
        self.head = head
        self.tail = tail


def enqueue(queue: LinkedQueue, value) -> None:
    if queue.tail is None:
        queue.tail = Node(value, None)
        queue.head = queue.tail
    else:
        queue.tail.next = Node(value, None)
        queue.tail = queue.tail.next


queue = LinkedQueue()
enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)
print(queue.head)
print(queue.tail)
