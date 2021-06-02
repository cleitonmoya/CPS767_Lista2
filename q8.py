# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:11:37 2021

@author: cleiton
"""

import numpy as np
from scipy.stats import binom, randint, uniform, triang
import matplotlib.pyplot as plt


n = 1000
p = 0.2
Y = binom(n,p)

# Rejection Sampling
c = 0.032


# Distribuição q_X
x = np.arange(binom.ppf(0.001, n, p),
              binom.ppf(0.999, n, p))

x = np.arange(160,241)

# Distribuição p_X
a,b = 200-40,200+40
X1 = randint(a,b)
c1 = 2.56

a = 160
b = 240
X2 = triang(c=0.5, loc=a, scale=b-a)
c2 = 1.35

fig, ax = plt.subplots()
ax.vlines(x, 0, Y.pmf(x), lw=1, label=r'$q_X$')
ax.vlines(x, 0, X1.pmf(x), colors='C1', lw=1, alpha=0.5, label=r'$p_{1,X}$')
ax.scatter(x, c1*X1.pmf(x), s=3, color='C1', label=r'$c_1\times p_{1,X}$')
ax.plot(x, c2*X2.pdf(x), color='C3', label=r'$c_2\times p_{2,X}$')
ax.legend(loc='center right')


# Rejection Sampling
N = 10000

# a)
U = []
R = []
Q = []

for k in range(N):
    i = X1.rvs()
    p_i = X1.pmf(i)
    q_i = Y.pmf(i)
    u = uniform.rvs(0, c2*p_i)
    if u<q_i:
        R.append(i)
    U.append(u)
    Q.append(q_i)
    
# eficiência
e = len(R)/len(U)
print('Eficiência p1:',e)

fig, ax = plt.subplots()
x_, f = np.unique(R,return_counts=True)
p_ = f/f.sum()
ax.vlines(x_,0, p_, lw=1)
ax.legend()

# b)
U = []
R = []
Q = []

for k in range(N):
    i = round(X2.rvs())
    p_i = X2.pdf(i)
    q_i = Y.pmf(i)
    u = uniform.rvs(0, c2*p_i)
    if u<q_i:
        R.append(i)
    U.append(u)
    Q.append(q_i)
    
# eficiência
e = len(R)/len(U)
print('Eficiência p2:',e)

fig, ax = plt.subplots()
x_, f = np.unique(R,return_counts=True)
p_ = f/f.sum()
ax.vlines(x_,0, p_, lw=1)
ax.legend()