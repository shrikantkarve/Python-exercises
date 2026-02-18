"""
Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

from typing import List

def max_product(nums: List[int]) -> int:
    """
    Finds the contiguous subarray within an array (containing at least one number) 
    which has the largest product.
    
    Args:
        nums: List of integers.
        
    Returns:
        The maximum product of a contiguous subarray.
    """
    if not nums:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]
        
        # Capture the potential max and min products ending at the current position
        # We need to consider three candidates for max and min:
        # 1. curr (starting a new subarray here)
        # 2. curr * max_so_far (extending the previous max subarray)
        # 3. curr * min_so_far (extending the previous min subarray - important if curr is negative)
        
        temp_max = max(curr, max(curr * max_so_far, curr * min_so_far))
        min_so_far = min(curr, min(curr * max_so_far, curr * min_so_far))
        
        max_so_far = temp_max
        
        result = max(max_so_far, result)

    return result

if __name__ == "__main__":
    # Example usage
    nums = [2, 3, -2, 4]
    print(f"Nums: {nums}, Max Product: {max_product(nums)}")
    
    nums = [-2, 0, -1]
    print(f"Nums: {nums}, Max Product: {max_product(nums)}")
