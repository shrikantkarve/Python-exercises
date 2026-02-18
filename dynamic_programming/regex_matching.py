"""
Regular Expression Matching (Hard - 2D DP)

Given an input string s and a pattern p, implement regular expression matching
with support for '.' and '*' where:

  '.' Matches any single character.
  '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
"""


def is_match(s: str, p: str) -> bool:
    """
    Determines if the string s fully matches the pattern p.

    Uses bottom-up DP where dp[i][j] indicates whether s[:i] matches p[:j].

    State transitions:
      - If p[j-1] == '.' or p[j-1] == s[i-1]:
            dp[i][j] = dp[i-1][j-1]   (consume one char from both)
      - If p[j-1] == '*':
            dp[i][j] = dp[i][j-2]     (zero occurrences of preceding char)
            OR if p[j-2] matches s[i-1]:
            dp[i][j] |= dp[i-1][j]    (one or more occurrences)

    Args:
        s: The input string.
        p: The pattern string with '.' and '*' support.

    Returns:
        True if s fully matches p, False otherwise.
    """
    m, n = len(s), len(p)

    # dp[i][j] = True if s[:i] matches p[:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c* that can match empty string
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                # Current chars match (or pattern has '.'), carry forward
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # Zero occurrences of the preceding element
                dp[i][j] = dp[i][j - 2]

                # One or more occurrences: check if preceding pattern char
                # matches current string char
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[m][n]


if __name__ == "__main__":
    # Example usage
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
    ]
    for s, p, expected in test_cases:
        result = is_match(s, p)
        status = "✓" if result == expected else "✗"
        print(f"{status} s=\"{s}\", p=\"{p}\", result={result}, expected={expected}")
