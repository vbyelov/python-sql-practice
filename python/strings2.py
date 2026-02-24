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

mylist1 = list('This is a very long string')
print(mylist1)
mylist1 = mylist1[::-1]
print(mylist1)

print(mylist1.count('l'))
print(mylist1.count(' '))


