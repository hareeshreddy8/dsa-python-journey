# Pattern : Sliding Window
# Approach : set usage
# time complexity : O(n)
# Space COmplexity : O(n)
from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        curr_sum , left = 0 , 0
        sub_array = set()
        max_sum = 0
        for right in range(len(nums)):
            while nums[right] in sub_array:
                sub_array.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            sub_array.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum,curr_sum)
        return max_sum