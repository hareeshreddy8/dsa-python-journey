from collections import Counter
from typing import List

def removeduplicates(nums:list):
    seen = set()
    unique_nums = []
    for num in nums:
        if num not in seen :
            seen.add(num)
            unique_nums.append(num)
    return unique_nums

nums = [1,2,2,3,1,4]
print(removeduplicates(nums))