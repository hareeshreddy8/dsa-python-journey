'''
Pattern : Prefix Sum
Approach : Hashmap
Time Complexity : O(n)
space complexity : O(n)
'''
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        runningsum_map = {0 : 1}
        for i in nums :
            running_sum += i
            if (running_sum - k)  in runningsum_map :
                count += runningsum_map[running_sum - k]
            runningsum_map[running_sum] = runningsum_map.get(running_sum,0)+1
        return count 