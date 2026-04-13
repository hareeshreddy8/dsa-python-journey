s = str(input())
words = s.split()
if not words :
     print("input is empty")
freq ={}
#word count
for word in words :
#     if word in freq :
#         freq[word] += 1
#     else:
#         freq[word] = 1
      freq[word] = freq.get(word,0) + 1

print("frequency of elements :",freq)
#frequent word
print("most frequent element:",max(freq,key=freq.get))
#uniqueword
print("unique words :")
count = 0
for key in freq:
    if freq[key] == 1 :
        count += 1
        print(key)
print("total words :",len(words))
print("total unique elements :", count)
