
import numpy as np
bounds = [(-4.5, 4.5)]

def constrain1(bounds , x= 38):
    p = 1
    d = 1
    D = len(bounds)
    Cp_old = np.mod(D - p + d + 1 , D)
    Cp = np.where(Cp_old != 0 , Cp_old , D)

    g = D**2 - sum((Cp * x)**2 for  i in range(D))
    return g


const_value = constrain1(bounds)


print(const_value)
