#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:20:08 2019

@author: neelu
"""
import numpy as np

import matplotlib.pyplot as plt

def dist(center,other):
    return sum((center-other)**2)
    

mn = target_sort.copy()

ab = ['true' for i in range(len(target_sort))]
rad = 4                                                                 # radius of influence
ab[0] = 'false'                                                                # seed set to false
seed = [0]                                                                      # store the index of centroid vector
s=[]                                                                           # store the value which are around the centroid
for i in range(popsize):                                                       # loops over the popsize
    other = mn[i]
    
    for j in seed:                                                             # loops over the number of centroid
        center = mn[j]
                                                       
        if ab[i]=='true' and dist(center,other) <= rad**2 :                    # function to evaluate the euclidian distance
            s.append([mn[i],j])
           
#        if qw ==0:
#            plt.plot(mn[i][0],mn[i][1],'^')
#            
#        else:
#            plt.plot(mn[i][0],mn[i][1],'*')
        
    if ab[i]=='true' and dist(center,other)>rad**2:
        seed.append(i)
        ab[i]='false'
        

#next loop
print(len([i for i in range(len(s)) if s[i][1]==0]))
m = 20
for k in seed:
    value = len([i for i in range(len(s)) if s[i][1]==k])
    if value < m:
        