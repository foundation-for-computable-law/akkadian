from datetime import date, timedelta

import pandas as pd

from dsl.V import *


# Determine the date n dates from a given date
# TODO: Make temporal; handle uncertainty
def AddDays(d, n):
    return (date.fromisoformat(d) + timedelta(days=n)).isoformat()


# CREATING BOOLEAN TIME SERIES


# Boolean time series that's true starting on a given date, and otherwise false
def EffectiveFrom(dt):
    return TS({DawnOfTime: False, dt: True})


# Boolean time series that's true up until a given date, and otherwise false
def EffectiveUntil(dt):
    return TS({DawnOfTime: True, AddDays(dt, 1): False})


# Boolean time series that's true between two dates, and otherwise false
def EffectiveBetween(start, end):
    return And(EffectiveFrom(start), EffectiveUntil(end))


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
