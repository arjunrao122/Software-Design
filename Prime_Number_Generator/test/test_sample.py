import unittest
from src.sample import *


class TestSample(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_sample(self):
        self.assertEqual(1, sample_function())


if __name__ == '__main__':
    unittest.main()
