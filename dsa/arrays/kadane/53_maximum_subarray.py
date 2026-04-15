# Pattern : Kadane algorithm
# Approach : checking for max current sum everytime to handle negative numbers
# Time complexity : O(n)
# Space complexity : O(1)




class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i],current_sum + nums[i])
            max_sum = max(max_sum,current_sum)
        return max_sum