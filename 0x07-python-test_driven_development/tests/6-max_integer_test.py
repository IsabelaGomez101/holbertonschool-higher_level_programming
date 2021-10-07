#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_maxinteger(self):
        """
        test
        """
        self.assertAlmostEqual(max_integer([2, 4, 6]), 6)
        self.assertAlmostEqual(max_integer([-2, -4, -6]), -2)
        self.assertAlmostEqual(max_integer([0]), 0)
        self.assertAlmostEqual(max_integer([2, 8, 1]), 8)
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_list_empty(self):
        """
        test
        """
        self.assertAlmostEqual(max_integer([]), None)

    def test_typeError(self):
        """
        test
        """
        self.assertRaises(TypeError, max_integer, [2, 4, "n"])
        self.assertRaises(TypeError, max_integer, [2, "hello", 12])
        self.assertRaises(TypeError, max_integer, 1, 2, 4)
        self.assertRaises(TypeError, max_integer, 14)
        self.assertRaises(TypeError, max_integer, [2, 4, [2, 4], 7])
        self.assertRaises(TypeError, max_integer, 2, 4)
