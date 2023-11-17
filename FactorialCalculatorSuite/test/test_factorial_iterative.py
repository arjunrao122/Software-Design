import unittest
from src.factorial_imperative_iteration import factorial
from common import test_factorial


class TestImperativeIteration(test_factorial.TestFactorial):
    def get_factorial(self):
        return factorial


if __name__ == '__main__':
    unittest.main()
