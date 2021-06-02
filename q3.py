# -*- coding: utf-8 -*-
"""
Created on Sun May 30 19:30:23 2021

@author: cleiton
"""

import numpy as np
import matplotlib.pyplot as plt

n = 64
P = [1/4, 1/2, 1/4]
X = [0, 1, 2]

# Simulação

nit = 100000
G =[]
for i in range(nit):
    C = np.random.choice(X, size=n, p=P)
    G.append(C.sum())

g,f = np.unique(G, return_counts=True)
plt.bar(g,f)

# Número máximo de sanduíches demandados:
print()