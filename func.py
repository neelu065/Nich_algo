import numpy as np
def func1(x):
    # Sphere function, use any bounds, f(0,...,0)=0
    return sum([x[i]**2 for i in range(len(x))])

def func2(x):
    # Sine function
    return -np.sin( 5 * np.pi * x ) + 1

def func3(x):
    # 
    return ( x[0]**2 + x[1] - 11 )**2 + ( x[0] + x[1]**2 - 7 )**2 + 1
