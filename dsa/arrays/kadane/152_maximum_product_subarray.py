# Pattern : Kadanes Algorithm
# Approach : Here egatives handling is very important so we also track min_product
# Time complexity : O(n)
# Space complexity : O(1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_curr = nums[0]
        min_curr = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
           num = nums[i]

           temp = max_curr

           max_curr = max(num,num * max_curr,num * min_curr)
           min_curr = min(num,num * temp,num * min_curr)

           result = max(result,max_curr)
        return result