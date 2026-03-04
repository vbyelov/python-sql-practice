# multiline = '''Line #1
# Line 3, Line 4
# Line #2'''
#
# print(len(multiline))
#
# print(multiline)
#
# str1 = 'a'
# str2 = 'b'
#
# print(str1 + str2)
# print(str2 + str1)
# print(5 * 'a')
# print('b' * 4)
#
# def line_mult(a,b):
#     return a * b
#
# def line_add(a,b):
#     return a + b
#
#
# print(line_mult("Today ",4))
# print(line_mult(5,"Tomorrow "))
#
# print(line_add("Today is ", '20.02.2026'))
#
#
# char_1 = 'Ä'
# char_2 = 'Ö'  # space
#
# print(ord(char_1))
# print(ord(char_2))
#
# ii = 'Tomorrow is expected to be a sunny day'
# import string
#
#
# def all_letters():
#     # i = string.whitespace
#     for letter in ii:
#         print(letter, '-', ord(letter))
#     return None
#
# all_letters()
#
#
# for i in range(32,128):
#     print(i, '--',chr(i))
#
# for i in range(len(ii)):
#     print (ii[i], end ='')
# print()
# for i in range(1, (len(ii) + 1)):
#     print (ii[-i], end ='')
#
#
# print()
#
# print(ii[::-1])
#

string = input("Enter the string: ")

def reverse_letters(the_list):
    return the_list[::-1]

words = string.split()
final_word = []
for word in words:
    print(word)
    word = reverse_letters(word)
    final_word.append(word)


print('Final word is:')
finalresult = ' '.join(final_word)
print(finalresult)
import string
if "321" in finalresult:
    print("Yes, 123 is here")
else:
    print("No, 123 is not here")

print()
flag = False
for char in finalresult:
    if char.isupper():
        flag = True
        break
if flag:
    print("Yes, Uppercase is here")
else:
    print("No, Uppercase is not here")
