#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:20:08 2019

@author: neelu
"""
import numpy as np

import matplotlib.pyplot as plt

def dist(centroid,neighbour):
    return sum((centroid-neighbour)**2)
    

mn = target_sort.copy()

ab = ['true' for i in range(len(target_sort))]
rad = 3                                                                # radius of influence
ab[0] = 'false'                                                                # seed set to false
seed = [0]                                                                      # store the index of centroid vector
s=[]                                                                           # store the neighbour with centroid index
for i in range(popsize):                                                       # loops over the popsize
    neighbour = mn[i]
    
    for j in seed:                                                             # loops over the number of centroid
        centroid = mn[j]
                                                       
        if ab[i] == 'true' and dist(centroid,neighbour) < rad**2 :                    # function to evaluate the euclidian distance
            s.append([neighbour,j])
            
    if ab[i] == 'true' and all([dist(mn[item],neighbour) > rad**2 for item in seed]) :
        seed.append(i)
        ab[i]='false'
        

#next loop
for k in seed:
    count = 0
    for i in range(len(s)):
        if s[i][1]==k:
            count +=1
    print("neighbour count around centroid index {} = ".format(k), count )
m = 20
#print(seed)
#print(s )
for k in seed:
    neigh_point = len([i for i in range(len(s)) if s[i][1]==k])
    if neigh_point < m:
        random_points = np.random.uniform(-radius , radius , size = (m - neigh_point , D))
        
        for i in range(len(random_points)):
            x=random_points[0][i]
            y=random_points[1][i]
            plt.plot(x,y,'*')