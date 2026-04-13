""" 
Pattern : Sliding Window

Approach : Using Frequency 

"""
from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_map = Counter(p)
        window_map = Counter()
        left , right = 0 , 0
        output = []

        for right in range(len(s)):
            window_map[s[right]] += 1
            
            if right - left + 1 > len(p):
                if s[left] in window_map:
                    window_map[s[left]] -= 1
                    if window_map[s[left]] == 0:
                        window_map.pop(s[left])
                left += 1
            
            if window_map == p_map :
                output.append(left)
        
        return output