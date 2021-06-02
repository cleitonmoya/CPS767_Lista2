# -*- coding: utf-8 -*-
"""
Created on Sat May 15 23:50:43 2021

@author: cleiton
"""

from scipy.stats import binom
from math import exp, sqrt, log
import matplotlib.pyplot as plt

# Questão 2.4
p = 3/20
k = 300
n = 1000
p1 = 0
for i in range(301,n+1):
    p1 = p1 + binom.pmf(i,n,p)


mu = n*p
sigma = n*p*(1-p)
p_chern = (exp(1)/4)**mu

# Questão 2.5
n = 1000
mu = n*p

z1 = mu + sqrt(2*mu*log(n)) 
z2 = mu - sqrt(2*mu*log(n)) 


d1 = (z1-mu)/mu
d2 = (z2-mu)/mu

P1 = exp(-d1**2*mu/2)
P2 = exp(-d2**2*mu/2)

Y = []
for z in range(1000):
    y = z**2 - 2*mu*z + mu**2 - 2*mu*log(n)
    Y.append(y)
    
plt.plot(range(1000),Y)
    