import unittest

from dsl import *


class TestDSL(unittest.TestCase):

    def test_and(self):
        self.assertEqual(And(T(True), T(False)).value, False)
        self.assertEqual(And(T(True), T(True)).value, True)
        self.assertEqual(And(T(False), T(False)).value, False)
        self.assertEqual(And(T(False), T(True)).value, False)
        self.assertEqual(And(T(None), T(True)).value, None)
        self.assertEqual(And(T(None), T(False)).value, False)
        self.assertEqual(And(T(False), T(None)).value, False)
        self.assertEqual(And(T(None), T(False)).value, False)
        self.assertEqual(And(T(True), T(None)).value, None)
        self.assertEqual(And(T(None), T(None)).value, None)
        self.assertEqual(And(T(True), True).value, True)
        self.assertEqual(And(True, T(True)).value, True)
        self.assertEqual(And(False, T(True)).value, False)
        self.assertEqual(And(False, T(None)).value, False)
        self.assertEqual(And(False, T(None), True).value, False)
        self.assertEqual(And(False, "anything", True).value, False)
        self.assertEqual(And(Stub(), T(True)).value, StubVal)
        self.assertEqual(And(T(True), Stub()).value, StubVal)
        self.assertEqual(And(Stub(), T(False)).value, False)
        self.assertEqual(And(T(False), Stub()).value, False)
        self.assertEqual(And(Stub(), T(None)).value, None)
        self.assertEqual(And(T(None), Stub()).value, None)

    def test_or(self):
        self.assertEqual(Or(T(True), T(False)).value, True)
        self.assertEqual(Or(T(True), T(True)).value, True)
        self.assertEqual(Or(T(False), T(False)).value, False)
        self.assertEqual(Or(T(False), T(True)).value, True)
        self.assertEqual(Or(T(None), T(True)).value, True)
        self.assertEqual(Or(T(None), T(False)).value, None)
        self.assertEqual(Or(T(False), T(None)).value, None)
        self.assertEqual(Or(T(True), T(None)).value, True)
        self.assertEqual(Or(T(None), T(None)).value, None)
        self.assertEqual(Or(True, T(True)).value, True)
        self.assertEqual(Or(False, T(True)).value, True)
        self.assertEqual(Or(False, T(None)).value, None)
        self.assertEqual(Or(True, T(None)).value, True)
        self.assertEqual(Or(True, T(False)).value, True)
        self.assertEqual(Or(Stub(), T(True)).value, True)
        self.assertEqual(Or(T(True), Stub()).value, True)
        self.assertEqual(Or(Stub(), T(False)).value, StubVal)
        self.assertEqual(Or(T(False), Stub()).value, StubVal)
        self.assertEqual(Or(Stub(), T(None)).value, None)
        self.assertEqual(Or(T(None), Stub()).value, None)

    def test_not(self):
        self.assertEqual(Not(T(True)).value, False)
        self.assertEqual(Not(T(False)).value, True)
        self.assertEqual(Not(T(None)).value, None)
        self.assertEqual(Not(True).value, False)
        self.assertEqual(Not(False).value, True)
        self.assertEqual(Not(Stub()).value, StubVal)

    def test_ge(self):
        self.assertEqual((T(99) >= T(70)).value, True)
        self.assertEqual((T(70) >= T(70)).value, True)
        self.assertEqual((T(99) >= T(170)).value, False)
        self.assertEqual((T(99.023) >= T(170)).value, False)
        self.assertEqual((T(99) >= 70).value, True)
        self.assertEqual((354 >= T(70)).value, True)
        self.assertEqual((354 >= T(670)).value, False)
        self.assertEqual((354 >= T(None)).value, None)
        self.assertEqual((T(None) >= 34).value, None)
        self.assertEqual((T(None) >= T(None)).value, None)
        self.assertEqual((Stub() >= T(None)).value, StubVal)
        self.assertEqual((T(None) >= Stub()).value, StubVal)
        self.assertEqual((Stub() >= 34).value, StubVal)
        self.assertEqual((44 >= Stub()).value, StubVal)

    def test_gt(self):
        self.assertEqual((T(99) > T(70)).value, True)
        self.assertEqual((T(70) > T(70)).value, False)
        self.assertEqual((T(99) > T(170)).value, False)
        self.assertEqual((T(99.023) > T(170)).value, False)
        self.assertEqual((T(99) > 70).value, True)
        self.assertEqual((354 > T(70)).value, True)
        self.assertEqual((354 > T(670)).value, False)
        self.assertEqual((354 > T(None)).value, None)
        self.assertEqual((T(None) > 34).value, None)
        self.assertEqual((T(None) > T(None)).value, None)
        self.assertEqual((T('2000-01-01') > T('1999-02-02')).value, True)
        self.assertEqual((T('2000-01-01') > T('2010-02-02')).value, False)
        self.assertEqual(('2000-01-01' > T('1999-02-02')).value, True)
        self.assertEqual(('2000-01-01' > T('2010-02-02')).value, False)
        self.assertEqual((T('2000-01-01') > '1999-02-02').value, True)
        self.assertEqual((T('2000-01-01') > '2010-02-02').value, False)

    def test_le(self):
        self.assertEqual((T(99) <= T(70)).value, False)
        self.assertEqual((T(70) <= T(70)).value, True)
        self.assertEqual((T(99) <= T(170)).value, True)
        self.assertEqual((T(99.023) <= T(170)).value, True)
        self.assertEqual((T(99) <= 70).value, False)
        self.assertEqual((354 <= T(70)).value, False)
        self.assertEqual((354 <= T(670)).value, True)
        self.assertEqual((354 <= T(None)).value, None)
        self.assertEqual((T(None) <= 34).value, None)
        self.assertEqual((T(None) <= T(None)).value, None)

    def test_lt(self):
        self.assertEqual((T(99) < T(70)).value, False)
        self.assertEqual((T(70) < T(70)).value, False)
        self.assertEqual((T(99) < T(170)).value, True)
        self.assertEqual((T(99.023) < T(170)).value, True)
        self.assertEqual((T(99) < 70).value, False)
        self.assertEqual((354 < T(70)).value, False)
        self.assertEqual((354 < T(670)).value, True)
        self.assertEqual((354 < T(None)).value, None)
        self.assertEqual((T(None) < 34).value, None)
        self.assertEqual((T(None) < T(None)).value, None)

    def test_eq(self):
        self.assertEqual((T(99) == T(70)).value, False)
        self.assertEqual((T(70) == T(70)).value, True)
        self.assertEqual((T(99) == 70).value, False)
        self.assertEqual((354 == T(70)).value, False)
        self.assertEqual((354 == T(354)).value, True)
        self.assertEqual((354 == T(None)).value, None)
        self.assertEqual((T(None) == 34).value, None)
        self.assertEqual((T(None) == T(None)).value, None)
        self.assertEqual((T("hello") == T("hello")).value, True)
        self.assertEqual((T("hello") == T("meow")).value, False)
        self.assertEqual((T(None) == T("meow")).value, None)
        self.assertEqual((T("hello") == T(None)).value, None)
        self.assertEqual(("hello" == T(None)).value, None)
        self.assertEqual(("hello" == T("hello")).value, True)

    def test_ne(self):
        self.assertEqual((T(99) != T(70)).value, True)
        self.assertEqual((T(70) != T(70)).value, False)
        self.assertEqual((T(99) != 70).value, True)
        self.assertEqual((354 != T(70)).value, True)
        self.assertEqual((354 != T(354)).value, False)
        self.assertEqual((354 != T(None)).value, None)
        self.assertEqual((T(None) != 34).value, None)
        self.assertEqual((T(None) != T(None)).value, None)
        self.assertEqual((T("hello") != T("hello")).value, False)
        self.assertEqual((T("hello") != T("meow")).value, True)
        self.assertEqual((T(None) != T("meow")).value, None)
        self.assertEqual((T("hello") != T(None)).value, None)

    def test_is_none(self):
        self.assertEqual(is_none(9), False)
        self.assertEqual(is_none(T(9)), False)
        self.assertEqual(is_none(T(True)), False)
        self.assertEqual(is_none(T(None)), True)
        self.assertEqual(is_none(Stub()), False)

    def test_add(self):
        self.assertEqual((T(5) + T(7)).value, 12)
        self.assertEqual((T(4) + T(-9)).value, -5)
        self.assertEqual((T(99) + 70).value, 169)
        self.assertEqual((1 + T(70)).value, 71)
        self.assertEqual((1 + T(354)).value, 355)
        self.assertEqual((1 + T(None)).value, None)
        self.assertEqual((T(None) + 34).value, None)
        self.assertEqual((T(None) + T(None)).value, None)

    def test_mul(self):
        self.assertEqual((T(5) * T(7)).value, 35)
        self.assertEqual((T(4) * T(-9)).value, -36)
        self.assertEqual((T(9) * 7).value, 63)
        self.assertEqual((1 * T(7)).value, 7)
        self.assertEqual((1 * T(34)).value, 34)
        self.assertEqual((1 * T(None)).value, None)
        self.assertEqual((T(None) * 34).value, None)
        self.assertEqual((T(None) * T(None)).value, None)
        self.assertEqual((T(None) * 0).value, 0)
        self.assertEqual((0 * T(None)).value, 0)
        self.assertEqual((Stub() * 0).value, 0)
        self.assertEqual((0 * Stub()).value, 0)
        self.assertEqual((Stub() * 5).value, StubVal)
        self.assertEqual((5 * Stub()).value, StubVal)

    def test_sub(self):
        self.assertEqual((T(5) - T(7)).value, -2)
        self.assertEqual((T(4) - T(-9)).value, 13)
        self.assertEqual((T(9) - 7).value, 2)
        self.assertEqual((1 - T(7)).value, -6) 
        self.assertEqual((1 - T(34)).value, -33)
        self.assertEqual((1 - T(None)).value, None)
        self.assertEqual((T(None) - 34).value, None)
        self.assertEqual((T(None) - T(None)).value, None)

    def test_div(self):
        self.assertEqual((T(6) / T(2)).value, 3)
        self.assertEqual((T(6) / T(-2)).value, -3)
        self.assertEqual((T(9) / 3).value, 3)
        self.assertEqual((12 / T(3)).value, 4) 
        self.assertEqual((12 / T(1)).value, 12)
        self.assertEqual((1 / T(None)).value, None)
        self.assertEqual((T(None) / 34).value, None)
        self.assertEqual((T(None) / T(None)).value, None)

    def test_if(self):
        self.assertEqual(If(T(None), 1, 2).value, None)
        self.assertEqual(If(T(True), 1, 2).value, 1)
        self.assertEqual(If(True, 1, 2).value, 1)
        self.assertEqual(If(T(False), 1, 2).value, 2)
        self.assertEqual(If(False, 1, 2).value, 2)
        self.assertEqual(If(Stub(), 1, 2).value, StubVal)
        self.assertEqual(If(True, Stub(), 2).value, StubVal)

    def test_cf(self):
        self.assertEqual(And(T(True,.84), T(True,.92)).cf, 0.7728)
        self.assertEqual(Or(T(True,.8), T(True,.9)).cf, 0.9800000000000001)
        self.assertEqual((T(9,.5) + T(23,.7)).cf, 0.35)
        self.assertEqual(Not(T(True,.4)).cf, 0.4)

    def test_list_contains_non(self):
        self.assertEqual(list_contains_none([3, T(None), 8]), True)
        self.assertEqual(list_contains_none([3, 4, 8]), False)
        self.assertEqual(list_contains_none([]), False)

    def test_map(self):
        self.assertEqual(Map(lambda x: x * 8, [3, 5, 8]).value, [24, 40, 64])
        self.assertEqual(Map(lambda x: x * 8, T([3, 5, 8])).value, [24, 40, 64])
        self.assertEqual(Map(lambda x: x * 8, T(None)).value, None)
        self.assertEqual(Map(lambda x: x * 8, Stub()).value, StubVal)
        self.assertEqual(Map(lambda x: x * 8, [3, T(None), 8]).value, None)
        self.assertEqual(Map(lambda x: x * 8, T([3, T(None), 8])).value, None)
        self.assertEqual(Map(lambda x: x * 8, Stub()).value, StubVal)

    def test_any(self):
        self.assertEqual(Any([3, 5, 8]).value, False)
        self.assertEqual(Any(T([3, 5, 8])).value, False)
        self.assertEqual(Any(T([3, 5, True])).value, True)
        self.assertEqual(Any(T([3, 5, T(True)])).value, True)
        self.assertEqual(Any([3, 5, T(True)]).value, True)
        self.assertEqual(Any([3, 5, T(False)]).value, False)
        self.assertEqual(Any([3, 5, T(None)]).value, None)
        self.assertEqual(Any(T(None)).value, None)
        self.assertEqual(Any([3, 5, Stub()]).value, StubVal)
        self.assertEqual(Any(Stub()).value, StubVal)
        self.assertEqual(Any([3, True, Stub()]).value, True)
        self.assertEqual(Any([True, Stub()]).value, True)
        self.assertEqual(Any([T(True), Stub()]).value, True)
        self.assertEqual(Any([False, False, True]).value, True)

    def test_all(self):
        self.assertEqual(All([3, 5, 8]).value, False)
        self.assertEqual(All(T([3, 5, 8])).value, False)
        self.assertEqual(All(T([3, 5, True])).value, False)
        self.assertEqual(All(T([3, 5, T(True)])).value, False)
        self.assertEqual(All([3, 5, T(True)]).value, False)
        self.assertEqual(All([3, 5, T(False)]).value, False)
        self.assertEqual(All([T(True), T(True), T(True)]).value, True)
        self.assertEqual(All([T(True), True, T(True)]).value, True)
        self.assertEqual(All([3, 5, Stub()]).value, StubVal)
        self.assertEqual(All(Stub()).value, StubVal)
        self.assertEqual(All([3, False, Stub()]).value, False)
        self.assertEqual(All([False, Stub()]).value, False)
        self.assertEqual(All([T(False), Stub()]).value, False)

    def test_exists(self):
        self.assertEqual(Exists(lambda x: x > 6, T([3, 5, 8])).value, True)
        self.assertEqual(Exists(lambda x: x > 16, T([3, 5, 8])).value, False)

    def test_forall(self):
        self.assertEqual(ForAll(lambda x: x > 6, T([3, 5, 8])).value, False)
        self.assertEqual(ForAll(lambda x: x > 1, T([3, 5, 8])).value, True)

    def test_ts_trim(self):
        self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: False, '2020-01-01': True, '2021-01-01': True})),
                         traces.TimeSeries({DawnOfTime: False, '2020-01-01': True}))
        self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: False, '2020-01-01': Stub(), '2021-01-01': Stub()})),
                         traces.TimeSeries({DawnOfTime: False, '2020-01-01': Stub()}))
        self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: False, '2020-01-01': None, '2021-01-01': None})),
                         traces.TimeSeries({DawnOfTime: False, '2020-01-01': None}))
        self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: 3, '2020-01-01': 4, '2021-01-01': 4.0})),
                         traces.TimeSeries({DawnOfTime: 3, '2020-01-01': 4}))

    # Constructing time series
    def test_ts_construction_1(self):
        self.assertEqual(TrueFrom('2020-01-01').value,
                         TS({DawnOfTime: False, '2020-01-01': True}).value)

    def test_ts_construction_2(self):
        self.assertEqual(TrueUntil('2020-01-01').value,
                         TS({DawnOfTime: True, '2020-01-02': False}).value)

    def test_ts_construction_3(self):
        self.assertEqual(TrueBetween('2020-01-01', '2021-01-01').value,
                         TS({DawnOfTime: False, '2020-01-01': True, '2021-01-02': False}).value)

    def test_ts_construction_4(self):
        self.assertEqual(TS({DawnOfTime: False, '2020-01-01': True, '2021-01-01': True}).value,
                         TS({DawnOfTime: False, '2020-01-01': True}).value)

    # Time series AND
    def test_ts_and_1(self):
        self.assertEqual(And(tsbool1, tsbool2).value,
                         TS({DawnOfTime: False,
                             '2020-01-01': True,
                             '2021-01-01': None,
                             '2023-01-01': False,
                             '2024-01-01': None}).value)

    def test_ts_and_2(self):
        self.assertEqual(Pretty(And(tsbool2, Stub())),
                         Pretty(TS({DawnOfTime: Stub(),
                                    '2023-01-01': False,
                                    '2024-01-01': Stub()})))

    def test_ts_and_3(self):
        self.assertEqual(Pretty(And(tsbool1, Stub())),
                         Pretty(TS({DawnOfTime: False,
                                    '2020-01-01': Stub(),
                                    '2021-01-01': None})))

    def test_ts_and_4(self):
        self.assertEqual(Pretty(And(True,
                                    TS({'1900-01-01': Stub(),
                                        '1997-09-01': False,
                                        '2008-07-24': True}))),
                         Pretty(TS({'1900-01-01': Stub(),
                                    '1997-09-01': False,
                                    '2008-07-24': True})))

    def test_ts_and_5(self):
        self.assertEqual(Pretty(And(False,
                                    TS({'1900-01-01': Stub(),
                                        '1997-09-01': False,
                                        '2008-07-24': True}))),
                         Pretty(T(False)))

    # Time series OR
    def test_ts_or_1(self):
        self.assertEqual(Pretty(Or(tsbool1, tsbool2)),
                         Pretty(TS({DawnOfTime: True,
                                    '2023-01-01': None})))

    def test_ts_or_2(self):
        self.assertEqual(Pretty(Or(tsbool2, Stub())),
                         Pretty(TS({DawnOfTime: True,
                                    '2023-01-01': Stub()})))

    def test_ts_or_3(self):
        self.assertEqual(Pretty(Or(tsbool1, Stub())),
                         Pretty(TS({DawnOfTime: Stub(),
                                    '2020-01-01': True,
                                    '2021-01-01': None})))

    def test_ts_or_4(self):
        self.assertEqual(Pretty(Or(T(False),
                                   TS({'1900-01-01': Stub(),
                                       '1997-09-01': False,
                                       '2008-07-24': True}))),
                         Pretty(TS({'1900-01-01': Stub(),
                                    '1997-09-01': False,
                                    '2008-07-24': True})))

    def test_ts_or_5(self):
        self.assertEqual(Pretty(Or(False,
                                   TS({'1900-01-01': Stub(),
                                       '1997-09-01': False,
                                       '2008-07-24': True}))),
                         Pretty(TS({'1900-01-01': Stub(),
                                    '1997-09-01': False,
                                    '2008-07-24': True})))

    def test_ts_or_6(self):
        self.assertEqual(Pretty(Or(True,
                                   TS({'1900-01-01': Stub(),
                                       '1997-09-01': False,
                                       '2008-07-24': True}))),
                         Pretty(T(True)))

    # Time series NOT
    def test_ts_not_1(self):
        self.assertEqual(Pretty(Not(tsbool1)),
                         Pretty(TS({DawnOfTime: True, '2020-01-01': False, '2021-01-01': None})))

    def test_ts_not_2(self):
        self.assertEqual(Pretty(Not(tsbool2)),
                         Pretty(TS({DawnOfTime: False, '2023-01-01': True, '2024-01-01': Stub()})))

    # Time series addition
    def test_ts_add_1(self):
        self.assertEqual(Pretty(tsnum1 + tsnum2),
                         Pretty(TS({DawnOfTime: 28,
                                    '2020-01-01': 32,
                                    '2021-01-01': None,
                                    '2024-01-01': Stub()})))

    # Time series subtraction
    def test_ts_sub_1(self):
        self.assertEqual(Pretty(tsnum1 - tsnum2),
                         Pretty(TS({DawnOfTime: -20,
                                    '2020-01-01': -16,
                                    '2021-01-01': None,
                                    '2024-01-01': Stub()})))

    # Time series multiplication
    def test_ts_mult_1(self):
        self.assertEqual(Pretty(tsnum1 * tsnum2),
                         Pretty(TS({DawnOfTime: 96,
                                    '2020-01-01': 192,
                                    '2021-01-01': None,
                                    '2024-01-01': Stub()})))

    def test_ts_mult_2(self):
        self.assertEqual(Pretty(tsnum1 * 0),
                         Pretty(T(0)))

    def test_ts_mult_3(self):
        self.assertEqual(Pretty(TS({DawnOfTime: 0, '2020-01-01': 8}) * 5),
                         Pretty(TS({DawnOfTime: 0, '2020-01-01': 40})))

    # Equality of two time series
    def test_ts_eq_1(self):
        self.assertEqual(Pretty(tsnum1 == tsnum2),
                         Pretty(TS({DawnOfTime: False,
                                    '2021-01-01': None,
                                    '2024-01-01': Stub()})))

    def test_ts_eq_2(self):
        self.assertEqual(Pretty(TS({DawnOfTime: 5}) == T(5)),
                         Pretty(T(True)))

    # Time series comparison
    def test_ts_cmp_1(self):
        self.assertEqual(Pretty(TS({DawnOfTime: 4, '2020-01-01': 8}) > 5),
                         Pretty(TS({DawnOfTime: False,
                                    '2020-01-01': True})))


# Used to test time series logic
tsbool1 = TS({DawnOfTime: False, '2020-01-01': True, '2021-01-01': None})
tsbool2 = TS({DawnOfTime: True, '2023-01-01': False, '2024-01-01': Stub()})
tsnum1 = TS({DawnOfTime: 4, '2020-01-01': 8, '2021-01-01': None})
tsnum2 = TS({DawnOfTime: 24, '2023-01-01': 3, '2024-01-01': Stub()})


if __name__ == '__main__':
    unittest.main()
