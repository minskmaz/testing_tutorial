#!/usr/bin/env python

import unittest
from my_program import average

class AverageTest(unittest.TestCase):
    '''Test my_program.average function'''

    def test_empty_arguments(self):
        self.assertEqual(average([]), None)
