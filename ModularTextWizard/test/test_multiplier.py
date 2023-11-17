import unittest
from src.multiplier import *


class TestMultiplier(unittest.TestCase):

    def test_multiplier_subtest(self):
        input_list = [("abc", "aabbcc"), ("ABC", "AABBCC"), ("aBc", "aaBBcc"), ("a1Z", "aa11ZZ"), ("", "")]

        for text, result in input_list:
            with self.subTest(msg="multiply the text by 2", text=text):
                self.assertEqual(result, multiplier(text))


if __name__ == '__main__':
    unittest.main()
