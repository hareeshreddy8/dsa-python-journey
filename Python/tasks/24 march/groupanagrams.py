from collections import defaultdict
def group_anagram(s):
    anagram_map = defaultdict(list)
    for word in s :
        key = "".join(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

