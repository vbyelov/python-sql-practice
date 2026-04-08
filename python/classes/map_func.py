import random
def xvadrat(x):
    return x * x + 1

mylist = [x for x in range(10, 200, 7)]
myrandomlist = list(random.sample(mylist, 17))

print(myrandomlist)


print(mylist)

mynewlist = map(xvadrat, mylist)
mynewlist2 = map(xvadrat, mylist[::-1])

for i in mynewlist:
    print(i, end=":")
print()

for j in mynewlist2:
    print(j, end=":")

myrandomlistfunc = map(xkvadrat, myrandomlist)
print(myrandomlistfunc)