def longest_word(words):
    return max(words,key = lambda x:len(x))

words = ["hi", "hello", "world", "a"]
print(longest_word(words))