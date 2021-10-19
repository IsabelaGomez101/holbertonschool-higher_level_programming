#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_docstrings(self):
        self.assertIs(hasattr(Rectangle, "__init__"), True)
        self.assertIs(hasattr(Rectangle, "update"), True)
        self.assertIs(hasattr(Rectangle, "area"), True)
        self.assertIs(hasattr(Rectangle, "display"), True)
        self.assertIs(hasattr(Rectangle, "__str__"), True)
        self.assertIs(hasattr(Rectangle, "to_dictionary"), True)
        self.assertIs(hasattr(Rectangle, "width"), True)

    def test_rectangle(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6)
        r2 = Rectangle(4, 5, 7)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertAlmostEqual(r1.id, 1)
        self.assertAlmostEqual(r2.id, 2)
        self.assertAlmostEqual(r3.id, 3)

    def test_validate_attribute(self):
        self.assertRaises(TypeError, Rectangle, ("2", 10))
        self.assertRaises(TypeError, Rectangle, (2, "10"))
        self.assertRaises(TypeError, Rectangle, (2, 4, "10"))
        self.assertRaises(TypeError, Rectangle, (2, 4, 6, "10"))
        self.assertRaises(TypeError, Rectangle, (10, 2, 3, -1))
        self.assertRaises(TypeError, Rectangle, (10, 2, 3, 4, 5))
