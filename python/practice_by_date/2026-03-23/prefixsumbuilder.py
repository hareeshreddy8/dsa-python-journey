def sum_array(array) :
    sum_arr = []
    total = 0
    for num in array :
        total += num
        sum_arr.append(total)
    return sum_arr
array = array = list(map(int,input().split()))
print(sum_array(array))