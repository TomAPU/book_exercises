# encoding: utf-8
from date import Date

# an Activities Calendar ADT below that can keep
# track of one activity per day over a given range of dates
class ActivitiesCalendar:
    def __init__(self, dateFrom, dateTo):
        assert dateTo >= dateFrom, "dateFrom must precede to dateTo"
        assert dateTo.year() == dateFrom.year(), "dateTo cannot overlap the day and month of dateFrom for the next year"
        self._dateFrom = dateFrom
        self._dateTo = dateTo
        self._activities = {}

    def __len__(self):
        return len(self._activities.keys())

    def getActivity(self, date):
        return self._activities.get(date, None)

    def addActivity(self, date, activity):
        assert self._dateFrom <= date <= self._dateTo, "The date must be within the valid date range for the calendar"
        self._activities[date] = activity

    def displayMonth(self, month):
        activities = [(k, v) for k,v in self._activities.items() if k.month() == month]
        activities.sort(key = lambda kv: kv[0].day())

        if len(activities) <=0 :
            print ('No activity in month', month)
        else:
            print("%04d-%02d" % (self._dateTo.year(), month))
            for a in activities:
                print(a[1])

if __name__ == '__main__':
    df = Date(2017, 1, 1)
    dt = Date(2017,1,30)
    ac = ActivitiesCalendar(df, dt)
    ac.displayMonth(1)
    ac.addActivity(Date(2017,1,9), "read book1")
    ac.addActivity(Date(2017,1,10), "read book2")
    ac.displayMonth(1)
