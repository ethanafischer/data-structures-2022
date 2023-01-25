import unittest

from bst import (
    TreeNode, prefix_iterator, infix_iterator, postfix_iterator)


class Tests(unittest.TestCase):
    def test_sample(self):
        tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7)))

        infix_iter = infix_iterator(tree)
        expected = [1, 2, 3, 4, 5, 6, 7]

        for value in expected:
            self.assertEqual(next(infix_iter), value)

        with self.assertRaises(StopIteration):
            next(infix_iter)

    def test_sample2(self):
        tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7)))

        prefix_iter = prefix_iterator(tree)
        expected = [4, 2, 1, 3, 6, 5, 7]

        for value in expected:
            self.assertEqual(next(prefix_iter), value)

        with self.assertRaises(StopIteration):
            next(prefix_iter)

    def test_sample3(self):
        tree = TreeNode(
            12,
            TreeNode(7, TreeNode(2), TreeNode(10, TreeNode(9), None)),
            TreeNode(18, TreeNode(14), TreeNode(20)))

        postfix_iter = postfix_iterator(tree)
        expected = [2, 9, 10, 7, 14, 20, 18, 12]

        for value in expected:
            self.assertEqual(next(postfix_iter), value)

        with self.assertRaises(StopIteration):
            next(postfix_iter)


if __name__ == '__main__':
    unittest.main()
