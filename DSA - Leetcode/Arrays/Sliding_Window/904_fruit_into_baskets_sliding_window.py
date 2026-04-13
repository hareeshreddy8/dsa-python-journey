"""
Pattern : Slding Window

Approach : Using Dictionary

"""
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_fruitCount = 0
        basket_map = {}
        
        for right in range(len(fruits)):
            basket_map[fruits[right]] = basket_map.get(fruits[right],0) + 1
            
            while len(basket_map) > 2:
                basket_map[fruits[left]] -= 1
                if basket_map[fruits[left]] == 0:
                    del basket_map[fruits[left]]
                left += 1
            max_fruitCount = max(max_fruitCount,right - left + 1)
        
        return max_fruitCount