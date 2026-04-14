# Pattern : Two Pointers
# Approach : Using absolute and comparing
# Time complexity : O(n)
# Space complexity : O(1)

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        i , j = 0 , n - 1
        pos = n - 1
        while i <= j :
            if abs(nums[i]) > abs(nums[j]) :
                res[pos] = nums[i] * nums[i]
                i += 1
            else :
                res[pos] = nums[j] * nums[j] 
                j -= 1
            pos -= 1
        return res