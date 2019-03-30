import unittest

from dsl import *


class TestDSL(unittest.TestCase):

    # AND

    def test_and_1(self):
        self.assertEqual(And(T(True), T(False)).value, False)

    def test_and_2(self):
        self.assertEqual(And(T(True), T(True)).value, True)

    def test_and_3(self):
        self.assertEqual(And(T(False), T(False)).value, False)

    def test_and_4(self):
        self.assertEqual(And(T(False), T(True)).value, False)

    def test_and_5(self):
        self.assertEqual(And(T(None), T(True)).value, None)

    def test_and_6(self):
        self.assertEqual(And(T(None), T(False)).value, False)

    def test_and_7(self):
        self.assertEqual(And(T(False), T(None)).value, False)

    def test_and_8(self):
        self.assertEqual(And(T(None), T(False)).value, False)

    def test_and_9(self):
        self.assertEqual(And(T(True), T(None)).value, None)

    def test_and_10(self):
        self.assertEqual(And(T(None), T(None)).value, None)

    def test_and_11(self):
        self.assertEqual(And(T(True), True).value, True)

    def test_and_12(self):
        self.assertEqual(And(True, T(True)).value, True)

    def test_and_13(self):
        self.assertEqual(And(False, T(True)).value, False)

    def test_and_14(self):
        self.assertEqual(And(False, T(None)).value, False)

    def test_and_15(self):
        self.assertEqual(And(False, T(None), True).value, False)

    def test_and_16(self):
        self.assertEqual(And(False, "anything", True).value, False)

    def test_and_17(self):
        self.assertEqual(And(Stub(), T(True)).value, StubVal)

    def test_and_18(self):
        self.assertEqual(And(T(True), Stub()).value, StubVal)

    def test_and_19(self):
        self.assertEqual(And(Stub(), T(False)).value, False)

    def test_and_20(self):
        self.assertEqual(And(T(False), Stub()).value, False)

    def test_and_21(self):
        self.assertEqual(And(Stub(), T(None)).value, None)

    def test_and_22(self):
        self.assertEqual(And(T(None), Stub()).value, None)

    # OR

    def test_or_1(self):
        self.assertEqual(Or(T(True), T(False)).value, True)

    def test_or_2(self):
        self.assertEqual(Or(T(True), T(True)).value, True)

    def test_or_3(self):
        self.assertEqual(Or(T(False), T(False)).value, False)

    def test_or_4(self):
        self.assertEqual(Or(T(False), T(True)).value, True)

    def test_or_5(self):
        self.assertEqual(Or(T(None), T(True)).value, True)

    def test_or_6(self):
        self.assertEqual(Or(T(None), T(False)).value, None)

    def test_or_7(self):
        self.assertEqual(Or(T(False), T(None)).value, None)

    def test_or_8(self):
        self.assertEqual(Or(T(True), T(None)).value, True)

    def test_or_9(self):
        self.assertEqual(Or(T(None), T(None)).value, None)

    def test_or_10(self):
        self.assertEqual(Or(True, T(True)).value, True)

    def test_or_11(self):
        self.assertEqual(Or(False, T(True)).value, True)

    def test_or_12(self):
        self.assertEqual(Or(False, T(None)).value, None)

    def test_or_13(self):
        self.assertEqual(Or(True, T(None)).value, True)

    def test_or_14(self):
        self.assertEqual(Or(True, T(False)).value, True)

    def test_or_15(self):
        self.assertEqual(Or(Stub(), T(True)).value, True)

    def test_or_16(self):
        self.assertEqual(Or(T(True), Stub()).value, True)

    def test_or_17(self):
        self.assertEqual(Or(Stub(), T(False)).value, StubVal)

    def test_or_18(self):
        self.assertEqual(Or(T(False), Stub()).value, StubVal)

    def test_or_19(self):
        self.assertEqual(Or(Stub(), T(None)).value, None)

    def test_or_20(self):
        self.assertEqual(Or(T(None), Stub()).value, None)

    # NOT

    def test_not_1(self):
        self.assertEqual(Not(T(True)).value, False)

    def test_not_2(self):
        self.assertEqual(Not(T(False)).value, True)

    def test_not_3(self):
        self.assertEqual(Not(T(None)).value, None)

    def test_not_4(self):
        self.assertEqual(Not(True).value, False)

    def test_not_5(self):
        self.assertEqual(Not(False).value, True)

    def test_not_6(self):
        self.assertEqual(Not(Stub()).value, StubVal)

    # >=

    def test_ge_1(self):
        self.assertEqual((T(99) >= T(70)).value, True)

    def test_ge_2(self):
        self.assertEqual((T(70) >= T(70)).value, True)

    def test_ge_3(self):
        self.assertEqual((T(99) >= T(170)).value, False)

    def test_ge_4(self):
        self.assertEqual((T(99.023) >= T(170)).value, False)

    def test_ge_5(self):
        self.assertEqual((T(99) >= 70).value, True)

    def test_ge_6(self):
        self.assertEqual((354 >= T(70)).value, True)

    def test_ge_7(self):
        self.assertEqual((354 >= T(670)).value, False)

    def test_ge_8(self):
        self.assertEqual((354 >= T(None)).value, None)

    def test_ge_9(self):
        self.assertEqual((T(None) >= 34).value, None)

    def test_ge_10(self):
        self.assertEqual((T(None) >= T(None)).value, None)

    def test_ge_11(self):
        self.assertEqual((Stub() >= T(None)).value, StubVal)

    def test_ge_12(self):
        self.assertEqual((T(None) >= Stub()).value, StubVal)

    def test_ge_13(self):
        self.assertEqual((Stub() >= 34).value, StubVal)

    def test_ge_14(self):
        self.assertEqual((44 >= Stub()).value, StubVal)

    # >

    def test_gt_1(self):
        self.assertEqual((T(99) > T(70)).value, True)

    def test_gt_2(self):
        self.assertEqual((T(70) > T(70)).value, False)

    def test_gt_3(self):
        self.assertEqual((T(99) > T(170)).value, False)

    def test_gt_4(self):
        self.assertEqual((T(99.023) > T(170)).value, False)

    def test_gt_5(self):
        self.assertEqual((T(99) > 70).value, True)

    def test_gt_6(self):
        self.assertEqual((354 > T(70)).value, True)

    def test_gt_7(self):
        self.assertEqual((354 > T(670)).value, False)

    def test_gt_8(self):
        self.assertEqual((354 > T(None)).value, None)

    def test_gt_9(self):
        self.assertEqual((T(None) > 34).value, None)

    def test_gt_10(self):
        self.assertEqual((T(None) > T(None)).value, None)

    def test_gt_11(self):
        self.assertEqual((T('2000-01-01') > T('1999-02-02')).value, True)

    def test_gt_12(self):
        self.assertEqual((T('2000-01-01') > T('2010-02-02')).value, False)

    def test_gt_13(self):
        self.assertEqual(('2000-01-01' > T('1999-02-02')).value, True)

    def test_gt_14(self):
        self.assertEqual(('2000-01-01' > T('2010-02-02')).value, False)

    def test_gt_15(self):
        self.assertEqual((T('2000-01-01') > '1999-02-02').value, True)

    def test_gt_16(self):
        self.assertEqual((T('2000-01-01') > '2010-02-02').value, False)

    # <=

    def test_le_1(self):
        self.assertEqual((T(99) <= T(70)).value, False)

    def test_le_2(self):
        self.assertEqual((T(70) <= T(70)).value, True)

    def test_le_3(self):
        self.assertEqual((T(99) <= T(170)).value, True)

    def test_le_4(self):
        self.assertEqual((T(99.023) <= T(170)).value, True)

    def test_le_5(self):
        self.assertEqual((T(99) <= 70).value, False)

    def test_le_6(self):
        self.assertEqual((354 <= T(70)).value, False)

    def test_le_7(self):
        self.assertEqual((354 <= T(670)).value, True)

    def test_le_8(self):
        self.assertEqual((354 <= T(None)).value, None)

    def test_le_9(self):
        self.assertEqual((T(None) <= 34).value, None)

    def test_le_10(self):
        self.assertEqual((T(None) <= T(None)).value, None)

    # <

    def test_lt_1(self):
        self.assertEqual((T(99) < T(70)).value, False)

    def test_lt_2(self):
        self.assertEqual((T(70) < T(70)).value, False)

    def test_lt_3(self):
        self.assertEqual((T(99) < T(170)).value, True)

    def test_lt_4(self):
        self.assertEqual((T(99.023) < T(170)).value, True)

    def test_lt_5(self):
        self.assertEqual((T(99) < 70).value, False)

    def test_lt_6(self):
        self.assertEqual((354 < T(70)).value, False)

    def test_lt_7(self):
        self.assertEqual((354 < T(670)).value, True)

    def test_lt_8(self):
        self.assertEqual((354 < T(None)).value, None)

    def test_lt_9(self):
        self.assertEqual((T(None) < 34).value, None)

    def test_lt_10(self):
        self.assertEqual((T(None) < T(None)).value, None)

    # ==

    def test_eq_1(self):
        self.assertEqual((T(99) == T(70)).value, False)

    def test_eq_2(self):
        self.assertEqual((T(70) == T(70)).value, True)

    def test_eq_3(self):
        self.assertEqual((T(99) == 70).value, False)

    def test_eq_4(self):
        self.assertEqual((354 == T(70)).value, False)

    def test_eq_5(self):
        self.assertEqual((354 == T(354)).value, True)

    def test_eq_6(self):
        self.assertEqual((354 == T(None)).value, None)

    def test_eq_7(self):
        self.assertEqual((T(None) == 34).value, None)

    def test_eq_8(self):
        self.assertEqual((T(None) == T(None)).value, None)

    def test_eq_9(self):
        self.assertEqual((T("hello") == T("hello")).value, True)

    def test_eq_10(self):
        self.assertEqual((T("hello") == T("meow")).value, False)

    def test_eq_11(self):
        self.assertEqual((T(None) == T("meow")).value, None)

    def test_eq_12(self):
        self.assertEqual((T("hello") == T(None)).value, None)

    def test_eq_13(self):
        self.assertEqual(("hello" == T(None)).value, None)

    def test_eq_14(self):
        self.assertEqual(("hello" == T("hello")).value, True)

    # !=

    def test_ne_1(self):
        self.assertEqual((T(99) != T(70)).value, True)

    def test_ne_2(self):
        self.assertEqual((T(70) != T(70)).value, False)

    def test_ne_3(self):
        self.assertEqual((T(99) != 70).value, True)

    def test_ne_4(self):
        self.assertEqual((354 != T(70)).value, True)

    def test_ne_5(self):
        self.assertEqual((354 != T(354)).value, False)

    def test_ne_6(self):
        self.assertEqual((354 != T(None)).value, None)

    def test_ne_7(self):
        self.assertEqual((T(None) != 34).value, None)

    def test_ne_8(self):
        self.assertEqual((T(None) != T(None)).value, None)

    def test_ne_9(self):
        self.assertEqual((T("hello") != T("hello")).value, False)

    def test_ne_10(self):
        self.assertEqual((T("hello") != T("meow")).value, True)

    def test_ne_11(self):
        self.assertEqual((T(None) != T("meow")).value, None)

    def test_ne_12(self):
        self.assertEqual((T("hello") != T(None)).value, None)

    # IS_NONE

    def test_is_none_1(self):
        self.assertEqual(is_none(9), False)

    def test_is_none_2(self):
        self.assertEqual(is_none(T(9)), False)

    def test_is_none_3(self):
        self.assertEqual(is_none(T(True)), False)

    def test_is_none_4(self):
        self.assertEqual(is_none(T(None)), True)

    def test_is_none_5(self):
        self.assertEqual(is_none(Stub()), False)

    # ADDITION

    def test_add_1(self):
        self.assertEqual((T(5) + T(7)).value, 12)

    def test_add_2(self):
        self.assertEqual((T(4) + T(-9)).value, -5)

    def test_add_3(self):
        self.assertEqual((T(99) + 70).value, 169)

    def test_add_4(self):
        self.assertEqual((1 + T(70)).value, 71)

    def test_add_5(self):
        self.assertEqual((1 + T(354)).value, 355)

    def test_add_6(self):
        self.assertEqual((1 + T(None)).value, None)

    def test_add_7(self):
        self.assertEqual((T(None) + 34).value, None)

    def test_add_8(self):
        self.assertEqual((T(None) + T(None)).value, None)

    # MULTIPLICATION

    def test_mul_1(self):
        self.assertEqual((T(5) * T(7)).value, 35)

    def test_mul_2(self):
        self.assertEqual((T(4) * T(-9)).value, -36)

    def test_mul_3(self):
        self.assertEqual((T(9) * 7).value, 63)

    def test_mul_4(self):
        self.assertEqual((1 * T(7)).value, 7)

    def test_mul_5(self):
        self.assertEqual((1 * T(34)).value, 34)

    def test_mul_6(self):
        self.assertEqual((1 * T(None)).value, None)

    def test_mul_7(self):
        self.assertEqual((T(None) * 34).value, None)

    def test_mul_8(self):
        self.assertEqual((T(None) * T(None)).value, None)

    def test_mul_9(self):
        self.assertEqual((T(None) * 0).value, 0)

    def test_mul_10(self):
        self.assertEqual((0 * T(None)).value, 0)

    def test_mul_11(self):
        self.assertEqual((Stub() * 0).value, 0)

    def test_mul_12(self):
        self.assertEqual((0 * Stub()).value, 0)

    def test_mul_13(self):
        self.assertEqual((Stub() * 5).value, StubVal)

    def test_mul_14(self):
        self.assertEqual((5 * Stub()).value, StubVal)

    # SUBTRACTION

    def test_sub_1(self):
        self.assertEqual((T(5) - T(7)).value, -2)

    def test_sub_2(self):
        self.assertEqual((T(4) - T(-9)).value, 13)

    def test_sub_3(self):
        self.assertEqual((T(9) - 7).value, 2)

    def test_sub_4(self):
        self.assertEqual((1 - T(7)).value, -6)

    def test_sub_5(self):
        self.assertEqual((1 - T(34)).value, -33)

    def test_sub_6(self):
        self.assertEqual((1 - T(None)).value, None)

    def test_sub_7(self):
        self.assertEqual((T(None) - 34).value, None)

    def test_sub_8(self):
        self.assertEqual((T(None) - T(None)).value, None)

    # DIVISION

    def test_div_1(self):
        self.assertEqual((T(6) / T(2)).value, 3)

    def test_div_2(self):
        self.assertEqual((T(6) / T(-2)).value, -3)

    def test_div_3(self):
        self.assertEqual((T(9) / 3).value, 3)

    def test_div_4(self):
        self.assertEqual((12 / T(3)).value, 4)

    def test_div_5(self):
        self.assertEqual((12 / T(1)).value, 12)

    def test_div_6(self):
        self.assertEqual((1 / T(None)).value, None)

    def test_div_7(self):
        self.assertEqual((T(None) / 34).value, None)

    def test_div_8(self):
        self.assertEqual((T(None) / T(None)).value, None)

    # IF

    def test_if_1(self):
        self.assertEqual(If(T(None), 1, 2).value, None)

    def test_if_2(self):
        self.assertEqual(If(T(True), 1, 2).value, 1)

    def test_if_3(self):
        self.assertEqual(If(True, 1, 2).value, 1)

    def test_if_4(self):
        self.assertEqual(If(T(False), 1, 2).value, 2)

    def test_if_5(self):
        self.assertEqual(If(False, 1, 2).value, 2)

    def test_if_6(self):
        self.assertEqual(If(Stub(), 1, 2).value, StubVal)

    def test_if_7(self):
        self.assertEqual(If(True, Stub(), 2).value, StubVal)

    # CFs - OR

    def test_cf_or_1(self):
        self.assertEqual(Or(T(True, 1), T(True, 1)).cf, 1)

    def test_cf_or_2(self):
        self.assertEqual(Or(T(True, 0), T(True, 1)).cf, 1)

    def test_cf_or_3(self):
        self.assertEqual(Or(T(True, 0), T(True, 0)).cf, 0)

    def test_cf_or_4(self):
        self.assertEqual(Or(T(True, 1), T(False, 1)).cf, 1)

    def test_cf_or_5(self):
        self.assertEqual(Or(T(True, 0), T(False, 1)).cf, 0)

    def test_cf_or_6(self):
        self.assertEqual(Or(T(True, 1), T(False, 0)).cf, 1)

    def test_cf_or_7(self):
        self.assertEqual(Or(T(True, 0), T(False, 0)).cf, 0)

    def test_cf_or_8(self):
        self.assertEqual(Or(T(False, 1), T(False, 1)).cf, 1)

    def test_cf_or_9(self):
        self.assertEqual(Or(T(False, 0), T(False, 1)).cf, 0)

    def test_cf_or_10(self):
        self.assertEqual(Or(T(False, 0), T(False, 0)).cf, 0)

    def test_cf_or_11(self):
        self.assertEqual(Or(T(True, 1), T(True, .7)).cf, 1)

    def test_cf_or_12(self):
        self.assertEqual(Or(T(True, 0), T(True, .7)).cf, .7)

    def test_cf_or_13(self):
        self.assertEqual(Or(T(True, .3), T(True, .7)).cf, .7)

    def test_cf_or_14(self):
        self.assertEqual(Or(T(True, 1), T(False, .4)).cf, 1)

    def test_cf_or_15(self):
        self.assertEqual(Or(T(True, .4), T(False, 1)).cf, .4)

    def test_cf_or_16(self):
        self.assertEqual(Or(T(True, 0), T(False, .4)).cf, 0)

    def test_cf_or_17(self):
        self.assertEqual(Or(T(True, .2), T(False, 0)).cf, .2)

    def test_cf_or_18(self):
        self.assertEqual(Or(T(True, .4), T(False, .5)).cf, .4)

    def test_cf_or_19(self):
        self.assertEqual(Or(T(False, 1), T(False, .4)).cf, .4)

    def test_cf_or_20(self):
        self.assertEqual(Or(T(False, 0), T(False, .4)).cf, 0)

    def test_cf_or_21(self):
        self.assertEqual(Or(T(False, .6), T(False, .4)).cf, .4)

    def test_cf_or_22(self):
        self.assertEqual(Or(T(None, .6), T(None, .4)).cf, .6)

    def test_cf_or_23(self):
        self.assertEqual(Or(T(None, .6), T(Stub(), .4)).cf, .6)

    def test_cf_or_24(self):
        self.assertEqual(Or(T(Stub(), .6), T(Stub(), .4)).cf, .6)

    # CFS - AND

    def test_cf_and_1(self):
        self.assertEqual(And(T(True, 1), T(True, 1)).cf, 1)

    def test_cf_and_2(self):
        self.assertEqual(And(T(True, 0), T(True, 1)).cf, 0)

    def test_cf_and_3(self):
        self.assertEqual(And(T(True, 0), T(True, 0)).cf, 0)

    def test_cf_and_4(self):
        self.assertEqual(And(T(True, 1), T(False, 1)).cf, 1)

    def test_cf_and_5(self):
        self.assertEqual(And(T(True, 0), T(False, 1)).cf, 1)

    def test_cf_and_6(self):
        self.assertEqual(And(T(True, 1), T(False, 0)).cf, 0)

    def test_cf_and_7(self):
        self.assertEqual(And(T(True, 0), T(False, 0)).cf, 0)

    def test_cf_and_8(self):
        self.assertEqual(And(T(False, 1), T(False, 1)).cf, 1)

    def test_cf_and_9(self):
        self.assertEqual(And(T(False, 0), T(False, 1)).cf, 1)

    def test_cf_and_10(self):
        self.assertEqual(And(T(False, 0), T(False, 0)).cf, 0)

    def test_cf_and_11(self):
        self.assertEqual(And(T(True, 1), T(True, .7)).cf, .7)

    def test_cf_and_12(self):
        self.assertEqual(And(T(True, 0), T(True, .7)).cf, 0)

    def test_cf_and_13(self):
        self.assertEqual(And(T(True, .3), T(True, .7)).cf, .3)

    def test_cf_and_14(self):
        self.assertEqual(And(T(True, 1), T(False, .4)).cf, .4)

    def test_cf_and_15(self):
        self.assertEqual(And(T(True, .4), T(False, 1)).cf, 1)

    def test_cf_and_16(self):
        self.assertEqual(And(T(True, 0), T(False, .4)).cf, .4)

    def test_cf_and_17(self):
        self.assertEqual(And(T(True, .2), T(False, 0)).cf, 0)

    def test_cf_and_18(self):
        self.assertEqual(And(T(True, .4), T(False, .5)).cf, .5)

    def test_cf_and_19(self):
        self.assertEqual(And(T(False, 1), T(False, .4)).cf, 1)

    def test_cf_and_20(self):
        self.assertEqual(And(T(False, 0), T(False, .4)).cf, .4)

    def test_cf_and_21(self):
        self.assertEqual(And(T(False, .6), T(False, .4)).cf, .6)

    def test_cf_and_22(self):
        self.assertEqual(And(T(None, .6), T(None, .4)).cf, .6)

    def test_cf_and_23(self):
        self.assertEqual(And(T(None, .6), T(Stub(), .4)).cf, .6)

    def test_cf_and_24(self):
        self.assertEqual(And(T(Stub(), .6), T(Stub(), .4)).cf, .6)

    # CFS - OTHER
    
    def test_cf_other_1(self):
        self.assertEqual((T(9, .5) + T(23, .7)).cf, 0.5)

    def test_cf_other_2(self):
        self.assertEqual(Not(T(True, .4)).cf, 0.4)

    def test_cf_other_3(self):
        self.assertEqual((T(3, .6) * T(0, .4)).cf, .4)

    def test_cf_other_4(self):
        self.assertEqual((T(3, .3) * T(0, .4)).cf, .4)

    def test_cf_other_5(self):
        self.assertEqual((T(0, .6) * T(0, .4)).cf, .6)

    def test_cf_other_6(self):
        self.assertEqual((T(8, .6) + T(1, .4)).cf, .4)

    def test_cf_other_7(self):
        self.assertEqual((T(None, .6) + T(1, .4)).cf, .6)

    def test_cf_other_8(self):
        self.assertEqual((T(None, .6) + T(None, .4)).cf, .6)

    def test_cf_other_9(self):
        self.assertEqual((Stub(.6) + T(1, .4)).cf, .6)

    def test_cf_other_10(self):
        self.assertEqual((Stub(.6) + Stub(.4)).cf, .6)

    def test_cf_other_11(self):
        self.assertEqual((Stub(.6) + T(None, .4)).cf, .6)

    def test_list_contains_none_1(self):
        self.assertEqual(list_contains_none([3, T(None), 8]), True)

    def test_list_contains_none_2(self):
        self.assertEqual(list_contains_none([3, 4, 8]), False)

    def test_list_contains_none_3(self):
        self.assertEqual(list_contains_none([]), False)

    # MAP

    def test_map_1(self):
        self.assertEqual(Map(lambda x: x * 8, [3, 5, 8]).value, [24, 40, 64])

    def test_map_2(self):
        self.assertEqual(Map(lambda x: x * 8, T([3, 5, 8])).value, [24, 40, 64])

    def test_map_3(self):
        self.assertEqual(Map(lambda x: x * 8, T(None)).value, None)

    def test_map_4(self):
        self.assertEqual(Map(lambda x: x * 8, Stub()).value, StubVal)

    def test_map_5(self):
        self.assertEqual(Map(lambda x: x * 8, [3, T(None), 8]).value, None)

    def test_map_6(self):
        self.assertEqual(Map(lambda x: x * 8, T([3, T(None), 8])).value, None)

    def test_map_7(self):
        self.assertEqual(Map(lambda x: x * 8, Stub()).value, StubVal)

    # ANY

    def test_any_1(self):
        self.assertEqual(Any([3, 5, 8]).value, False)

    def test_any_2(self):
        self.assertEqual(Any(T([3, 5, 8])).value, False)

    def test_any_3(self):
        self.assertEqual(Any(T([3, 5, True])).value, True)

    def test_any_4(self):
        self.assertEqual(Any(T([3, 5, T(True)])).value, True)

    def test_any_5(self):
        self.assertEqual(Any([3, 5, T(True)]).value, True)

    def test_any_6(self):
        self.assertEqual(Any([3, 5, T(False)]).value, False)

    def test_any_7(self):
        self.assertEqual(Any([3, 5, T(None)]).value, None)

    def test_any_8(self):
        self.assertEqual(Any(T(None)).value, None)

    def test_any_9(self):
        self.assertEqual(Any([3, 5, Stub()]).value, StubVal)

    def test_any_10(self):
        self.assertEqual(Any(Stub()).value, StubVal)

    def test_any_11(self):
        self.assertEqual(Any([3, True, Stub()]).value, True)

    def test_any_12(self):
        self.assertEqual(Any([True, Stub()]).value, True)

    def test_any_13(self):
        self.assertEqual(Any([T(True), Stub()]).value, True)

    def test_any_14(self):
        self.assertEqual(Any([False, False, True]).value, True)

    # ALL

    def test_all_1(self):
        self.assertEqual(All([3, 5, 8]).value, False)

    def test_all_2(self):
        self.assertEqual(All(T([3, 5, 8])).value, False)

    def test_all_3(self):
        self.assertEqual(All(T([3, 5, True])).value, False)

    def test_all_4(self):
        self.assertEqual(All(T([3, 5, T(True)])).value, False)

    def test_all_5(self):
        self.assertEqual(All([3, 5, T(True)]).value, False)

    def test_all_6(self):
        self.assertEqual(All([3, 5, T(False)]).value, False)

    def test_all_7(self):
        self.assertEqual(All([T(True), T(True), T(True)]).value, True)

    def test_all_8(self):
        self.assertEqual(All([T(True), True, T(True)]).value, True)

    def test_all_9(self):
        self.assertEqual(All([3, 5, Stub()]).value, StubVal)

    def test_all_10(self):
        self.assertEqual(All(Stub()).value, StubVal)

    def test_all_11(self):
        self.assertEqual(All([3, False, Stub()]).value, False)

    def test_all_12(self):
        self.assertEqual(All([False, Stub()]).value, False)

    def test_all_13(self):
        self.assertEqual(All([T(False), Stub()]).value, False)

    # EXISTS

    def test_exists_1(self):
        self.assertEqual(Exists(lambda x: x > 6, T([3, 5, 8])).value, True)

    def test_exists_2(self):
        self.assertEqual(Exists(lambda x: x > 16, T([3, 5, 8])).value, False)

    # FORALL

    def test_forall_1(self):
        self.assertEqual(ForAll(lambda x: x > 6, T([3, 5, 8])).value, False)

    def test_forall_2(self):
        self.assertEqual(ForAll(lambda x: x > 1, T([3, 5, 8])).value, True)

    # TS_TRIM

    def test_ts_trim_1(self):
        self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: False, '2020-01-01': True, '2021-01-01': True})),
                         traces.TimeSeries({DawnOfTime: False, '2020-01-01': True}))

    def test_ts_trim_2(self):
        self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: False, '2020-01-01': Stub(), '2021-01-01': Stub()})),
                         traces.TimeSeries({DawnOfTime: False, '2020-01-01': Stub()}))

    def test_ts_trim_3(self):
        self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: False, '2020-01-01': None, '2021-01-01': None})),
                         traces.TimeSeries({DawnOfTime: False, '2020-01-01': None}))

    def test_ts_trim_4(self):
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
