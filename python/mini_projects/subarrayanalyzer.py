def total(nums) :
    total = 0
    for num in nums:
        total += num
    return total
def sum_array(nums) :
    sum_arr = nums[:]
    total = 0
    for i in range(1,len(nums)):
        sum_arr[i] = sum_arr[i] + sum_arr[i - 1]

        
    return sum_arr
def max_subarrsum(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1,len(nums)) :
        current_sum = max(nums[i] , current_sum + nums[i])
        max_sum = max(max_sum,current_sum)
    return max_sum