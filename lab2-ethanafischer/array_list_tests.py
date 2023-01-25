import unittest

from array_list import (
    empty_list, add, length, get, setitem, remove, ArrayList)

lst = ArrayList()
lst.arr = [0, 10, 20, 30, None]
lst.capacity = 5
lst.size = 4


class Tests(unittest.TestCase):
    def test_length_empty_list(self) -> None:
        my_list = empty_list()
        self.assertEqual(length(my_list), 0)

    def test_small_add(self):
        lst = add(add(empty_list(), 0, 12), 1, 4)

        self.assertEqual(length(lst), 2)
        self.assertEqual(get(lst, 0), 12)
        self.assertEqual(get(lst, 1), 4)

        with self.assertRaises(IndexError):
            get(lst, 2)

    def test_add_IndexError(self):
        with self.assertRaises(IndexError):
            add(lst, 100, 2)

    def test_length(self):
        self.assertEqual(length(lst), lst.size)

    def test_get(self):
        self.assertEqual(get(lst, 2), 20)

    def test_get_IndexError(self):
        with self.assertRaises(IndexError):
            get(lst, 100)

    def test_setitem(self):
        lst = add(add(add(empty_list(), 0, 2), 0, 78), 0, 1000)
        setitem(lst, 2, 0)
        self.assertEqual(length(lst), 3)
        self.assertEqual(get(lst, 2), 0)

    def test_setitem_IndexError(self):
        with self.assertRaises(IndexError):
            setitem(lst, 100, 0)

    def test_small_remove(self):
        lst = add(add(add(empty_list(), 0, 2), 0, 78), 0, 1000)
        val, lst = remove(lst, 0)

        self.assertEqual(val, 1000)
        self.assertEqual(length(lst), 2)
        self.assertEqual(get(lst, 0), 78)
        self.assertEqual(get(lst, 1), 2)

        with self.assertRaises(IndexError):
            get(lst, 2)

    def test_remove_IndexError(self):
        with self.assertRaises(IndexError):
            remove(lst, 100)


if __name__ == '__main__':
    unittest.main()
