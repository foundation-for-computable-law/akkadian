from dsl.basic import *
from dsl.helpers import *
from dsl.Value import *


# The dawn of time
Dawn = '0001-01-01'
AssessmentStart = '2018-01-01'
AssessmentEnd = '2020-12-31'

# Internal representation of a time series
# Dates are ordinals (integers representing the day)
# Values are Value objects
# ts1 = {
#     1: Value(8234),
#     234: Value(921),
#     1351: Value(44)
# }


# Internal representation of the data
# Not instantiated directly by users
class TimeSeries:
    def __init__(self, contents):

        # Dictionary of the time series data
        if type(contents) is dict:

            # Add a Null entry for the dawn of time, if that entry is missing
            if 1 not in contents:
                d = contents
                d.update({1: Null})
                self.dict = internal_ts_sort(d)

            # Otherwise, take the dictionary as it is
            else:
                self.dict = contents
        else:
            self.dict = {1: contents}

    # Arithmetic...
    def __add__(self, o):
        return process_binary_ts(internal_add, self, o)

    def __radd__(self, o):
        return process_binary_ts(internal_add, self, o)

    def __sub__(self, o):
        return process_binary_ts(internal_sub, self, o)

    def __rsub__(self, o):
        return process_binary_ts(internal_sub, o, self)

    def __mul__(self, o):
        return process_binary_ts(internal_mul, self, o)

    def __rmul__(self, o):
        return process_binary_ts(internal_mul, self, o)

    def __truediv__(self, o):
        return process_binary_ts(internal_div, self, o)

    def __rtruediv__(self, o):
        return process_binary_ts(internal_div, o, self)

    # Comparison...
    def __lt__(self, o):
        return process_binary_ts(internal_lt, self, o)

    def __le__(self, o):
        return process_binary_ts(internal_lt, self, o)

    def __eq__(self, o):
        # Hacking equality == playing with fire
        return process_binary_ts(internal_eq, self, o)

    def __ne__(self, o):
        return Not((self == o))

    def __gt__(self, o):
        return process_binary_ts(internal_gt, self, o)

    def __ge__(self, o):
        return process_binary_ts(internal_ge, self, o)


# Get the value of a time series on a given day
# Output: Value
def internal_asof(dt: int, ts: dict):
    last = 0
    for key, value in ts.items():
        if dt >= last and dt < key:
            return ts[last]
        else:
            last = key
    return ts[list(ts)[-1]]


# Merge two time series together
# Output: dictionary
def internal_ts_thread(ts1: dict, ts2: dict):
    new_keys = list(set(list(ts1.keys()) + list(ts2.keys())))
    return {x: [internal_asof(x, ts1), internal_asof(x, ts2)] for x in new_keys}


# Map a unary function to the values of a time series dictionary
# Output: dictionary
def internal_ts_map_unary_fcn(f, ts: dict):
    vals = [f(x) for x in ts.values()]
    return internal_ts_from_keys_vals(ts.keys(), vals)


# Map a binary function to the values of a time series dictionary
# Output: dictionary
def internal_ts_map_binary_fcn(f, ts: dict):
    vals = [f(x, y) for [x, y] in ts.values()]
    return internal_ts_from_keys_vals(ts.keys(), vals)


# Apply a binary function to two TimeSeries objects
# Output: TimeSeries
def process_binary_ts(f, ts1: TimeSeries, ts2: TimeSeries):
    t1 = try_converting_to_ts(ts1).dict
    t2 = try_converting_to_ts(ts2).dict
    pairs = internal_ts_sort(internal_ts_thread(t1, t2))
    return TimeSeries(internal_ts_trim(internal_ts_map_binary_fcn(f, pairs)))


# Remove redundant intervals
# Output: dictionary
def internal_ts_trim(ts: dict):
    previous_value = Value(-1)
    redundant = []
    for time, value in ts.items():
        if internal_should_be_merged(value, previous_value):
            redundant.append(time)
        previous_value = value
    for time in redundant:
        del ts[time]
    return ts


# Determines whether a time series entry is redundant
# Output: Boolean
def internal_should_be_merged(a: Value, b: Value):
    return values_are_equivalent(a, b)


# Sort the time series dictionary by its (integer) keys
# Output: dictionary
def internal_ts_sort(ts: dict):
    return {x: ts[x] for x in sorted(ts.keys())}


# Build a time series dictionary from lists of keys and values
# Output: dictionary
def internal_ts_from_keys_vals(keys: list, values: list):
    return dict(zip(keys, values))


# If item is a Value object, return it; otherwise convert it to a Value object
# Output: TimeSeries
def try_converting_to_ts(a):
    if isinstance(a, TimeSeries):
        return a
    else:
        return TimeSeries(a)


# INSTANTIATE A TIME SERIES


# Public constructor of a legal TimeSeries
# Converts string dates to ordinal dates, and scalars to Value objects
# Output: TimeSeries
def TS(dct: dict):
    return TimeSeries(internal_ts_trim({str_date_to_ordinal(x[0]): try_converting_to_val(x[1]) for x in dct.items()}))


# DISPLAYING TIME SERIES


# Generates a string that explains what's in the TimeSeries object
# Output: string
def Pretty(ts: TimeSeries):
    if len(ts.dict) == 1:
        return list(ts.dict.values())[0].pretty()
    else:
        s = '<TimeSeries>\n'
        for k, v in ts.dict.items():
            s += " " + ordinal_to_str_date(k) + ": " + v.pretty() + "\n"
        return s + '</TimeSeries>'
