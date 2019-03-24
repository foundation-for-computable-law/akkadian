from datetime import date, timedelta

import traces


# Note: Dates are represented as strings 'yyyy-mm-dd'
# result = ts1.merge([ts1,ts2],compact=False, operation=None)


# Time-related constants
DawnOfTime = '1900-01-01'
AssessmentStart = '2018-01-01'
AssessmentEnd = '2020-12-31'


# NOT TEMPORAL YET
def AddDays(d, n):
    return (date.fromisoformat(d) + timedelta(days=n)).isoformat()


# Boolean time series that's true starting on a given date, and otherwise false
# def TrueFrom(dt):
#     return traces.TimeSeries([[DawnOfTime, False], [dt, True]])


# Boolean time series that's true up until a given date, and otherwise false
# def TrueUntil(dt):
#     return traces.TimeSeries([[DawnOfTime, True], [AddDays(dt, 1), False]])


# Boolean time series that's true between two dates, and otherwise false
# def TrueBetween(start, end):
#     return And(TrueFrom(start), TrueUntil(end))


# Time series Boolean AND function
# def And(ts1, ts2):
#     return ts1.operation(ts2, lambda x, y: x and y)


# Time series Boolean OR function
# def Or(ts1, ts2):
#     return ts1.operation(ts2, lambda x, y: x or y)


# Time series Boolean NOT function
# def Not(ts):
#     return ts.operation(ts, lambda x, y: not x)


# Value of a time series on a given date
# def AsOf(ts, dt):
#     return ts[dt]


# Internal function: Detect whether an object is a time series
def is_timeseries(a):
    return type(a) is traces.timeseries.TimeSeries


# Apply a binary function to two time series
def apply_binary_ts_fcn(f, ts1, ts2):
    return ts1.operation(ts2, lambda x, y: f(x, y))

