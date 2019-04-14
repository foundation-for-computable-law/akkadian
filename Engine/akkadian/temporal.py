import functools
import math
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
# from pandas import date_range
from akkadian.TimeSeries import *
from akkadian.Value import *


# AND, OR, NOT


# Time series NOT
# Output: TimeSeries
def Not(ts: TimeSeries):
    return TimeSeries(internal_ts_map_unary_fcn(internal_not, ts.dict))


# Internal, static version of the logical NOT function
# Output: Value
def internal_not(a_in: Value):
    a = try_converting_to_val(a_in)

    if a.is_stub or a.is_null:
        return a
    else:
        return Value(not a.value, cf=a.cf)


# Time series Boolean AND
# Output: TimeSeries
def And(*args):
    return functools.reduce(inner_and, args)


# Only allows two arguments; supports the version above
def inner_and(ts1: TimeSeries, ts2: TimeSeries):
    return process_binary_ts(internal_and, ts1, ts2)


# Internal, static Boolean AND function
# Output: Value
def internal_and(a_in: Value, b_in: Value):
    a = try_converting_to_val(a_in)
    b = try_converting_to_val(b_in)

    if a.value is False and b.value is False:
        return Value(False, cf=max(a.cf, b.cf))
    elif a.value is False:
        return Value(False, cf=a.cf)
    elif b.value is False:
        return Value(False, cf=b.cf)
    elif a.value is True and b.value is True:
        return Value(True, cf=min(a.cf, b.cf))
    elif a.value is True:
        return Value(b.value, cf=b.cf)
    elif b.value is True:
        return Value(a.value, cf=a.cf)
    elif a.is_null and b.is_null:
        return Value("Null", cf=max(a.cf, b.cf), null=True)
    elif a.is_null:
        return Value("Null", cf=a.cf, null=True)
    elif b.is_null:
        return Value("Null", cf=b.cf, null=True)
    else:
        return Value("Stub", cf=max(a.cf, b.cf), stub=True)


# Time series Boolean OR function
# Output: TimeSeries
def Or(*args):
    return functools.reduce(inner_or, args)


# Only allows two arguments; supports the version above
def inner_or(ts1: TimeSeries, ts2: TimeSeries):
    return process_binary_ts(internal_or, ts1, ts2)


# Internal, static Boolean OR function
# Output: Value
def internal_or(a_in: Value, b_in: Value):
    a = try_converting_to_val(a_in)
    b = try_converting_to_val(b_in)

    if a.value is True and b.value is True:
        return Value(True, cf=max(a.cf, b.cf))
    elif a.value is True:
        return Value(True, cf=a.cf)
    elif b.value is True:
        return Value(True, cf=b.cf)
    elif a.value is False and b.value is False:
        return Value(False, cf=min(a.cf, b.cf))
    elif a.value is False:
        return Value(b.value, cf=b.cf)
    elif b.value is False:
        return Value(a.value, cf=a.cf)
    elif a.is_null and b.is_null:
        return Value("Null", cf=max(a.cf, b.cf), null=True)
    elif a.is_null:
        return Value("Null", cf=a.cf, null=True)
    elif b.is_null:
        return Value("Null", cf=b.cf, null=True)
    else:
        return Value("Stub", cf=max(a.cf, b.cf), stub=True)


# CONDITIONALS

# IF - An if-then-else statement that can take time series arguments
# Can take an arbitrary number of arguments
# Odd-numbered arguments are Boolean tests; even-numbered arguments are possible return values
# The final argument is the default value (required)
# The resulting CF is the minimum CF of all Boolean tests evaluated in order to get a result,
# and also of the CF of the return value
# TODO: Time series
# TODO: Implement lazy evaluation so args are only invoked as needed
def If(*args):
    return internal_if(1, *args)


