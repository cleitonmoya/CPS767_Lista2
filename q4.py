# -*- coding: utf-8 -*-
"""
Created on Mon May 31 09:48:53 2021

@author: cleiton
"""

from scipy.stats import binom
import numpy as np
from numpy import sqrt, log
import matplotlib.pyplot as plt

n = 1000
p = 0.5
D = binom(n,p)

x = np.arange(300,801)
y = D.pmf(x)


beta= 1-1/n
gamma = D.ppf(beta)
print('Gamma 1:', gamma)

plt.plot(x,y,'o', ms=2)
plt.vlines(x,0, y, lw=1)
x_ = np.arange(0,gamma+1)
plt.fill_between(x_, D.pmf(x_), 0, alpha=0.2, color='g', label=r'$P[D\leq \gamma]$')
plt.vlines(gamma,0,D.pmf(gamma),lw=3, color='g', label=r'$D=\gamma$')
plt.xlim(20,80)
plt.legend()

# 38
mu = n*p
gamma = mu + sqrt(3*mu*log(n))
print(gamma)