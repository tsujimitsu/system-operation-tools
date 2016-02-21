# -*- coding: utf-8 -*-
# test_utils.py

from unittest import TestCase, main
from utils import calc

class UtilsTestCase(TestCase):
    def setUp(self):
        # initialize settings
        pass

    def tearDown(self):
        # finalize settings
        pass

    def test_calc_success(self):
        self.assertEqual(50, calc(5))

    def test_calc_fail(self):
        self.assertEqual(500, calc(10))

    def test_calc_typesuccess(self):
        self.assertRaises(TypeError, calc, 'test string')

if __name__ == '__main__':
    main()

