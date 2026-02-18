"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters using sliding window.

    Time Complexity: O(n) - we iterate through the string once.
    Space Complexity: O(min(m, n)) - we store at most unique characters (m is alphabet size).

    Args:
        s: Input string

    Returns:
        Length of longest substring without repeating characters
    """
    char_map = {}  # Stores the last seen index of each character
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]

        # If char is already in the map and is inside the current window
        if char in char_map and char_map[char] >= left:
            # Move the left pointer to the right of the last occurrence
            left = char_map[char] + 1
        
        # Update/Add the character's index
        char_map[char] = right
        
        # Calculate current window length and update max
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", "", " "]
    for t in test_cases:
        print(f"'{t}': {length_of_longest_substring(t)}")
