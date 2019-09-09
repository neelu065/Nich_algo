from de import de
from func import *
from constrain_const import constrain_const
import matplotlib.pyplot as plt

# Inputs
Fn           = 10                                                                # Function to be evaluated
popsize      = 100
mut          = 0.6
crossp       = 0.7
iter_max     = 50
func_eval    = func2                                                            # func to be evaluated
value        = constrain_const(Fn)                                              # func which decide the Dimension and parameter(p)
D            = value[0]
bounds       = [(-(D+1),(D+1)) for i in range(D)]                               # search space
bounds = [(0 , 1)]
print(bounds)
# Execution

a , b  = de(func_eval, bounds, mut, crossp, popsize, iter_max, Fn)

print( a , b )

plt.plot(a , b)
