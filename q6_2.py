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

x0 = 1
alpha=2
def inv(u):
    x = ((alpha/u)*x0**alpha)**(1/(alpha+1))
    return x

def par(x):
    y = alpha*x0**alpha/x**(alpha+1)
    return y

X = inv(U)
X2 = np.arange(0.2,3,0.1)
Y2 = par(X2)


plt.figure()
plt.scatter(X,U,s=0.1)

plt.scatter(X2,Y2,s=0.5,c='r')
plt.xscale('log')
plt.yscale('log')


