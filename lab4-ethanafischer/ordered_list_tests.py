import unittest

from ordered_list import (
    OrderedList, insert, remove, contains, index, get, pop, is_empty, size)


class Tests(unittest.TestCase):
    def test_simple(self) -> None:
        my_list = OrderedList()

        insert(my_list, 10)

        self.assertEqual(size(my_list), 1)
        self.assertTrue(contains(my_list, 10))
        self.assertFalse(is_empty(my_list))
        self.assertEqual(index(my_list, 10), 0)
        self.assertEqual(get(my_list, 0), 10)

        remove(my_list, 10)

        self.assertEqual(size(my_list), 0)
        self.assertFalse(contains(my_list, 10))
        self.assertTrue(is_empty(my_list))

        insert(my_list, 10)

        self.assertEqual(pop(my_list, 0), 10)
        self.assertEqual(size(my_list), 0)
        self.assertFalse(contains(my_list, 10))
        self.assertTrue(is_empty(my_list))

    def test_insert(self):
        lst = OrderedList()

        insert(lst, 4)
        insert(lst, 10)
        insert(lst, 40)
        insert(lst, 3)
        insert(lst, -1)
        self.assertEqual(size(lst), 5)
        self.assertTrue(get(lst, 0), -1)

    def test_remove(self):
        lst = OrderedList()

        insert(lst, 4)
        insert(lst, 10)
        insert(lst, 40)
        insert(lst, 3)
        insert(lst, -1)

        remove(lst, 40)
        self.assertEqual(size(lst), 4)
        with self.assertRaises(ValueError):
            remove(lst, 200)

    def test_contains(self):
        lst = OrderedList()

        insert(lst, 4)
        insert(lst, 10)
        insert(lst, 40)
        insert(lst, 3)
        insert(lst, -1)
        self.assertFalse(contains(lst, 200))
        self.assertTrue(contains(lst, 3))

    def test_index(self):
        lst = OrderedList()

        insert(lst, 4)
        insert(lst, 10)
        insert(lst, 40)
        insert(lst, 40)
        insert(lst, 3)
        insert(lst, -1)
        self.assertEqual(index(lst, 40), 4)
        with self.assertRaises(ValueError):
            index(lst, 200)

    def test_get(self):
        lst = OrderedList()

        insert(lst, 4)
        insert(lst, 10)
        insert(lst, 40)
        insert(lst, 3)
        insert(lst, -1)
        self.assertEqual(get(lst, 2), 4)
        with self.assertRaises(IndexError):
            get(lst, size(lst) + 3)

    def test_pop(self):
        lst = OrderedList()

        insert(lst, 4)
        insert(lst, 10)
        insert(lst, 40)
        insert(lst, 3)
        insert(lst, -1)

        pop(lst, 2)

        self.assertEqual(size(lst), 4)
        self.assertFalse(contains(lst, 4))
        with self.assertRaises(IndexError):
            pop(lst, size(lst) + 3)

    def test_pop2(self):
        lst = OrderedList()

        insert(lst, 4)
        insert(lst, 10)
        insert(lst, 40)
        insert(lst, 3)
        insert(lst, -1)
        self.assertEqual(pop(lst, 0), -1)

    def test_is_empty(self):
        lst = OrderedList()

        self.assertTrue(is_empty(lst))
        insert(lst, 4)
        insert(lst, 10)
        insert(lst, 40)
        insert(lst, 3)
        insert(lst, -1)
        self.assertFalse(is_empty(lst))

    def test_size(self):
        lst = OrderedList()

        insert(lst, 4)
        insert(lst, 5)
        self.assertEqual(size(lst), 2)


if __name__ == '__main__':
    unittest.main()
