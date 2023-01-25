from __future__ import annotations
import unittest
from typing import Optional



class Point:  # todo example
    """Represents a point in 2D space."""

    def __init__(self, x: float, y: float):  # initialize object
        self.x = x
        self.y = y

    def __repr__(self):  # the string will look identical to the code used to create what is being printed
        return 'Point(%r, %r)' % (self.x, self.y)

    def __eq__(self, other):  # compares two elements to see if they are equal
        return (
                isinstance(other, Point) and
                self.x == other.x and
                self.y == other.y
        )


# Optional[int] means,
# - int, or
# - None
def quadrant(p: Point) -> Optional[int]:
    """Returns the quadrant the given point is in.

    If the point is on an axis or the origin, returns None.
    """
    if p.x > 0 and p.y > 0:
        return 1
    elif p.x < 0 and p.y > 0:
        return 2
    elif p.x < 0 and p.y < 0:
        return 3
    elif p.x > 0 and p.y < 0:
        return 4
    else:
        return None


class PointTestCases(unittest.TestCase):
    def test(self):
        self.assertEqual(5, 5)

    def test_quadrant1(self):
        self.assertEqual(
            quadrant(Point(2, 2)), 1)

    def test_quadrant2(self):
        self.assertEqual(
            quadrant(Point(-3, 3)), 2)

    def test_quadrant3(self):
        self.assertEqual(
            quadrant(Point(-3, -7)), 3)

    def test_quadrant4(self):
        self.assertEqual(
            quadrant(Point(3, -6)), 4)

    def test_axis(self):
        # self.assertEqual(quadrant(Point(6, 0)), None)
        # is roughly the same as
        self.assertIsNone(quadrant(Point(6, 0)))


def sum_iterative(n: int) -> int:
    """Returns the sum 0 + 1 + 2 + ... + n."""
    total = 0
    for i in range(n + 1):
        total += 1
    return total


def sum_recursive(n: int) -> int:
    """Returns the sum 0 + 1 + 2 + ... + n."""
    if n == 0:
        return 0

    return sum_recursive(n - 1) + n


def sum_rec2(n: int, total: int = 0) -> int:
    """Returns the sum 0 + 1 + 2 + ... + n."""
    if n == 0:
        return total

    return sum_rec2(n - 1, total + n)


def contains(lst: list[int], value: int) -> bool:
    """Returns True if the value is in the list, False otherwise."""
    for num in lst:
        if num == value:
            return True
    return False


def contains_rec(lst: list[int], value: int) -> bool:
    """Returns True if the value is in the list, False otherwise."""
    if len(lst) == 0:
        return False

    return value == lst[0] or contains_rec(lst[1:], value)

'''
 def contains_rec2(lst: list[int], value: int) -> bool:
    """Returns True if the value is in the list, False otherwise."""
    if len(lst) == 0:
        return False

    return value == lst[index] or contains_rec2(lst, value, index + 1)
'''

if __name__ == '__main__':
    unittest.main()
