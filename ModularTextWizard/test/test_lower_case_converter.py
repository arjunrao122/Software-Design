import unittest
from src.lower_case_converter import *


class TestLowerCaseConverter(unittest.TestCase):

    def test_lower_case_converter_subtest(self):
        input_list = [("abc", "abc"), ("ABC", "abc"), ("aBc", "abc"), ("a1Z", "a1z"), ("", "")]

        for text, result in input_list:
            with self.subTest(msg="convert into upper case", text=text):
                self.assertEqual(result, lower_case_converter(text))


if __name__ == '__main__':
    unittest.main()
