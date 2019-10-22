#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:49:05 2019

@author: neelu
"""

import numpy as np
from selection import selection
from constrain_const import constrain_const
from figure_plot import figure_plot
import matplotlib.pyplot as plt

def de(fobj, mut, crossp, popsize, its, Fn):

    value        = constrain_const(Fn)                                         # func which decide the Dimension and parameter(p)
    D            = value[0]
    bounds       = [(-(D+1),(D+1)) for i in range(D)]    
    
      # Initilisation
    target = np.random.uniform(-(D+1),(D+1),size = (popsize , D))

    if Fn ==11 or Fn ==12:
        D = 2
        bounds  = [(-(5+1),(5+1)) for i in range(2)]                          # search space
        target = np.random.uniform(-(5+1),(5+1),size = (popsize, 2))
    print('bounds = {}'.format(bounds))

    if len(target[0]) == 2:
        plt.title('Initial Uniformly Distributed target vector')
        figure_plot(target , popsize )

    fitness = np.asarray([fobj(ind , Fn) for ind in target])                        # func value evaluation

    for i in range(its):
        target = target_sort