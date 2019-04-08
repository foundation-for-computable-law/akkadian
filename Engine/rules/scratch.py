from dsl import *



# ts1 = TS2({'0001-01-01': Null,
#           '2000-01-02': Value(False, cf=.83),
#           '2010-04-02': False})
#
#
# ts2 = TS2({'0001-01-01': Null,
#           '1999-01-02': True,
#           '2005-04-02': False})
#
#
#
# print(type({'0001-01-01': Null,
#           '1999-01-02': True,
#           '2005-04-02': False}))



# result = Or2(ts1, ts2)

# print(result)

# print(Pretty(
#     result
# ))
#
# print(
# Pretty(TimeSeries(internal_ts_trim({1: Value("a"), 234: Value("b"), 1351: Value("c")})))
# # Pretty(TimeSeries({1: Value("a"), 234: Value("b"), 1351: Value("c")}))
# )

r = EffectiveBetween(Now, '2050-02-03')

print(Pretty(r))