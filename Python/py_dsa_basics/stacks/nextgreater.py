def next_greater(nums):
    stack = []
    map = {}
    for num in nums:
        while stack and num > stack[-1] :
            prev = stack.pop()
            map[prev] = num
        stack.append(num)
    while stack :
        map[stack.pop()] = -1
    result = []
    for num in nums:
        result.append(map[num])
    return result
def next_greater_duplicates(nums):
    stack = []
    result = [-1]*len(nums)
    for i in range(len(nums)) :
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result