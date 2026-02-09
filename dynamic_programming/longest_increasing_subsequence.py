"""Longest Increasing Subsequence (LIS) - dynamic programming exercise.

Function provided: `longest_increasing_subsequence(arr)`
- returns `(length, subsequence_list)` where `length` is the LIS length
  and `subsequence_list` is one valid increasing subsequence.

Complexity: O(n^2) time, O(n) space.
"""
from typing import List, Tuple


def longest_increasing_subsequence(arr: List[int]) -> Tuple[int, List[int]]:
    """Return length and one LIS for the input list `arr`.

    Examples
    >>> longest_increasing_subsequence([10,9,2,5,3,7,101,18])
    (4, [2, 3, 7, 101])
    >>> longest_increasing_subsequence([])
    (0, [])
    """
    if not arr:
        return 0, []

    n = len(arr)
    dp = [1] * n
    prev = [-1] * n

    max_len = 1
    max_idx = 0

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i

    # Reconstruct subsequence
    seq: List[int] = []
    i = max_idx
    while i != -1:
        seq.append(arr[i])
        i = prev[i]
    seq.reverse()

    return max_len, seq
