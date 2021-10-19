#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
	def test_docstrings(self):
		self.assertIs(hasattr(Base, "__init__"), True)
		self.assertIs(hasattr(Base, "to_json_string"), True)
		self.assertIs(hasattr(Base, "save_to_file"), True)

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
