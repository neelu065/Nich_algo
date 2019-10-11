#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:45:53 2019

@author: neelu
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:20:08 2019

@author: neelu
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dist(center,other):
    return sum((center-other)**2)
    

mn = target_sort.copy()
mn2=pd.DataFrame(mn)

rad = 1.2                                                                      # radius of influence

seed = []                                                                      # store the index of centroid vector
seed.append(np.random.randint(1,popsize))
s=[]   
                                                                        # store the value which are around the centroid
for i in range(popsize):                                                       # loops over the popsize
    other = mn[i]
    
    for j in seed:                                                             # loops over the number of centroid
        center = mn[j]
        qw = dist(center,other)                                                # function to evaluate the euclidian distance
        
        if qw !=0 and qw <= rad**2:
#            print("True" , qw)
            s.append([mn[i], j])
            
#        if qw ==0:
#            plt.plot(mn[i][0],mn[i][1],'^')
#            
#        else:
#            plt.plot(mn[i][0],mn[i][1],'*')
        
    if any(mn[i] != item for item in s):
        seed.append(i)
        print(i)
plt.xlim(-3,3)
plt.ylim(-3,3)
        
species_df = pd.DataFrame(s)

len(np.unique(species_df[1].values))
ccc = species_df[species_df[1]==0]
len(ccc)

