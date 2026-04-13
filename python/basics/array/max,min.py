nums = [1, 3, 33, 4, 57, 99, 10, 8]
min,max = nums[0],nums[0]
for i in range(len(nums)) :
    if min > nums[i] :
        min = nums[i]
    if max < nums[i] :
        max = nums[i]
print(min,max)