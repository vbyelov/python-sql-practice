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

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))
