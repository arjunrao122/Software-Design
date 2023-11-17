import unittest
from src.prime_number_generator import *


class TestComputePrimeNumbers(unittest.TestCase):
    def test_prime_number_generation(self):
        input_list = [(1, [2]), (2, [2, 3]), (3, [2, 3, 5]), (10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])]

        for number, result in input_list:
            with self.subTest(msg="generate prime numbers", text=number):
                self.assertEqual(result, generate_prime_numbers(number))


if __name__ == '__main__':
    unittest.main()
