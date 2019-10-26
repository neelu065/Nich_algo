import numpy as np


def fobj(x, Fn):

    if 1 <= Fn <= 9:
        # Sphere function, use any bounds, f(0,...,0)=0
        return np.sum(x ** 2)

    if Fn == 10:
        # F10
        # Sine function
        return -np.sin(5 * np.pi * x) ** 6 + 1

    if Fn == 11 or Fn == 12:
        # F11 to F12
        # Himmelblau function
        return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2 + 1

# def func4(x):
#    # F13 to F18
#    # Modified version of Rastrigin function
#    return sum([10(1+np.cos(2*np.pi*kd*x[i])) + 2*kd*(x[i] - 1)**2 * H[x[i] -1] for i in range(len(x))])
#
    
    if Fn == 19:
        # Egg holder function
        return -(x[1] + 47) * np.sin(np.sqrt(abs(x[1] + 0.5 * x[0] + 47))) - x[0] * np.sin(np.sqrt(abs(x[0] - x[1] - 47)))