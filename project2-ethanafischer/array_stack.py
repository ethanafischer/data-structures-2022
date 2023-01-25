from __future__ import annotations

from typing import Any


class ArrayStack:
    def __init__(self, capacity: int = 5):
        self.items: list[Any] = [None] * capacity
        self.capacity: int = capacity
        self.size: int = 0


stack = ArrayStack()
stack.items: list[Any] = [0, 100, 200, 300, 400]
stack.capacity: int = 5
stack.size: int = 5


def empty_stack() -> ArrayStack:
    return ArrayStack()


def push(stack: ArrayStack, value: Any) -> None:
    if stack.size == stack.capacity:
        stack.capacity *= 2
        new_stack: list[Any] = [None] * stack.capacity
        for i in range(0, stack.size):
            new_stack[i] = stack.items[i]
        stack.items = new_stack
    stack.items[stack.size] = value
    stack.size += 1


def pop(stack: ArrayStack) -> Any:
    if stack.size == 0:
        raise IndexError
    stack.size -= 1
    removed = stack.items[stack.size]
    stack.items[stack.size] = None
    return removed


def peek(stack: ArrayStack) -> Any:
    if stack.size == 0:
        raise IndexError
    return stack.items[stack.size - 1]


def is_empty(stack: ArrayStack) -> bool:
    if stack.size == 0:
        return True
    return False


def size(stack: ArrayStack) -> int:
    return stack.size
