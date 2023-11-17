import unittest
from src.factorial_functional_iterator import factorial
from common import test_factorial


class TestFunctionalIteration(test_factorial.TestFactorial):
    def get_factorial(self):
        return factorial


if __name__ == '__main__':
    unittest.main()
