def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
x = boring_function()
print("This lesson is boring...")

print(x)


value = None
if value is None:
    print("Sorry, you don't carry any value")


def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(7))
print(strange_function(8))
print(strange_function(9))

#sending a list to a function

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum([1, 2, 3, 4, 5]))
print(list_sum([10, 255, 365, 414, 512, 333]))


#Returning a list from a function

def strange_list_fun(n, direction):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(direction, i)

    return strange_list


print(strange_list_fun(50,1))
print(strange_list_fun(50,-1))


#Leap year
def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
#
# Write your code here.
#

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


#Return days and months

def days_in_month(year, month):
    if year < 1 or month < 1 or month > 12:
        return None

    month_days = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    if month == 2 and is_leap_year(year):
        return 29

    return month_days[month - 1]

print(days_in_month(1900, 2))


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    year = test_years[i]
    month = test_months[i]
    print(year, month, "->", end=" ")
    result = days_in_month(year, month)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")