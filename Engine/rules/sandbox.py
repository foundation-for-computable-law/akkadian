from dsl import *

from datetime import datetime


# RULES

# Substantive rules


def is_qualifying_relative(a, b):
    return And(age(a) < 18,
               age(b) >= 18,
               gender(b) == 'Female',
               Not(relationship(a, b) == "Child"),
               assessment_date() > '2001-01-01')


def another_rule(p):
    return Or(expedited_app(p),
              hourly_wage(p) < fed_min_wage(),
              assessment_date() > Now,
              age(p) >= 12,
              citizenship(p) == "U.S. Citizen")


# Federal minimum wage for all covered, nonexempt workers
# Source: https://www.dol.gov/whd/minwage/chart.htm
def fed_min_wage():
    return TS({DawnOfTime: Stub(),
               '1997-09-01': 5.15,
               '2007-07-24': 5.85,
               '2008-07-24': 6.55,
               '2009-07-24': 7.25})

# FACTS

def age(p):
    return In("num", "age", p, None, "How old is {0}?")


def gender(p):
    return In("str", "gender", p, None, "What is {0}'s gender?")


def relationship(a, b):
    return In("str", "relationship", a, b, "How is {0} related to {1}?")


def citizenship(p):
    return In("str", "citizenship", p, None, "What is {0}'s U.S. citizenship status?")


def assessment_date():
    return In("date", "assessment_date", None, None, "What is the assessment date?")


def expedited_app(p):
    return In("bool", "expedited_app", p, None, "Does {0} require an expedited application?")


def hourly_wage(p):
    return In("num", "hourly_wage", p, None, "How much is {0} paid per hour?")

# USAGE


# Getting the value of a fact
# fact("gender","jim").value
# fact("relationship","jim","jane").value

# Invoking rules
# is_qualifying_relative("jim","jane").value

# Apply the rules to a fact pattern
# print(Apply_rules(['sandbox.is_qualifying_relative("Jim","Lucy")','sandbox.another_rule("Lucy")']))

# Initiate an interactive interview
# Investigate(['sandbox.is_qualifying_relative("Jim","Lucy")'],[Fact("assessment_date", None, None, Date(1999,1,1))])
# Investigate(['sandbox.is_qualifying_relative("Jim","Lucy")'])
# Investigate(['sandbox.another_rule("Neela")'])


# result = DateRange(start='2020-01-01', end='2022-01-01', periods=5)



# def TimeSeriesMergeArgs(*args):
#     return traces.TimeSeries.merge([a.value for a in args])


# ts1 = TS({DawnOfTime: 0, Now: 6})
# ts2 = TS({DawnOfTime: 5, '2001-02-03': 13, '2019-04-19': 38, '2020-04-19': 38})
# ts3 = TS({DawnOfTime: 5, '2000-02-03': 3, '2019-07-09': 50, '2021-04-19': 138})

ts1 = TS({DawnOfTime: False, Now: True})
ts2 = TS({DawnOfTime: False, '2001-02-03': True, '2019-04-19': False, '2020-04-19': True})
ts3 = TS({DawnOfTime: False, '2000-02-03': True, '2019-07-09': False, '2021-04-19': True})

tsnum1 = TS({DawnOfTime: 4, '2020-01-01': 8, '2021-01-01': None})
tsnum2 = TS({DawnOfTime: 24, '2023-01-01': 3, '2024-01-01': Stub()})


thrd = time_series_thread(ts1, ts2, ts3)

# y = apply_unary_ts_fcn(lambda x: V(x), thrd)

# y = V(apply_unary_ts_fcn(Any, thrd))


y = process_unary(Any, thrd)

time_series_thread(tsnum1, tsnum2)

x = str(Pretty(TS({'1900-01-01': [4, 24],
                                    '2020-01-01': [8, 24],
                                    '2021-01-01': [None, 25],
                                    '2023-01-01': [None, 3]})))

print(Pretty(
    # TimeSeriesMerge(ts1, ts2, ts3)
    # TimeSeriesMap(max, TimeSeriesMerge([ts1, ts2, ts3]))
    # TimeSeriesMergeMap(len, ts1, ts2, ts3)
    # TimeSeriesMap(lambda x: x*8, ts3)

    time_series_thread(tsnum1, tsnum2)

))

print(str(Pretty(TS({'1900-01-01': [4, 24],
                                    '2020-01-01': [8, 24],
                                    '2021-01-01': [None, 25],
                                    '2023-01-01': [None, 3]}))))

print(type(x))
