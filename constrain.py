from constrain_const import constrain_const
import numpy as np
bounds = [(3,3)]



def constrain1(bounds , x= 38):
    D, P = constrain_const(4)                                             # input to be the func which need to solved(1 = F1)
    for p in range(1,P):
        for d in range(1,D):
            Cp_old = np.mod(D - p + d + 1 , D)
            Cp = np.where(Cp_old != 0 , Cp_old , D)
            ap = sum([(Cp * x) ** 2])
        g = D**2 - ap
    return

const_value = constrain1(bounds)

print(const_value)
