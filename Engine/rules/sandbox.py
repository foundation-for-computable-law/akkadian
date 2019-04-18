from akkadian import *


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
    return TS({Dawn: Stub,
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
# Fact("gender", "jim").value
# Fact("relationship", "jim", "jane").value

# Invoking rules
# Pretty(is_qualifying_relative("jim", "jane"))

# Apply the rules to a fact pattern
# print(ApplyRules([(is_qualifying_relative, "Jim", "Lucy"), (another_rule, "Lucy")]))

# Initiate an interactive interview
# Investigate([(is_qualifying_relative, "Jim", "Lucy")],[Fact("assessment_date", None, None, '2020-02-02')])
# Investigate([(is_qualifying_relative, "Jim", "Lucy")])
# Investigate([(another_rule, "Neela")])


# Assumes(['spouse_of', 1, 2], ['family_relationship', 1, 2, "Spouse"])


# result = DateRange(start='2020-01-01', end='2022-01-01', periods=5)

# print(Pretty(
#     TS({Dawn: 32, ToScalar(Now): 44})
# ))

# Get the value of a time series on a given day
# Output: Value
# def internal_asof(dt: int, ts: dict):
#     last = 0
#     for key, value in ts.items():
#         if dt >= last and dt < key:
#             return ts[last]
#         else:
#             last = key
#     return ts[list(ts)[-1]]




def _asof_values(x: Value, y: Value):
    return process_binary_val(f, x, y)

def f(a, b):
    return [a,b]


ts = TS({Dawn: "a", '2002-02-02': "c"})
dt = Now

print(Pretty(
    process_binary_ts(_asof_values, ts, dt)
))

print(ToScalar(process_binary_ts(_asof_values, ts, dt)))
