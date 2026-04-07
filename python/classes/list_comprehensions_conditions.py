the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

the_list = [0 if x % 2 != 0 else 1 for x in range(10)]

print(the_list)
