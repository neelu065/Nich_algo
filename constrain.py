from constrain_const import constrain_const
import numpy as np
bounds = [(3,3)]

def constrain1(bounds , x= 38):
    D, p = constrain_const(1)                                              # input to be the func which need to solved(1 = F1)
    # d = constrain_const()
    # D = len(bounds)
    print(D , p)
    # Cp_old = np.mod(D - p + d + 1 , D)
    # Cp = np.where(Cp_old != 0 , Cp_old , D)
    #
    # g = D**2 - sum((Cp * x)**2 for  i in range(D))
    return D , p 


const_value = constrain1(bounds)


#print(const_value)
