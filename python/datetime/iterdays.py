import calendar

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")


import calendar

# c = calendar.Calendar()
#
# for iter in c.itermonthdates4(2019, 11):
#     print(iter, end=" ")

import calendar

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)