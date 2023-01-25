# NOTE: Do not import anything else.
from __future__ import annotations

from typing import Any


class MaxHeap:
    def __init__(self):
        self.items: list[Any] = [None]


def enqueue(heap: MaxHeap, item: Any) -> None:
    heap.items.append(item)
    idx = size(heap)
    while idx > 1 and item > heap.items[idx // 2]:
        heap.items[idx], heap.items[idx // 2] = heap.items[idx // 2], heap.items[idx]
        idx //= 2


def dequeue(heap: MaxHeap) -> Any:
    if size(heap) == 0:
        raise IndexError

    if size(heap) == 1:
        return heap.items.pop(1)

    rem, heap.items[1] = heap.items[1], heap.items.pop()
    percolate_down(heap, 1)
    return rem


def peek(heap: MaxHeap) -> Any:
    if heap.items == [None]:
        raise IndexError
    return heap.items[1]


def size(heap: MaxHeap) -> Any:
    return len(heap.items) - 1


# NOTE: To be used for testing
def _contents(heap: MaxHeap) -> list[Any]:
    return heap.items[1:]


def heapify(lst: list[Any]) -> MaxHeap:
    heap = MaxHeap()
    heap.items += lst
    for i in range(len(heap.items) - 1, 0, -1):
        percolate_down(heap, i)
    return heap


def percolate_down(heap, idx):
    swap = True
    while idx * 2 < (size(heap) + 1) and swap:
        g = heap.items[2 * idx]
        g_idx = 2 * idx
        if 2 * idx + 1 < size(heap) + 1 and g < heap.items[2 * idx + 1]:
            g = heap.items[2 * idx + 1]
            g_idx = 2 * idx + 1
        if heap.items[idx] < g:
            heap.items[idx], heap.items[g_idx] = heap.items[g_idx], heap.items[idx]
            idx = g_idx
        else:
            swap = False
    return heap


def heap_sort(lst: list[Any]) -> None:
    # call heapify, then dequeue
    heap = heapify(lst)
    for i in range(len(lst) - 1, -1, -1):
        lst[i] = dequeue(heap)
# h = MaxHeap()
