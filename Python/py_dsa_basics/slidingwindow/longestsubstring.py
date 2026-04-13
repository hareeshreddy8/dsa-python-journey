s = str(input())
n= len(s)
sub_string = set()
left ,right = 0 , 0
max_length = 0
for right in range(n) :
    if s[right] in sub_string:
        sub_string.remove(s[left])
        left += 1
    sub_string.add(s[right])
    max_length = max(right - left +1 , max_length)
print(max_length)
