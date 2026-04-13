# prefix_sum = 0
# prefix_map = {0 : [-1]}
# result =[]
# for i in range(len(nums)):
#     prefix_sum += nums[i]
#     if prefix_sum - k in prefix_map :
#         for start in prefix_map[prefix_sum- k] :
#             result.append(nums[start + 1 : i + 1])
#     if prefix_sum in prefix_map :
#         prefix_map[prefix_sum].append(i)
#     else :
#         prefix_map[prefix_sum] = [i]
# return result