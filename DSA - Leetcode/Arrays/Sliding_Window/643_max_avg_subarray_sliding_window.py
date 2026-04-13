"""
Pattern : Sliding Window 

Approach : Usage of Prefix Sum

"""
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n <= 1 :
            return nums[0]
        k_sum = sum(nums[:k])
        max_sum = k_sum 
        for i in range(k , n):
            k_sum = k_sum - nums[i - k] + nums[i]
            max_sum = max(k_sum,max_sum)
        return max_sum / k
    