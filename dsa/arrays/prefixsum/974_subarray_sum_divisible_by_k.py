"""
Pattern : Prefix Sum
Approach : Hash Map
Time Complexity : O(n)
Space Complexity : O(n)
"""
from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        rem_map = {0:1}
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            rem= prefix_sum % k
            if rem in rem_map :
                count += rem_map[rem]
            rem_map[rem] = rem_map.get(rem,0) + 1
        return count 