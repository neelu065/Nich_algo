import numpy as np

def selection(phi_a , phi_b , f , fitness):                                                  # phi_a correcponds to target vector
    if (phi_a == 0 & phi_b == 0 ):                                              # phi_b corr to donor vector
        idx = np.argmin([f, fitness])
        return np.where(f < fitness[j] , f , fitness[j])
    if (phi_b == 0 )
    return
