import unittest
from src.factorial_simple_recursion import factorial
from common import test_factorial


class TestSimpleRecursion(test_factorial.TestFactorial):
    def get_factorial(self):
        return factorial


if __name__ == '__main__':
    unittest.main()
