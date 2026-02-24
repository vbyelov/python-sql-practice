alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

# Demonstrating min() - Example 1:
print(min("!AbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')
print('[' + max(t) + ']')

t = [0, 1, 2, -7]
print(min(t))
print(max(t))

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

mylist = list(t)
print(mylist)

for numbers in mylist:
    print(int(numbers)*7)

mylist1 = list('''
I can put many many lines here.
From the very beginning till the end of file
More and more
This is a very long string
'''
               )
print(mylist1)
mylist1 = mylist1[::-1]
print(mylist1)

print(mylist1.count('l'))
print(mylist1.count(' '))
print(mylist1.count('\n'))

#Capitalize

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())


# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(60) + ']')
print('[' + 'gamma'.center(20, '%') + ']')

# Demonstrating the endswith() method:
if "the great epsilon".endswith("on"):
    print("yes")
else:
    print("no")

# t = "zeta"
# print(t.endswith("a"))
# print(t.endswith("A"))
# print(t.endswith("et"))
# print(t.endswith("eta"))
#
#
# the_text = """A variation of the ordinary lorem ipsum
# text has been used in typesetting since the 1960s
# or earlier, when it was popularized by advertisements
# for Letraset transfer sheets. It was introduced to
# the Information Age in the mid-1980s by the Aldus Corporation,
# which employed it in graphics and word-processing templates
# for its desktop publishing program PageMaker (from Wikipedia)"""
#
# fnd = the_text.find('the')
# while fnd != -1:
#     print(fnd)
#     fnd = the_text.find('the', fnd + 1)
#
# # Demonstrating the isalnum() method:
# print('lambda30'.isalnum())
# print('lambda'.isalnum())
# print('30'.isalnum())
# print('@'.isalnum())
# print('lambda_30'.isalnum())
# print(''.isalnum())

# # Example 1: Demonstrating the isapha() method:
# print("Moooo".isalpha())
# print('Mu40'.isalpha())
#
# # Example 2: Demonstrating the isdigit() method:
# print('2018'.isdigit())
# print("Year2019".isdigit())
#
#
# # Example 1: Demonstrating the islower() method:
# print("Moooo".islower())
# print('moooo'.islower())
#
# # Example 2: Demonstrating the isspace() method:
# print(' \n '.isspace())
# print(" ".isspace())
# print("mooo mooo mooo".isspace())
#
# # Example 3: Demonstrating the isupper() method:
# print("Moooo".isupper())
# print('moooo'.isupper())
# print('MOOOO'.isupper())

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))


# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
