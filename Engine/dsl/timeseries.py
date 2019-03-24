from datetime import date, timedelta

from dsl.T import *


# Determine the date n dates from a given date
# TODO: Make temporal; handle uncertainty
def AddDays(d, n):
    return (date.fromisoformat(d) + timedelta(days=n)).isoformat()


# Boolean time series that's true starting on a given date, and otherwise false
def TrueFrom(dt):
    return TS([[DawnOfTime, False], [dt, True]])


# Boolean time series that's true up until a given date, and otherwise false
def TrueUntil(dt):
    return T(traces.TimeSeries([[DawnOfTime, True], [AddDays(dt, 1), False]]))


# Boolean time series that's true between two dates, and otherwise false
# def TrueBetween(start, end):
#     return And(TrueFrom(start), TrueUntil(end))


# Time series Boolean AND function
# def And(ts1, ts2):
#     return ts1.operation(ts2, lambda x, y: x and y)


# Time series Boolean OR function
# def Or(ts1, ts2):
#     return ts1.operation(ts2, lambda x, y: x or y)


# Value of a time series on a given date
# TODO: Handle uncertainty
def AsOf(ts, dt):
    return ts[dt]



