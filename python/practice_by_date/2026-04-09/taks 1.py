d = {"a":3, "b":1, "c":2}
result = sorted(d.items(),key = lambda x : x[1])
print(result)