nums = [1,2,4,6,8,9]
# res = []
# for num in nums:
#     if num % 2 == 0:
#         res.append(num * num)
res = list(map(lambda x : x*x,filter(lambda x : x % 2 == 0,nums)))
print(res)