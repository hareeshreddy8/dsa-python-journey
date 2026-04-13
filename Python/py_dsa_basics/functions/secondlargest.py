def second_largest(nums,k) :
    nums.sort()
    return nums[len(nums) - k]
    # sortednums = [0]*k
    # for i in range(sorted(nums)):
    #     sorted(nums).append(nums[i])
    

nums = list(map(int,input().split()))
k = int(input())
result = second_largest(nums,k)
print(result)