def internal_if(cf, *args):

    arg0 = try_converting_to_val(args[0])

    # "ELSE" - Return the default value
    if len(args) == 1:
        return Value(arg0.value, cf=min(cf, arg0.cf))

    # "IF" - If the test evaluates to True

    # First catch Stub and None
    if arg0.is_stub:
        return arg0
    elif arg0.is_null:
        arg1 = try_converting_to_val(args[1])
        if arg1.is_stub:
            return arg1
        else:
            return arg0

    # Does test evaluate to True?
    if arg0.value:
        # "THEN"
        arg1 = try_converting_to_val(args[1])
        return Value(arg1.value, cf=min(cf, arg0.cf, arg1.cf))

    # Compress the expression and recurse
    else:
        return internal_if(min(cf, arg0.cf), *args[2:])


# COMPOSE A TIME SERIES


# Compose a time series from a list of dates and a list of values
def ComposeTS(dates: list, values: list):
    return TS(internal_compose_ts(dates, values))


# CONSTRUCTING BOOLEAN TIME SERIES


# Boolean time series that's true starting on a given date, and otherwise false
def EffectiveFrom(dt):
    return TS({Dawn: False, dt: True})


# Boolean time series that's true up until a given date, and otherwise false
# TODO: Use AddDays once time series can be declared with V objects as dates
def EffectiveUntil(dt):
    return TS({Dawn: True, _simple_add_days(dt, 1): False})


# Boolean time series that's true between two dates, and otherwise false
def EffectiveBetween(start, end):
    return And(EffectiveFrom(start), EffectiveUntil(end))


# Creates a time series that has a given value forever
def Eternal(val):
    return TimeSeries({1: try_converting_to_val(val)})


# IDENTIFYING INDETERMINATE PERIODS


# Returns True when a TimeSeries is Null; otherwise returns False
# Output: TimeSeries
def IsNull(ts):
    return TimeSeries(internal_ts_trim(internal_ts_map_unary_fcn(internal_is_null, try_converting_to_ts(ts).dict)))


# Internal, static version of the IsNull function
# Output: Value
def internal_is_null(a_in: Value):
    return Value(try_converting_to_val(a_in).is_null)


# Returns True when a TimeSeries is Stub; otherwise returns False
# Output: TimeSeries
def IsStub(ts):
    return TimeSeries(internal_ts_trim(internal_ts_map_unary_fcn(internal_is_stub, try_converting_to_ts(ts).dict)))


# Internal, static version of the IsStub function
# Output: Value
def internal_is_stub(a_in: Value):
    return Value(try_converting_to_val(a_in).is_stub)


# MANIPULATING CERTAINTY FACTORS


# Get the certainty factor (CF) of the values in the time line
# Output: TimeSeries
def GetCF(ts):
    return TimeSeries(internal_ts_trim(internal_ts_map_unary_fcn(internal_get_cf, try_converting_to_ts(ts).dict)))


# Internal, static version of the GetCF function
# Output: Value
def internal_get_cf(a_in: Value):
    return Value(try_converting_to_val(a_in).cf)


# Set the CF on a time series (the CF can vary over time)
# Output: TimeSeries
def SetCF(ts, cf):
    return process_binary_ts(_set_cf, ts, cf)


# Internal, static version of SetCF
# Output: Value
def _set_cf(v: Value, cf: Value):
    return Value(v.value, cf=max(min(cf.value, 1), 0))


# Rescales the CF of a TimeSeries by a given factor
# Output: TimeSeries
def RescaleCF(ts, factor):
    return SetCF(ts, GetCF(ts) * factor)


# DATE ARITHMETIC

# AddDays

# Determine the date n days from a given date
def AddDays2(d, n):
    return process_binary_ts(_add_days, d, n)


# Internal, static version of AddDays
def _add_days(d: Value, n: Value):
    return process_binary_val(_simple_add_days, d, n)


# Returns a date in (string) ISO format
def _simple_add_days(d: str, n: int):
    return (str_to_date(d) + timedelta(days=n)).isoformat()


# AddWeeks


# Determine the date n weeks from a given date
def AddWeeks(d, n):
    return process_binary_ts(_add_weeks, d, n)


