from dsl.timeseries import *
from dsl.time_series import _add_days

# AND, OR, NOT


# Time series NOT
# Output: TimeSeries
def Not(ts: TimeSeries):
    return TimeSeries(internal_ts_map_unary_fcn(internal_not2, ts.dict))


# Internal, static version of the logical NOT function
# Output: Value
def internal_not2(a_in: Value):
    a = try_converting_to_val(a_in)

    if a.is_stub or a.is_null:
        return a
    else:
        return Value(not a.value, cf=a.cf)


# Time series Boolean AND
# Output: TimeSeries
def And2(ts1: TimeSeries, ts2: TimeSeries):
    return internal_binary_fcn(internal_and2, ts1, ts2)


# Internal, static Boolean AND function
# Output: Value
def internal_and2(a_in: Value, b_in: Value):
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
def Or2(ts1: TimeSeries, ts2: TimeSeries):
    return internal_binary_fcn(internal_or2, ts1, ts2)


# Internal, static Boolean OR function
# Output: Value
def internal_or2(a_in: Value, b_in: Value):
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


# CONSTRUCTING BOOLEAN TIME SERIES


# Boolean time series that's true starting on a given date, and otherwise false
def EffectiveFrom(dt):
    return TS2({Dawn: False, dt: True})


# Boolean time series that's true up until a given date, and otherwise false
# TODO: Use AddDays once time series can be declared with V objects as dates
def EffectiveUntil(dt):
    return TS2({Dawn: True, _add_days(dt, 1): False})


# Boolean time series that's true between two dates, and otherwise false
def EffectiveBetween(start, end):
    return And2(EffectiveFrom(start), EffectiveUntil(end))
