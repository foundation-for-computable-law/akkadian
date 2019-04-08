import unittest

from dsl import *


class TestDSL(unittest.TestCase):

    # AND
    #
    # def test_and_1(self):
    #     self.assertEqual(And(V(True), V(False)).value, False)
    #
    # def test_and_2(self):
    #     self.assertEqual(And(V(True), V(True)).value, True)
    #
    # def test_and_3(self):
    #     self.assertEqual(And(V(False), V(False)).value, False)
    #
    # def test_and_4(self):
    #     self.assertEqual(And(V(False), V(True)).value, False)
    #
    # def test_and_5(self):
    #     self.assertEqual(And(V(None), V(True)).value, None)
    #
    # def test_and_6(self):
    #     self.assertEqual(And(V(None), V(False)).value, False)
    #
    # def test_and_7(self):
    #     self.assertEqual(And(V(False), V(None)).value, False)
    #
    # def test_and_8(self):
    #     self.assertEqual(And(V(None), V(False)).value, False)
    #
    # def test_and_9(self):
    #     self.assertEqual(And(V(True), V(None)).value, None)
    #
    # def test_and_10(self):
    #     self.assertEqual(And(V(None), V(None)).value, None)
    #
    # def test_and_11(self):
    #     self.assertEqual(And(V(True), True).value, True)
    #
    # def test_and_12(self):
    #     self.assertEqual(And(True, V(True)).value, True)
    #
    # def test_and_13(self):
    #     self.assertEqual(And(False, V(True)).value, False)
    #
    # def test_and_14(self):
    #     self.assertEqual(And(False, V(None)).value, False)
    #
    # def test_and_15(self):
    #     self.assertEqual(And(False, V(None), True).value, False)
    #
    # def test_and_16(self):
    #     self.assertEqual(And(False, "anything", True).value, False)
    #
    # def test_and_17(self):
    #     self.assertEqual(And(Stub(), V(True)).value, StubVal)
    #
    # def test_and_18(self):
    #     self.assertEqual(And(V(True), Stub()).value, StubVal)
    #
    # def test_and_19(self):
    #     self.assertEqual(And(Stub(), V(False)).value, False)
    #
    # def test_and_20(self):
    #     self.assertEqual(And(V(False), Stub()).value, False)
    #
    # def test_and_21(self):
    #     self.assertEqual(And(Stub(), V(None)).value, None)
    #
    # def test_and_22(self):
    #     self.assertEqual(And(V(None), Stub()).value, None)
    #
    # # OR
    #
    # def test_or_1(self):
    #     self.assertEqual(Or(V(True), V(False)).value, True)
    #
    # def test_or_2(self):
    #     self.assertEqual(Or(V(True), V(True)).value, True)
    #
    # def test_or_3(self):
    #     self.assertEqual(Or(V(False), V(False)).value, False)
    #
    # def test_or_4(self):
    #     self.assertEqual(Or(V(False), V(True)).value, True)
    #
    # def test_or_5(self):
    #     self.assertEqual(Or(V(None), V(True)).value, True)
    #
    # def test_or_6(self):
    #     self.assertEqual(Or(V(None), V(False)).value, None)
    #
    # def test_or_7(self):
    #     self.assertEqual(Or(V(False), V(None)).value, None)
    #
    # def test_or_8(self):
    #     self.assertEqual(Or(V(True), V(None)).value, True)
    #
    # def test_or_9(self):
    #     self.assertEqual(Or(V(None), V(None)).value, None)
    #
    # def test_or_10(self):
    #     self.assertEqual(Or(True, V(True)).value, True)
    #
    # def test_or_11(self):
    #     self.assertEqual(Or(False, V(True)).value, True)
    #
    # def test_or_12(self):
    #     self.assertEqual(Or(False, V(None)).value, None)
    #
    # def test_or_13(self):
    #     self.assertEqual(Or(True, V(None)).value, True)
    #
    # def test_or_14(self):
    #     self.assertEqual(Or(True, V(False)).value, True)
    #
    # def test_or_15(self):
    #     self.assertEqual(Or(Stub(), V(True)).value, True)
    #
    # def test_or_16(self):
    #     self.assertEqual(Or(V(True), Stub()).value, True)
    #
    # def test_or_17(self):
    #     self.assertEqual(Or(Stub(), V(False)).value, StubVal)
    #
    # def test_or_18(self):
    #     self.assertEqual(Or(V(False), Stub()).value, StubVal)
    #
    # def test_or_19(self):
    #     self.assertEqual(Or(Stub(), V(None)).value, None)
    #
    # def test_or_20(self):
    #     self.assertEqual(Or(V(None), Stub()).value, None)
    #
    # # NOT
    #
    # def test_not_1(self):
    #     self.assertEqual(Not(V(True)).value, False)
    #
    # def test_not_2(self):
    #     self.assertEqual(Not(V(False)).value, True)
    #
    # def test_not_3(self):
    #     self.assertEqual(Not(V(None)).value, None)
    #
    # def test_not_4(self):
    #     self.assertEqual(Not(True).value, False)
    #
    # def test_not_5(self):
    #     self.assertEqual(Not(False).value, True)
    #
    # def test_not_6(self):
    #     self.assertEqual(Not(Stub()).value, StubVal)
    #
    # # >=
    #
    # def test_ge_1(self):
    #     self.assertEqual((V(99) >= V(70)).value, True)
    #
    # def test_ge_2(self):
    #     self.assertEqual((V(70) >= V(70)).value, True)
    #
    # def test_ge_3(self):
    #     self.assertEqual((V(99) >= V(170)).value, False)
    #
    # def test_ge_4(self):
    #     self.assertEqual((V(99.023) >= V(170)).value, False)
    #
    # def test_ge_5(self):
    #     self.assertEqual((V(99) >= 70).value, True)
    #
    # def test_ge_6(self):
    #     self.assertEqual((354 >= V(70)).value, True)
    #
    # def test_ge_7(self):
    #     self.assertEqual((354 >= V(670)).value, False)
    #
    # def test_ge_8(self):
    #     self.assertEqual((354 >= V(None)).value, None)
    #
    # def test_ge_9(self):
    #     self.assertEqual((V(None) >= 34).value, None)
    #
    # def test_ge_10(self):
    #     self.assertEqual((V(None) >= V(None)).value, None)
    #
    # def test_ge_11(self):
    #     self.assertEqual((Stub() >= V(None)).value, StubVal)
    #
    # def test_ge_12(self):
    #     self.assertEqual((V(None) >= Stub()).value, StubVal)
    #
    # def test_ge_13(self):
    #     self.assertEqual((Stub() >= 34).value, StubVal)
    #
    # def test_ge_14(self):
    #     self.assertEqual((44 >= Stub()).value, StubVal)
    #
    # # >
    #
    # def test_gt_1(self):
    #     self.assertEqual((V(99) > V(70)).value, True)
    #
    # def test_gt_2(self):
    #     self.assertEqual((V(70) > V(70)).value, False)
    #
    # def test_gt_3(self):
    #     self.assertEqual((V(99) > V(170)).value, False)
    #
    # def test_gt_4(self):
    #     self.assertEqual((V(99.023) > V(170)).value, False)
    #
    # def test_gt_5(self):
    #     self.assertEqual((V(99) > 70).value, True)
    #
    # def test_gt_6(self):
    #     self.assertEqual((354 > V(70)).value, True)
    #
    # def test_gt_7(self):
    #     self.assertEqual((354 > V(670)).value, False)
    #
    # def test_gt_8(self):
    #     self.assertEqual((354 > V(None)).value, None)
    #
    # def test_gt_9(self):
    #     self.assertEqual((V(None) > 34).value, None)
    #
    # def test_gt_10(self):
    #     self.assertEqual((V(None) > V(None)).value, None)
    #
    # def test_gt_11(self):
    #     self.assertEqual((V('2000-01-01') > V('1999-02-02')).value, True)
    #
    # def test_gt_12(self):
    #     self.assertEqual((V('2000-01-01') > V('2010-02-02')).value, False)
    #
    # def test_gt_13(self):
    #     self.assertEqual(('2000-01-01' > V('1999-02-02')).value, True)
    #
    # def test_gt_14(self):
    #     self.assertEqual(('2000-01-01' > V('2010-02-02')).value, False)
    #
    # def test_gt_15(self):
    #     self.assertEqual((V('2000-01-01') > '1999-02-02').value, True)
    #
    # def test_gt_16(self):
    #     self.assertEqual((V('2000-01-01') > '2010-02-02').value, False)
    #
    # # <=
    #
    # def test_le_1(self):
    #     self.assertEqual((V(99) <= V(70)).value, False)
    #
    # def test_le_2(self):
    #     self.assertEqual((V(70) <= V(70)).value, True)
    #
    # def test_le_3(self):
    #     self.assertEqual((V(99) <= V(170)).value, True)
    #
    # def test_le_4(self):
    #     self.assertEqual((V(99.023) <= V(170)).value, True)
    #
    # def test_le_5(self):
    #     self.assertEqual((V(99) <= 70).value, False)
    #
    # def test_le_6(self):
    #     self.assertEqual((354 <= V(70)).value, False)
    #
    # def test_le_7(self):
    #     self.assertEqual((354 <= V(670)).value, True)
    #
    # def test_le_8(self):
    #     self.assertEqual((354 <= V(None)).value, None)
    #
    # def test_le_9(self):
    #     self.assertEqual((V(None) <= 34).value, None)
    #
    # def test_le_10(self):
    #     self.assertEqual((V(None) <= V(None)).value, None)
    #
    # # <
    #
    # def test_lt_1(self):
    #     self.assertEqual((V(99) < V(70)).value, False)
    #
    # def test_lt_2(self):
    #     self.assertEqual((V(70) < V(70)).value, False)
    #
    # def test_lt_3(self):
    #     self.assertEqual((V(99) < V(170)).value, True)
    #
    # def test_lt_4(self):
    #     self.assertEqual((V(99.023) < V(170)).value, True)
    #
    # def test_lt_5(self):
    #     self.assertEqual((V(99) < 70).value, False)
    #
    # def test_lt_6(self):
    #     self.assertEqual((354 < V(70)).value, False)
    #
    # def test_lt_7(self):
    #     self.assertEqual((354 < V(670)).value, True)
    #
    # def test_lt_8(self):
    #     self.assertEqual((354 < V(None)).value, None)
    #
    # def test_lt_9(self):
    #     self.assertEqual((V(None) < 34).value, None)
    #
    # def test_lt_10(self):
    #     self.assertEqual((V(None) < V(None)).value, None)
    #
    # # ==
    #
    # def test_eq_1(self):
    #     self.assertEqual((V(99) == V(70)).value, False)
    #
    # def test_eq_2(self):
    #     self.assertEqual((V(70) == V(70)).value, True)
    #
    # def test_eq_3(self):
    #     self.assertEqual((V(99) == 70).value, False)
    #
    # def test_eq_4(self):
    #     self.assertEqual((354 == V(70)).value, False)
    #
    # def test_eq_5(self):
    #     self.assertEqual((354 == V(354)).value, True)
    #
    # def test_eq_6(self):
    #     self.assertEqual((354 == V(None)).value, None)
    #
    # def test_eq_7(self):
    #     self.assertEqual((V(None) == 34).value, None)
    #
    # def test_eq_8(self):
    #     self.assertEqual((V(None) == V(None)).value, None)
    #
    # def test_eq_9(self):
    #     self.assertEqual((V("hello") == V("hello")).value, True)
    #
    # def test_eq_10(self):
    #     self.assertEqual((V("hello") == V("meow")).value, False)
    #
    # def test_eq_11(self):
    #     self.assertEqual((V(None) == V("meow")).value, None)
    #
    # def test_eq_12(self):
    #     self.assertEqual((V("hello") == V(None)).value, None)
    #
    # def test_eq_13(self):
    #     self.assertEqual(("hello" == V(None)).value, None)
    #
    # def test_eq_14(self):
    #     self.assertEqual(("hello" == V("hello")).value, True)
    #
    # # !=
    #
    # def test_ne_1(self):
    #     self.assertEqual((V(99) != V(70)).value, True)
    #
    # def test_ne_2(self):
    #     self.assertEqual((V(70) != V(70)).value, False)
    #
    # def test_ne_3(self):
    #     self.assertEqual((V(99) != 70).value, True)
    #
    # def test_ne_4(self):
    #     self.assertEqual((354 != V(70)).value, True)
    #
    # def test_ne_5(self):
    #     self.assertEqual((354 != V(354)).value, False)
    #
    # def test_ne_6(self):
    #     self.assertEqual((354 != V(None)).value, None)
    #
    # def test_ne_7(self):
    #     self.assertEqual((V(None) != 34).value, None)
    #
    # def test_ne_8(self):
    #     self.assertEqual((V(None) != V(None)).value, None)
    #
    # def test_ne_9(self):
    #     self.assertEqual((V("hello") != V("hello")).value, False)
    #
    # def test_ne_10(self):
    #     self.assertEqual((V("hello") != V("meow")).value, True)
    #
    # def test_ne_11(self):
    #     self.assertEqual((V(None) != V("meow")).value, None)
    #
    # def test_ne_12(self):
    #     self.assertEqual((V("hello") != V(None)).value, None)

    # IS_NONE

    # def test_is_none_1(self):
    #     self.assertEqual(is_none(9), False)
    #
    # def test_is_none_2(self):
    #     self.assertEqual(is_none(V(9)), False)
    #
    # def test_is_none_3(self):
    #     self.assertEqual(is_none(V(True)), False)
    #
    # def test_is_none_4(self):
    #     self.assertEqual(is_none(V(None)), True)
    #
    # def test_is_none_5(self):
    #     self.assertEqual(is_none(Stub()), False)

    # ADDITION

    # def test_add_1(self):
    #     self.assertEqual((V(5) + V(7)).value, 12)
    #
    # def test_add_2(self):
    #     self.assertEqual((V(4) + V(-9)).value, -5)
    #
    # def test_add_3(self):
    #     self.assertEqual((V(99) + 70).value, 169)
    #
    # def test_add_4(self):
    #     self.assertEqual((1 + V(70)).value, 71)
    #
    # def test_add_5(self):
    #     self.assertEqual((1 + V(354)).value, 355)
    #
    # def test_add_6(self):
    #     self.assertEqual((1 + V(None)).value, None)
    #
    # def test_add_7(self):
    #     self.assertEqual((V(None) + 34).value, None)
    #
    # def test_add_8(self):
    #     self.assertEqual((V(None) + V(None)).value, None)
    #
    # # MULTIPLICATION
    #
    # def test_mul_1(self):
    #     self.assertEqual((V(5) * V(7)).value, 35)
    #
    # def test_mul_2(self):
    #     self.assertEqual((V(4) * V(-9)).value, -36)
    #
    # def test_mul_3(self):
    #     self.assertEqual((V(9) * 7).value, 63)
    #
    # def test_mul_4(self):
    #     self.assertEqual((1 * V(7)).value, 7)
    #
    # def test_mul_5(self):
    #     self.assertEqual((1 * V(34)).value, 34)
    #
    # def test_mul_6(self):
    #     self.assertEqual((1 * V(None)).value, None)
    #
    # def test_mul_7(self):
    #     self.assertEqual((V(None) * 34).value, None)
    #
    # def test_mul_8(self):
    #     self.assertEqual((V(None) * V(None)).value, None)
    #
    # def test_mul_9(self):
    #     self.assertEqual((V(None) * 0).value, 0)
    #
    # def test_mul_10(self):
    #     self.assertEqual((0 * V(None)).value, 0)
    #
    # def test_mul_11(self):
    #     self.assertEqual((Stub() * 0).value, 0)
    #
    # def test_mul_12(self):
    #     self.assertEqual((0 * Stub()).value, 0)
    #
    # def test_mul_13(self):
    #     self.assertEqual((Stub() * 5).value, StubVal)
    #
    # def test_mul_14(self):
    #     self.assertEqual((5 * Stub()).value, StubVal)
    #
    # # SUBTRACTION
    #
    # def test_sub_1(self):
    #     self.assertEqual((V(5) - V(7)).value, -2)
    #
    # def test_sub_2(self):
    #     self.assertEqual((V(4) - V(-9)).value, 13)
    #
    # def test_sub_3(self):
    #     self.assertEqual((V(9) - 7).value, 2)
    #
    # def test_sub_4(self):
    #     self.assertEqual((1 - V(7)).value, -6)
    #
    # def test_sub_5(self):
    #     self.assertEqual((1 - V(34)).value, -33)
    #
    # def test_sub_6(self):
    #     self.assertEqual((1 - V(None)).value, None)
    #
    # def test_sub_7(self):
    #     self.assertEqual((V(None) - 34).value, None)
    #
    # def test_sub_8(self):
    #     self.assertEqual((V(None) - V(None)).value, None)
    #
    # # DIVISION
    #
    # def test_div_1(self):
    #     self.assertEqual((V(6) / V(2)).value, 3)
    #
    # def test_div_2(self):
    #     self.assertEqual((V(6) / V(-2)).value, -3)
    #
    # def test_div_3(self):
    #     self.assertEqual((V(9) / 3).value, 3)
    #
    # def test_div_4(self):
    #     self.assertEqual((12 / V(3)).value, 4)
    #
    # def test_div_5(self):
    #     self.assertEqual((12 / V(1)).value, 12)
    #
    # def test_div_6(self):
    #     self.assertEqual((1 / V(None)).value, None)
    #
    # def test_div_7(self):
    #     self.assertEqual((V(None) / 34).value, None)
    #
    # def test_div_8(self):
    #     self.assertEqual((V(None) / V(None)).value, None)

    # IF

    def test_if_1(self):
        self.assertEqual(If(V(None), 1, 2).value, None)

    def test_if_2(self):
        self.assertEqual(If(V(True), 1, 2).value, 1)

    def test_if_3(self):
        self.assertEqual(If(True, 1, 2).value, 1)

    def test_if_4(self):
        self.assertEqual(If(V(False), 1, 2).value, 2)

    def test_if_5(self):
        self.assertEqual(If(False, 1, 2).value, 2)

    def test_if_6(self):
        self.assertEqual(If(Stub(), 1, 2).value, StubVal)

    def test_if_7(self):
        self.assertEqual(If(True, Stub(), 2).value, StubVal)

    # def test_if_cf_1(self):
    #     self.assertEqual(
    #         If(V(False, 0.08), V(2, .7),
    #            V(False, 0.9), V(3, 0.6),
    #            V(False, 0.5), V(4, 0.3),
    #            V(1, 0.19)).cf,
    #         0.08)
    #
    # def test_if_cf_2(self):
    #     self.assertEqual(
    #         If(V(True, 0.8), V(2, .7),
    #            V(False, 0.9), V(3, 0.6),
    #            V(False, 0.5), V(4, 0.3),
    #            V(1, 0.19)).cf,
    #         0.7)
    #
    # def test_if_cf_3(self):
    #     self.assertEqual(
    #         If(V(True, 0.3), V(2, .7),
    #            V(False, 0.9), V(3, 0.6),
    #            V(False, 0.5), V(4, 0.3),
    #            V(1, 0.19)).cf,
    #         0.3)
    #
    # def test_if_cf_4(self):
    #     self.assertEqual(
    #         If(V(False, 0.8), V(2, .7),
    #            V(True, 0.9), V(3, 0.6),
    #            V(False, 0.5), V(4, 0.3),
    #            V(1, 0.19)).cf,
    #         0.6)
    #
    # def test_if_cf_5(self):
    #     self.assertEqual(
    #         If(V(False, 0.8), V(2, .7),
    #            V(True, 0.1), V(3, 0.6),
    #            V(False, 0.5), V(4, 0.3),
    #            V(1, 0.19)).cf,
    #         0.1)
    #
    # def test_if_cf_6(self):
    #     self.assertEqual(
    #         If(V(False, 0.8), V(2, .7),
    #            V(False, 0.9), V(3, 0.6),
    #            V(False, 0.5), V(4, 0.3),
    #            V(1, 0.19)).cf,
    #         0.19)
    #
    # def test_if_cf_7(self):
    #     self.assertEqual(
    #         If(V(False, 0.8), V(2, .7),
    #            V(False, 0.9), V(3, 0.6),
    #            V(False, 0.5), V(4, 0.3),
    #            V(1, 0.9)).cf,
    #         0.5)
    #
    # # CFs - OR
    #
    # def test_cf_or_1(self):
    #     self.assertEqual(Or(V(True, 1), V(True, 1)).cf, 1)
    #
    # def test_cf_or_2(self):
    #     self.assertEqual(Or(V(True, 0), V(True, 1)).cf, 1)
    #
    # def test_cf_or_3(self):
    #     self.assertEqual(Or(V(True, 0), V(True, 0)).cf, 0)
    #
    # def test_cf_or_4(self):
    #     self.assertEqual(Or(V(True, 1), V(False, 1)).cf, 1)
    #
    # def test_cf_or_5(self):
    #     self.assertEqual(Or(V(True, 0), V(False, 1)).cf, 0)
    #
    # def test_cf_or_6(self):
    #     self.assertEqual(Or(V(True, 1), V(False, 0)).cf, 1)
    #
    # def test_cf_or_7(self):
    #     self.assertEqual(Or(V(True, 0), V(False, 0)).cf, 0)
    #
    # def test_cf_or_8(self):
    #     self.assertEqual(Or(V(False, 1), V(False, 1)).cf, 1)
    #
    # def test_cf_or_9(self):
    #     self.assertEqual(Or(V(False, 0), V(False, 1)).cf, 0)
    #
    # def test_cf_or_10(self):
    #     self.assertEqual(Or(V(False, 0), V(False, 0)).cf, 0)
    #
    # def test_cf_or_11(self):
    #     self.assertEqual(Or(V(True, 1), V(True, .7)).cf, 1)
    #
    # def test_cf_or_12(self):
    #     self.assertEqual(Or(V(True, 0), V(True, .7)).cf, .7)
    #
    # def test_cf_or_13(self):
    #     self.assertEqual(Or(V(True, .3), V(True, .7)).cf, .7)
    #
    # def test_cf_or_14(self):
    #     self.assertEqual(Or(V(True, 1), V(False, .4)).cf, 1)
    #
    # def test_cf_or_15(self):
    #     self.assertEqual(Or(V(True, .4), V(False, 1)).cf, .4)
    #
    # def test_cf_or_16(self):
    #     self.assertEqual(Or(V(True, 0), V(False, .4)).cf, 0)
    #
    # def test_cf_or_17(self):
    #     self.assertEqual(Or(V(True, .2), V(False, 0)).cf, .2)
    #
    # def test_cf_or_18(self):
    #     self.assertEqual(Or(V(True, .4), V(False, .5)).cf, .4)
    #
    # def test_cf_or_19(self):
    #     self.assertEqual(Or(V(False, 1), V(False, .4)).cf, .4)
    #
    # def test_cf_or_20(self):
    #     self.assertEqual(Or(V(False, 0), V(False, .4)).cf, 0)
    #
    # def test_cf_or_21(self):
    #     self.assertEqual(Or(V(False, .6), V(False, .4)).cf, .4)
    #
    # def test_cf_or_22(self):
    #     self.assertEqual(Or(V(None, .6), V(None, .4)).cf, .6)
    #
    # def test_cf_or_23(self):
    #     self.assertEqual(Or(V(None, .6), V(Stub(), .4)).cf, .6)
    #
    # def test_cf_or_24(self):
    #     self.assertEqual(Or(V(Stub(), .6), V(Stub(), .4)).cf, .6)
    #
    # # CFS - AND
    #
    # def test_cf_and_1(self):
    #     self.assertEqual(And(V(True, 1), V(True, 1)).cf, 1)
    #
    # def test_cf_and_2(self):
    #     self.assertEqual(And(V(True, 0), V(True, 1)).cf, 0)
    #
    # def test_cf_and_3(self):
    #     self.assertEqual(And(V(True, 0), V(True, 0)).cf, 0)
    #
    # def test_cf_and_4(self):
    #     self.assertEqual(And(V(True, 1), V(False, 1)).cf, 1)
    #
    # def test_cf_and_5(self):
    #     self.assertEqual(And(V(True, 0), V(False, 1)).cf, 1)
    #
    # def test_cf_and_6(self):
    #     self.assertEqual(And(V(True, 1), V(False, 0)).cf, 0)
    #
    # def test_cf_and_7(self):
    #     self.assertEqual(And(V(True, 0), V(False, 0)).cf, 0)
    #
    # def test_cf_and_8(self):
    #     self.assertEqual(And(V(False, 1), V(False, 1)).cf, 1)
    #
    # def test_cf_and_9(self):
    #     self.assertEqual(And(V(False, 0), V(False, 1)).cf, 1)
    #
    # def test_cf_and_10(self):
    #     self.assertEqual(And(V(False, 0), V(False, 0)).cf, 0)
    #
    # def test_cf_and_11(self):
    #     self.assertEqual(And(V(True, 1), V(True, .7)).cf, .7)
    #
    # def test_cf_and_12(self):
    #     self.assertEqual(And(V(True, 0), V(True, .7)).cf, 0)
    #
    # def test_cf_and_13(self):
    #     self.assertEqual(And(V(True, .3), V(True, .7)).cf, .3)
    #
    # def test_cf_and_14(self):
    #     self.assertEqual(And(V(True, 1), V(False, .4)).cf, .4)
    #
    # def test_cf_and_15(self):
    #     self.assertEqual(And(V(True, .4), V(False, 1)).cf, 1)
    #
    # def test_cf_and_16(self):
    #     self.assertEqual(And(V(True, 0), V(False, .4)).cf, .4)
    #
    # def test_cf_and_17(self):
    #     self.assertEqual(And(V(True, .2), V(False, 0)).cf, 0)
    #
    # def test_cf_and_18(self):
    #     self.assertEqual(And(V(True, .4), V(False, .5)).cf, .5)
    #
    # def test_cf_and_19(self):
    #     self.assertEqual(And(V(False, 1), V(False, .4)).cf, 1)
    #
    # def test_cf_and_20(self):
    #     self.assertEqual(And(V(False, 0), V(False, .4)).cf, .4)
    #
    # def test_cf_and_21(self):
    #     self.assertEqual(And(V(False, .6), V(False, .4)).cf, .6)
    #
    # def test_cf_and_22(self):
    #     self.assertEqual(And(V(None, .6), V(None, .4)).cf, .6)
    #
    # def test_cf_and_23(self):
    #     self.assertEqual(And(V(None, .6), V(Stub(), .4)).cf, .6)
    #
    # def test_cf_and_24(self):
    #     self.assertEqual(And(V(Stub(), .6), V(Stub(), .4)).cf, .6)
    #
    # # CFS - OTHER
    #
    # def test_cf_other_1(self):
    #     self.assertEqual((V(9, .5) + V(23, .7)).cf, 0.5)
    #
    # def test_cf_other_2(self):
    #     self.assertEqual(Not(V(True, .4)).cf, 0.4)
    #
    # def test_cf_other_3(self):
    #     self.assertEqual((V(3, .6) * V(0, .4)).cf, .4)
    #
    # def test_cf_other_4(self):
    #     self.assertEqual((V(3, .3) * V(0, .4)).cf, .4)
    #
    # def test_cf_other_5(self):
    #     self.assertEqual((V(0, .6) * V(0, .4)).cf, .6)
    #
    # def test_cf_other_6(self):
    #     self.assertEqual((V(8, .6) + V(1, .4)).cf, .4)
    #
    # def test_cf_other_7(self):
    #     self.assertEqual((V(None, .6) + V(1, .4)).cf, .6)
    #
    # def test_cf_other_8(self):
    #     self.assertEqual((V(None, .6) + V(None, .4)).cf, .6)
    #
    # def test_cf_other_9(self):
    #     self.assertEqual((Stub(.6) + V(1, .4)).cf, .6)
    #
    # def test_cf_other_10(self):
    #     self.assertEqual((Stub(.6) + Stub(.4)).cf, .6)
    #
    # def test_cf_other_11(self):
    #     self.assertEqual((Stub(.6) + V(None, .4)).cf, .6)
    #
    # def test_list_contains_none_1(self):
    #     self.assertEqual(list_contains_none([3, V(None), 8]), True)
    #
    # def test_list_contains_none_2(self):
    #     self.assertEqual(list_contains_none([3, 4, 8]), False)
    #
    # def test_list_contains_none_3(self):
    #     self.assertEqual(list_contains_none([]), False)

    # MAP

    def test_map_1(self):
        self.assertEqual(Map(lambda x: x * 8, [3, 5, 8]).value, [24, 40, 64])

    def test_map_2(self):
        self.assertEqual(Map(lambda x: x * 8, V([3, 5, 8])).value, [24, 40, 64])

    def test_map_3(self):
        self.assertEqual(Map(lambda x: x * 8, V(None)).value, None)

    def test_map_4(self):
        self.assertEqual(Map(lambda x: x * 8, Stub()).value, StubVal)

    def test_map_5(self):
        self.assertEqual(Map(lambda x: x * 8, [3, V(None), 8]).value, None)

    def test_map_6(self):
        self.assertEqual(Map(lambda x: x * 8, V([3, V(None), 8])).value, None)

    def test_map_7(self):
        self.assertEqual(Map(lambda x: x * 8, Stub()).value, StubVal)

    # ANY

    def test_any_1(self):
        self.assertEqual(Any([3, 5, 8]).value, False)

    def test_any_2(self):
        self.assertEqual(Any(V([3, 5, 8])).value, False)

    def test_any_3(self):
        self.assertEqual(Any(V([3, 5, True])).value, True)

    def test_any_4(self):
        self.assertEqual(Any(V([3, 5, V(True)])).value, True)

    def test_any_5(self):
        self.assertEqual(Any([3, 5, V(True)]).value, True)

    def test_any_6(self):
        self.assertEqual(Any([3, 5, V(False)]).value, False)

    def test_any_7(self):
        self.assertEqual(Any([3, 5, V(None)]).value, None)

    def test_any_8(self):
        self.assertEqual(Any(V(None)).value, None)

    def test_any_9(self):
        self.assertEqual(Any([3, 5, Stub()]).value, StubVal)

    def test_any_10(self):
        self.assertEqual(Any(Stub()).value, StubVal)

    def test_any_11(self):
        self.assertEqual(Any([3, True, Stub()]).value, True)

    def test_any_12(self):
        self.assertEqual(Any([True, Stub()]).value, True)

    def test_any_13(self):
        self.assertEqual(Any([V(True), Stub()]).value, True)

    def test_any_14(self):
        self.assertEqual(Any([False, False, True]).value, True)

    # ALL

    def test_all_1(self):
        self.assertEqual(All([3, 5, 8]).value, False)

    def test_all_2(self):
        self.assertEqual(All(V([3, 5, 8])).value, False)

    def test_all_3(self):
        self.assertEqual(All(V([3, 5, True])).value, False)

    def test_all_4(self):
        self.assertEqual(All(V([3, 5, V(True)])).value, False)

    def test_all_5(self):
        self.assertEqual(All([3, 5, V(True)]).value, False)

    def test_all_6(self):
        self.assertEqual(All([3, 5, V(False)]).value, False)

    def test_all_7(self):
        self.assertEqual(All([V(True), V(True), V(True)]).value, True)

    def test_all_8(self):
        self.assertEqual(All([V(True), True, V(True)]).value, True)

    def test_all_9(self):
        self.assertEqual(All([3, 5, Stub()]).value, StubVal)

    def test_all_10(self):
        self.assertEqual(All(Stub()).value, StubVal)

    def test_all_11(self):
        self.assertEqual(All([3, False, Stub()]).value, False)

    def test_all_12(self):
        self.assertEqual(All([False, Stub()]).value, False)

    def test_all_13(self):
        self.assertEqual(All([V(False), Stub()]).value, False)

    # EXISTS

    def test_exists_1(self):
        self.assertEqual(Exists(lambda x: x > 6, V([3, 5, 8])).value, True)

    def test_exists_2(self):
        self.assertEqual(Exists(lambda x: x > 16, V([3, 5, 8])).value, False)

    # FORALL

    def test_forall_1(self):
        self.assertEqual(ForAll(lambda x: x > 6, V([3, 5, 8])).value, False)

    def test_forall_2(self):
        self.assertEqual(ForAll(lambda x: x > 1, V([3, 5, 8])).value, True)

    # TS_TRIM

    # def test_ts_trim_1(self):
    #     self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: False, '2020-01-01': True, '2021-01-01': True})),
    #                      traces.TimeSeries({DawnOfTime: False, '2020-01-01': True}))
    #
    # def test_ts_trim_2(self):
    #     self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: False, '2020-01-01': Stub(), '2021-01-01': Stub()})),
    #                      traces.TimeSeries({DawnOfTime: False, '2020-01-01': Stub()}))
    #
    # def test_ts_trim_3(self):
    #     self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: False, '2020-01-01': None, '2021-01-01': None})),
    #                      traces.TimeSeries({DawnOfTime: False, '2020-01-01': None}))
    #
    # def test_ts_trim_4(self):
    #     self.assertEqual(ts_trim(traces.TimeSeries({DawnOfTime: 3, '2020-01-01': 4, '2021-01-01': 4.0})),
    #                      traces.TimeSeries({DawnOfTime: 3, '2020-01-01': 4}))

    # # Constructing time series
    #
    # def test_ts_construction_1(self):
    #     self.assertEqual(EffectiveFrom('2020-01-01').value,
    #                      TS({DawnOfTime: False, '2020-01-01': True}).value)
    #
    # def test_ts_construction_2(self):
    #     self.assertEqual(EffectiveUntil('2020-01-01').value,
    #                      TS({DawnOfTime: True, '2020-01-02': False}).value)
    #
    # def test_ts_construction_3(self):
    #     self.assertEqual(EffectiveBetween('2020-01-01', '2021-01-01').value,
    #                      TS({DawnOfTime: False, '2020-01-01': True, '2021-01-02': False}).value)
    #
    # def test_ts_construction_4(self):
    #     self.assertEqual(TS({DawnOfTime: False, '2020-01-01': True, '2021-01-01': True}).value,
    #                      TS({DawnOfTime: False, '2020-01-01': True}).value)

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
                         Pretty(V(False)))

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
        self.assertEqual(Pretty(Or(V(False),
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
                         Pretty(V(True)))

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
                         Pretty(V(0)))

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
        self.assertEqual(Pretty(TS({DawnOfTime: 5}) == V(5)),
                         Pretty(V(True)))

    # Time series comparison

    def test_ts_cmp_1(self):
        self.assertEqual(Pretty(TS({DawnOfTime: 4, '2020-01-01': 8}) > 5),
                         Pretty(TS({DawnOfTime: False,
                                    '2020-01-01': True})))

    # ADDDAYS

    def test_adddays_1(self):
        self.assertEqual(
            Pretty(AddDays(TS({DawnOfTime: '2001-02-02', '2010-08-03': '2020-08-10'}),
                            TS({DawnOfTime: 23, '2010-02-03': 234}))),
            Pretty(TS({'1900-01-01': '2001-02-25',
                       '2010-02-03': '2001-09-24',
                       '2010-08-03': '2021-04-01'
                })))

    def test_adddays_2(self):
        self.assertEqual(
            Pretty(AddDays('2000-01-01', TS({DawnOfTime: 23, '2010-02-03': 234}))),
            Pretty(TS({'1900-01-01': '2000-01-24', '2010-02-03': '2000-08-22'})))

    def test_adddays_3(self):
        self.assertEqual(
            Pretty(AddDays('2000-01-01', 5232)),
            Pretty(V('2014-04-29')))

    def test_adddays_4(self):
        self.assertEqual(
            Pretty(AddDays('2000-01-01', Stub())),
            Pretty(Stub()))

    def test_adddays_5(self):
        self.assertEqual(
            Pretty(AddDays('2000-01-01', None)),
            Pretty(None))

    def test_adddays_6(self):
        self.assertEqual(
            Pretty(AddDays('2000-01-01', TS({DawnOfTime: 23, '2010-02-03': None}))),
            Pretty(TS({'1900-01-01': '2000-01-24', '2010-02-03': None})))

# is_stub

    # def test_is_stub_1(self):
    #     self.assertEqual(is_stub(Stub()), True)
    #
    # def test_is_stub_2(self):
    #     self.assertEqual(is_stub(V(45)), False)
    #
    # def test_is_stub_3(self):
    #     self.assertEqual(is_stub(V([1, 2, 3])), False)
    #
    # def test_is_stub_4(self):
    #     self.assertEqual(is_stub([False, False, True]), False)
    #
    # def test_is_stub_5(self):
    #     self.assertEqual(is_stub(True), False)
    #
    # def test_is_stub_6(self):
    #     self.assertEqual(is_stub(TS({DawnOfTime: 4}).value), False)
    #
    # def test_is_stub_7(self):
    #     self.assertEqual(is_stub(TS({DawnOfTime: 4})), False)

    # Time series thread

    # # TODO: This isn't actually working...the test comparison is broken
    # def time_series_thread_1(self):
    #     self.assertEqual(Pretty(time_series_thread(tsnum1, tsnum2)),
    #                      Pretty(TS({'1900-01-01': [4, 24],
    #                                 '2020-01-01': [8, 24],
    #                                 '2021-01-01': [None, 24],
    #                                 '2023-01-01': [None, 3]})))


# Used to test time series logic
tsbool1 = TS({DawnOfTime: False, '2020-01-01': True, '2021-01-01': None})
tsbool2 = TS({DawnOfTime: True, '2023-01-01': False, '2024-01-01': Stub()})
tsnum1 = TS({DawnOfTime: 4, '2020-01-01': 8, '2021-01-01': None})
tsnum2 = TS({DawnOfTime: 24, '2023-01-01': 3, '2024-01-01': Stub()})


if __name__ == '__main__':
    unittest.main()
