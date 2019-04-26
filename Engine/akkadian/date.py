from akkadian.temporal import *


# Construct a date
def Date(y_in, m_in, d_in):
    y = try_converting_to_ts(y_in)
    m = try_converting_to_ts(m_in)
    d = try_converting_to_ts(d_in)

    return TimeSeries(internal_ts_map_unary_fcn(_internal_date, internal_ts_thread_multi([y.dict, m.dict, d.dict])))


# The input is assumed to be a Value object that contains a list of Values
def _internal_date(dt: Value):
    y = try_converting_to_val(dt.value[0])
    m = try_converting_to_val(dt.value[1])
    d = try_converting_to_val(dt.value[2])

    if y.is_stub or m.is_stub or d.is_stub:
        return Stub
    elif y.is_null or m.is_null or d.is_null:
        return Null
    else:
        cf = min(y.cf, m.cf, d.cf)
        return Value(str(y.value) + "-" + str(m.value).zfill(2) + "-" + str(d.value).zfill(2), cf=cf)


# Returns the current date
Now = date.today().isoformat()
