"""
Pattern : Sliding Window 
Key Idea : Set Usage

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        sub_string =set()
        max_length = 0
        left = 0
        for i in range(n) :
            while s[i] in sub_string :
                sub_string.remove(s[left])
                left += 1
            sub_string.add(s[i])
            max_length = max(max_length,len(sub_string))
        return max_length 