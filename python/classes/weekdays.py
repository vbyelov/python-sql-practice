class WeekDayError(Exception):
    pass


class Weeker:
    daylist = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    def __init__(self, day):

        if self.__day not in self.daylist:
            raise WeekDayError('Invalid day')
        self.__day = day


    def __str__(self):
        print(self.__day)


    def add_days(self, n):

    #
    # Write code here.
    #

    def subtract_days(self, n):


#
# Write code here.
#


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