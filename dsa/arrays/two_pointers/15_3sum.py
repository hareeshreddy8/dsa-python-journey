# Pattern : Two Pointers
# Approach : Two pointers
# Time Complexity : O(n)
# Space Complexity : O(1)

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j = 0 , len(height)-1 
        maxvol = 0
        while i < j : 
            h = min(height[i],height[j])
            maxvol = max(maxvol,h * (j-i))
            if height[i] < height[j] :
                i += 1
            else :
                j -= 1
        return maxvol