def frequency(nums) :
    hashmap = {}
    for num in nums :
        if num in hashmap :
            hashmap[num] += 1
        else :
            hashmap[num] = 1
    return hashmap
nums = list(map(int,input().split()))
freq = frequency(nums)

print(freq)