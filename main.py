from de import de
from func import *
from constrain_const import constrain_const

value = constrain_const(1)
D = value[0]
bounds = [(-(D+1),(D+1)), (-(D+1),(D+1))]  # search space
popsize = 20
mut = 0.6
crossp = 0.7
iter_max = 100
a, b = de(func1, bounds, mut, crossp, popsize, iter_max)
print(a , b )
