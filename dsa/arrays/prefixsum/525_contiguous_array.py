"""
Pattern : Prefix Sum
Approach : Hash Map and Modulo Operator
Time Complexity : O(n)
Space Complexity : O(n)
"""
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        hashmap = {0 : -1}
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in hashmap:
                length = i - hashmap[prefix_sum]
                max_count = max(max_count,length)

            else :
                hashmap[prefix_sum] = i
        return max_count