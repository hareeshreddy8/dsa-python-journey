def intersection(nums1,nums2):
    res = []
    for i in range(len(nums1)) :
        for j in range(len(nums2)):
            if nums1[i] == nums2[j] and nums1[i] not in res:
                res.append(nums1[i])
    return res
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
print(intersection(nums1,nums2))