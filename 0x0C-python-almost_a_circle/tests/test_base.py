#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_docstrings(self):
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIs(hasattr(Base, "to_json_string"), True)

    def test_to_json_string(self):
        self.assertAlmostEqual(Base.to_json_string(None), "[]")
        self.assertAlmostEqual(Base.to_json_string([]), "[]")
        self.assertAlmostEqual(Base.to_json_string({'x': 2, 'width': 10}), '{"width": 10, "x": 2}')

    def test_id(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertAlmostEqual(b1.id, 1)
        self.assertAlmostEqual(b2.id, 2)
        self.assertAlmostEqual(b3.id, 3)
        self.assertAlmostEqual(b4.id, 12)
        self.assertAlmostEqual(b5.id, 4)

    def test_validate_attributes(self):
        """ class Rectangle"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertAlmostEqual(r1.id, 5)
        self.assertAlmostEqual(r2.id, 6)
        self.assertRaises(TypeError, Rectangle, (2, "10"))
