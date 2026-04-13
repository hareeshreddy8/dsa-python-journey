words = ["apple", "banana", "kiwi", "grape"]
sorted_words= [-1]*len(words)
sorted_words = sorted(words,key = lambda x : len(x))

items = [("apple", 50), ("banana", 20), ("mango", 100)]
sorted_by_price = sorted(items,key = lambda x : x[1],reverse = True)
students = [("hareesh", 90), ("ravi", 90), ("ram", 80)]
sorted_students = sorted(students,key =lambda x:(x[1],x[0]))
students.sort(key = lambda x:x[1],reverse = True)
students.sort(key  = lambda x:x[0])