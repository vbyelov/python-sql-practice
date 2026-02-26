# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)


si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)


s1 = 'Where are The Snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3)
print(s3[1])