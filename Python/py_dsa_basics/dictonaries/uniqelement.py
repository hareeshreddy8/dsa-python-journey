s = str(input())
elements = {}
for i in range(len(s)) :
    elements[s[i]] = i
print(dict(elements))