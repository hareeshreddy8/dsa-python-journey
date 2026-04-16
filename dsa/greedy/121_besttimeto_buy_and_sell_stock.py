# Pattern : Greedy Algorithm
# Approach : Keep tracking for best stock
# Time Complexity : O(n)
# Space Complexity : O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        for right in range(1,len(prices)) :
            if prices[right] < prices[left] :
                left = right
            else :
                profit = max(profit,prices[right]-prices[left])
        return profit