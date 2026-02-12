import unittest
import sys
import os

# Add the parent directory to sys.path to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dynamic_programming.word_break import word_break

class TestWordBreak(unittest.TestCase):
    
    def test_simple_segmentation(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(word_break(s, wordDict))

    def test_reuse_words(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(word_break(s, wordDict))

    def test_impossible_segmentation(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(word_break(s, wordDict))

    def test_empty_string(self):
        # Empty string is technically valid if we consider 0 words, or handled by logic
        # Typically constraints say 1 <= s.length, but our logic handles it as True (base case)
        # Depending on problem constraints, might be different. 
        # For this implementation dp[0]=True so word_break("", []) -> True?
        # Actually loop range(1, 0 + 1) -> range(1, 1) doesn't run. returns dp[0]=True.
        # Let's assume standard behavior for empty string is True (0 words).
        self.assertTrue(word_break("", ["a"]))

    def test_single_char_match(self):
        s = "a"
        wordDict = ["a"]
        self.assertTrue(word_break(s, wordDict))

    def test_single_char_no_match(self):
        s = "a"
        wordDict = ["b"]
        self.assertFalse(word_break(s, wordDict))

    def test_long_string_and_dict(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        # This case is tricky for recursion without memoization but DP handles it well
        self.assertFalse(word_break(s, wordDict))

if __name__ == '__main__':
    unittest.main()
