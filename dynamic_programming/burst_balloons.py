"""
Burst Balloons (Hard - Interval DP)

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted
with a number on it represented by an array nums. You are asked to burst all
the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1]
coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if
there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
Input: nums = [3, 1, 5, 8]
Output: 167
Explanation:
  nums = [3, 1, 5, 8] --> [3, 5, 8] --> [3, 8] --> [8] --> []
  coins =  3*1*5      +   3*5*8    +  1*3*8   + 1*8*1 = 167

Example 2:
Input: nums = [1, 5]
Output: 10
"""


from typing import List

def max_coins(nums: List[int]) -> int:
    """
    Finds the maximum coins obtainable by bursting all balloons.

    Uses interval DP where dp[left][right] represents the maximum coins
    obtainable by bursting all balloons in the open interval (left, right).

    The key insight is to think about which balloon to burst LAST in each
    interval, rather than which to burst first. If balloon k is the last
    one burst in interval (left, right), the coins gained from that burst
    are nums[left] * nums[k] * nums[right], because all other balloons
    in the interval are already gone.

    Args:
        nums: List of integers representing balloon values.

    Returns:
        The maximum coins collectible.
    """
    if not nums:
        return 0

    # Pad with sentinel 1s on both ends
    balloons = [1] + nums + [1]
    n = len(balloons)

    # dp[left][right] = max coins from bursting all balloons
    # strictly between indices left and right
    dp = [[0] * n for _ in range(n)]

    # Iterate over increasing interval lengths
    # length is the number of elements strictly between left and right
    for length in range(1, n - 1):
        for left in range(0, n - 1 - length):
            right = left + length + 1
            for k in range(left + 1, right):
                # k is the last balloon burst in interval (left, right)
                coins = (
                    balloons[left] * balloons[k] * balloons[right]
                    + dp[left][k]
                    + dp[k][right]
                )
                dp[left][right] = max(dp[left][right], coins)

    return dp[0][n - 1]


if __name__ == "__main__":
    # Example usage
    nums = [3, 1, 5, 8]
    print(f"Nums: {nums}, Max Coins: {max_coins(nums)}")

    nums = [1, 5]
    print(f"Nums: {nums}, Max Coins: {max_coins(nums)}")
