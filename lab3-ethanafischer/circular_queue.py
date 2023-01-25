from typing import Any


class CircularQueue:
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.items = capacity * [None]
        self.start = 0
        self.size = 0


def empty_queue() -> CircularQueue:
    return CircularQueue()


def enqueue(queue: CircularQueue, value: Any) -> None:
    if queue.size == queue.capacity:
        new_queue = [None] * queue.capacity * 2
        for i in range(queue.size):
            new_queue[i] = queue.items[(queue.start + i) % queue.capacity]
        queue.items = new_queue
        queue.capacity *= 2
        queue.start = 0
    queue.items[(queue.start + queue.size) % queue.capacity] = value
    queue.size += 1


def dequeue(queue: CircularQueue) -> Any:
    if queue.size <= 0:
        raise IndexError
    removed = queue.items[queue.start]
    queue.items[queue.start] = None
    queue.start += 1
    queue.size -= 1
    return removed


def peek(queue: CircularQueue) -> Any:
    if queue.size <= 0:
        raise IndexError
    return queue.items[queue.start]


def is_empty(queue: CircularQueue) -> bool:
    if queue.size == 0:
        return True
    return False


def size(queue: CircularQueue) -> int:
    return queue.size
