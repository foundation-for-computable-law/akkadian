from akkadian.TimeSeries import *
from akkadian.Value import *


# TODO: Refactor and simplify these functions


# Map a function over a list
# Output: TimeSeries
# TODO: Implement CFs
def Map(f, ts):
    return TimeSeries(internal_ts_map_unary_fcn(lambda x: internal_map(f, x), try_converting_to_ts(ts).dict))


# Internal, static version of the Map function
# Output: Value
def internal_map(f, a_in):
    a = try_converting_to_val(a_in)

    if a.is_stub or a.is_null:
        return a
    elif list_contains_null(a.value):
        return Null
    else:
        return Value(list(map(f, a.value)))


# Returns true if any element of a list is True
# Output: TimeSeries
def Any(ts):
    return TimeSeries(internal_ts_map_unary_fcn(internal_any, try_converting_to_ts(ts).dict))


# Internal, static version of Any
# Output: Value
def internal_any(a_in: Value):
    a = try_converting_to_val(a_in)

    if a.is_stub or a.is_null:
        return a
    elif list_any_true(a.value):
        return Value(True)
    elif list_contains_stub(a.value):
        return Stub
    elif list_contains_null(a.value):
        return Null
    else:
        return Value(list_any_true(a.value))


# Returns true if all elements of a list are True
# Output: TimeSeries
def All(ts):
    return TimeSeries(internal_ts_map_unary_fcn(internal_all, try_converting_to_ts(ts).dict))


# Internal, static version of All
# Output: Value
def internal_all(a_in: Value):
    a = try_converting_to_val(a_in)

    if a.is_stub or a.is_null:
        return a
    elif list_any_false(a.value):
        return Value(False)
    elif list_contains_stub(a.value):
        return Stub
    elif list_contains_null(a.value):
        return Null
    else:
        return Value(list_all_true(a.value))


# Returns True if any element in a list meets a Boolean test f
def Exists(f, a):
    return Any(Map(f, a))


# Returns True if all elements in a list meet a Boolean test f
def ForAll(f, a):
    return All(Map(f, a))


# Returns the minimum of the values in a list
# Output: TimeSeries
def Min(tss: list):
    return TimeSeries(internal_ts_map_unary_fcn(internal_min, normalize_list_of_ts(tss).dict))
    # return TimeSeries(internal_ts_map_unary_fcn(internal_min, try_converting_to_ts(ts).dict))


# Internal, static version of the Min function
# Output: Value
def internal_min(a_in):
    return internal_list_fcn(min, a_in)


# Returns the maximum of the values in a list
# Output: TimeSeries
def Max(ts):
    return TimeSeries(internal_ts_map_unary_fcn(internal_max, try_converting_to_ts(ts).dict))


# Internal, static version of the Max function
# Output: Value
def internal_max(a_in):
    return internal_list_fcn(max, a_in)


# Returns the length of a list
# Output: TimeSeries
def Len(ts):
    return TimeSeries(internal_ts_map_unary_fcn(internal_len, try_converting_to_ts(ts).dict))


# Internal, static version of the Len function
# Output: Value
def internal_len(a_in):
    return internal_list_fcn(len, a_in)


# Returns the sum of a list of numbers
# Output: TimeSeries
def Sum(ts):
    return TimeSeries(internal_ts_map_unary_fcn(internal_sum, try_converting_to_ts(ts).dict))


# Internal, static version of the Sum function
# Output: Value
def internal_sum(a_in):
    return internal_list_fcn(sum, a_in)


# Applies a list function to a Value object that is assumed to contain a list
# Output: Value
def internal_list_fcn(f, a_in):
    a = try_converting_to_val(a_in)

    if a.is_stub or a.is_null:
        return a
    elif list_contains_stub(a.value):
        return Stub
    elif list_contains_null(a.value):
        return Null
    else:
        return Value(f(a.value))


# SUPPORTING FUNCTIONS


# Does a list contain Null?
def list_contains_null(a: list):
    for x in a:
        if try_converting_to_val(x).is_null:
            return True
    return False


# Does a list contain Stub?
def list_contains_stub(a: list):
    for x in a:
        if try_converting_to_val(x).is_stub:
            return True
    return False


# Does a list contain any True elements?
def list_any_true(a: list):
    for x in a:
        if try_converting_to_val(x).value is True:
            return True
    return False


# Does a list contain a False?
def list_any_false(a: list):
    for x in a:
        if try_converting_to_val(x).value is False:
            return True
    return False


# Does a list contain a True?
def list_all_true(a: list):
    for x in a:
        if try_converting_to_val(x).value is not True:
            return False
    return True
