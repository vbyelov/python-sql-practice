from datetime import date
import time

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)


d = date.fromisoformat('2019-11-04')

print(str(d) + ' This is ISO Format')


d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)


from datetime import date

d = date(2019, 11, 7)
print(d.weekday())
