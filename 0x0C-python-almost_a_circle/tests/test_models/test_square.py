#!/usr/bin/python3
"""
test cases for square class
"""

"""
importing modules
"""
import unittest
import io
import os
import json
from models import square
from models.base import Base
from contextlib import redirect_stdout

Square = square.Square


class testcases(unittest.TestCase):
    """testing square class"""
    @classmethod
    def setUpClass(cls):
        Base._Base_objects = 0
        cls.c1 = Square(1)
        cls.c2 = Square(2, 3)
        cls.c3 = Square(3, 4, 5)
        cls.c4 = Square(5, 6, 7)
        cls.c5 = Square(7, 8, 9, 10)
    
    def test_id(self):
        self.assertEqual(self.c1.id, 1)
        self.assertEqual(self.c2.id, 2)
        self.assertEqual(self.c3.id, 3)
        self.assertEqual(self.c4.id, 4)
        self.assertEqual(self.c5.id, 10)

    def test_size(self):
        self.assertEqual(self.c1.size, 1)
        self.assertEqual(self.c2.size, 2)
        self.assertEqual(self.c3.size, 3)
        self.assertEqual(self.c4.size, 5)
        self.assertEqual(self.c5.size, 7)

    def test_width(self):
        self.assertEqual(self.c1.width, 1)
        self.assertEqual(self.c2.width, 2)
        self.assertEqual(self.c3.width, 3)
        self.assertEqual(self.c4.width, 5)
        self.assertEqual(self.c5.width, 7)

    def test_height(self):
        self.assertEqual(self.c1.height, 1)
        self.assertEqual(self.c2.height, 2)
        self.assertEqual(self.c3.height, 3)
        self.assertEqual(self.c4.height, 5)
        self.assertEqual(self.c5.height, 7)

    def test_x(self):
        self.assertEqual(self.c1.x, 0)
        self.assertEqual(self.c2.x, 3)
        self.assertEqual(self.c3.x, 4)
        self.assertEqual(self.c4.x, 6)
        self.assertEqual(self.c5.x, 8)

    def test_y(self):
        self.assertEqual(self.c1.y, 0)
        self.assertEqual(self.c2.y, 0)
        self.assertEqual(self.c3.y, 5)
        self.assertEqual(self.c4.y, 7)
        self.assertEqual(self.c5.y, 9)

    def test_arg(self):
        with self.assertRaises(TypeError):
            s = Square()

    def testing_size_typerror(self):
        """testing typerror error for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("fizz")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(False)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square([1, 3])

    def testing_x_typerror(self):
        """testing typerror error for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "fizz")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(3, [1, 3])

    def testing_y_typerror(self):
        """testing typerror error for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 3, "fizz")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 2,  False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(3, 4, [1, 3])

    def testing_size_valuerror(self):
        """testing value error for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def testing_x_valuerror(self):
        """testing value error for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def testing_y_valuerror(self):
        """testing value error for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)


    def test_area(self):
        """Testing area, assigments comes from lines 19"""
        self.assertEqual(self.c1.area(), 1)
        self.assertEqual(self.c2.area(), 4)
        self.assertEqual(self.c3.area(), 9)
        self.assertEqual(self.c4.area(), 25)
        self.assertEqual(self.c5.area(), 49)

    def test_area_args(self):
        """we just can call area, not pass args"""
        with self.assertRaises(TypeError):
            self.c1.area(1)

    def test_display(self):
        """tesing display aoutput"""
        test = Square(3, 0, 0, 3)
        with io.StringIO() as fi, redirect_stdout(fi):
            self.c1.display()
            output = fi.getvalue()
            self.assertEqual(output, "#\n")

        with io.StringIO() as fi, redirect_stdout(fi):
            test.display()
            output = fi.getvalue()
            self.assertEqual(output, ("#" * 3 + "\n") * 3)

    def test_display_arg(self):
        """we just can call display, no pars args"""
        with self.assertRaises(TypeError):
            self.c1.display(1)

    def test_str(self):
        """testing __str__"""
        self.assertEqual(str(self.c1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.c2), "[Square] (2) 3/0 - 2")
        self.assertEqual(str(self.c3), "[Square] (3) 4/5 - 3")
        self.assertEqual(str(self.c4), "[Square] (4) 6/7 - 5")
        self.assertEqual(str(self.c5), "[Square] (10) 8/9 - 7")