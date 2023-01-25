import unittest

from exp_eval import postfix_eval, infix_to_postfix


class Tests(unittest.TestCase):
    def test_infix_to_postfix_01(self):
        self.assertAlmostEqual(infix_to_postfix('1 + 2'), '1 2 +')

    def test_infix_to_postfix_02(self):
        infix = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"
        postfix = "3 4 2 * 1 5 - 2 3 ^ ^ / +"
        self.assertEqual(infix_to_postfix(infix), postfix)

    def test_infix_to_postfix_03(self):
        infix = "7 - 6 + ( 5 // 23 * 2 / 1 ) ^ 2"
        postfix = "7 6 - 5 23 // 2 * 1 / 2 ^ +"
        self.assertEqual(infix_to_postfix(infix), postfix)

    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval('1 2 +'), 3.0)

    def test_postfix_eval_02(self):
        postfix = "3 4 + 7 *"
        self.assertAlmostEqual(postfix_eval(postfix), 49)

    def test_postfix_eval_03(self):
        str_invalid_token = "2 a +"
        with self.assertRaises(ValueError):
            postfix_eval(str_invalid_token)

    def test_postfix_eval_04(self):
        str_empty = ""
        with self.assertRaises(ValueError):
            postfix_eval(str_empty)

    def test_postfix_eval_05(self):
        str_0_err = "2 0 /"
        with self.assertRaises(ZeroDivisionError):
            postfix_eval(str_0_err)

    def test_postfix_eval_06(self):
        str_insufficient = "2 +"
        with self.assertRaises(ValueError):
            postfix_eval(str_insufficient)

    def test_postfix_eval_07(self):
        str_too_many = "2 3 4 +"
        with self.assertRaises(ValueError):
            postfix_eval(str_too_many)

    def test_postfix_eval_08(self):
        str_0_err = "2 0 //"
        with self.assertRaises(ZeroDivisionError):
            postfix_eval(str_0_err)

    def test_postfix_eval_09(self):
        postfix = "3 2 ^ 8 -"
        self.assertAlmostEqual(postfix_eval(postfix), 1)


if __name__ == '__main__':
    unittest.main()
