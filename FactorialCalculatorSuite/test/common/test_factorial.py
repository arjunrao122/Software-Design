import unittest


class TestFactorial(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_factorial_for_negative_number(self):
        self.assertRaisesRegex(ValueError, 'Number should be Zero or greater', self.get_factorial(), -1)

    def test_factorial_for_whole_numbers(self):
        input_list = [(0, 1), (1, 1), (2, 2), (5, 120), (10, 3628800), (20, 2432902008176640000),
                      (50, 30414093201713378043612608166064768844377641568960512000000000000)]

        for number, result in input_list:
            with self.subTest(msg="Factorial of the number", number=number):
                self.assertEqual(result, self.get_factorial()(number))
