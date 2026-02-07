"""
Unit tests for Longest Common Subsequence implementation
"""

import unittest
from lcs import lcs_length, lcs_string, lcs_all, lcs_space_optimized


class TestLCSLength(unittest.TestCase):
    """Test cases for lcs_length function"""
    
    def test_basic_example(self):
        """Test basic LCS example"""
        self.assertEqual(lcs_length("AGGTAB", "GXTXAYB"), 4)
    
    def test_another_example(self):
        """Test another basic example"""
        self.assertEqual(lcs_length("ABCDGH", "AEDFHR"), 3)
    
    def test_identical_strings(self):
        """Test with identical strings"""
        self.assertEqual(lcs_length("HELLO", "HELLO"), 5)
    
    def test_no_common_subsequence(self):
        """Test with no common characters"""
        self.assertEqual(lcs_length("ABC", "DEF"), 0)
    
    def test_empty_strings(self):
        """Test with empty strings"""
        self.assertEqual(lcs_length("", "ABC"), 0)
        self.assertEqual(lcs_length("ABC", ""), 0)
        self.assertEqual(lcs_length("", ""), 0)
    
    def test_one_character_match(self):
        """Test with single character match"""
        self.assertEqual(lcs_length("A", "A"), 1)
        self.assertEqual(lcs_length("ABC", "XAY"), 1)
    
    def test_reversed_strings(self):
        """Test with reversed strings"""
        self.assertEqual(lcs_length("ABC", "CBA"), 1)
    
    def test_substring(self):
        """Test when one string is substring of another"""
        self.assertEqual(lcs_length("ABCDEF", "ACE"), 3)
    
    def test_repeated_characters(self):
        """Test with repeated characters"""
        self.assertEqual(lcs_length("AAAA", "AA"), 2)
    
    def test_long_sequences(self):
        """Test with longer sequences"""
        seq1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        seq2 = "ACEGIKMOQSUWY"
        self.assertEqual(lcs_length(seq1, seq2), 13)


class TestLCSString(unittest.TestCase):
    """Test cases for lcs_string function"""
    
    def test_basic_example(self):
        """Test basic LCS string recovery"""
        result = lcs_string("AGGTAB", "GXTXAYB")
        self.assertEqual(len(result), 4)
        self.assertIn(result, ["GTAB"])
    
    def test_another_example(self):
        """Test another example"""
        result = lcs_string("ABCDGH", "AEDFHR")
        self.assertEqual(len(result), 3)
        self.assertIn(result, ["ADH"])
    
    def test_identical_strings(self):
        """Test with identical strings"""
        self.assertEqual(lcs_string("HELLO", "HELLO"), "HELLO")
    
    def test_no_common_subsequence(self):
        """Test with no common characters"""
        self.assertEqual(lcs_string("ABC", "DEF"), "")
    
    def test_empty_strings(self):
        """Test with empty strings"""
        self.assertEqual(lcs_string("", "ABC"), "")
        self.assertEqual(lcs_string("ABC", ""), "")
    
    def test_single_character(self):
        """Test with single character"""
        self.assertEqual(lcs_string("A", "A"), "A")
    
    def test_with_lists(self):
        """Test with list inputs"""
        result = lcs_string([1, 2, 3, 4], [2, 4, 3])
        self.assertEqual(result, [2, 4])
    
    def test_result_is_subsequence(self):
        """Verify result is valid subsequence of both inputs"""
        seq1 = "ABCDEFGH"
        seq2 = "AEBDFH"
        result = lcs_string(seq1, seq2)
        
        # Check that result is a subsequence of seq1
        idx = 0
        for char in result:
            idx = seq1.find(char, idx) + 1
            self.assertGreater(idx, 0)
        
        # Check that result is a subsequence of seq2
        idx = 0
        for char in result:
            idx = seq2.find(char, idx) + 1
            self.assertGreater(idx, 0)


