# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from matplotlib import pyplot as plt
import numpy as np
radius = 3
points = 10
#rho = np.sqrt(np.random.uniform(0, 10, 500))
data_point = np.sqrt(np.random.uniform(0, radius**2, points))
angle = np.random.uniform(0, 2*np.pi, points)

x = data_point * np.cos(angle)
y = data_point * np.sin(angle)

x += 5
y += 5
#plt.scatter(5,5, s = 15)
plt.scatter(x, y, s = 4)
plt.axis()
