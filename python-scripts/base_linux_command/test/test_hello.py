# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest import TestSuite
from unittest import makeSuite
from hello import *

class TestSample(TestCase):
    def test_success(self):
        self.assertEqual("Hello, World!", hello_world())


def suite():
    suite = TestSuite()
    suite.addTests(makeSuite(TestSample))
    return suite
