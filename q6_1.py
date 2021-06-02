# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:36:52 2021

@author: cleiton
"""

import numpy as np
from numpy import log, exp, sqrt
from numpy.random import uniform
import matplotlib.pyplot as plt

N = 1000

U = uniform(0,1,N)

lamb = 5
def inv(u):
    x = (log(lamb)-log(u))/lamb
    return x
    
X = inv(U)

def expon(x):
    y = lamb*exp(-lamb*x)
    return y

x0 = 1
alpha=2

plt.figure()
plt.scatter(X,U,s=0.1)
plt.scatter(X2,Y2,s=0.5,c='r')

# ------------ ITEM 2

def inv_par(u):
    x = sqrt((alpha/u)*x0**alpha)
    return x

X2 = np.arange(0.2,3,0.1)
Y2 = expon(X2)