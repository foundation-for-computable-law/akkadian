import unittest

from dsl import *


class TestDSL(unittest.TestCase):

    def test_and(self):
        self.assertEqual(T(True) & T(False), T(False))
        self.assertEqual(T(True) & T(True), T(True))
        self.assertEqual(T(False) & T(False), T(False))
        self.assertEqual(T(False) & T(True), T(False))
        self.assertEqual(T(None) & T(True), T(None))
        self.assertEqual(T(None) & T(False), T(False))
        self.assertEqual(T(False) & T(None), T(False))
        self.assertEqual(T(True) & T(None), T(None))
        self.assertEqual(T(None) & T(None), T(None))


    def test_or(self):
        self.assertEqual(T(True) | T(False), T(True))
        self.assertEqual(T(True) | T(True), T(True))
        self.assertEqual(T(False) | T(False), T(False))
        self.assertEqual(T(False) | T(True), T(True))
        self.assertEqual(T(None) | T(True), T(True))
        self.assertEqual(T(None) | T(False), T(None))
        self.assertEqual(T(False) | T(None), T(None))
        self.assertEqual(T(True) | T(None), T(True))
        self.assertEqual(T(None) | T(None), T(None))

        
    def test_not(self):
        self.assertEqual(~T(True), T(False))
        self.assertEqual(~T(False), T(True))
        self.assertEqual(~T(None), T(None))



if __name__ == '__main__':
    unittest.main()
