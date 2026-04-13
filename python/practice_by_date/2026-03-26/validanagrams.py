def valid_anagram(str1,str2) :
    if len(str1) != len(str2):
        return False 
    
    freq_str1 = {}
    
    freq_str2 = {}
    
    for ch in str1 :
        freq_str1[ch] = freq_str1.get(ch,0) + 1
    
    for ch in str2:
        freq_str2[ch] = freq_str2.get(ch,0) + 1
    
    for ch in freq_str1 :
        if freq_str1[ch] != freq_str2.get(ch,0) :
            return False
    
    # return freq_str1 == freq_str2
    
    return True 
def isvalid_anagram(s1,s2) :
    if len(s1) != len(s2):
        return False 
    
    freq_s1 = {}

    for ch in s1 :
        freq_s1[ch] = freq_s1.get(ch,0) + 1
    
    for ch in s2 :
        if ch not in freq_s1:
            return False
        freq_s1[ch] -= 1
        if freq_s1[ch] < 0:
            return False
    
    return True
