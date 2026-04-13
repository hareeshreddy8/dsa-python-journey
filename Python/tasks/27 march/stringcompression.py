def string_compression(str):
    res = ""
    count = 1
    for i in range(1,len(str)):
        if str[i] == str[i-1] :
            count += 1
        
        else :
            res += str[i-1] + "count"
            count = 1
    res += str[-1] + "count"
    return res