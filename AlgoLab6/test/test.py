import unittest

from src.rabin_karp import rabin_karp


class TestRabinKarp(unittest.TestCase):
    def test_rabin_karp(self):
        haystack_1 = "ababcababcabcabc"
        needle_1 = "abc"
        result_1 = rabin_karp(haystack_1, needle_1)
        self.assertEqual(result_1, [2, 7, 10, 13])

        haystack_2 = "abcdef"
        needle_2 = ""
        result_2 = rabin_karp(haystack_2, needle_2)
        self.assertEqual(result_2, [])

        haystack_3 = ""
        needle_3 = "abc"
        result_3 = rabin_karp(haystack_3, needle_3)
        self.assertEqual(result_3, [])

        haystack_4 = "abcdef"
        needle_4 = "xyz"
        result_4 = rabin_karp(haystack_4, needle_4)
        self.assertEqual(result_4, [])


if __name__ == '__main__':
    unittest.main()
