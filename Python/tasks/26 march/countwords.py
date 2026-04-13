def count_words(s):
    count = 0
    for i in range(len(s)) :
        if s[i].isalnum() and (i == 0 or not s[i - 1].isalnum()):
            count += 1
    return count 
        