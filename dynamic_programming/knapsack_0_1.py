"""0/1 Knapsack Problem - dynamic programming exercise.

Function provided: `knapsack_0_1(weights, values, capacity)`
- returns the maximum value that can be put in a knapsack of capacity `capacity`.

Complexity: O(N * W) time, O(N * W) space where N is the number of items and W is the capacity.
"""
from typing import List


def knapsack_0_1(weights: List[int], values: List[int], capacity: int) -> int:
    """Return the maximum value that can be put in a knapsack of capacity `capacity`.

    Args:
        weights: List of weights of the items.
        values: List of values of the items.
        capacity: Maximum weight capacity of the knapsack.

    Returns:
        Maximum value that can be obtained.

    Examples:
        >>> knapsack_0_1([10, 20, 30], [60, 100, 120], 50)
        220
        >>> knapsack_0_1([1, 2, 3], [10, 15, 40], 6)
        65
    """
    n = len(values)
    if n == 0 or capacity == 0:
        return 0

    # dp[i][w] will store the maximum value that can be attained with
    # maximum capacity w using only the first i items
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # max(value of including the item, value of excluding the item)
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                # If weight of the nth item is more than Knapsack capacity W,
                # then this item cannot be included in the optimal solution
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
