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


from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)

import time

timestamp = 1592879180
print(time.ctime(timestamp))