# Internal, static version of AddWeeks
def _add_weeks(d: Value, n: Value):
    return process_binary_val(_simple_add_weeks, d, n)


# Returns a date in (string) ISO format
def _simple_add_weeks(d: str, n: int):
    return (str_to_date(d) + timedelta(weeks=n)).isoformat()


# AddMonths


# Determine the date n months from a given date
def AddMonths(d, n):
    return process_binary_ts(_add_months, d, n)


# Scalar version of AddMonths (for internal use only)
def _add_months(d: Value, n: Value):
    return process_binary_val(_simple_add_months, d, n)


# Returns a date in (string) ISO format
def _simple_add_months(d: str, n: int):
    return (str_to_date(d) + relativedelta(months=n)).isoformat()


# AddYears


# Determine the date n years from a given date
def AddYears2(d, n):
    return process_binary_ts(_add_years, d, n)


# Scalar version of AddMonths (for internal use only)
def _add_years(d, n):
    return process_binary_val(_simple_add_years, d, n)


# Returns a date in (string) ISO format
def _simple_add_years(d: str, n: int):
    return (str_to_date(d) + relativedelta(years=n)).isoformat()







# DATE ARITHMETIC: ___Delta
# Currently does later - earlier and then converts to the desired interval


# Determine the number of days between two dates
# def DayDelta(earlier, later):
#     return process_binary(lambda x, y: _day_delta(x, y), earlier, later)


# Scalar version of DayDelta (for internal use only)
# def _day_delta(earlier, later):
#     return (date.fromisoformat(later) - date.fromisoformat(earlier)).days


# Determine the number of weeks between two dates
# def WeekDelta(earlier, later):
#     return DayDelta(earlier, later) / 7


# def month_delta(earlier, later):
#     delta = relativedelta(date.fromisoformat(later), date.fromisoformat(earlier))
#     return delta.years * 12 + delta.months + (delta.days / 30)


# DECOMPOSING A DATE

# def Year(dt):
#     return process_unary(lambda x: date.fromisoformat(x).year, dt)
#
#
# def Month(dt):
#     return process_unary(lambda x: date.fromisoformat(x).month, dt)
#
#
# def Day(dt):
#     return process_unary(lambda x: date.fromisoformat(x).day, dt)


# MATH
# These functions are the time series versions of those in the Python math library


# Time series version of math.ceil(x)
# def Ceil(x):
#     return process_unary(math.ceil, x)


# Time series version of math.floor(x)
# def Floor(x):
#     return process_unary(math.floor, x)


# Time series version of math.remainder(x, y)
# def Remainder(x, y):
#     return process_binary(lambda a, b: math.remainder(a, b), x, y)


# Time series version of math.trunc(x)
# def Trunc(x):
#     return process_unary(math.trunc, x)


# Time series version of math.exp(x)
# def Exp(x):
#     return process_unary(math.exp, x)


# Time series version of math.log(x[, base])
# def Log(x, base=math.e):
#     return process_binary(lambda a, b: math.log(a, b), x, base)


# Time series version of math.pow(x, y)
# def Pow(x, y):
#     return process_binary(lambda a, b: math.pow(a, b), x, y)


# For consistency...
E = math.e


# EXTRACTING VALUES FROM A TIME SERIES


# Value of a time series on a given date
# The implementation uses the "traces" Python package
# TODO: Handle uncertainty
def AsOf(ts, dt):
    return ts[dt]


# TIME SERIES COMPONENTS


# def DateRange(start=None, end=None, periods=None, freq=None):
#     return list(map(lambda x: x.date().isoformat(),
#                     date_range(start=start, end=end, periods=periods, freq=freq).to_pydatetime()))


# TODO...

# def BalancingTest(*args):
#     score = Total(Map(lambda x, y: Bool(x) * y, Partition(args, 2)))
#     limit = If(score < 0, x, y)
#     return RescaleCF(Bool(score), score/limit)

