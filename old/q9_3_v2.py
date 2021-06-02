# -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:11:15 2021

@author: cleiton
"""

import numpy as np
from numpy import exp, log
from scipy.stats import uniform, truncexpon
import scipy.integrate as integrate
import matplotlib.pyplot as plt


# funções

g = lambda i: exp(-i**2)

# Integração numérica (valor "exato")
a,b,=0,10
I,e = integrate.quad(g,a=a,b=b)
print('I:',I)

n = 1000000


np.random.seed(42)
# Integração de Monte-Carlo - Método Simples - Área
X = uniform(a,b)
Y = uniform(0,1)
X_i = X.rvs(n)
Y_i = Y.rvs(n)
H_i = g(X_i)
Gn0 = Y_i <= H_i
Gn_m0 = (b-a)*Gn0.cumsum()/range(1,n+1)
e0 = abs(Gn_m0-I)/I
print('I0:', Gn_m0[-1])


# Integração de Monte-Carlo - Método Simples - Direto
np.random.seed(42)
X = uniform(a,b)
X_i = X.rvs(n)
Gn1 = g(X_i)
Gn_m1 = (b-a)*Gn1.cumsum()/range(1,n+1)
e1 = abs(Gn_m1-I)/I
print('I1:', Gn_m1[-1])


# Integração de Monte-Carlo - Importance Sampling
A = 1/(1-exp(-b))
h = lambda i: A*exp(-i)
Y = truncexpon(b)
Y_i = Y.rvs(size=n)
Gn2 = g(Y_i)/h(Y_i)
Gn_m2 = Gn2.cumsum()/range(1,n+1)
e2 = abs(Gn_m2-I)/I
print('I2:', Gn_m2[-1])


# Gráficos de erros
plt.figure()
plt.plot(Gn_m0, linewidth=0.5, label='MC Simples - Método 1')
plt.plot(Gn_m1, linewidth=0.5, label='MC Simples - Método 2')
plt.plot(Gn_m2, linewidth=0.5, label='Import. Sampling')
plt.axhline(y=I, linewidth=0.5, linestyle='--', color='r', label='Valor ref.')
plt.xscale('log')
plt.xlabel('n')
plt.ylabel('Integral')
plt.legend()

plt.figure()
plt.plot(e0, linewidth=0.5, label='MC Simples - Método 1')
plt.plot(e1, linewidth=0.5, label='MC Simples - Método 2')
plt.plot(e2, linewidth=0.5, label='Import. Sampling')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Erro rel.')
plt.legend()
