import unittest
from src.k_blocker import k_blocker


class TestkBlocker(unittest.TestCase):

    def test_k_blocker_subtest(self):
        input_list = [("abck", "abc"), ("ABCK", "ABCK"), ("kakBkc", "aBc"), ("kk", ""), ("", "")]

        for text, result in input_list:
            with self.subTest(msg="remove k from the text", text=text):
                self.assertEqual(result, k_blocker(text))


if __name__ == '__main__':
    unittest.main()
