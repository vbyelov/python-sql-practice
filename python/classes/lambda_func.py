pwr_third = lambda pwr: pwr * pwr * pwr
opposite_number = lambda x : 1 / x

for x in range(10, 20):
    print(x, opposite_number(x))
    print()
    print(pwr_third(x))