# Day 3 — Python
# Task 2: count_vowels_dict
#
# Rewrite the vowel counter using a dictionary as an accumulator.
#
# Write a function count_vowels_dict(text) that:
# 1. Takes a string as input
# 2. Counts vowels: a, e, i, o, u
# 3. Is case-insensitive
# 4. Uses ONE dictionary to store and update counts
# 5. Returns the dictionary with final counts
#
# Restrictions:
# - Use for-loop
# - Use if
# - Use a dictionary (no separate variables a, e, i, o, u)
# - Do NOT use collections, str.count(), or regex
#
# Example:
# count_vowels_dict("Hello World")
# -> {"a": 0, "e": 1, "i": 0, "o": 2, "u": 0}

def count_vowels_dict(text):
    vowels_dict = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    text = text.lower()
    for char in text:
        if char == "a":
            vowels_dict["a"] += 1
        elif char == "e":
            vowels_dict["e"] += 1
        elif char == "i":
            vowels_dict["i"] += 1
        elif char == "o":
            vowels_dict["o"] += 1
        elif char == "u":
            vowels_dict["u"] += 1
    return vowels_dict