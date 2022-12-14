import unittest
from src.get_user_input import *


class TestUserInput(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_get_user_input(self):
        input_list = [(1, 1), (2, 2), (3, 3), (10, 10), (100, 100)]

        for number, result in input_list:
            with self.subTest(msg="get user input", text=number):
                self.assertEqual(result, get_user_input(number))


if __name__ == '__main__':
    unittest.main()

