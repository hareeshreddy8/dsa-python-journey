s = str(input())
words = list(map(str,s.split()))
result = words[::-1]
print("".join(result))
# words.reverse()
# print("".join(words))
