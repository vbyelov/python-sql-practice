class WeekDayError(Exception):
    pass


class Weeker:
    daylist = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    def __init__(self, day):

        if self.__day not in self.daylist:



    #
    # Write code here.
    #

    def __str__(self):



    # Write code here.
    #

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