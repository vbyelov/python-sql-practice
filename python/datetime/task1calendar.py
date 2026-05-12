from calendar import Calendar


class MyCalendar(Calendar):

    def count_weekday_in_year(self, year, weekday):

        count = 0

        for month in range(1, 13):

            weeks = self.monthdays2calendar(year, month)

            for week in weeks:
                for day in week:

                    if day[0] != 0 and day[1] == weekday:
                        count += 1

        return count


cal = MyCalendar()

print(cal.count_weekday_in_year(2019, 0))
print(cal.count_weekday_in_year(2030, 6))