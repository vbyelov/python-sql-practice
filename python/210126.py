# Day 4 — Python
# Task 1: word_frequencies
#
# Write a function word_frequencies(text) that:
# 1. Takes a string as input
# 2. Counts how many times each word appears
# 3. Is case-insensitive ("Hello" == "hello")
# 4. Ignores punctuation (.,!?:;)
# 5. Returns a dictionary: {word: count}
#
# Restrictions:
# - Use for-loop
# - Use if
# - Use a dictionary as an accumulator
# - Do NOT use collections.Counter
# - Do NOT use regex
#
# Example:
# word_frequencies("Hello, hello world!")
# -> {"hello": 2, "world": 1}

def word_frequency(text):
    words = text.lower().split()
    result_dict = {}

    for word in words:
        clean_word = ""

        for char in word:
            if char.isalpha():
                clean_word += char

        if clean_word:
            result_dict[clean_word] = result_dict.get(clean_word, 0) + 1

    return result_dict