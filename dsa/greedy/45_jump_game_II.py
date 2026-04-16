# Pattern : Greedy Algorithm
# Approach : I kept track of landing when current range ends and go again until current range to land 
# Time Complexity : O(n)
# Space Complexity : O(1)


class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        jump_count = 0
        current_end = 0

        for i in range(len(nums)-1):
            farthest = max(farthest,nums[i] + i)

            if i == current_end:
                current_end = farthest
                jump_count += 1


        return jump_count