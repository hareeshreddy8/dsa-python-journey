'''
Pattern : Sliding Window

Approach : Using atmost 

'''
from typing import List
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(nums,k):
            window_map = {}
            left = 0
            count = 0

            for right in range(len(nums)):
                window_map[nums[right]] = window_map.get(nums[right],0) + 1
                while len(window_map) > k:
                    window_map[nums[left]] -= 1
                    if window_map[nums[left]] == 0:
                        del window_map[nums[left]] 

                    left += 1
                count += (right - left + 1)

            return count
        return atMost(nums,k) - atMost(nums,k-1)