#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:02:43 2019

@author: luke
"""

import numpy as np

isa = isinstance


Symbol = str          # A q Symbol is implemented as a Python str
List   = list         # A q List is implemented as a Python list
array = np.ndarray
Number = (int, float) # A q Number is implemented as a Python int or float

Matrix = (array) # a q matrix is either an array, or a member of BraKet

