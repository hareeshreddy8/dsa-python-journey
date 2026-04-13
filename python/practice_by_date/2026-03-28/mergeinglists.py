def merging_lists(nums1,nums2):
    result = []
    i , j = 0 , 0
    while i < len(nums1) and j < len(nums2) :
        if nums1[i] < nums2[j] :
            result.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j] :
            result.append(nums2[j])
            j += 1
        else :
            result.append(nums1[i])
            result.append(nums2[j])
            i+= 1
            j += 1
        
        # while i < len(nums1):
        #     result.append(nums1[i])
        #     i += 1
    if i < len(nums1):
        result.extend(nums1[i:])
        # while j < len(nums2):
        #     result.append(nums2[j])
        #     j += 1
    if j < len(nums2):
        result.extend(nums2[j:])
    return result