import numpy as np

def selection(phi_a , phi_b , f , fitness , pop , trial):
    q1 = phi_a == 0 and phi_b == 0
    q2 = f < fitness
    r1 = phi_b == 0
    r2 = phi_a > 0
    s1 = phi_b < phi_a
    s2 = phi_a > 0 and phi_b > 0                                             # phi_a correcponds to target vector
    if ((q1 and q2) or (r1 and r2) or (s1 and s2)):
        fitness = f ; pop = trial                                             # phi_b corr to donor vector
        return fitness , pop
    else:
        return fitness , pop
