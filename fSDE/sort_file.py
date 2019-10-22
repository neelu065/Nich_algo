#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:08:20 2019

@author: neelu
"""
import numpy as np
from constrain import const_violation


def sorttarget(Fn, popsize, target, fitness):
    b = [] # b = is list of fitness value
    c = [] # c = list of violated values
    e = [] # e = index of feasible fitness value
    f = [] # f = index of violated values

    for i in range(popsize):  
        violation = const_violation(target[i], Fn)  
        if violation == 0:  
            b.append(fitness[i])  
            e.append(i)
        else:
            c.append(violation)
            f.append(i)

    d = b.copy() # d = copy of b for reference
    b.sort()
    g = c.copy()
    c.sort()

    target_sort = []

    for i in range(len(b)):
        indx = d.index(b[i])
        target_indx = e[indx]
        target_sort.append(target[target_indx])

    for i in range(len(c)):
        indx = g.index(c[i])
        target_indx = f[indx]
        target_sort.append(target[target_indx])

    target_sort = np.asarray(target_sort)

    return target_sort
