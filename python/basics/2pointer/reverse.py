list = [1, 2, 3, 4, 5, 6]
left , right = 0 , len(list) - 1
while left <= right :
    list[left] , list[right] = list[right] , list[left]
    left += 1
    right -= 1
print(list)