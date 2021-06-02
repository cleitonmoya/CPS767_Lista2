# -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:11:15 2021

@author: cleiton
"""

import numpy as np
from numpy import exp
from scipy.stats import uniform, truncexpon
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# Função de integeração
a,b=0,10
g = lambda i: exp(-i**2)

# Integração numérica (valor "exato")
I = integrate.quad(g,a,b)[0]
print('I:',I)

# Integração de Monte-Carlo - Método Simples
np.random.seed(42)
def mc_s(n):
    X = uniform(a,b)
    X_i = X.rvs(n)
    Gn = g(X_i)
    I = (b-a)*Gn.mean()
    I_n = (b-a)*Gn.cumsum()/range(1,n+1)
    return I, I_n


# Integração de Monte-Carlo - Importance Sampling
A = 1/(1-exp(-b))
h = lambda i: A*exp(-i)
def mc_is(n):
    Y = truncexpon(b)
    Y_i = Y.rvs(size=n)
    Gn = g(Y_i)/h(Y_i)
    I = Gn.mean()
    I_n = Gn.cumsum()/range(1,n+1)
    return I, I_n

# Erro relativo
def e_rel(In):
    e = abs(In-I)/I
    return e

# a) Monte Carlo Simples
_, I0_n = mc_s(1000000)
_, I1_n = mc_s(1000000)
plt.figure()
plt.plot(I0_n, linewidth=0.5, label='MC Simples')
plt.plot(I1_n, linewidth=0.5, label='Import. Sampling')
plt.axhline(y=I, linewidth=1, linestyle='--', color='r', label='Valor ref.')
plt.xscale('log')
plt.xlabel('n')
plt.ylabel('Integral')
plt.legend()

# c) Erro relativo
nit = 100
e1=[]
e2=[]
for n in range(nit):

    N = np.logspace(1,6,6, dtype='int')
    I1 = [mc_s(n)[0] for n in N]
    I2 = [mc_is(n)[0] for n in N]
    
    # Gráfico de erros
    e1.append([e_rel(i1) for i1 in I1])
    e2.append([e_rel(i2) for i2 in I2])

e1 = np.array(e1)
e2 = np.array(e2)

e1m = e1.mean(axis=0)
e2m = e2.mean(axis=0)

plt.figure()
plt.plot(N,e1m, marker='o', label='MC Simples')
plt.plot(N,e2m, marker='o', label='Import. Sampling')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Erro rel.')
plt.legend()