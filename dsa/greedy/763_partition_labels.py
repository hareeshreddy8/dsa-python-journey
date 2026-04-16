# Pattern : Greedy Algorithm
# Approach : We keep track current max end element and return length of current partition 
# Time Complexity : O(n)
# Space Complexity : O(1) 

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        result =[]

        for i,ch in enumerate(s):#gives (index,value) pairs
            last[ch] = i

        start = 0
        end = 0
        for i,ch in enumerate(s):
            end = max(end,last[ch])

            if i == end:
                result.append(end - start + 1)

                start = i + 1

        return result