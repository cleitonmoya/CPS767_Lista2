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
A = 1/(1-exp(-1))
g = lambda i: exp(-i**2)

# Integração numérica (valor "exato")
a,b,=0,10
I,e = integrate.quad(g,a=a,b=b)
print('I:',I)

n = 100000

# Integração de Monte-Carlo - Método Simples
np.random.seed(42)
X = uniform(0,10)
X_i = X.rvs(n)
Gn1 = g(X_i)
Gn_m1 = (b-a)*Gn1.cumsum()/range(1,n+1)
e1 = abs(Gn_m1-I)/I
print('I1:', Gn_m1[-1])

'''
# Integração de Monte-Carlo - Importance Sampling
h = lambda i: A*exp(-i)
b = 1
Y = truncexpon(b)
Y_i = Y.rvs(size=n)
Gn2 = g(Y_i)/h(Y_i)
Gn_m2 = Gn2.cumsum()/range(1,n+1)
e2 = abs(Gn_m2-I)/I


# Resultados
print('I1:', Gn_m1[-1])
print('I2:', Gn_m2[-1])


# Gráfico da função
plt.figure()
x = np.arange(0,1.01,0.01)
plt.plot(x,g(x), label='g(x)')
plt.ylim(0, 1.1)
#plt.fill_between(x, g(x), 0, alpha=0.2)
plt.legend()

# Gráficos de erros
plt.figure()
plt.plot(Gn_m1, linewidth=0.5, label='MC Simples')
plt.plot(Gn_m2, linewidth=0.5, label='Import. Sampling')
plt.xscale('log')
plt.xlabel('n')
plt.ylabel('Integral')
plt.legend()

plt.figure()
plt.plot(e1, linewidth=0.5, label='MC Simples')
plt.plot(e2, linewidth=0.5, label='Import. Sampling')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Erro rel.')
plt.legend()
'''