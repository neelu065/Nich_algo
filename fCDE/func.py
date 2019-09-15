import numpy as np
def func1(x):
    # F1 to F9
    # Sphere function, use any bounds, f(0,...,0)=0
    return sum([x[i]**2 for i in range(len(x))])

def func2(x):
    # F10
    # Sine function
    return -np.sin( 5 * np.pi * x )**6 + 1

def func3(x):
    # F11 to F12
    # Himmelblau function
    return ( x[0]**2 + x[1] - 11 )**2 + ( x[0] + x[1]**2 - 7 )**2 + 1

def func4(x):
    # F13 to F18
    # Modified version of Rastrigin function
    return sum([10(1+np.cos(2*np.pi*kd*x[i])) + 2*kd*(x[i] - 1)**2 * H[x[i] -1] for i in range(len(x))])
