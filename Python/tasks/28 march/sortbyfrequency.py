def sort_by_freq(s):
    result = ""
    freq ={}
    for ch in s :
        freq[ch] = freq.get(ch,0) + 1
    sorted_chars = sorted(freq,key = freq.get,reverse = True)
    for ch in sorted_chars:
        result += ch * freq[ch]
    return result
def using_join(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    return "".join(ch * freq[ch] for ch in sorted(freq,key = freq.get,reverse = True))