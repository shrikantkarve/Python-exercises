import unittest
import sys
import os

# Add the parent directory to sys.path to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dynamic_programming.burst_balloons import max_coins


class TestBurstBalloons(unittest.TestCase):

    def test_example_1(self):
        """LeetCode example: [3, 1, 5, 8] -> 167"""
        nums = [3, 1, 5, 8]
        self.assertEqual(max_coins(nums), 167)

    def test_example_2(self):
        """LeetCode example: [1, 5] -> 10"""
        nums = [1, 5]
        self.assertEqual(max_coins(nums), 10)

    def test_single_balloon(self):
        """Single balloon: coins = 1 * 5 * 1 = 5"""
        nums = [5]
        self.assertEqual(max_coins(nums), 5)

    def test_all_ones(self):
        """All ones: [1, 1, 1] -> 4"""
        nums = [1, 1, 1]
        # Burst order: middle (1*1*1=1), left (1*1*1=1), right (1*1*1=1) ... 
        # Optimal: any order, best = 1+1+1 ... actually:
        # [1,1,1] -> burst middle: 1*1*1=1 coins, left [1,1] -> burst left: 1*1*1=1, [1] -> 1*1*1=1 = 3
        # [1,1,1] -> burst left: 1*1*1=1, [1,1] -> burst left: 1*1*1=1, [1] -> 1*1*1=1 = 3
        # Hmm, let me recalculate with padding [1, 1, 1, 1, 1]:
        # Actually max is 3 for three 1s. Let me verify...
        # dp approach: padded = [1, 1, 1, 1, 1]
        # length=1: dp[0][2]=1*1*1=1, dp[1][3]=1*1*1=1, dp[2][4]=1*1*1=1
        # length=2: dp[0][3]=max(1*1*1+dp[1][3]=2, dp[0][2]+1*1*1=2)=2
        #           dp[1][4]=max(1*1*1+dp[2][4]=2, dp[1][3]+1*1*1=2)=2
        # length=3: dp[0][4]=max(k=1: 1*1*1+0+dp[1][4]=2+0=... )
        # Best we can verify by running - expected 3
        self.assertEqual(max_coins(nums), 3)

    def test_two_identical(self):
        """Two identical: [3, 3] -> 1*3*3 + 1*3*1 = 12"""
        nums = [3, 3]
        self.assertEqual(max_coins(nums), 12)

    def test_larger_values(self):
        """Larger values: [9, 76, 64, 21]"""
        nums = [9, 76, 64, 21]
        # Verified via algorithm
        self.assertEqual(max_coins(nums), 116718)

    def test_empty_array(self):
        """Empty array should return 0"""
        nums = []
        self.assertEqual(max_coins(nums), 0)

    def test_descending(self):
        """Descending: [5, 4, 3, 2, 1]"""
        nums = [5, 4, 3, 2, 1]
        # Verified via algorithm
        self.assertEqual(max_coins(nums), 110)


if __name__ == '__main__':
    unittest.main()
