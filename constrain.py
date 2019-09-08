from constrain_const import constrain_const
import numpy as np


def const_violation(a , Fn):
    D, P = constrain_const(Fn)
    for p in np.arange(P):
        ap = 0
        for d in np.arange(D):
            Cp_old = np.mod(D - (p+1) + (d+1) + 1 , D)
            Cp = np.where(Cp_old != 0 , Cp_old , D)
            ap = sum([(Cp * a[d]) ** 2])
        gp = D**2 - ap
        phi_indv = max(0,gp)
        const_viol = sum([phi_indv])
    return const_viol
