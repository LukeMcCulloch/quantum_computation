#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 02:45:08 2019

@author: luke
"""

import numpy as np
import unittest

import Gate
from Gate import X,Y,Z
from BraKet import BraKet, normalize, matrix_to_qubit_representaion

from utilities import isa, Matrix
from complex_bit_def import cb0, cb1, cbi
    
class TestGates(unittest.TestCase):

    
    def sp_equal(self, test, control):
        """
        q1  = BraKet([cb0,cb1])
        One   = Gate.One
        q2 = One()*q1
        test = q2.array
        control = q1.array
        
        
        
        q1 = BraKet([0.,1.])
        q2 = BraKet([0.,1.])
        q3 = q1*q2
        
        test = q3.array
        control = np.asarray([[0.,0.],[0.,1.]]) 
        """
        if np.size(test) > 2:
            for ti, ci in zip( test, control ):
                for tii, cii in zip(ti,ci):
                    print tii, cii
                    self.assertEqual(tii,cii)
        else:
            for ti, ci in zip( test, control ):
                print ti, ci
                if isa(ti, np.complex):
                    self.assertEqual(ti,ci)
                elif isa(ti, float):
                    print ti ==ci
                    self.assertEqual(ti,ci)
#                elif isa(ti, Matrix):
#                    print 'Warning, unexpected matrices'
#                    for tii, cii in zip(ti,ci):
#                        print 'is ti == ci?'
#                        print ti == ci
#                        print '----'
#                        self.assertEqual(tii,cii)
                else:
                    print 'Warning, unexpected type'
                    print 'test type = ',type(test)
                    print 'control type = ',type(control)
                    self.assertEqual(ti,ci)
    
    #    def sp_equal(self, test, control):
    #        for ti, ci in zip( test, control ):
    #            print ti, ci
    #            self.assertEqual(ti,ci)


    def test_One_real(self):
        print 'test One'
        q1  = BraKet([0.,1.])
        One   = Gate.One
        q2 = One()*q1
        self.sp_equal(q2.array, q1.array)
        self.sp_equal( q1.array , q2.array,  )
        
        

    def test_One_complex(self):
        print 'test One'
        #q1  = BraKet([0.,1.])
        q1  = BraKet([cb0,cb1])
        One   = Gate.One
        q2 = One()*q1
        self.sp_equal(q2.array, q1.array)
        
        
        
    def test_X(self):
        print 'test X'
        q0 = BraKet([1.,0.])
        q1  = BraKet([0.,1.])
        X   = Gate.X
        q2 = X()*q1
        self.sp_equal(q2.array, q0.array)
        
        


    def test_mul(self):
        print 'test tensor product'
        q1 = BraKet([0.,1.])
        q2 = BraKet([0.,1.])
        q3 = q1*q2
        self.sp_equal(q3.array, np.asarray([[0.,0.],[0.,1.]])  )
        
        
        
    def test_supperposition(self):
        print 'test superposition'
        alpha = .6
        beta = .8
        q0 = BraKet([cb1,cb0])
        q1  = BraKet([cb0,cb1])
        ans = alpha*q0 + beta*q1
        self.sp_equal(ans.array, np.asarray([.6,.8]).T )
        self.sp_equal(ans.array, np.asarray([[.6],[.8]]) )
        
    def test_X_superposition(self):
        """NOT the superposition-state
        """
        print 'test X_superposition'
        alpha = .6
        beta = .8
        q0 = BraKet([cb1,cb0])
        q1  = BraKet([0.,1.])
        initial_state = alpha*q0 + beta*q1
        X   = Gate.X
        final_state = X()*(initial_state)
        
        ans = X()*final_state
        self.sp_equal(initial_state.array, ans.array)

    
if __name__ == """__main__""":
    
    import Gate
    X = Gate.X
    H = Gate.H
    One = Gate.One
    
    q0 = BraKet(array=[1.,0.])
    q1 = BraKet(array=[0.,1.])
    
    q2 = BraKet(array=[1.,0.])
    self = q2
    other = q2
    q3 = q0*q1*q0
    print matrix_to_qubit_representaion((q1*q0*q1).array,'C')
    q4 = q1*q0*q1
    
    q1*X()
    X()*q1
    
    print isa(X(),Gate.Operator)
    
    
    #    
    #    q1  = BraKet([0.,1.])
    #    q1p  = BraKet([0.,1.01])
    #    X   = Gate.X
    #    q2 = X()*q1
    #    
    test = q1
    control = q2
    
    unittest.main()
    
    print '|+>  '
    print H()*q0
    print ''
    print '|->  '
    print H()*q1
    print ''
    h = H()
    print h*q0
    print h*q1 
    
    print ''
    print 'H|+> == q0 '
    print q0,' =?=',H()*H()*q0, '\nyes, to floating point precision'
    print ''
    print 'H|-> == q1 '
    print q1,' =?=',H()*H()*q1, '\nyes, to floating point precision'
    
    print ''
    print 'identity relations'
    print X()*X()
    print ''
    print Y()*Y()
    print ''
    print Z()*Z()
    print ''
    print cbi*X()*Y()*Z()