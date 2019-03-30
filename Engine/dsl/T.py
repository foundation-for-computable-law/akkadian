import functools
import operator
import traces


# TEMPORAL SUBSTRATE


# Lays the foundation for time series processing
# Much of the heavy lifting is done by the "traces" Python module
# Most of the functions below serve as wrappers to that module


# Time-related constants
DawnOfTime = '1900-01-01'
AssessmentStart = '2018-01-01'
AssessmentEnd = '2020-12-31'


# Apply a binary function to the values in two time series
def apply_binary_ts_fcn(f, ts1, ts2):
    return ts_trim(ts1.operation(ts2, lambda x, y: f(x, y)))


# Apply a unary function to the values in a time series
def apply_unary_ts_fcn(f, ts):
    return ts_trim(ts.operation(ts, lambda x, y: f(x)))


# Instantiate a new time series, given a list of date-value pairs
# Reduces eternal time series to simple T objects
def TS(pairs):
    ts = ts_trim(traces.TimeSeries(pairs))
    if is_eternal_ts(ts):
        return T(pairs[DawnOfTime])
    else:
        return T(ts)


# Does a time series start at the dawn of time and have the same value forever?
def is_eternal_ts(ts: traces.TimeSeries):
    return ts.n_measurements() == 1 and ts.first_key() == DawnOfTime


# Removes redundant intervals from a time series
# Adapted from the "traces" module's compact() function
def ts_trim(a: traces.TimeSeries):
    previous_value = object()
    redundant = []
    for time, value in a:
        if should_be_merged(value, previous_value):
            redundant.append(time)
        previous_value = value
    for time in redundant:
        del a[time]
    return a


# Determines whether a time series entry is redundant
def should_be_merged(a, b):
    if is_stub(a) and is_stub(b):
        return True
    elif is_none(a) and is_none(b):
        return True
    elif is_scalar(a) and is_scalar(b):
        return a == b
    else:
        return False


# Have any None values in the time series been eradicated?
def ts_is_known(ts: traces.TimeSeries):
    # Returns False when the time series has a None value, True otherwise
    return ts.exists()


# T OBJECTS


class T:
    def __init__(self, value, cf=1):

        # Substantive content of the object
        self.value = value

        # Certainty factor
        self.cf = cf

        # Time series indicator
        if type(value) is traces.timeseries.TimeSeries:
            self.ts = True
        else:
            self.ts = False

    # Arithmetic...
    def __add__(self, o):
        return process_binary(operator.add, self, o)

    def __radd__(self, o):
        return process_binary(operator.add, self, o)

    def __mul__(self, o):
        return process_binary(operator.mul, self, o)

    def __rmul__(self, o):
        return process_binary(operator.mul, self, o)

    def __sub__(self, o):
        return process_binary(operator.sub, self, o)

    def __rsub__(self, o):
        return process_binary(operator.sub, o, self)

    def __truediv__(self, o):
        return process_binary(operator.truediv, self, o)

    def __rtruediv__(self, o):
        return process_binary(operator.truediv, o, self)

    # Comparison...
    def __lt__(self, o):
        return process_binary(operator.lt, self, o)

    def __le__(self, o):
        return process_binary(operator.le, self, o)

    def __eq__(self, o):
        # Hacking equality == playing with fire
        return process_binary(operator.eq, self, o)

    def __ne__(self, o):
        return Not((self == o))

    def __gt__(self, o):
        return process_binary(operator.gt, self, o)

    def __ge__(self, o):
        return process_binary(operator.ge, self, o)

    # TODO: Add list operators


# Internal processing of most binary operators
# TODO: Catch uncertainty within assessment range for time series
def process_binary(f, a_in, b_in):

    # Extract the values and CFs
    a = get_val(a_in)
    b = get_val(b_in)
    cfa = get_cf(a_in)
    cfb = get_cf(b_in)

    # Short-circuit for multiplication by 0
    if f is operator.mul and (a is 0 or b is 0):
        if a is 0 and b is 0:
            return T(0, max(cfa, cfb))
        elif a is 0:
            return T(0, cfa)
        else:
            return T(0, cfb)

    # Otherwise, compute the result, based on the object types
    elif a is StubVal and b is StubVal:
        return Stub(max(cfa, cfb))
    elif a is StubVal:
        return Stub(cfa)
    elif b is StubVal:
        return Stub(cfb)
    elif a is None and b is None:
        return T(None, max(cfa, cfb))
    elif a is None:
        return T(None, cfa)
    elif b is None:
        return T(None, cfb)
    elif is_timeseries(a) and is_timeseries(b):
        return T(apply_binary_ts_fcn(lambda x, y: process_binary(f, x, y), a, b), 1) # TODO: CF?
    elif is_timeseries(a):
        return T(apply_binary_ts_fcn(f, a, traces.TimeSeries({DawnOfTime: b})), 1) # TODO: CF?
    elif is_timeseries(b):
        return T(apply_binary_ts_fcn(f, traces.TimeSeries({DawnOfTime: a}), b), 1) # TODO: CF?
    else:
        return T(f(a, b), min(cfa, cfb))


