#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:12:30 2019

@author: luke
"""
import numpy as np

from BraKet import BraKet, normalize
from utilities import isa, Symbol, List, array, Number, Matrix
from complex_bit_def import cb0, cb1, cbi


Matrix = (array, BraKet) # a q matrix is either an array, or a member of BraKet


class Operator(BraKet):
    
    def __init__(self, array, rep='Op'):
        self.repmap = {'bra':0,'ket':1}
        self.rep = rep
        self.array = array
        self.init_array(array)
    
    def init_array(self, array):
        if type(array) is list:
            self.array = np.asarray(array)
#            #print 'got list'
#            if type(array[0]) is list:
#                #print 'got list OO'
#                self.array = np.asarray(array)
#            else:
#                self.array = np.asarray([array],float).T
        elif type(array) is np.ndarray:
            self.array = array
        else:
            print 'ERROR, type is',type(array)
        return 
    
    def __call__(self):
        return self.array
        
    def __str__(self):
        """print self"""
        return self.rep+'\n{}'.format(self.array)
    
    def __repr__(self):
        """>>> self"""
        return self.rep+'\n{}'.format(self.array)
        
    def print_array(self):
        return self.array
    
    def __mul__(self,other):
        """tensor (outer) product"""
        if isa(other, Matrix):
            #print 'true, other is a matrix' 
            #if isa(X(),Gate.Operator)
            return Operator( np.dot(self.array,other.array) )
        elif isa(other, Operator):
            return Operator( np.dot(self.array,other.array) )
        else:
            #print 'false, other is a ',type(other) 
            return Operator( self.array * other )
    
    def __rmul__(self, other):
        """which pattern is better?
            1.)  handle the non self-type case here
            2.) handle the non-self-type case in the original op?
            here we use option 2.
        """
        return self * other
    
    
    def elementwise_mul(self,other):
        """tensor (outer) product"""
        return Operator( np.multiply(self.array,other.array ) )


Matrix = (array, BraKet, Operator)

def One(N=None, target=0):
    """Quantum object representing the Identity gate.

    

    """
    #if N is not None:
    #    return gate_expand_1toN(snot(), N, target)
    #else:
    return Operator([[cb1, cb0],
                     [cb0, cb1]])
    
    
#def H(N=None, target=0):
class H(Operator):
    """Quantum object representing the SNOT (Hadamard) gate.

    Returns
    -------
    H : Operator
        Quantum object representation of SNOT gate.

    Examples
    --------
    >>> H()
    Operator: dims = [[2], [2]], \
    shape = [2, 2], type = oper, isHerm = True
    Oerator array =
    [[ 0.70710678+0.j  0.70710678+0.j]
     [ 0.70710678+0.j -0.70710678+0.j]]

    """
    def __init__(self):
        self.rep = 'Op'
        self.array = 1. / np.sqrt(2.0) * np.asarray([[cb1, cb1],
                                                     [cb1, -cb1]])
        return
    
    def __call__():
        #if N is not None:
        #    return gate_expand_1toN(snot(), N, target)
        #else:
        return 1. / np.sqrt(2.0) * Operator([[cb1, cb1],
                                            [cb1, -cb1]])
    
def CNOT():
    """
    In the computational basis
    """
    return Operator([[cb1, cb0, cb0, cb0],
                     [cb0, cb1, cb0, cb0],
                     [cb0, cb0, cb0, cb1],
                     [cb0, cb0, cb1, cb0]])

def X(N=None, target=0):
    """Quantum object representing the Not gate.
    aka the Pauli-X gate

    """
    return Operator([[cb0, cb1],
                     [cb1, cb0]])


def Y(N=None, target=0):
    """Quantum object representing the Pauli-Y gate.


    """
    return Operator([[cb0, -cbi],
                     [cbi, cb0]])

def Z(N=None, target=0):
    """Quantum object representing the Pauli-Z gate.


    """
    return Operator([[cb1, cb0],
                     [cb0, -cb1]])