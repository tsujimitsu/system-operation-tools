# -*- coding: utf-8 -*-
import unittest
from sample import Calc

class TestSample(unittest.TestCase):
    def test_success(self):
        calc = Calc()
        self.assertEqual(20, calc.add(2))


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestSample))
    return suite
