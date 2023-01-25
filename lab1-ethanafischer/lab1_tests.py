import unittest

import lab1


class Tests(unittest.TestCase):
    def test_max_none(self) -> None:
        with self.assertRaises(ValueError):
            lab1.max_iterative(None)

    def test_max_1(self):
        lst = []
        self.assertEqual(lab1.max_iterative(lst), None)

    def test_max_2(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(lab1.max_iterative(lst), 5)

    def test_max_3(self):
        lst = [5, 5, 5, 5, 5]
        self.assertEqual(lab1.max_iterative(lst), 5)

    def test_max_4(self):
        lst = [5, 6, 5, 7, 6]
        self.assertEqual(lab1.max_iterative(lst), 7)

    def test_max_5(self):
        lst = [5, 4, 3, 2, 1]
        self.assertEqual(lab1.max_iterative(lst), 5)

    def test_max_6(self):
        lst = [0, 0, 0, -1, -2, 0]
        self.assertEqual(lab1.max_iterative(lst), 0)

    def test_reverse_iterative_none(self) -> None:
        with self.assertRaises(ValueError):
            lab1.reverse_list_iterative(None)

    def test_reverse_iterative_1(self):
        lst = [0, 3, 0, -1, -2, 0]
        self.assertEqual(lab1.reverse_list_iterative(lst), [0, -2, -1, 0, 3, 0])

    def test_reverse_iterative_2(self):
        lst = [5, 5, 5, 5, 5]
        self.assertEqual(lab1.reverse_list_iterative(lst), [5, 5, 5, 5, 5])

    def test_reverse_iterative_3(self):
        lst = []
        self.assertEqual(lab1.reverse_list_iterative(lst), [])

    def test_reverse_iterative_4(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(lab1.reverse_list_iterative(lst), [5, 4, 3, 2, 1])

    def test_reverse_iterative_5(self):
        lst = [5, 5, 5, 5, 5]
        self.assertEqual(lab1.reverse_list_iterative(lst), [5, 5, 5, 5, 5])

    def test_reverse_iterative_6(self):
        lst = [5, 4, 3, 2, 1]
        self.assertEqual(lab1.reverse_list_iterative(lst), [1, 2, 3, 4, 5])

    def test_reverse_iterative_7(self):
        lst = [1]
        self.assertEqual(lab1.reverse_list_iterative(lst), [1])

    def test_reverse_recursive_none(self) -> None:
        with self.assertRaises(ValueError):
            lab1.reverse_list_recursive(None)

    def test_reverse_recursive_1(self):
        lst = [0, 3, 0, -1, -2, 0]
        self.assertEqual(lab1.reverse_list_recursive(lst), [0, -2, -1, 0, 3, 0])

    def test_reverse_recursive_2(self):
        lst = [5, 5, 5, 5, 5]
        self.assertEqual(lab1.reverse_list_recursive(lst), [5, 5, 5, 5, 5])

    def test_reverse_recursive_3(self):
        lst = []
        self.assertEqual(lab1.reverse_list_recursive(lst), [])

    def test_reverse_recursive_4(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(lab1.reverse_list_recursive(lst), [5, 4, 3, 2, 1])

    def test_reverse_recursive_5(self):
        lst = [5, 5, 5, 5, 5]
        self.assertEqual(lab1.reverse_list_recursive(lst), [5, 5, 5, 5, 5])

    def test_reverse_recursive_6(self):
        lst = [5, 4, 3, 2, 1]
        self.assertEqual(lab1.reverse_list_recursive(lst), [1, 2, 3, 4, 5])

    def test_reverse_recursive_7(self):
        lst = [1]
        self.assertEqual(lab1.reverse_list_recursive(lst), [1])

    # TODO: Add more tests!


if __name__ == '__main__':
    unittest.main()
