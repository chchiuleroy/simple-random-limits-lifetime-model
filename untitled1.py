# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 11:16:37 2022

@author: user
"""
import pandas as pd, numpy as np
from sklearn.linear_model import LinearRegression
from scipy.optimize import dual_annealing

epm_d = pd.read_excel('C:/Users/user/Desktop/fatigue_lifetime_stress.xlsx', engine = 'openpyxl')

def random_limits(u):
    k = sum([np.sort(np.random.uniform(u[0], u[1], 15)).tolist() for i in range(5)], [])
    y = np.log(epm_d['Y1'].values)
    s = np.log(epm_d['X1'].values - np.array(k)).reshape(-1, 1)
    model = LinearRegression()
    model.fit(s ,y)
    y_hat = model.predict(s)
    ase = np.absolute(y-y_hat).sum()
    return ase

bounds = [(0.2, 0.5), (0.5, 0.675)]
val = dual_annealing(random_limits, bounds = bounds, maxiter=10_000)
min_val = val.fun
x = val.x

def random_limits(u):
    k = sum([np.sort(np.random.uniform(u[0], u[1], 15)).tolist() for i in range(5)], [])
    y = np.log(epm_d['Y1'].values)
    s = np.log(epm_d['X1'].values - np.array(k)).reshape(-1, 1)
    model = LinearRegression()
    model.fit(s ,y)
    a = model.intercept_
    b = model.coef_
    y_hat = model.predict(s)
    ase = np.absolute(y-y_hat).sum()
    sse = ((y-y_hat)**2).sum()
    return  k, a, b, ase, sse

m = 1_000_000
results = [random_limits(x) for i in range(m)]
ase_opt = np.argmin([results[i][3] for i in range(m)])
final = results[ase_opt]