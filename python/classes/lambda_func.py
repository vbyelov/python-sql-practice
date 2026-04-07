pwr_third = lambda pwr: pwr * pwr * pwr
opposite_number = lambda x : 1 / x

for x in range(10, 20):
    print(x, opposite_number(x))
    print()
    print(pwr_third(x))


def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

