def allduplicates(nums):
    freq = {}
    result = []
    for num in nums:
        freq[num] = freq.get(num,0) + 1
    for num in freq.keys():
        if freq[num] > 1:
            result.append(num)

    return result

#using set
def all_dups(nums):
    uniques = set()
    duplicates = set()
    for num in nums:
        if num not in uniques :
            uniques.add(num)

        else :
            duplicates.add(num)

    return list(duplicates)