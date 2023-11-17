import unittest
from src.get_all_blocks import get_all_blocks
from src.upper_case_converter import upper_case_converter
from src.lower_case_converter import lower_case_converter


class TestgetAllBlocks(unittest.TestCase):

    def test_get_all_blocks_returns_non_empty_set(self):
        self.assertTrue(get_all_blocks())

    def test_get_all_blocks_includes_upper_case_convertor(self):
        self.assertTrue(upper_case_converter in get_all_blocks())

    def test_get_all_blocks_includes_multiplier(self):
        self.assertTrue(lower_case_converter in get_all_blocks())


if __name__ == '__main__':
    unittest.main()
