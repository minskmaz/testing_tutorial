#!/usr/bin/env python

import unittest
import os
from subprocess import getoutput

from my_program import average

CODE_PATH = os.path.dirname(__file__)

class AverageTest(unittest.TestCase):
    '''Test my_program.average function'''

    def test_empty_arguments(self):
        self.assertEqual(average([]), None)

    def test_cli_empty_arguments(self):
        out = getoutput('{}/{}'.format(CODE_PATH, 'my_program.py'))
        self.assertEqual(out, 'None')
