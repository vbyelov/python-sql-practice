class WeekDayError(Exception):
    pass


class Weeker:
    daylist = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    def __init__(self, day):

        if day not in self.daylist:
            raise WeekDayError('Invalid day')
        self.__day = day


    def __str__(self):
        return (self.__day)


    def add_days(self, n):
        currentpos = self.daylist.index(self.__day)
        newpos = currentpos + n
        self.__day =  self.daylist[newpos % 7]



    def subtract_days(self, n):
        self.add_days(-n)


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")