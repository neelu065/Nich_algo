from de import de
from func import *
from constrain_const import constrain_const

# Inputs
Fn           = 4                                                               # Function to be evaluated
popsize      = 50
mut          = 0.6
crossp       = 0.7
iter_max     = 400
func_eval    = func1                                                            # func to be evaluated
value        = constrain_const(Fn)                                              # func which decide the Dimension and parameter(p)
D            = value[0]
bounds       = [(-(D+1),(D+1)) for i in range(D)]                               # search space
print(value)
# Execution

a , b  = de(func_eval, bounds, mut, crossp, popsize, iter_max, Fn)

print( a , b )
