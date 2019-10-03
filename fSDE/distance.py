#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:59:58 2019

@author: neelappagouda
"""
import matplotlib.pyplot as plt
import time
def dist(center,other):
    return sum((center-other)**2)
    

mn = target_sort.copy()


rad = 3

center = mn[6]
for i in range(popsize):
    other = mn[i]
    
    
    qw = dist(center,other)
    if  qw <= rad**2 :
        print("True" , qw)
    
    if qw ==0:
        plt.plot(mn[i][0],mn[i][1],'^')
    else:
        plt.plot(mn[i][0],mn[i][1],'*')
    