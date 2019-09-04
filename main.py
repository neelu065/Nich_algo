from de import de
from func import *
from constrain_const import constrain_const


Fn = 1                                                                          # Function to be evaluated
popsize = 20
mut = 0.6
crossp = 0.7
iter_max = 100

value = constrain_const(Fn)
D = value[0]
bounds = [(-(D+1),(D+1)) for i in range(D)]                                     # search space

a, b = de(func1, bounds, mut, crossp, popsize, iter_max)
print(a , b )
