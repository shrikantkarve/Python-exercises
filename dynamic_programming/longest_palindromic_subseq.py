"""
Longest Palindromic Subsequence (Medium-Hard - 2D DP)

Given a string s, find the length of the longest palindromic subsequence in s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining
elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""


def longest_palindromic_subseq(s: str) -> int:
    """
    Finds the length of the longest palindromic subsequence in s.

    Uses 2D DP where dp[i][j] represents the length of the longest
    palindromic subsequence in s[i..j] (inclusive).

    Recurrence:
      - If s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
      - Else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    Base case: dp[i][i] = 1 (every single character is a palindrome).

    We iterate over increasing substring lengths, filling the table
    bottom-up from shorter to longer substrings.

    Args:
        s: The input string.

    Returns:
        Length of the longest palindromic subsequence.
    """
    n = len(s)
    if n == 0:
        return 0

    # dp[i][j] = LPS length in s[i..j]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters
    for i in range(n):
        dp[i][i] = 1

    # Fill for increasing substring lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


if __name__ == "__main__":
    test_cases = [
        ("bbbab", 4),
        ("cbbd", 2),
        ("abcba", 5),
        ("racecar", 7),
        ("character", 5),
    ]
    for s, expected in test_cases:
        result = longest_palindromic_subseq(s)
        status = "✓" if result == expected else "✗"
        print(f'{status} s="{s}", result={result}, expected={expected}')
