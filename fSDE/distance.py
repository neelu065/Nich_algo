#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:20:08 2019

@author: neelu
"""
import numpy as np
from figure_plot import figure_plot
import matplotlib.pyplot as plt

def dist(centroid,neighbour):                                                  # function to define euclidian distance
    return sum((centroid-neighbour)**2)
    

ab = ['true' for i in range(len(target_sort))]
radius = 3                                                                     # radiusius of influence
ab[0] = 'false'                                                                # seed set to false
seed = [0]                                                                     # store the index of centroid vector
s=[]                                                                           # store the neighbour with centroid index
for i in range(popsize):                                                       # loops over the popsize
    neighbour = target_sort[i]
    
    for j in seed:                                                             # loops over the number of centroid
        centroid = target_sort[j]
                                                       
        if ab[i] == 'true' and dist(centroid,neighbour) < radius**2 :          # function to evaluate the euclidian distance
            s.append([neighbour,j])
            
    if ab[i] == 'true' and all([dist(target_sort[item],neighbour) > radius**2 for item in seed]) :
        seed.append(i)                                                         # new seed is generated
        ab[i]='false'                                                          # so that this point wont become the neighbour of any centroid vector
        

#######################comment when not needed ################################
for k in seed:
    count = 0
    for i in range(len(s)):
        if s[i][1]==k:
            count +=1
    print("neighbour count around centroid index {} = ".format(k), count )
#######################comment when not needed ################################

m = 20                                                                         # user defined value

for k in seed:
    neigh_point = len([i for i in range(len(s)) if s[i][1]==k])                 
    
    if neigh_point < m:
        new_pop = m - neigh_point                                              # This value represent the new random points to be generated
        random_points = target_sort[k] + np.random.uniform(-radius , radius , size = (new_pop , D))
        
        for i in range(new_pop):
            s.append([random_points[i],k])

#######################comment when not needed ################################
        if D==2:
            plt.figure(k)
            plt.title('plot corresponds to target_sort[{}] as centroid '.format(k))
            plt.plot(target_sort[k][0],target_sort[k][1],'^')
            figure_plot(random_points, new_pop)                                # figure_plot function is called.
            print(target_sort[k])
#######################comment when not needed ################################
        