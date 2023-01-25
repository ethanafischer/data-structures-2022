import unittest

from linked_list import (
    empty_list, add, length, get, setitem, remove, Pair)


class Tests(unittest.TestCase):

    def test_length_empty_list(self) -> None:
        my_list = empty_list()
        self.assertEqual(length(my_list), 0)

    def test_contents_empty_list(self) -> None:
        my_list = empty_list()
        self.assertEqual(my_list, None)

    def test_add_1(self) -> None:
        lst = Pair(0, Pair(100, Pair(200, Pair(300, None))))
        my_list = add(lst, 3, 12)
        my_list2 = Pair(0, Pair(100, Pair(200, Pair(12, Pair(300, None)))))
        self.assertEqual(my_list, my_list2)

    def test_add_IndexError(self) -> None:
        lst = Pair(0, Pair(100, Pair(200, Pair(300, None))))
        with self.assertRaises(IndexError):
            add(lst, 100, 12)

    def test_length_1(self) -> None:
        lst = Pair(0, Pair(100, Pair(200, Pair(300, None))))
        my_list = length(lst)
        self.assertEqual(my_list, 4)

    def test_length_None(self) -> None:
        lst = None
        self.assertEqual(length(lst), 0)

    def test_get_1(self) -> None:
        lst = Pair(0, Pair(100, Pair(200, Pair(300, None))))
        self.assertEqual(get(lst, 2), 200)

    def test_get_IndexError(self) -> None:
        lst = Pair(0, Pair(100, Pair(200, Pair(300, None))))
        with self.assertRaises(IndexError):
            get(lst, 100)

    def test_setitem_1(self) -> None:
        lst = Pair(0, Pair(100, Pair(200, Pair(300, None))))
        my_list = Pair(0, Pair(100, Pair(201, Pair(300, None))))
        self.assertEqual(setitem(lst, 2, 201), my_list)

    def test_setitem_IndexError(self) -> None:
        lst = Pair(0, Pair(100, Pair(200, Pair(300, None))))
        with self.assertRaises(IndexError):
            setitem(lst, 100, 201)

    def test_remove_1(self) -> None:
        lst = Pair(0, Pair(100, Pair(200, Pair(300, None))))
        removed = 200
        rem_list = Pair(0, Pair(100, Pair(300, None)))
        self.assertEqual(remove(lst, 2), (removed, rem_list))

    def test_remove_IndexError(self) -> None:
        lst = Pair(0, Pair(100, Pair(200, Pair(300, None))))
        with self.assertRaises(IndexError):
            remove(lst, 100)


if __name__ == '__main__':
    unittest.main()
