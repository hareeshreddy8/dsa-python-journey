def minimum_subarray(target,nums):
    min_length = float('-inf')
    current_sum = 0
    left = 0
    for i in range(len(nums)):
        current_sum += nums[i] 
        while current_sum >= sum:
            min_length = min(i - left + 1,min_length)
            current_sum -= nums[left]
            left += 1

    return 0 if min_length == float('-inf') else min_length