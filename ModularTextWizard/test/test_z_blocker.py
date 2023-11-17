import unittest
from src.z_blocker import z_blocker


class TestzBlocker(unittest.TestCase):

    def test_z_blocker_subtest(self):
        input_list = [("abcz", "abc"), ("ABCZ", "ABCZ"), ("zazBzc", "aBc"), ("zz", ""), ("", "")]

        for text, result in input_list:
            with self.subTest(msg="remove z from the text", text=text):
                self.assertEqual(result, z_blocker(text))


if __name__ == '__main__':
    unittest.main()
