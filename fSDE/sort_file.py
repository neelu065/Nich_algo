#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:08:20 2019

@author: neelu
"""


import numpy as np
from constrain_const import constrain_const
from func import fobj
from constrain import const_violation
Fn = 3
popsize      = 5
value        = constrain_const(Fn)                                         # func which decide the Dimension and parameter(p)
D            = value[0]
target = np.random.uniform(-(D+1),(D+1),size = (popsize , D))
fitness = np.asarray([fobj(ind , Fn) for ind in target])

#a = [const_violation(target[i],Fn) for i in range(popsize)]
#print(a)
b = [] ; c = []
e = [] ; f = []                                                                 # b is list of fitness value



for i in range(popsize):                                                        # c= list of violated values
    violation = const_violation(target[i],Fn)                                           # d= cpoy of b for reference
    if violation == 0:                                                                  # e= index of feasible fitness value
        b.append(fitness[i])                                                    # f = index of violated values
        e.append(i)
    else:
        c.append(violation)
        f.append(i)

d = b.copy()  ; g = c.copy()
b.sort()      ; c.sort()
target_sort = []

print()
print('-----feasible vectors-----')
print()

for i in range(len(b)):
    indx = d.index(b[i])
    target_indx = e[indx]
    target_sort.append(target[target_indx])
    #print(target_indx)
    print(target[target_indx] , target_indx)

print()
print('-----infeasible vectors-----')
print()

for i in range(len(c)):
    indx = g.index(c[i])
    target_indx = f[indx]
    target_sort.append(target[target_indx])
#    print(target_indx)
    print(target[target_indx] , target_indx)

print()
target_sort = np.asarray(target_sort)
print()
print('-----sorted target vector-----')
print()
print(target_sort)
