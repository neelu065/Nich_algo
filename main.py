from de import de
from func import *

import matplotlib.pyplot as plt

# Inputs
Fn           = 2                                                                # Function to be evaluated
popsize      = 1
mut          = 0.6
crossp       = 0.7
iter_max     = 100
func_eval    = func1                                                            # func to be evaluated

#bounds = [(0 , 1)]




# Execution

a , b  = de(func_eval, mut, crossp, popsize, iter_max, Fn)


min_b, max_b = np.asarray(bounds).T
diff = np.fabs(min_b - max_b)                                               # fabs func to get floating positive difference
pop_denorm = min_b + a * diff
print( 'pop_denorm = {}'.format(pop_denorm) )
print('function value = {}'.format(b))



plt.plot(a)
