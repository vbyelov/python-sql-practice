# Task: max_number
#
# Write a function max_number(numbers) that:
# - takes a list (or tuple) of integers
# - returns the maximum number
#
# Restrictions:
# - do NOT use max()
# - use for-loop
# - use if
#
# Example:
# max_number([3, 7, 2, 10, 4]) -> 10
import time
time.sleep(0.5)

def max_number(numbers):
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number
        print
    return current_max


numbers = [
    12, 45, 3, 67, 23, 89, 4, 56, 78, 9,
    34, 21, 90, 11, 6, 54, 32, 18, 27, 41,
    73, 5, 60, 38, 14, 25, 80, 19, 48, 2,
    66, 29, 7, 52, 16, 83, 31, 10, 59, 44,
    1, 72, 36, 20, 85, 8, 40, 63, 28, 95
]

result = max_number(numbers)
print("Maximum number is:", result)
