import unittest
from src.z_caps_blocker import z_caps_blocker


class TestZCapsBlocker(unittest.TestCase):

    def test_z_caps_blocker_subtest(self):
        input_list = [("abcZ", "abc"), ("ABCz", "ABCz"), ("ZaZBZc", "aBc"), ("ZZ", ""), ("", "")]

        for text, result in input_list:
            with self.subTest(msg="remove Z from the text", text=text):
                self.assertEqual(result, z_caps_blocker(text))


if __name__ == '__main__':
    unittest.main()
