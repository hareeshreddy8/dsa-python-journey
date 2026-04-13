def sum_array(array) :
    sum_arr = []
    total = 0
    for i in range(len(array)) :
        total += array[i]
        sum_arr.append(sum)
    return sum_arr
#modifing given array inpalce
def modified_array(array):
    for i in range(len(array)):
        if i == 0 :
            continue
        array[i] = array[i] + array[i - 1]
    return array
array = list(map(int,input().split()))
print("running sum array : ",sum_array(array))
print(modified_array(array))