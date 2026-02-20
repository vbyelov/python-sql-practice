multiline = '''Line #1
Line 3, Line 4
Line #2'''

print(len(multiline))

print(multiline)

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

def line_mult(a,b):
    return a * b

def line_add(a,b):
    return a + b


print(line_mult("Today ",4))
print(line_mult(5,"Tomorrow "))

print(line_add("Today is ", '20.02.2026'))


char_1 = 'Ä'
char_2 = 'Ö'  # space

print(ord(char_1))
print(ord(char_2))

import string

def all_letters():
    # i = string.whitespace
    i = 'Tomorrow is expected to be a sunny day'
    for letter in i:
        print(letter, '-', ord(letter))
    return None

all_letters()


