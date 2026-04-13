def all_duplicates(nums):
    freq = {}
    duplicates = []
    for num in nums :
        freq[num] = freq.get(num,0) + 1
    for num in freq:
        if freq[num] > 1:
            duplicates.append(num)
    
    return duplicates
