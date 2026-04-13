d = {1: "c", 2: "a", 3: "b"}

result = dict(sorted(d.items(),key = lambda x : x[1]))
print(result)