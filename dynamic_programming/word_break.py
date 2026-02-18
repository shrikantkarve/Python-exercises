"""
Word Break Problem

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

from typing import List

def word_break(s: str, wordDict: List[str]) -> bool:
    """
    Determines if the string s can be segmented into a space-separated sequence 
    of one or more dictionary words.
    
    Args:
        s: The input string to segment.
        wordDict: A list of words in the dictionary.
        
    Returns:
        True if s can be segmented, False otherwise.
    """
    # Convert wordDict to a set for O(1) lookups
    word_set = set(wordDict)
    n = len(s)
    
    # dp[i] is True if s[0...i-1] can be segmented into dictionary words
    dp = [False] * (n + 1)
    
    # Base case: empty string is always valid
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            # If substring s[0...j] is valid (dp[j] is True) 
            # AND substring s[j...i] is in the dictionary
            # then s[0...i] is also valid
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
                
    return dp[n]

if __name__ == "__main__":
    # Example usage
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(f"String: {s}, Dict: {wordDict}, Result: {word_break(s, wordDict)}")
    
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(f"String: {s}, Dict: {wordDict}, Result: {word_break(s, wordDict)}")
    
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(f"String: {s}, Dict: {wordDict}, Result: {word_break(s, wordDict)}")
