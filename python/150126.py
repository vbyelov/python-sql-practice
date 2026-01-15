# Day 3 — Python
# Task: count_vowels
#
# Write a function count_vowels(text) that:
# 1. Takes a string as input
# 2. Counts vowels: a, e, i, o, u
# 3. Is case-insensitive (A == a)
# 4. Returns a dictionary with counts for each vowel:
#    {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
#
# Restrictions:
# - Use for-loop
# - Use if
# - Use a dictionary
# - Do NOT use collections, str.count(), or regex
#
# Example:
# count_vowels("Hello World")
# -> {"a": 0, "e": 1, "i": 0, "o": 2, "u": 0}

def count_vowels(text):
    a = e = i = o = u = 0
    text = text.lower()
    for char in text:
        if char == 'a':
            a += 1
        elif char == 'e':
            e += 1
        elif char == 'i':
            i += 1
        elif char == 'o':
            o += 1
        elif char == 'u':
            u += 1
    return {"a": a, "e": e, "i": i, "o": o, "u": u}