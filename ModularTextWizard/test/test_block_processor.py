import unittest
from src.block_processor import block_processor
from src.lower_case_converter import lower_case_converter
from src.upper_case_converter import upper_case_converter
from src.multiplier import multiplier


class TestBlockProcessor(unittest.TestCase):

    def test_block_processor_no_blocks(self):
        self.assertEqual('aBc', block_processor('aBc'))

    def test_block_processor_for_upper_case(self):
        self.assertEqual('ABC', block_processor('aBc', upper_case_converter))

    def test_block_processor_for_lower_case(self):
        self.assertEqual('abc', block_processor('aBc', lower_case_converter))

    def test_block_processor_for_upper_case_and_multiplier(self):
        self.assertEqual('AABBCC', block_processor('aBc', upper_case_converter, multiplier))

    def test_block_processor_for_upper_case_multiplier_and_lower_case(self):
        self.assertEqual('aabbcc', block_processor('aBc', upper_case_converter, multiplier, lower_case_converter))


if __name__ == '__main__':
    unittest.main()
