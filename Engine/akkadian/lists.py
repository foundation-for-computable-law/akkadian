from akkadian.TimeSeries import *
from akkadian.temporal import *
from akkadian.Value import *


# TODO: Refactor and simplify these functions


# LIST FUNCTIONS


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


# Internal, static version of the Min function
# Output: Value
def internal_min(a_in):
    return internal_list_fcn(min, a_in)


# Returns the maximum of the values in a list
# Output: TimeSeries
def Max(tss: list):
    return TimeSeries(internal_ts_map_unary_fcn(internal_max, normalize_list_of_ts(tss).dict))


# Internal, static version of the Max function
# Output: Value
def internal_max(a_in):
    return internal_list_fcn(max, a_in)


# Returns the length of a list
# Output: TimeSeries
def Len(tss: list):
    return TimeSeries(internal_ts_map_unary_fcn(internal_len, normalize_list_of_ts(tss).dict))

# Internal, static version of the Len function
# Output: Value
def internal_len(a_in):
    return internal_list_fcn(len, a_in)


# Returns the sum of a list of numbers
# Output: TimeSeries
def Sum(tss: list):
    return TimeSeries(internal_ts_map_unary_fcn(internal_sum, normalize_list_of_ts(tss).dict))


# Internal, static version of the Sum function
# Output: Value
def internal_sum(a_in):
    return internal_list_fcn(sum, a_in)


# SET FUNCTIONS


# Returns the intersection of two lists
# Output: TimeSeries
def Intersection(tss1: list, tss2: list):
    return process_binary_ts(internal_intersection,
                             normalize_list_of_ts(tss1),
                             normalize_list_of_ts(tss2))


# Internal, static version of Intersection
# It is assumed that each Value.value is a list
# Output: Value
def internal_intersection(a: Value, b: Value):
    return internal_two_list_operation_on_vals(_list_intersection, a, b)


# Scalar intersection function
# Output: list
def _list_intersection(a: list, b: list):
    return list(set(a).intersection(set(b)))


# Returns the union of two lists
# Output: TimeSeries
def Union(tss1: list, tss2: list):
    return process_binary_ts(internal_union,
                             normalize_list_of_ts(tss1),
                             normalize_list_of_ts(tss2))


# Internal, static version of Union
# It is assumed that each Value.value is a list
# Output: Value
def internal_union(a: Value, b: Value):
    return internal_two_list_operation_on_vals(_list_union, a, b)


# Scalar union function
# Output: list
def _list_union(a: list, b: list):
    return list(set(a).union(set(b)))


# Indicates whether one list is the subset of another
# Output: TimeSeries
def IsSubsetOf(tss1: list, tss2: list):
    return process_binary_ts(internal_subsetq,
                             normalize_list_of_ts(tss1),
                             normalize_list_of_ts(tss2))


# Internal, static version of subsetq
# It is assumed that each Value.value is a list
# Output: Value
def internal_subsetq(a: Value, b: Value):
    return internal_two_list_operation_on_vals(_list_subsetq, a, b)


# Scalar union function
# Output: list
def _list_subsetq(a: list, b: list):
    return set(a).issubset(set(b))


# Returns the complement of two lists (the first set - the second set)
# Output: TimeSeries
def Complement(tss1: list, tss2: list):
    return process_binary_ts(internal_complement,
                             normalize_list_of_ts(tss1),
                             normalize_list_of_ts(tss2))


# Internal, static version of Complement
# It is assumed that each Value.value is a list
# Output: Value
def internal_complement(a: Value, b: Value):
    return internal_two_list_operation_on_vals(_list_complement, a, b)


# Scalar complement function
# Output: list
def _list_complement(a: list, b: list):
    return list(set(a).difference(set(b)))


# Indicates whether an item is a member of a list
def IsIn(item, lst):
    return IsSubsetOf([item], lst)


# Indicates whether an item is not a member of a list
def IsNotIn(item, lst):
    return Not(IsIn(item, lst))


# Indicates whether two lists have any elements in common
def IntersectionQ(tss1: list, tss2: list):
    return Len(Intersection(tss1, tss2)) > 0



# SUPPORTING FUNCTIONS


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
        return Value(f([try_converting_to_val(x).value for x in a.value]))


# Applies a function f to two Value objects, each of which contains a list
def internal_two_list_operation_on_vals(f, a: Value, b: Value):
    if a.is_stub or b.is_stub:
        return Stub
    elif a.is_null or b.is_null:
        return Null
    else:
        alist = list_of_values_to_list(a)
        blist = list_of_values_to_list(b)
        if list_contains_stub(a.value) or list_contains_stub(b.value):
            return Stub
        elif list_contains_null(a.value) or list_contains_null(b.value):
            return Null
        else:
            return Value(f(alist, blist))


# Input: A Value object containing a list of Value objects
# Output: A list of scalars
def list_of_values_to_list(a: Value):
    return [try_getting_value(x) for x in a.value]


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
