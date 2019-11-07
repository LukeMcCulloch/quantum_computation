#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:30:03 2019

@author: luke
"""

import numpy as np



isa = isinstance
Symbol = str          # A q Symbol is implemented as a Python str
List   = list         # A q List is implemented as a Python list
array = np.ndarray
Number = (int, float) # A Number is implemented as a Python int or float
Matrix = (array)



from complex_bit_def import cb0, cb1


#def normalize(vector):
#
#    mag = np.linalg.norm(vector)
#    return mag*vector

def normalize(vector):
    """
    vector = H().array
    cvector = vector.conj()
    """
    if np.size(vector) >2: 
        cvector = vector.conj()
        mag = np.sqrt( np.dot(cvector.T, vector) )
        return (1./mag)*vector
    
def matrix_to_qubit_representaion(matrix, type_='C'):
    """This seems to match with text book conventions
    """
    return np.asarray([matrix.flatten(type_)]).T

def TensorProduct(ket1,ket2):
    return np.kron(ket1.array,ket2.array)

def closeto(self,target,tol=1.e-6):
    if abs(self-target)>tol:
        return True

class BraKet(object):
    
    def __init__(self, array, rep='ket', force_real_valued=False):
        self.repmap = {'bra':0,'ket':1}
        self.rep = rep
        self.force_real_valued = force_real_valued
        self.array = array
        self.init_array(array)
        self.iszero = False
        self.isone = False
        if closeto(self.array[0,0],1.) and closeto(self.array[1,0],0.):
            self.iszero = True
        elif closeto(self.array[1,0],1.) and closeto(self.array[1,0],0.):
            self.isone = True
            
        
#        self.mag = normalize(
#                matrix_to_qubit_representaion(
#                        self.array))
    
    def init_array(self, array):
        if isa(array, list):
            self.array = np.asarray([array]).T 
            #if not self.force_real_valued:
            #    self.array = np.asarray(array,complex).T
            #else:
            #    self.array = np.asarray(array,float).T 
        elif isa(array, np.ndarray):
            #if not self.force_real_valued:
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
    
    def normalize(self):
        return normalize(self.array)
    
    
    def __add__(self,other):
        """elementwise addition"""
        if isa(other, BraKet):
            return BraKet( self.array + other.array)
        else:
            return BraKet( self.array + other )
            
    
    def __radd__(self, other):
        return self.__add__(other)
    
    
    def __mul__(self,other):
        """tensor (outer) product"""
        if isa(other, BraKet):
            return BraKet( TensorProduct(self,other) )
        else:
            return BraKet( np.kron(self.array,other) )
            
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    
    def elementwise_mul(self,other):
        """elementwise product"""
        return BraKet( np.multiply(self.array,other.array ) )
    

     
class qubit_factory(object):
    """TBD
    """
    def __init__(self):
        self.map = {'0' : BraKet([cb1,cb0]),
                    '1' : BraKet([cb0,cb1]) 
                    }
    
    def __call__(self, alpha = 1., beta = 1., zero=1., one = 1.):
        
        return np.copy(self.map[key])
    
class bloch_factory(object):
    """TBD
    """
    def __init__(self):
        self.map = {'0' : BraKet([cb1,cb0]),
                    '1' : BraKet([cb0,cb1]) 
                    }
    
    def __call__(self, alphs, theta, beta, phi):
        return np.copy(self.map[key])
        