nums = list(map(int,input().split()))
k = int(input())
freq_map = {}
result = []
for num in nums :
    freq_map[num] = freq_map.get(num,0) + 1
result = sorted(freq_map, key=lambda x: freq_map[x], reverse=True)
print(result[:k])
