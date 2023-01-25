import unittest

from bst import (
    is_empty, search, insert, delete, find_min, find_max, height, TreeNode, prefix_iterator)


class Tests(unittest.TestCase):
    def test_sample(self):
        tree = None

        self.assertTrue(is_empty(tree))
        self.assertEqual(height(tree), -1)
        self.assertFalse(search(tree, 10))
        self.assertEqual(delete(tree, 10), tree)

        with self.assertRaises(ValueError):
            find_min(tree)

        with self.assertRaises(ValueError):
            find_max(tree)

        tree = insert(tree, 10)

        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 10))
        self.assertEqual(find_min(tree), 10)
        self.assertEqual(find_max(tree), 10)

    def test_sample2(self):
        tree = TreeNode(
            12,
            TreeNode(7, TreeNode(2), TreeNode(10, TreeNode(9), None)),
            TreeNode(18, TreeNode(14), TreeNode(20)))

        self.assertTrue(search(tree, 18))
        self.assertFalse(search(tree, 299))

        tree = insert(tree, -1)
        tree = insert(tree, 3)
        tree = insert(tree, 19)
        tree = insert(tree, 31)

        self.assertTrue(search(tree, 19))
        self.assertTrue(search(tree, 3))
        self.assertEqual(find_min(tree), -1)
        self.assertEqual(find_max(tree), 31)
        self.assertEqual(height(tree), 3)

    def test_sample3(self):
        tree = TreeNode(
            12,
            TreeNode(7, TreeNode(2), TreeNode(10, TreeNode(9), None)),
            TreeNode(18, TreeNode(14), TreeNode(20)))

        delete(tree, 18)
        delete(tree, 10)
        delete(tree, 9)

        self.assertTrue(search(tree, 20))
        self.assertFalse(search(tree, 18))
        self.assertFalse(search(tree, 9))
        self.assertEqual(height(tree), 2)

    def test_sample4(self):
        tree = TreeNode(
            12,
            TreeNode(7, TreeNode(2), TreeNode(10, TreeNode(9), None)),
            TreeNode(18, TreeNode(14), TreeNode(20)))

        delete(tree, 7)

        self.assertFalse(search(tree, 7))

    def test_sample5(self):
        tree = TreeNode(
            12,
            TreeNode(7, TreeNode(2), TreeNode(10, TreeNode(9), None)),
            TreeNode(18, TreeNode(14), TreeNode(20)))

        delete(tree, 12)

        self.assertFalse(search(tree, 12))


if __name__ == '__main__':
    unittest.main()
