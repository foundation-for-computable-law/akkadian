from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import math

# from numpy import timedelta64, datetime64

import pandas as pd

from dsl.V import *


# DATE ARITHMETIC: Add___

# Determine the date n days from a given date
def AddDays(d, n):
    return process_binary(lambda x, y: _add_days(x, y), d, n)


# Scalar version of AddDays (for internal use only)
def _add_days(d, n):
    return (date.fromisoformat(d) + timedelta(days=n)).isoformat()


# Determine the date n weeks from a given date
def AddWeeks(d, n):
    return process_binary(lambda x, y: _add_weeks(x, y), d, n)


# Scalar version of AddWeeks (for internal use only)
def _add_weeks(d, n):
    return (date.fromisoformat(d) + timedelta(weeks=n)).isoformat()


# Determine the date n months from a given date
def AddMonths(d, n):
    return process_binary(lambda x, y: _add_months(x, y), d, n)


# Scalar version of AddMonths (for internal use only)
def _add_months(d, n):
    return (date.fromisoformat(d) + relativedelta(months=n)).isoformat()


# Determine the date n years from a given date
def AddYears(d, n):
    return process_binary(lambda x, y: _add_years(x, y), d, n)


# Scalar version of AddMonths (for internal use only)
def _add_years(d, n):
    return (date.fromisoformat(d) + relativedelta(years=n)).isoformat()


# DATE ARITHMETIC: ___Delta
# Currently does later - earlier and then converts to the desired interval


# Determine the number of days between two dates
def DayDelta(earlier, later):
    return process_binary(lambda x, y: _day_delta(x, y), earlier, later)


# Scalar version of DayDelta (for internal use only)
def _day_delta(earlier, later):
    return (date.fromisoformat(later) - date.fromisoformat(earlier)).days


# Determine the number of weeks between two dates
def WeekDelta(earlier, later):
    return DayDelta(earlier, later) / 7


# def month_delta(earlier, later):
#     delta = relativedelta(date.fromisoformat(later), date.fromisoformat(earlier))
#     return delta.years * 12 + delta.months + (delta.days / 30)


# DECOMPOSING A DATE

def Year(dt):
    return process_unary(lambda x: date.fromisoformat(x).year, dt)


def Month(dt):
    return process_unary(lambda x: date.fromisoformat(x).month, dt)


def Day(dt):
    return process_unary(lambda x: date.fromisoformat(x).day, dt)


# MATH
# These functions are the time series versions of those in the Python math library


# Time series version of math.ceil(x)
def Ceil(x):
    return process_unary(math.ceil, x)


# Time series version of math.floor(x)
def Floor(x):
    return process_unary(math.floor, x)


# Time series version of math.remainder(x, y)
def Remainder(x, y):
    return process_binary(lambda a, b: math.remainder(a, b), x, y)


# Time series version of math.trunc(x)
def Trunc(x):
    return process_unary(math.trunc, x)


# Time series version of math.exp(x)
def Exp(x):
    return process_unary(math.exp, x)


# Time series version of math.log(x[, base])
def Log(x, base=math.e):
    return process_binary(lambda a, b: math.log(a, b), x, base)


# Time series version of math.pow(x, y)
def Pow(x, y):
    return process_binary(lambda a, b: math.pow(a, b), x, y)


# For consistency...
E = math.e


# CREATING BOOLEAN TIME SERIES


# Boolean time series that's true starting on a given date, and otherwise false
# def EffectiveFrom(dt):
#     return TS({DawnOfTime: False, dt: True})


# Boolean time series that's true up until a given date, and otherwise false
# TODO: Use AddDays once time series can be declared with V objects as dates
# def EffectiveUntil(dt):
#     return TS({DawnOfTime: True, _add_days(dt, 1): False})


# Boolean time series that's true between two dates, and otherwise false
# def EffectiveBetween(start, end):
#     return And(EffectiveFrom(start), EffectiveUntil(end))


# EXTRACTING VALUES FROM A TIME SERIES


# Value of a time series on a given date
# The implementation uses the "traces" Python package
# TODO: Handle uncertainty
def AsOf(ts, dt):
    return ts[dt]


# TIME SERIES COMPONENTS


def DateRange(start=None, end=None, periods=None, freq=None):
    return list(map(lambda x: x.date().isoformat(),
                    pd.date_range(start=start, end=end, periods=periods, freq=freq).to_pydatetime()))


# TODO...

# def BalancingTest(*args):
#     score = Total(Map(lambda x, y: Bool(x) * y, Partition(args, 2)))
#     limit = If(score < 0, x, y)
#     return RescaleCF(Bool(score), score/limit)

