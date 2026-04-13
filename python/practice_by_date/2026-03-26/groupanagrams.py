from collections import defaultdict
def group_anagram(s):
    anagram_map = defaultdict(list)

    for word in s:
        count = [0]*26
        for ch in word :
            count[ord(ch) - ord('a')] += 1

        key = tuple(count)

        anagram_map[key].append(word)
    return list(anagram_map.values())
