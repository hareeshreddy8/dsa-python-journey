"""
Pattern : Prefix Sum
Approach : Hash Map and Modulo Operator
Time Complexity : O(n)
Space Complexity : O(n)
"""
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_map = {0:-1}
        prefix_sum = 0
        if k == 0 :
            return True
        for index,value in enumerate(nums) :
            prefix_sum += value
            rem = prefix_sum % k
            if rem in rem_map :
                if index - rem_map[rem] >= 2:
                    return True 
            else :
                rem_map[rem] = index
        return False