# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:32:48 2021

@author: cleiton
"""

import string
import requests
import numpy as np
from requests.exceptions import ConnectionError
from itertools import product
import matplotlib.pyplot as plt

   
# Atributos
A = list(string.ascii_lowercase)

# Gera o espaço amostral S
perm = []
for i in range(1,5):
    perm.extend(product(A,repeat=i))
S = [''.join(i) for i in perm] 
nS = len(S)

'''
# Parâmetros da simulação
N = 100000
k = 4
Ga_n = []

# Gera uma amostra das sequências
np.random.seed(42)
S_a = np.random.choice(S, size=N, replace=False)

for n in range(N):
   
    # Verifica se a sequência pertence ao domínio ufrj.br
    try:
        _ = requests.get(f'http://www.{S_a[n]}.ufrj.br', timeout=1)
    except ConnectionError:
        Ga_n.append(0)
    else:
        Ga_n.append(1)
    

np.save('Ga_n2', Ga_n)

# Cálculo de G
Ga = sum(Ga_n) 
G = Ga*(nS/N)

Ga_t= np.cumsum(Ga_n)
G_t = [ga*nS/(n+1) for n,ga in enumerate(Ga_t)]

# Plota o gráfico
plt.plot(G_t, linewidth=1)
plt.xlabel('Iterações')
'''