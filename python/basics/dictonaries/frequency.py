# from collections import Counter
s= str(input())
# freq = Counter(nums)
# print(dict(freq))
# freq = {}
# for num in nums:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# print(freq)
freq = {}
for ch in s :
    freq[ch] = freq.get(ch,0) + 1
print(freq)
max_freq = max(freq.values())
print(max(freq,key=freq.get))
index = {}
for i in range(len(s)) :
    if s[i] in index and i - index[s[i]] == 1:
        print(s[i])
    else:
        index[s[i]] = i 
print(len(freq) == len(s))