# STUBS


# Global variable representing a rule stub
def Stub(cf=1):
    return T(StubVal, cf)


# Used internally to indicate that a T object is a stub
StubVal = "#stub#"


# LOGIC


def And(*args):
    return functools.reduce(internal_and, args)


def Or(*args):
    return functools.reduce(internal_or, args)


def Not(a):
    if is_none(a) or is_stub(a):
        return a
    elif is_ts_T(a):
        return T(apply_unary_ts_fcn(Not, a.value), get_cf(a))
    else:
        return T(not get_val(a), get_cf(a))


# DISPLAY


# Display a T object as a comprehensible string
def Pretty(a):
    if is_ts_T(a):
        return apply_unary_ts_fcn(Pretty, a.value)
    else:
        return str("Stub" if is_stub(a) else get_val(a)) + " (" + str(round(get_cf(a) * 100)) + "% certain)"


# *******************************************************
# INTERNAL METHODS
# TODO: Make the methods below private, if possible
# *******************************************************


# VALUES AND CFs


# Gets the certainty factor of a T object or scalar
def get_cf(a):
    if type(a) is T:
        return a.cf
    else:
        return 1


# Gets the value of a T object or scalar
def get_val(a):
    if type(a) is T:
        return a.value
    else:
        return a


def internal_and(a, b):
    return more_internal_and(get_val(a), get_val(b), get_cf(a), get_cf(b))


# Boolean AND logic
# None of the inputs are T objects
def more_internal_and(a, b, cfa, cfb):
    if a is False and b is False:
        return T(False, max(cfa, cfb))
    elif a is False:
        return T(False, cfa)
    elif b is False:
        return T(False, cfb)
    elif a is True and b is True:
        return T(True, min(cfa, cfb))
    elif a is True:
        return T(b, cfb)
    elif b is True:
        return T(a, cfa)
    elif is_timeseries(a) or is_timeseries(b):
        return T(apply_binary_ts_fcn(And, get_val(a), get_val(b)), 1) # TODO: CF?
    elif a is None and b is None:
        return T(None, max(cfa, cfb))
    elif a is None:
        return T(None, cfa)
    elif b is None:
        return T(None, cfb)
    else:
        return T(Stub(), max(cfa, cfb))


def internal_or(a, b):
    return more_internal_or(get_val(a), get_val(b), get_cf(a), get_cf(b))


# Boolean OR logic
# None of the inputs are T objects
def more_internal_or(a, b, cfa, cfb):
    if a is True and b is True:
        return T(True, max(cfa, cfb))
    elif a is True:
        return T(True, cfa)
    elif b is True:
        return T(True, cfb)
    elif a is False and b is False:
        return T(False, min(cfa, cfb))
    elif a is False:
        return T(b, cfb)
    elif b is False:
        return T(a, cfa)
    elif is_timeseries(a) or is_timeseries(b):
        return T(apply_binary_ts_fcn(Or, get_val(a), get_val(b)), 1) # TODO: CF?
    elif a is None and b is None:
        return T(None, max(cfa, cfb))
    elif a is None:
        return T(None, cfa)
    elif b is None:
        return T(None, cfb)
    else:
        return T(Stub(), max(cfa, cfb))


# CONDITIONALS


# TODO: Allow an arbitrary number of arguments
# TODO: Implement lazy evaluation so args b and c are only invoked as needed
# TODO: Implement certainty factors
def If(a, b, c):
    if is_none(a) or is_stub(a):
        return a
    #if get_val(a) is None:
    #    return T(None, get_cf(a))
    #elif is_stub(a):
    #    return a
    elif get_val(a):
        if type(b) is T:
            return b
        else:
            return T(b)
    else:
        if type(c) is T:
            return c
        else:
            return T(c)


# TYPE TESTING


# Internal function: Detect whether an object is a time series
def is_timeseries(a):
    return type(a) is traces.timeseries.TimeSeries


# Object is a T whose contents is a time series
def is_ts_T(a):
    return type(a) is T and a.ts


# Determines whether an object is a T with a value of None
def is_none(a):
    return (type(a) is T and a.value is None) or a is None


# Determines whether a T object is a stub
def is_stub(a):
    return not is_ts_T(a) and get_val(a) == StubVal


# Determines whether an object is a stub and not a time series
def is_stub_and_not_ts(a):
    return not is_timeseries(a) and get_val(a) == StubVal

# Determines whether an object is a scalar
def is_scalar(a):
    return type(a) is not T and type(a) is not None and not is_timeseries(a)