class TestLCSAll(unittest.TestCase):
    """Test cases for lcs_all function"""
    
    def test_single_lcs(self):
        """Test case with single LCS"""
        result = lcs_all("AGGTAB", "GXTXAYB")
        self.assertEqual(len(result), 1)
        self.assertIn("GTAB", result)
    
    def test_multiple_lcs(self):
        """Test case with multiple LCS"""
        result = lcs_all("ABCD", "ACBD")
        # Possible LCS: "ABD" and "ACD" both have length 3
        self.assertGreater(len(result), 0)
        for lcs in result:
            self.assertEqual(len(lcs), 3)
    
    def test_empty_result(self):
        """Test with no common subsequence"""
        result = lcs_all("ABC", "DEF")
        self.assertEqual(len(result), 1)
        self.assertIn("", result)
    
    def test_identical_strings(self):
        """Test with identical strings"""
        result = lcs_all("ABC", "ABC")
        self.assertEqual(len(result), 1)
        self.assertIn("ABC", result)


class TestLCSSpaceOptimized(unittest.TestCase):
    """Test cases for space-optimized LCS"""
    
    def test_matches_standard_implementation(self):
        """Verify space-optimized version produces same results"""
        test_cases = [
            ("AGGTAB", "GXTXAYB"),
            ("ABCDGH", "AEDFHR"),
            ("HELLO", "HELLO"),
            ("ABC", "DEF"),
            ("", "ABC"),
            ("ABCDEFGHIJKLMNOP", "ACEGIKMO"),
        ]
        
        for seq1, seq2 in test_cases:
            with self.subTest(seq1=seq1, seq2=seq2):
                standard = lcs_length(seq1, seq2)
                optimized = lcs_space_optimized(seq1, seq2)
                self.assertEqual(standard, optimized)
    
    def test_different_length_sequences(self):
        """Test with sequences of different lengths"""
        self.assertEqual(lcs_space_optimized("ABCDE", "AC"), 2)
        self.assertEqual(lcs_space_optimized("AC", "ABCDE"), 2)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios"""
    
    def test_very_long_sequences(self):
        """Test with very long sequences"""
        seq1 = "A" * 100 + "B" + "A" * 100
        seq2 = "A" * 150 + "B"
        result = lcs_length(seq1, seq2)
        self.assertEqual(result, 150)  # 150 A's (B is not aligned properly)
    
    def test_all_same_character(self):
        """Test with sequences of same character"""
        self.assertEqual(lcs_length("AAAA", "AAA"), 3)
        self.assertEqual(lcs_length("BBB", "BBBBB"), 3)
    
    def test_alternating_pattern(self):
        """Test with alternating patterns"""
        self.assertEqual(lcs_length("ABABAB", "BABABA"), 5)
    
    def test_numeric_sequences(self):
        """Test with numeric sequences as lists"""
        seq1 = [1, 2, 3, 4, 5]
        seq2 = [2, 4, 5, 6]
        self.assertEqual(lcs_length(seq1, seq2), 3)
        self.assertEqual(lcs_string(seq1, seq2), [2, 4, 5])


class TestConsistency(unittest.TestCase):
    """Test consistency between different implementations"""
    
    def test_length_matches_string_length(self):
        """Verify lcs_length and len(lcs_string) are consistent"""
        test_cases = [
            ("AGGTAB", "GXTXAYB"),
            ("ABCDGH", "AEDFHR"),
            ("HELLO", "WORLD"),
            ("ABCDEF", "FEDCBA"),
            ("", "ABC"),
            ("ABC", ""),
        ]
        
        for seq1, seq2 in test_cases:
            with self.subTest(seq1=seq1, seq2=seq2):
                length = lcs_length(seq1, seq2)
                string = lcs_string(seq1, seq2)
                self.assertEqual(length, len(string))
    
    def test_all_lcs_have_same_length(self):
        """Verify all LCS found have the same length"""
        test_cases = [
            ("ABCD", "ACBD"),
            ("ABC", "ABC"),
            ("XYZZYX", "XZYXZY"),
        ]
        
        for seq1, seq2 in test_cases:
            with self.subTest(seq1=seq1, seq2=seq2):
                all_lcs = lcs_all(seq1, seq2)
                expected_length = lcs_length(seq1, seq2)
                for lcs in all_lcs:
                    self.assertEqual(len(lcs), expected_length)


if __name__ == '__main__':
    unittest.main(verbosity=2)
