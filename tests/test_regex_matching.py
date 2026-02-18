import unittest
import sys
import os

# Add the parent directory to sys.path to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dynamic_programming.regex_matching import is_match


class TestRegexMatching(unittest.TestCase):

    def test_no_match_short_pattern(self):
        """Pattern 'a' doesn't match 'aa'"""
        self.assertFalse(is_match("aa", "a"))

    def test_star_matches_multiple(self):
        """'a*' matches 'aa' (two a's)"""
        self.assertTrue(is_match("aa", "a*"))

    def test_dot_star_matches_anything(self):
        """'.*' matches any string"""
        self.assertTrue(is_match("ab", ".*"))

    def test_star_zero_occurrences(self):
        """'c*a*b' matches 'aab' - c* matches zero c's"""
        self.assertTrue(is_match("aab", "c*a*b"))

    def test_mississippi(self):
        """Classic tricky false case"""
        self.assertFalse(is_match("mississippi", "mis*is*p*."))

    def test_empty_string_star_pattern(self):
        """'a*' can match empty string (zero occurrences)"""
        self.assertTrue(is_match("", "a*"))

    def test_star_zero_at_end(self):
        """'ab*' matches 'a' - b* matches zero b's"""
        self.assertTrue(is_match("a", "ab*"))

    def test_star_overlap(self):
        """'a*a' matches 'aaa' - a* matches two a's, then literal a"""
        self.assertTrue(is_match("aaa", "a*a"))

    def test_exact_match(self):
        """Exact character-by-character match"""
        self.assertTrue(is_match("abc", "abc"))

    def test_dot_single_char(self):
        """'a.c' matches 'abc' - dot matches b"""
        self.assertTrue(is_match("abc", "a.c"))

    def test_empty_string_empty_pattern(self):
        """Both empty should match"""
        self.assertTrue(is_match("", ""))

    def test_empty_string_nonempty_pattern(self):
        """Non-star pattern can't match empty string"""
        self.assertFalse(is_match("", "a"))

    def test_nonempty_string_empty_pattern(self):
        """Empty pattern can't match non-empty string"""
        self.assertFalse(is_match("a", ""))

    def test_multiple_stars(self):
        """'a*b*c*' matches empty string"""
        self.assertTrue(is_match("", "a*b*c*"))

    def test_complex_pattern(self):
        """'a.*b' matches 'axxxxb'"""
        self.assertTrue(is_match("axxxxb", "a.*b"))

    def test_dot_star_dot_star(self):
        """'.*.*' matches 'ab'"""
        self.assertTrue(is_match("ab", ".*.*"))


if __name__ == '__main__':
    unittest.main()
