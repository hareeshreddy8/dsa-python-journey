"""
Pattern : Sliding Window

Approach : Usage of Prefix Sum 

"""
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = len(nums) + 1  # Use a large integer instead of float('inf')
        prefix_sum = 0

        for right in range(len(nums)):
            prefix_sum += nums[right]

            while prefix_sum >= target :
                prefix_sum -= nums[left]
                min_length = min((right - left + 1) , min_length)
                left += 1
            
        if min_length == len(nums) + 1:
            return 0
        
        return min_length