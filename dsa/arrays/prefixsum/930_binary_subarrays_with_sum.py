"""
Pattern : Prefix Sum
Approach : Hash Map
Time Complexity : O(n)
Space Complexity : O(n)
"""
from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        sum_map = {0:1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in sum_map :
                count += sum_map[prefix_sum - goal]
            sum_map[prefix_sum] = sum_map.get(prefix_sum,0) + 1
        return count