from collections import defaultdict
from typing import List
def GroupByLength(words : list[str]):
    group = defaultdict(list)
    for word in words :
        key = len(word) 
        group[key].append(word)

    return group

words = ["hi", "hello", "hey", "world", "a"]
print(GroupByLength(words))
def GroupByFirstLetter(words : List[str]):
    group = {}
    for word in words :
        key = word[0]
        group.setdefault(word[0],[]).append(word)
    return group
print(GroupByFirstLetter(words))
        