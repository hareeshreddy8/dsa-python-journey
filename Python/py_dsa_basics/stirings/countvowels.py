string = str(input())
count = 0
for s in string :
    if s in 'aeiouAEIOU':
        count += 1
print(count)