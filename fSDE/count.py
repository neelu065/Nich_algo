#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:28:32 2019

@author: neelappagouda
"""

#######################comment when not needed ################################
def count(k,seed,s):
    for k in seed:
        count = 0
        for i in range(len(s)):
            if s[i][1]==k:
                count +=1
        print("neighbour count around centroid index {} = ".format(k), count )
#######################comment when not needed ################################