# Pattern : Sliding Window
# Approach : checking for sub array with atMost one "0"
# Time Cmplexity: O(n)
# Space Complexity : O(1)
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        count_zeros = 0
        longest = 0
        for right in range(len(nums)):
            if nums[right] == 0 :
                count_zeros += 1

            while count_zeros > 1 :
                if nums[left] == 0 :
                    count_zeros -= 1
                left += 1
            longest = max(longest,right - left)
        return longest
