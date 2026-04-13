nums = list(map(int,input().split()))
# squares = lambda n : n * n , nums

# even = lambda i : i %2 == 0 , nums
# res1 = squares
# res2 = even

# print("square list :" , list(map(int,res1)))
# print("evens of the list :",list(map(int,res2)))
def square(nums):
    square_list = nums[:]
    for i in range(len(nums)) :
        square_list[i] = nums[i] * nums[i]
    return square_list
def even(nums):
    even_list = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0 :
            even_list.append(nums[i])

    return even_list
print(square(nums))
print(even(nums))