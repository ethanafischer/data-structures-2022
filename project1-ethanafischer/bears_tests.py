import unittest

from bears import bears


class Tests(unittest.TestCase):
    def test_bears_0(self):
        self.assertFalse(bears(0))

    def test_bears_40(self):
        self.assertFalse(bears(40))

    def test_bears_42(self):
        self.assertTrue(bears(42))

    def test_bears_53(self):
        self.assertFalse(bears(53))

    def test_bears_100(self):
        self.assertFalse(bears(100))

    def test_bears_101(self):
        self.assertFalse(bears(101))

    def test_bears_250(self):
        self.assertTrue(bears(250))


if __name__ == '__main__':
    unittest.main()
