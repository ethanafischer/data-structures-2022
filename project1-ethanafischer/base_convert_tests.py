import unittest

from base_convert import convert


class Tests(unittest.TestCase):
    def test_convert_base02_1(self):
        self.assertEqual(convert(0, 2), '0')

    def test_convert_base02_2(self):
        self.assertEqual(convert(45, 2), '101101')

    def test_convert_base04_1(self):
        self.assertEqual(convert(30, 4), '132')

    def test_convert_base04_2(self):
        self.assertEqual(convert(100, 4), '1210')

    def test_convert_base16_1(self):
        self.assertEqual(convert(107, 16), '6B')

    def test_convert_base16_2(self):
        self.assertEqual(convert(316, 16), '13C')


if __name__ == '__main__':
    unittest.main()
