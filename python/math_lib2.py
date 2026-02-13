# from math import pi, radians, degrees, sin, cos, tan, asin, exp, pow, floor, ceil, trunc, hypot
# import random
# ad = 90
# ar = radians(ad)
# ad = degrees(ar)
#
# print(ad == 90.)
# print(ar == pi / 2.)
# print(sin(ar) / cos(ar) == tan(ar))
# print(asin(sin(ar)) == ar)
#
# for i in range (360):
#     print(sin(radians(i)))
#     # try:
#     print(tan(radians(i)))
#     # except:
#     #     pass
#
#
# print(exp(5))
# print(pow(5, 2))
#
# from math import ceil, floor, trunc
#
# x = 1.4
# y = 2.6
#
# print(floor(x), floor(y))
# print(floor(-x), floor(-y))
# print(ceil(x), ceil(y))
# print(ceil(-x), ceil(-y))
# print(trunc(x), trunc(y))
# print(trunc(-x), trunc(-y))
#
# print(hypot(51, 5))
#
#
# while i < 1000:
#     i = i + 50 + random.random()
#     print(i)
# else:
#     print('done. i is ' + str(i))
#
#
# from random import random, seed
#
# seed(777)
#
# for i in range(5):
#     print(random())


from random import randint, randrange, seed

# seed(6)

for i in range(10):
    # print(str(randint(0, 100)) + ' rand int')
    print(str(randrange(0, 100, 5)) + ' randrange')


from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 333, 555, 777, 757]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

print(sample(my_list, 2))
