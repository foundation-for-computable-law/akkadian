import unittest

from dsl import *


class TestDSL(unittest.TestCase):


    def test_And(self):
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


    def test_Or(self):
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
        

    def test_Not(self):
        self.assertEqual(Not(T(True)).value, False)
        self.assertEqual(Not(T(False)).value, True)
        self.assertEqual(Not(T(None)).value, None)
        self.assertEqual(Not(True).value, False)
        self.assertEqual(Not(False).value, True)

        
    def test_and(self):
        self.assertEqual((T(True) & T(False)).value, False)
        self.assertEqual((T(True) & T(True)).value, True)
        self.assertEqual((T(False) & T(False)).value, False)
        self.assertEqual((T(False) & T(True)).value, False)
        self.assertEqual((T(None) & T(True)).value, None)
        self.assertEqual((T(None) & T(False)).value, False)
        self.assertEqual((T(False) & T(None)).value, False)
        self.assertEqual((T(None) & T(False)).value, False)
        self.assertEqual((T(True) & T(None)).value, None)
        self.assertEqual((T(None) & T(None)).value, None)
        self.assertEqual((T(True) & True).value, True)
        self.assertEqual((True & T(True)).value, True)
        self.assertEqual((False & T(True)).value, False)
        self.assertEqual((False & T(None)).value, False)


    def test_or(self):
        self.assertEqual((T(True) | T(False)).value, True)
        self.assertEqual((T(True) | T(True)).value, True)
        self.assertEqual((T(False) | T(False)).value, False)
        self.assertEqual((T(False) | T(True)).value, True)
        self.assertEqual((T(None) | T(True)).value, True)
        self.assertEqual((T(None) | T(False)).value, None)
        self.assertEqual((T(False) | T(None)).value, None)
        self.assertEqual((T(True) | T(None)).value, True)
        self.assertEqual((T(None) | T(None)).value, None)
        self.assertEqual((True | T(True)).value, True)
        self.assertEqual((False | T(True)).value, True)
        self.assertEqual((False | T(None)).value, None)
        self.assertEqual((True | T(None)).value, True)
        self.assertEqual((True | T(False)).value, True)


    def test_not(self):
        self.assertEqual((~T(True)).value, False)
        self.assertEqual((~T(False)).value, True)
        self.assertEqual((~T(None)).value, None)


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


    def test_If(self):
        self.assertEqual(If(None, 1, 2).value, None)
        self.assertEqual(If(T(None), 1, 2).value, None)
        self.assertEqual(If(T(True), 1, 2).value, 1)
        self.assertEqual(If(True, 1, 2).value, 1)
        self.assertEqual(If(T(False), 1, 2).value, 2)
        self.assertEqual(If(False, 1, 2).value, 2)


    def test_cf(self):
        self.assertEqual((T(True,.84) & T(True,.92)).cf, 0.7728)
        self.assertEqual((T(True,.8) | T(True,.9)).cf, 0.9800000000000001)
        self.assertEqual((T(9,.5) + T(23,.7)).cf, 0.35)
        self.assertEqual(Not(T(True,.4)).cf, 0.4)

        
if __name__ == '__main__':
    unittest.main()
