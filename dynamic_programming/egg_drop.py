"""
Egg Drop Problem (Hard - Optimization DP)

You are given k identical eggs and a building with n floors. You need to
determine the minimum number of trials (drops) needed in the worst case
to find the critical floor — the highest floor from which an egg can be
dropped without breaking.

Rules:
  - An egg that survives a drop can be reused.
  - A broken egg must be discarded.
  - The effect of a drop is the same for all eggs.
  - If an egg breaks when dropped from floor x, it would also break from
    any floor higher than x.
  - If an egg survives a drop from floor x, it would survive a drop from
    any floor lower than x.

Example 1:
Input: k = 1, n = 10
Output: 10
Explanation: With one egg, you must try each floor from 1 to 10 sequentially.

Example 2:
Input: k = 2, n = 100
Output: 14
"""


def egg_drop(k: int, n: int) -> int:
    """
    Finds the minimum number of trials needed in the worst case to
    determine the critical floor.

    Uses an optimized DP formulation where instead of asking "what is the
    min trials for n floors and k eggs?", we flip the question:

    dp[t][e] = maximum number of floors we can check with t trials and e eggs.

    Recurrence:
      dp[t][e] = dp[t-1][e-1] + dp[t-1][e] + 1
        - dp[t-1][e-1]: if egg breaks, floors checkable below
        - dp[t-1][e]:   if egg survives, floors checkable above
        - +1:           the current floor

    We find the smallest t such that dp[t][k] >= n.

    This runs in O(t * k) time where t = O(n) worst case but is typically
    much smaller (O(log n) when k is large).

    Args:
        k: Number of eggs.
        n: Number of floors.

    Returns:
        Minimum number of trials in the worst case.
    """
    if n == 0:
        return 0
    if k == 1:
        return n

    # dp[t][e] = max floors checkable with t trials and e eggs
    # We grow t until dp[t][k] >= n
    # Start with t = 1 and increase
    max_trials = n  # worst case is n trials with 1 egg

    dp = [[0] * (k + 1) for _ in range(max_trials + 1)]

    for t in range(1, max_trials + 1):
        for e in range(1, k + 1):
            dp[t][e] = dp[t - 1][e - 1] + dp[t - 1][e] + 1
        if dp[t][k] >= n:
            return t

    return max_trials


if __name__ == "__main__":
    test_cases = [
        (1, 10, 10),
        (2, 6, 3),
        (2, 10, 4),
        (2, 100, 14),
        (3, 14, 4),
        (1, 1, 1),
        (10, 1, 1),
    ]
    for k, n, expected in test_cases:
        result = egg_drop(k, n)
        status = "✓" if result == expected else "✗"
        print(f"{status} k={k}, n={n}, result={result}, expected={expected}")
