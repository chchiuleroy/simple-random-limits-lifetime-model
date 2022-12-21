# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 11:14:45 2022

@author: user
"""
import pandas as pd, numpy as np
from scipy.optimize import dual_annealing

epm_d = pd.read_excel('C:/Users/user/Desktop/fatigue_lifetime_stress.xlsx', engine = 'openpyxl')

def loss(p):
    v0 = p[0]; v1 = p[1]; a = p[2]; b = p[3]; s = p[4]
    x = epm_d['X1'].values; z = np.log(epm_d['Y1'].values)
    m = len(x)
    k1 = [(b/s)*(np.log(x[i]-v1)-(z[i]-a)/b) for i in range(m)]
    k0 = [(b/s)*(np.log(x[i]-v0)-(z[i]-a)/b) for i in range(m)]
    def f1(u):
        f1 = 1 - np.exp(-u**2/2)/(44/79 + 8/5*u + 5/6*(u**2+3)**0.5)
        return f1
    def f0(k0, k1):
        f0 = 1/((v1-v0)*b)*(f1(k1)-f1(k0))
        return f0
    l = np.prod([(f0(k0[i], k1[i])) for i in range(m)])
    return -l

bounds = [(0.2, 0.5), (0.5, 0.675), (-10, -0), (-10, -5), (0, 0.5)]
val = dual_annealing(loss, bounds = bounds, maxiter = 10_000)
min_val = val.fun
x = val.x 