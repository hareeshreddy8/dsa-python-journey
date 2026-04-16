# Pattern : Greedy Algo
# Approach : Keepon iterating until we have a best one 
# Time Complexity : O(n)
# Space Complexity : O(1)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = nums[0]
        for i in range(len(nums)):
            if i > max_reach :
                return False

            else:
                max_reach = max(max_reach,i + nums[i])

        return True