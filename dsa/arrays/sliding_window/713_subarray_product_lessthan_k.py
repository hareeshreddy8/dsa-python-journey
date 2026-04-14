# Pattern : Sliding Window 
# Approach : Shrink window when product not less than Key
# Time Complexity : O(n)
# Space Complexity : O(1)




from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        product = 1
        count = 0
        left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += (right - left + 1)
        return count