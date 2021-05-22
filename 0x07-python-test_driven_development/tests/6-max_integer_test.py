#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer([-3, 5, 5, 34, -35]), 34)
        self.assertEqual(max_integer([-3, 5, 5, 34, 192]), 192)
        self.assertEqual(max_integer([390, 5, 5, 34, -35]), 390)
        self.assertEqual(max_integer([45.34, 50.34, 50.35, -34]), 50.35)
        with self.assertRaises(TypeError):
            max_integer([3, 56, 'q', 5, 7])

        with self.assertRaises(TypeError):
            max_integer(100)

        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer([3, 4, 4, [23]])
