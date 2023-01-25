from __future__ import annotations

from typing import Optional
from circular_queue import dequeue, enqueue


class TreeNode:
    def __init__(
            self,
            value: int,
            left: Optional[TreeNode] = None,
            right: Optional[TreeNode] = None):
        self.value = value
        self.left = left
        self.right = right


IntTree = Optional[TreeNode]


def contains(tree: IntTree, value: int) -> bool:
    """Returns True if value is in tree, False otherwise."""
    if tree is None:
        return False
    else:
        return (
                tree.value == value or
                contains(tree.left, value) or
                contains(tree.right, value)
        )


def print_in_order(tree: IntTree) -> None:
    if tree is None:
        return

    print_in_order(tree.left)
    print(tree.value)
    print_in_order(tree.right)


def print_post_order(tree: IntTree) -> None:
    if tree is None:
        return
    print_post_order(tree.left)
    print_post_order(tree.right)
    print(tree.value)


def level_order_iterator(tree: IntTree) -> None:
    queue = empty_queue()
    if tree is not None:
        enqueue(queue, tree)

    while not is_empty(queue):
        cur = dequeue(queue)
        yield cur.value

        if cur.left is not None:
            enqueue(queue, cur.left)

        if cur.right is not None:
            enqueue(queue, cur.right)


def print_pre_order(tree: IntTree) -> None:
    if tree is None:
        return

    print(tree.value)
    print_pre_order(tree.left)
    print_pre_order(tree.right)


# It is O(n)
def search(lst: list[int], value: int) -> bool:
    """Returns True if value is in the list, False otherwise."""
    for item in lst:
        if item == value:
            return True

    return False


# It is O(log n)
def binary_search(lst: list[int], value: int) -> bool:
    """Returns True if value is in the list, False otherwise.

    The list *must* be sorted.
    """
    lo = 0
    hi = len(lst)

    while lo < hi:
        mid = (lo + hi) // 2

        if value < lst[mid]:
            hi = mid
        elif value > lst[mid]:
            lo = mid + 1
        else:
            return True


if __name__ == '__main__':
    my_tree = TreeNode(12, TreeNode(7, TreeNode(2), TreeNode(10, TreeNode(9), None)),
                       TreeNode(18, TreeNode(14), TreeNode(20)))

    """gen = level_order_iterator(my_tree)
    print(next(gen))"""
    for val in level_order_iterator(my_tree):
        print(val)

print_in_order(my_tree)
print_post_order(my_tree)
level_order_iterator(my_tree)
print_pre_order(my_tree)
