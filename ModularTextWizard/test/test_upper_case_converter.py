import unittest
from src.upper_case_converter import *


class TestUpperCaseConverter(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_upper_case_converter_subtest(self):
        input_list = [("abc", "ABC"), ("ABC", "ABC"), ("aBc", "ABC"), ("a1Z", "A1Z"), ("", "")]

        for text, result in input_list:
            with self.subTest(msg="convert into upper case", text=text):
                self.assertEqual(result, upper_case_converter(text))


if __name__ == '__main__':
    unittest.main()
