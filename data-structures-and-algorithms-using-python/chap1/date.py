# encoding: utf-8
# Implements a proleptic Gregorian calendar date as a Julian day number.

# Interfaces: 
# + Date(year, month, day): 创建一个 Date 实例并初始化成公历中的一天。西元前 1 年及之前的日期中的年部分用负数表示。
# + year(): 返回该公历日期的年。
# + month(): 返回该公历日期的月。
# + day(): 返回该公历日期的日。
# + monthName(): 返回该公历日期的月份名。
# + dayOfWeek(): 返回星期数，值为 [0-6]，0 表示星期一，6 表示星期日。
# + numDays(otherDate): 返回这两个日期间所差距的天数，是一个正整数。
# + isLeapYear(): 布尔值，检测该日期是否在一个闰年中。
# + advanceBy(days): 如果参数是正数，则返回的日期将增加这么多天，如果负数则减少，有必要的话，该日期将近似到西元前 4714 年的 12 月 24 日。
# + comparable(otherDate): 实现逻辑运算，如 &lt;, &lt;=, &gt;, &gt;=, ==, !==。
# + toString(): 返回 `yyyy-mm-dd` 形式的字符串表示。

from datetime import datetime

class Date:
    # Creates an object instance for the specified Gregorian date.
    def __init__(self, year=0, month=0, day=0):
        if year==0 and month==0 and day==0:
            date = datetime.now().date()
            year = date.year
            month = date.month
            day = date.day
        self._julianDay = 0
        assert self._isValidGregorian(year, month, day), \
                "Invalid Gregorian date."

        # Gredorian data --> julian day formula:
        # T = (M - 14) / 12
        # jday = D - 32075 + (1461 * (Y + 4800 + T) / 4) +
        #                    (367 * (M - 2 - T * 12) / 12) -
        #                    (3 * ((Y + 4900 + T) / 100) / 4)
        #
        # This first line of the equation, T = (M-14)/12, has to be changed
        # since Python's implementation of integer division is not the same
        # as mathematical definition
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + \
                (1461 * (year + 4800 + tmp) // 4) + \
                (367 * (month -2 - tmp * 12) // 12) - \
                (3 * ((year + 4900 + tmp) // 100) // 4)

    # 一月（31天），二月（平年28天，闰年29天），三月（31天），
    # 四月（30天），五月（31 天），六月（30天），七月（31天），
    # 八月（31天），九月（30天），十月（31天），十一月（30天），
    # 十二月（31天）。

    def _isValidGregorian(self, year, month, day):
        if month > 12 or month < 1:
            return False

        if day < 1 or day > 31:
            return False

        # months_31_days = [1, 3, 5, 7, 8, 10, 12]
        months_30_days = [4, 6, 9, 11]

        if month in months_30_days and day > 30:
            return False

        if month == 2:
            if self._leapYear(year):
                if day > 29:
                    return False
            if day > 28:
                return False

        return True
    # Extracts the appropriate Gregorian date component.
    def year(self):
        return (self._toGregorian())[0] # returing Y from (Y, M, D)

    def month(self):
        return (self._toGregorian())[1] # returing M from (Y, M, D)

    def day(self):
        return (self._toGregorian())[2] # returing D from (Y, M, D)

    def _dayOfWeek(self, year, month, day):
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + \
                year + year // 4 - year // 100 + year // 400 ) % 7
    # Returns day of the week as an int between 0 (Mon) and 6 (Sun).
    def dayOfWeek(self):
        year, month, day = self._toGregorian()
        return self._dayOfWeek(year, month, day)

    # Returns the date as a string in Gregorian format.
    def __str__(self):
        return self.asGregorian('/')

    # Returns the date as a string in Gregorian format.
    def __repr__(self):
        return str(self)

    def __hash__(self):
        return self._julianDay

    # Logically compares the two dates.
    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay


    # Returns the Gregorian date as a tuple: (year, month, day).
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return year, month, day

    def monthName(self):
        months = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December",]
        return months[self.month()-1]

    def _leapYear(self, year):
        if year % 400 == 0 or \
                (year % 4 == 0 and year % 100 != 0):
                return True
        return False

    def isLeapYear(self):
        return self._leapYear(self.year)


    def numDays(self, otherDate):
        if self._julianDay > otherDate._julianDay:
            return self._julianDay - otherDate._julianDay
        else:
            return otherDate._julianDay - self._julianDay

    def advanceBy(self, days):
        self._julianDay += days
        if self._julianDay < 0:
            self._julianDay = 0

    def dayOfWeekName(self):
        """
        returns a string containing the name of the day.
        """
        weeknames = ["Mo", "Tu", "We", "Tu", "Fr", "Sa", "Su"]
        return months[self.dayOfWeek()]

    def dayOfYear(self):
        """
        returns an integer indicating the day of the year.
        For example, the first day of February is day 32 of the year.
        """

        # 一月（31天），二月（平年28天，闰年29天），三月（31天），
        # 四月（30天），五月（31 天），六月（30天），七月（31天），
        # 八月（31天），九月（30天），十月（31天），十一月（30天），
        # 十二月（31天）。
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day =  self._toGregorian()

        days = 0
        for m in range(1, month):
            days + month_days[m]

        if month > 2:
            if self._leapYear(year):
                days += 1

        days += day
        return days

    def isWeekday(self):
        "determines if the date is a weekday."
        dw = self.dayOfWeek()
        # dayOfWeek(): 返回星期数，值为 [0-6]，0 表示星期一，6 表示星期日。
        if dw < 5:
            return False
        return True

    def asGregorian(self, divchar='/'):
        # similar to the str() method but uses the optional
        # argument divchar as the dividing character 
        # between the three components of the Gregorian date.
        year, month, day = self._toGregorian()
        return "%04d%s%02d%s%02d" % (year, divchar, month, divchar, day)

    def printCalendar(self, date):
        """
        accepts a Date object and prints a calendar for the month of the given
        date.
        """
        header = "%s  %d" % (date.monthName(), date.year())
        print(header.center(13*2))
        print("Su  Mo  Tu  We  Th  Fr  Sa")


        # 一月（31天），二月（平年28天，闰年29天），三月（31天），
        # 四月（30天），五月（31 天），六月（30天），七月（31天），
        # 八月（31天），九月（30天），十月（31天），十一月（30天），
        # 十二月（31天）。
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        month = date.month()
        month_day = month_days[month-1]
        if month == 2:
            if date.isLeapYear():
                month_day += 1

        # dayOfWeek(): 返回星期数，值为 [0-6]，0 表示星期一，6 表示星期日。
        dw = self._dayOfWeek(date.year(), month, 1)
        dw = (dw+1) % 7 # 值为 [0-6]，0 表示 Su，6 表示Sa

        for i in range(0, dw): # first day line
            print(" "*4, end='')

        for d in range(1, month_day+1):
            print("%2d  "%d, end='')
            dw += 1
            if dw % 7 == 0:
                print("")
        print("")

if __name__ == "__main__":
    date = Date(2007, 11, 3)
    date.printCalendar(date)
