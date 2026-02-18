import unittest
import sys
import os

# Add the parent directory to sys.path to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dynamic_programming.longest_palindromic_subseq import longest_palindromic_subseq


class TestLongestPalindromicSubseq(unittest.TestCase):

    def test_example_1(self):
        """'bbbab' -> 4 ('bbbb')"""
        self.assertEqual(longest_palindromic_subseq("bbbab"), 4)

    def test_example_2(self):
        """'cbbd' -> 2 ('bb')"""
        self.assertEqual(longest_palindromic_subseq("cbbd"), 2)

    def test_single_char(self):
        """Single character is itself a palindrome"""
        self.assertEqual(longest_palindromic_subseq("a"), 1)

    def test_already_palindrome(self):
        """'abcba' is already a palindrome -> 5"""
        self.assertEqual(longest_palindromic_subseq("abcba"), 5)

    def test_full_palindrome_racecar(self):
        """'racecar' is a full palindrome -> 7"""
        self.assertEqual(longest_palindromic_subseq("racecar"), 7)

    def test_character(self):
        """'character' -> 5 ('carac')"""
        self.assertEqual(longest_palindromic_subseq("character"), 5)

    def test_empty_string(self):
        """Empty string -> 0"""
        self.assertEqual(longest_palindromic_subseq(""), 0)

    def test_no_repeats(self):
        """'abcdef' -> 1 (any single char)"""
        self.assertEqual(longest_palindromic_subseq("abcdef"), 1)

    def test_all_same(self):
        """'aaaa' -> 4 (entire string)"""
        self.assertEqual(longest_palindromic_subseq("aaaa"), 4)

    def test_two_chars_different(self):
        """'ab' -> 1"""
        self.assertEqual(longest_palindromic_subseq("ab"), 1)

    def test_two_chars_same(self):
        """'aa' -> 2"""
        self.assertEqual(longest_palindromic_subseq("aa"), 2)


if __name__ == '__main__':
    unittest.main()
