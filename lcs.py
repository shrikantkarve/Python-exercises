"""
Longest Common Subsequence (LCS) Problem

Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

For example:
LCS of "ABCDGH" and "AEDFHR" is "ADH" of length 3.
LCS of "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.

This implementation uses dynamic programming to solve the problem efficiently.
Time Complexity: O(m*n) where m and n are lengths of the two sequences
Space Complexity: O(m*n) for the DP table
"""


def lcs_length(seq1, seq2):
    """
    Find the length of the longest common subsequence between two sequences.
    
    Args:
        seq1: First sequence (string or list)
        seq2: Second sequence (string or list)
    
    Returns:
        Integer representing the length of LCS
    """
    m, n = len(seq1), len(seq2)
    
    # Create a 2D DP table
    # dp[i][j] represents the length of LCS of seq1[0..i-1] and seq2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                # If characters match, add 1 to the diagonal value
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If characters don't match, take max of top or left cell
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def lcs_string(seq1, seq2):
    """
    Find the actual longest common subsequence between two sequences.
    
    Args:
        seq1: First sequence (string or list)
        seq2: Second sequence (string or list)
    
    Returns:
        The longest common subsequence as a string or list (same type as input)
    """
    m, n = len(seq1), len(seq2)
    
    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack to find the actual subsequence
    result = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            # If characters match, it's part of LCS
            result.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # Move up
            i -= 1
        else:
            # Move left
            j -= 1
    
    # Reverse the result as we built it backwards
    result.reverse()
    
    # Return same type as input
    if isinstance(seq1, str):
        return ''.join(result)
    else:
        return result


def lcs_all(seq1, seq2):
    """
    Find all longest common subsequences between two sequences.
    
    Args:
        seq1: First sequence (string or list)
        seq2: Second sequence (string or list)
    
    Returns:
        Set of all LCS (as strings or tuples depending on input type)
    """
    m, n = len(seq1), len(seq2)
    
    # Create a 2D DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack to find all subsequences
    def backtrack(i, j, current):
        if i == 0 or j == 0:
            result_str = ''.join(reversed(current)) if isinstance(seq1, str) else tuple(reversed(current))
            all_lcs.add(result_str)
            return
        
        if seq1[i - 1] == seq2[j - 1]:
            # If characters match, it must be part of LCS
            backtrack(i - 1, j - 1, current + [seq1[i - 1]])
        else:
            # Explore both directions if they have the same value
            if dp[i - 1][j] == dp[i][j]:
                backtrack(i - 1, j, current)
            if dp[i][j - 1] == dp[i][j]:
                backtrack(i, j - 1, current)
    
    all_lcs = set()
    backtrack(m, n, [])
    
    return all_lcs


def lcs_space_optimized(seq1, seq2):
    """
    Space-optimized version of LCS that only returns the length.
    Uses O(min(m,n)) space instead of O(m*n).
    
    Args:
        seq1: First sequence (string or list)
        seq2: Second sequence (string or list)
    
    Returns:
        Integer representing the length of LCS
    """
    # Make sure seq2 is the shorter sequence
    if len(seq1) < len(seq2):
        seq1, seq2 = seq2, seq1
    
    m, n = len(seq1), len(seq2)
    
    # Use only two rows instead of full table
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        
        # Swap rows
        prev, curr = curr, prev
    
    return prev[n]


if __name__ == "__main__":
    # Example usage
    seq1 = "AGGTAB"
    seq2 = "GXTXAYB"
    
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}")
    print(f"LCS Length: {lcs_length(seq1, seq2)}")
    print(f"LCS String: {lcs_string(seq1, seq2)}")
    print(f"All LCS: {lcs_all(seq1, seq2)}")
    print()
    
    seq1 = "ABCDGH"
    seq2 = "AEDFHR"
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}")
    print(f"LCS Length: {lcs_length(seq1, seq2)}")
    print(f"LCS String: {lcs_string(seq1, seq2)}")
    print(f"All LCS: {lcs_all(seq1, seq2)}")
