# Pattern : Greedy Algorithm
# Approach : develop a mathematical formula based on structure,the no of operations depends upon max frequent task label 
# Time Complexity : O(n)
# Space Complexity : O(n)
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        f_max = max(freq.values())
        max_count = 0
        for key in freq.keys():
            if freq[key] == f_max :
                max_count += 1

        return max(len(tasks),((f_max - 1)*(n+1) + max_count))