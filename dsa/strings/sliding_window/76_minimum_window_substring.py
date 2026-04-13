"""

Pattern : Sliding  Window

Approach : Checking of Have and Need 

"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_map = Counter(t)
        left , right = 0 , 0 
        window_map = {}
        have , need = 0 , len(target_map)
        min_length = float("inf")
        res = [-1,-1]
        for right in range(len(s)) :
            window_map[s[right]] = window_map.get(s[right],0) + 1
            if window_map[s[right]] == target_map[s[right]] :
                have += 1
            
            while have == need :
                length = right - left + 1
                if length < min_length :
                    min_length = length
                    res = [left,right]
                window_map[s[left]] -= 1
                if window_map[s[left]] < target_map[s[left]] :
                    have -= 1
                left += 1
        
        l,r = res
        return s[l:r+1] if min_length != float("inf") else  ""