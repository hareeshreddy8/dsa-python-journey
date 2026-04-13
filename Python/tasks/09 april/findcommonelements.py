def common_elements(nums1,nums2) :
    nums1_set = set(nums1)
    nums2_set = set(nums2)
    result = []
    for num in nums1:
        if num in nums2_set:
            result.append(num)

    return result

a = [1,2,3,4]
b = [3,4,5,6]
print(common_elements(a,b))
