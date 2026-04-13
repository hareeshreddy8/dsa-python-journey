def reverse(nums,start,end):
    while start < end:
        nums[start] , nums[end] = nums[end] , nums[start]
        start += 1
        end -= 1
    return nums
def rotate(nums,k) :
    k = k % len(nums)
    reverse(nums,0,len(nums) - 1)
    reverse(nums,0,k-1)
    reverse(nums,k,len(nums)-1)
    return nums
def slicing(nums,k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]
