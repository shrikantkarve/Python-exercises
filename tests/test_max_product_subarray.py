import unittest
import sys
import os

# Add the parent directory to sys.path to import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dynamic_programming.max_product_subarray import max_product

class TestMaxProductSubarray(unittest.TestCase):
    
    def test_standard_case(self):
        nums = [2, 3, -2, 4]
        self.assertEqual(max_product(nums), 6)

    def test_with_zero(self):
        nums = [-2, 0, -1]
        self.assertEqual(max_product(nums), 0)

    def test_all_negatives(self):
        nums = [-2, -3, -4]
        # [-2, -3] -> 6, [-3, -4] -> 12, [-2, -3, -4] -> -24
        # max is 12
        self.assertEqual(max_product(nums), 12)
        
    def test_negative_single(self):
        nums = [-2]
        self.assertEqual(max_product(nums), -2)
        
    def test_positive_single(self):
        nums = [5]
        self.assertEqual(max_product(nums), 5)
        
    def test_mixed_sequence(self):
        nums = [-2, 3, -4]
        # -2*3 = -6
        # 3*-4 = -12
        # -2*3*-4 = 24
        self.assertEqual(max_product(nums), 24)
        
    def test_zeros_in_middle(self):
        nums = [0, 2]
        self.assertEqual(max_product(nums), 2)
        
    def test_zeros_in_middle_2(self):
        nums = [2, 0, 3]
        self.assertEqual(max_product(nums), 3)

    def test_long_sequence(self):
        nums = [1, 2, 3, 4, 5, 0, 6, 7, 8]
        # 120 vs 336
        self.assertEqual(max_product(nums), 336)

if __name__ == '__main__':
    unittest.main()
