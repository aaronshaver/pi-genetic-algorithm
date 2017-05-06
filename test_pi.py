#!/usr/bin/python3

import unittest
import pi

class TestPi(unittest.TestCase):
    def test_bare_init(self):
        animal = pi.Animal()
        self.assertTrue(isinstance(animal.numerator, int))

