#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, unicode_literals
import unittest

from run import fibonacci


class FibonacciTestCase(unittest.TestCase):
    def test_fibonacci_of_0_should_return_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_of_1_should_return_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_of_6_should_return_8(self):
        self.assertEqual(fibonacci(6), 8)

if __name__ == '__main__':
    unittest.main()
