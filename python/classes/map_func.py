# import random
# def xvadrat(x):
#     return x * x + 1
#
# mylist = [x for x in range(10, 200, 7)]
# myrandomlist = list(random.sample(mylist, 17))
#
# print(myrandomlist)
#
#
# print(mylist)
#
# mynewlist = map(xvadrat, mylist)
# mynewlist2 = map(xvadrat, mylist[::-1])
#
# for i in mynewlist:
#     print(i, end=":")
# print()
#
# for j in mynewlist2:
#     print(j, end=":")
# print()
# print('______________')
# myrandomlistfunc = map(xvadrat, myrandomlist)
#
# for i in myrandomlistfunc:
#     print(i, end=":")
#
#
#
# print("EXAMPLE")
#
# list_1 = [x for x in range(5)]
# list_2 = list(map(lambda x: 2 ** x, list_1))
# print(list_2)
#
# for x in map(lambda x: x * x, list_2):
#     print(x, end=' ')
# print()
#
# print("fliter")
#
# from random import seed, randint
#
# seed()
# data = [randint(-100,100) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
#
# print(data)
# print(filtered)
#

nums = [-3, -2, -1, 0, 1, 2, 3, 4]

step1 = filter(lambda x: x >0, nums)
step2 = filter(lambda x: x % 2 == 0, step1)
finalstep = map(lambda x: x ** 2, step2)

print(list(finalstep))



final2 = [x ** 2 for x in nums if x > 0 and x % 2 == 0]
print(final2)


from random import seed, randint

seed()
data = [randint(-100,100) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)