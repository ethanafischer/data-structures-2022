import unittest

# NOTE: Do not add more imports
from sorts import selection_sort, insertion_sort, merge_sort


class Tests(unittest.TestCase):
    def test_merge_sort_01(self):
        lst = [10]

        # Sorting an singleton list should do no comparisons
        self.assertEqual(merge_sort(lst), 0)

        # The list shouldn't change
        self.assertEqual(lst, [10])

    def test_merge_sort_02(self):
        lst = [50, 60, 10, 20, 80, 40, 30, 70]

        merge_sort(lst)

        # The list should now be sorted
        self.assertEqual(lst, [10, 20, 30, 40, 50, 60, 70, 80])

    def test_selection_sort_01(self):
        lst = [25, 13, -100, -12, 60, 31, -76, 2]

        selection_sort(lst)

        self.assertEqual(lst, [-100, -76, -12, 2, 13, 25, 31, 60])

    def test_selection_sort_02(self):
        lst = [10]

        self.assertEqual(selection_sort(lst), 0)

        self.assertEqual(lst, [10])

    def test_insertion_sort_01(self):
        lst = [25, 13, -100, -12, 60, 31, -76, 2]

        insertion_sort(lst)

        self.assertEqual(lst, [-100, -76, -12, 2, 13, 25, 31, 60])

    def test_insertion_sort_02(self):
        lst = [10]

        self.assertEqual(insertion_sort(lst), 0)

        self.assertEqual(lst, [10])

    def test_insertion_sort_03(self):
        lst = [11, 5]

        self.assertEqual(insertion_sort(lst), 1)

        self.assertEqual(lst, [5, 11])


if __name__ == '__main__':
    unittest.main()
