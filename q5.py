# -*- coding: utf-8 -*-
"""
Created on Sun May 23 01:16:34 2021

@author: cleiton
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# Gera uma amostra de V
def amostraV():
    S = 0
    k = 0
    while S<1:
        k=k+1
        x = random.uniform(0,1)
        S = S + x
    return k

# Valor esperado de V - Método de Monte Carlo
N = 10000
V = np.array([amostraV() for _ in range(N)])
V_m = V.mean()
print(V_m)

# Gráfico
V_m_k = [V[:k].mean() for k in range(1,N+1)]
plt.plot(V_m_k, linewidth=1)