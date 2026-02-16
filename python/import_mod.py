# import module
from sys import path

path.append('/Users/Analyst/Desktop/Pesochnica/Pycharm Pesochnica/python-sql-practice/python/modules/')

from module1 import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

import sys

for p in sys.path:
    print(p)

