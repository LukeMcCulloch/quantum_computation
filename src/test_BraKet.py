#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:49:00 2019

@author: luke
"""
import numpy as np
import unittest

import qutip
from BraKet import BraKet


from utilities import isa
from complex_bit_def import cb0, cb1


class TestArithmeticMethods(unittest.TestCase):

    
    
    def sp_equal(self, test, control):
        if np.size(test) > 2:
            for ti, ci in zip( test, control ):
                for tii, cii in zip(ti,ci):
                    print tii, cii
                    self.assertEqual(ti,ci)
        else:
            for ti, ci in zip( test, control ):
                print ti, ci
                self.assertEqual(ti,ci)

        

    def test_mul(self):
        q1 = BraKet([0.,1.])
        q2 = BraKet([0.,1.])
        q3 = q1*q2
        self.assertEqual(q3.array, np.asarray([[0.,0.],[0.,1.]])  )
        
        
        
        
        

                  
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            

if __name__ == """__main""":
    
    q1 = BraKet([0.,1.])
    
    
    unittest.main()
    