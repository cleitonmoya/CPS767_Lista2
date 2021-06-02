# -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:11:15 2021

@author: cleiton
"""

import numpy as np
from numpy import exp
from numpy.random import uniform
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap


# Integração de Monte-Carlo

# função


n = 10000
a,b=0,10
X_i = uniform(a,b,n)
Y_i = uniform(0,1,n)

# função indicadora
h = lambda x: exp(-x**2)
H_i = h(X_i)
G = Y_i <= H_i
I_m = (b-a)*G.cumsum()/range(1,n+1)


print('I:',I_m[-1])

x = np.arange(0,b+0.01,0.01)
cmap = ListedColormap(['C0', 'C1'])

Y_i_1 = Y_i[G]
X_i_1 = X_i[G]
Y_i_0 = Y_i[np.logical_not(G)]
X_i_0 = X_i[np.logical_not(G)]

plt.figure()
plt.plot(x,h(x), color='k', linewidth=2, label='h(x)')
plt.scatter(X_i_1, Y_i_1, s=3, alpha=0.5, label='g(x,y)=1')
plt.scatter(X_i_0, Y_i_0, s=3, alpha=0.5, label='g(x,y)=0')
plt.legend(framealpha=1, markerscale=3)

plt.figure()
plt.plot(I_m, linewidth=1)