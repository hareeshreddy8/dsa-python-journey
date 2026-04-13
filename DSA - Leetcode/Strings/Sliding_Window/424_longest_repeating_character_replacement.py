"""
Pattern : Sliding Window

Approach : Using max_frequency

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left , right = 0 , 0
        max_length = 0
        max_freq = 0
        for right in range(len(s)):
            freq[s[right]] =freq.get(s[right],0) + 1
            max_freq = max(max_freq,freq[s[right]])
            if (right - left + 1) - max_freq > k :
                freq[s[left]] -= 1
                left += 1 
            max_length = max((right - left + 1) , max_length)
        return max_length