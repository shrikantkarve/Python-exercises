"""Minimum Coins (Coin Change) - dynamic programming exercise.

Function provided: `min_coins(coins, amount)`
- returns minimum number of coins needed to make `amount` using `coins` denominations
- returns `-1` when amount cannot be formed.

Complexity: O(amount * len(coins)) time, O(amount) space.
"""
from typing import List


def min_coins(coins: List[int], amount: int) -> int:
    """Return minimum number of coins to make `amount` using `coins`.

    Examples
    >>> min_coins([1,2,5], 11)
    3
    >>> min_coins([2], 3)
    -1
    >>> min_coins([1], 0)
    0
    """
    if amount < 0:
        return -1
    if amount == 0:
        return 0

    INF = amount + 1
    dp = [0] + [INF] * amount

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)

    return dp[amount] if dp[amount] != INF else -1
