# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 09:09:10 2018

@author: lokesh.r
"""
"""
Assignment 6 - Numpy session 1
Write a function so that the columns of the output matrix are powers of the input
vector.
"""
import numpy as np
a =np.array([2,4,5])
print("Input vector", a)
c = np.ones((3,3))
b = (a)*c
c =b.T
print("Out Put Matrices")
print(c**2)
