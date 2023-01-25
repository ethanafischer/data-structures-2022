from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Optional


class TreeNode:
    def __init__(
            self,
            value: Any,
            left: Optional[TreeNode] = None,
            right: Optional[TreeNode] = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode(%r, %r, %r)' % (self.value, self.left, self.right)


BST = Optional[TreeNode]


def is_empty(tree: BST) -> bool:
    """Returns True if the tree is empty, False otherwise."""
    if tree is None:
        return True
    return False


def search(tree: BST, value: Any) -> bool:
    """Returns True if value is in tree, False otherwise."""
    if tree is None:
        return False
    if tree.value == value:
        return True
    if tree.value < value:
        return search(tree.right, value)
    elif tree.value > value:
        return search(tree.left, value)


def insert(tree: BST, value: Any) -> BST:
    """Inserts the value into the tree in the proper location."""
    if tree is None:
        return TreeNode(value)
    if value < tree.value:
        return TreeNode(tree.value, insert(tree.left, value), tree.right)
    else:
        return TreeNode(tree.value, tree.left, insert(tree.right, value))


def delete_helper(tree):
    """Find leftmost leaf"""
    if tree.right is None:
        return tree.value, tree.left
    return delete_helper(tree.right)


def delete(tree: BST, value: Any) -> BST:
    """Removes the value from the tree (if present).

    If the value is not present, this function does nothing.
    """
    if tree is None:
        return tree

    if tree.value > value:
        tree.left = delete(tree.left, value)
    if tree.value < value:
        tree.right = delete(tree.right, value)

    if tree.value is value:
        if tree.left is None:
            return tree.right
        if tree.right is None:
            return tree.left
        temp_value, temp = delete_helper(tree.left)
        tree.value = temp_value
        tree.left = delete(tree.left, temp_value)

    return tree


def find_min(tree: BST) -> Any:
    """Returns the smallest value in the tree."""
    if tree is None:
        raise ValueError
    if tree.left is None:
        return tree.value
    return find_min(tree.left)


def find_max(tree: BST) -> Any:
    """Returns the largest value in the tree."""
    if tree is None:
        raise ValueError
    if tree.right is None:
        return tree.value
    return find_max(tree.right)


def height(tree: BST) -> int:
    """Returns the height of the tree."""
    if tree is None:
        return -1
    return 1 + max(height(tree.left), height(tree.right))


def prefix_iterator(tree: BST) -> Iterator[Any]:
    """Returns an iterator over the tree in prefix order."""
    if tree:
        yield tree.value
        yield from prefix_iterator(tree.left)
        yield from prefix_iterator(tree.right)


def infix_iterator(tree: BST) -> Iterator[Any]:
    """Returns an iterator over the tree in infix order."""
    if tree:
        yield from infix_iterator(tree.left)
        yield tree.value
        yield from infix_iterator(tree.right)


def postfix_iterator(tree: BST) -> Iterator[Any]:
    """Returns an iterator over the tree in postfix order."""
    if tree:
        yield from postfix_iterator(tree.left)
        yield from postfix_iterator(tree.right)
        yield tree.value
