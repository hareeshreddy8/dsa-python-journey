def noduplicates(s):
    freq  = {}
    for i in range(len(s)):
        if s[i] not in freq :
            freq[s[i]] = i
    result = ""
    for ch in freq:
        result += ch
    return result
#using set
def no_duplicates(s):
    seen = set()
    result = ""
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch
    return result 
