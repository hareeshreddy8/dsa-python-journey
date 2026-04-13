def count_of(string):
    vowels = 0
    consonants = 0
    for ch in string.lower() :
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else :
                consonants += 1
    return vowels,consonants