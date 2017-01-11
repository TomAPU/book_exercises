from mytime import Time
from date import Date

class TimeDate:
    def __init__(self, hour=0, minute=0, second=0, year=0, month=0, day=0):
        self._date = Date(year, month, day)
        self._time = Time(hour, minute, second)

    def __str__(self):
        return "%s %s" % (str(self._date), str(self._time))

    def year(self):
        return self._date.year()

    def month(self):
        return self._date.month()

    def day(self):
        return self._date.day()

    def hour(self):
        return self._time.hours()

    def minute(self):
        return self._time.minutes()

    def second(self):
        return self._time.seconds()

    def isAM(self):
        return self._time.isAM()

    def isPM(self):
        return self._time.isPM()

    def time(self):
        return self._time

    def date(self):
        return self._date

    def __eq__(self, other):
        return self._date == other.date() and self._time == other.time()

    def __gt__(self, other):
        if self._date > other.date():
            return True
        elif self._date == other.date():
            if self._time > other.time():
                return True
        return False

    # ...

if __name__ == '__main__':
    td = TimeDate(9,8, 10,2017,1,11)
    print( 'timedate: ', str(td))
    td2 = TimeDate(9,8, 10,2017,1,12)
    print( 'timedate2: ', str(td2))
    td3 = TimeDate(10,8, 10,2017,1,11)
    print ('timedate3: ', str(td3))

    print( 'td2>td?', td2>td)
    print( 'td3>td?', td3>td)

