#!/usr/bin/env python3

""" module.py - an example of a Python module """



# counter = 0

print("Inside a module!")
print('-----------------')
print(__name__)



__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod




if __name__ == '__main__':
    print("This is Main Script")
elif __name__ == 'module':
    print("Inside a module!")
else:
    print("Inside a function!")

my_list = [i+1 for i in range(5)]
print(suml(my_list) == 15)
print(__counter)
print(prodl(my_list) == 120)
print(__counter)