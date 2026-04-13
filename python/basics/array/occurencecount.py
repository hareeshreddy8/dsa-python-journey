list = [1,2,3,1,4,2,1,2,5]
#brute force
count = {}
# for i in range(len(list)) :
#     freq = 0
#     for j in range(i,len(list)) :
#         if list[i] == list[j] :
#             freq += 1
#         count[list[i]] = freq
# print(count)
        #optimised 
for num in list :
    count[num] = count.get(num,0) + 1
print(count)