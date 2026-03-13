class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        hours = self.__hours
        if hours < 10:
            hours = '0' + str(hours)
        else:
            hours = str(hours)
        minutes = self.__minutes
        if minutes < 10:
            minutes = '0' + str(minutes)
        else:
            minutes = str(minutes)
        seconds = self.__seconds
        if seconds < 10:
            seconds = '0' + str(seconds)
        else:
            seconds = str(seconds)
        return hours + ":" + minutes + ":" + seconds


    def next_second(self):
        if self.__seconds == 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0
        else:
            self.__seconds += 1
        # Write code here
        #

    def prev_second(self):
        if self.__seconds != 0:
            self.__seconds -= 1

        elif self.__minutes != 0:
            self.__minutes -= 1
            self.__seconds = 59
        elif self.__hours != 0:
            self.__hours -= 1
            self.__minutes = 59
            self.__seconds = 59
        else:
            self.__seconds = 59
            self.__minutes = 59
            self.__hours = 23
        # Write code here
        #


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)