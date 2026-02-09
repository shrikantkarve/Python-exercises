"""Minimum Path Sum - dynamic programming exercise.

Function provided: `min_path_sum(grid)`
- returns the minimum path sum from top left to bottom right of a grid.
- You can only move either down or right at any point in time.

Complexity: O(m * n) time, O(m * n) space where m and n are dimensions of grid.
"""
from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    """Return the minimum path sum from top-left to bottom-right.

    Args:
        grid: 2D list of integers.

    Returns:
        Minimum path sum.

    Examples:
        >>> min_path_sum([[1,3,1],[1,5,1],[4,2,1]])
        7
        >>> min_path_sum([[1,2,3],[4,5,6]])
        12
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[0][0] = grid[0][0]

    # Initialize first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Initialize first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[m - 1][n - 1]
