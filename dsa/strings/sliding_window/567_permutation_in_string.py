"""
Pattern : Sliding Window

Approach : maintain count

"""


from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        s2_map = {}
        left = 0
        if len(s1) > len(s2) :
            return False
        for i in range(len(s1)) :
            s2_map[s2[i]] = s2_map.get(s2[i],0) + 1
        if s1_map == s2_map :
                return True
        for right in range(len(s1),len(s2)) :
            
            s2_map[s2[left]] -= 1
            if s2_map[s2[left]] == 0:
                s2_map.pop(s2[left])
            left += 1
            s2_map[s2[right]] = s2_map.get(s2[right],0) + 1
            if s1_map == s2_map :
                return True
        return False